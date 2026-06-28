#!/usr/bin/env python3

import sys
from os import chdir
from os.path import join
import os
import warnings
import re
import json
import traceback
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from urllib.parse import quote

# Suppress the urllib3 warning about OpenSSL
warnings.filterwarnings('ignore', category=Warning)

# Ensure progress logs appear promptly in non-interactive runners (e.g. Jenkins)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)

# Set environment variable to skip GUI dependencies
os.environ['VFB_SKIP_GUI'] = '1'

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

version = 9

API_BASE = "https://v3-cached.virtualflybrain.org/get_term_info"
STATUS_URL = "https://vfbquery.virtualflybrain.org/status"
VFB_BROWSER_BASE = "https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto"

# Throttle settings — stay under 20 concurrent to keep API reliable
MAX_ACTIVE_BEFORE_BACKOFF = 20  # Back off when the server reports this many active queries
STATUS_CHECK_INTERVAL = 10     # Seconds between status checks while waiting
MAX_CAPACITY_WAIT_SECONDS = 600  # Give up waiting for capacity after this long
# Concurrent fetch/generate workers. Kept below MAX_ACTIVE_BEFORE_BACKOFF so our
# own load leaves headroom for other clients; the serial loop only ever used one
# slot, leaving the server (≈20 slots) mostly idle — this is the main speed-up.
MAX_WORKERS = int(os.environ.get("VFB_MAX_WORKERS", "12"))
# Per-request timeout. The old 9000s default was a workaround for serial stalls;
# with concurrency a hung term must not pin a worker for hours. Override with
# VFB_API_TIMEOUT_SECONDS if a genuinely heavy term needs longer.
API_TIMEOUT_SECONDS = int(os.environ.get("VFB_API_TIMEOUT_SECONDS", "600"))

# Known ID prefixes for internal link conversion
KNOWN_PREFIXES = (
    'FBbt_', 'FBbi_', 'FBcv_', 'FBdv_', 'FBal', 'FBrf', 'FBgn', 'FBti', 'FBtp',
    'VFB_', 'VFBexp_', 'VFBext_', 'VFBlicense_',
    'GO_', 'SO_', 'IAO_', 'GENO_', 'PATO_', 'PCO_',
    'UBERON_', 'RO_', 'OBI_', 'NCBITaxon_', 'ZP_',
    'WBPhenotype_', 'CARO_', 'BFO_',
)

# ─── HTTP Session ────────────────────────────────────────────────────────────

def create_session():
    """Create a requests session with retry logic and connection pooling."""
    session = requests.Session()
    retry = Retry(
        total=3,
        backoff_factor=5,
        status_forcelist=[429, 500, 502, 503, 504],
        respect_retry_after_header=True,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=MAX_WORKERS, pool_maxsize=MAX_WORKERS)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

session = create_session()

# ─── Server Throttling ───────────────────────────────────────────────────────

def check_server_status():
    """Check VFBquery server status. Returns (active, waiting) or None on error."""
    try:
        resp = session.get(STATUS_URL, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        active = data.get("active", 0)
        waiting = data.get("waiting", 0)
        return active, waiting
    except Exception as e:
        print(f"WARNING: Could not check server status: {e}")
        return None

# Cached, thread-safe view of server capacity so a pool of workers doesn't each
# poll /status before every request. One worker refreshes the cache at most once
# per STATUS_CHECK_INTERVAL; the rest read the cached verdict.
_status_lock = threading.Lock()
_status_cache = {"ts": 0.0, "ok": True}

def throttle(term_id=""):
    """Pause the calling worker while the server is at/over capacity.

    Reads a shared cached /status verdict (refreshed at most once per
    STATUS_CHECK_INTERVAL). Returns once the server has headroom, or after
    MAX_CAPACITY_WAIT_SECONDS so a single term can't block forever. With
    MAX_WORKERS below MAX_ACTIVE_BEFORE_BACKOFF our own load never trips this;
    it only engages when other clients are loading the server.
    """
    start = time.time()
    while True:
        now = time.time()
        with _status_lock:
            if (now - _status_cache["ts"]) >= STATUS_CHECK_INTERVAL:
                st = check_server_status()
                _status_cache["ts"] = now
                _status_cache["ok"] = True if st is None else st[0] < MAX_ACTIVE_BEFORE_BACKOFF
            ok = _status_cache["ok"]
        if ok:
            return
        if time.time() - start >= MAX_CAPACITY_WAIT_SECONDS:
            print(f"WARNING: proceeding with {term_id or 'request'} after waiting for capacity")
            return
        time.sleep(STATUS_CHECK_INTERVAL)

def wait_for_server_capacity(term_id=""):
    """Block until the server has capacity below our threshold.

    Monitors the /status endpoint and waits when active queries >= MAX_ACTIVE_BEFORE_BACKOFF
    and retries when the status endpoint is unavailable. Waits are bounded so a
    single term cannot block forever.
    """
    start_time = time.time()
    term_label = term_id or "request"
    while True:
        status = check_server_status()
        elapsed = time.time() - start_time

        if status is None:
            if elapsed >= MAX_CAPACITY_WAIT_SECONDS:
                print(
                    f"WARNING: Proceeding with {term_label} after {int(elapsed)}s because status checks failed."
                )
                return
            print(f"  Status endpoint unreachable, retrying in {STATUS_CHECK_INTERVAL}s...")
            time.sleep(STATUS_CHECK_INTERVAL)
            continue

        active, waiting = status
        if active >= MAX_ACTIVE_BEFORE_BACKOFF:
            if elapsed >= MAX_CAPACITY_WAIT_SECONDS:
                print(
                    f"WARNING: Proceeding with {term_label} after {int(elapsed)}s "
                    f"while busy (active={active}, waiting={waiting})."
                )
                return
            print(
                f"  Server busy: {active} active, {waiting} queued. "
                f"Retrying in {STATUS_CHECK_INTERVAL}s... (threshold: {MAX_ACTIVE_BEFORE_BACKOFF})"
            )
            time.sleep(STATUS_CHECK_INTERVAL)
            continue

        if waiting > 0:
            print(
                f"  Server queue detected ({waiting}) but active load is {active}; proceeding."
            )

        # Server has usable capacity
        return

# ─── Data Fetching ───────────────────────────────────────────────────────────

def fetch_term_info(term_id):
    """Fetch term info from VFBquery API. Returns dict or None on error.

    Checks server capacity before making the request to avoid flooding.
    """
    # Wait until the server isn't overloaded (shared cached capacity check)
    throttle(term_id)

    try:
        resp = session.get(API_BASE, params={"id": term_id}, timeout=API_TIMEOUT_SECONDS)
        resp.raise_for_status()
        data = resp.json()
        if not data or not data.get("Id"):
            print(f"WARNING: Empty or invalid response for {term_id}")
            return None
        return data
    except requests.exceptions.RequestException as e:
        print(f"WARNING: HTTP error fetching {term_id}: {e}")
        return None
    except (json.JSONDecodeError, ValueError) as e:
        print(f"WARNING: JSON parse error for {term_id}: {e}")
        return None

# ─── URL / Link Helpers ─────────────────────────────────────────────────────

def get_term_url(label, short_form):
    """Create canonical URL slug for a term."""
    url = label.replace('\\', '').replace(' ', '-').lower() + "-" + short_form.lower()
    return re.sub("[^0-9a-zA-Z-_]+", "", url)

def get_report_url(identifier):
    """Create the VFB report URL path for a term identifier."""
    return f'/reports/{identifier}'

def get_query_results_url(term_id, query_name):
    """Create a VFB viewer URL for a term query result set."""
    if not query_name:
        return f'{VFB_BROWSER_BASE}?id={term_id}'
    query = quote(f'{term_id},{query_name}', safe=',')
    return f'{VFB_BROWSER_BASE}?q={query}'

def is_known_id(identifier):
    """Check if an identifier matches a known VFB prefix."""
    return any(identifier.startswith(p) for p in KNOWN_PREFIXES)

def convert_internal_links(text):
    """Convert API markdown links [label](ID) to VFB report links.

    Handles:
    - Simple links: [medulla](FBbt_00003748) → [medulla](/reports/FBbt_00003748)
    - IDs that aren't known prefixes are left as-is
    """
    if not text:
        return ""

    def replace_link(match):
        label = match.group(1)
        identifier = match.group(2)
        if is_known_id(identifier):
            return f'[{label}]({get_report_url(identifier)})'
        return match.group(0)

    # Use a pattern that handles nested brackets in labels (e.g. gene names with [allele])
    # Match: [ ... ]( ID ) where the ID part has no spaces or parens
    return re.sub(r'\[([^\]]*(?:\[[^\]]*\][^\]]*)*)\]\(([^)\s]+)\)', replace_link, text)

# Markdown links nested inside a raw HTML block (e.g. the hero card <p>) are NOT
# processed by Hugo's Goldmark renderer — it passes HTML blocks through verbatim.
# So any `[label](id)` placed inside <p>…</p> would render as literal brackets.
# linkify_html emits real <a> anchors instead, mapping known ids to /reports/
# exactly like convert_internal_links does for plain markdown.
_MD_LINK_RE = re.compile(r'\[([^\]]*(?:\[[^\]]*\][^\]]*)*)\]\(([^)\s]+)\)')

def linkify_html(text):
    """Convert `[label](target)` markdown links to HTML <a> anchors.

    For embedding in raw HTML blocks (hero card description/comment), where
    Goldmark won't process markdown. Known VFB ids are rewritten to /reports/;
    other targets (already-resolved URLs) are used as-is. Newlines are collapsed
    to spaces so the surrounding HTML block isn't terminated by a blank line.
    """
    if not text:
        return ""

    def repl(match):
        label = match.group(1)
        identifier = match.group(2)
        href = get_report_url(identifier) if is_known_id(identifier) else identifier
        return f'<a href="{href}">{label}</a>'

    return _MD_LINK_RE.sub(repl, text).replace("\r", " ").replace("\n", " ")

def format_relationships_section(relationships_text):
    """Format Meta.Relationships into markdown bullets.

    Input format: [rel_name](rel_id): [target1](id1), [target2](id2); [rel2](id): [target](id)
    Output: - **rel_name**: [target1](/reports/...), [target2](/reports/...)
    """
    if not relationships_text:
        return ""

    lines = []
    entries = relationships_text.split("; ")
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        # Split on first ": " to separate relation from targets
        if ": " in entry:
            rel_part, targets_part = entry.split(": ", 1)
            # Extract relation label from [label](id) format
            rel_match = re.match(r'\[([^\]]+)\]\([^)]+\)', rel_part)
            if rel_match:
                rel_label = rel_match.group(1)
            else:
                rel_label = rel_part
            # Convert target links
            converted_targets = convert_internal_links(targets_part)
            lines.append(f'- **{rel_label}**: {converted_targets}')
        else:
            # No colon separator — just convert links
            lines.append(f'- {convert_internal_links(entry)}')
    return "\n".join(lines)

def format_types_section(types_text):
    """Format Meta.Types into markdown bullets.

    Input format: [type1](id1); [type2](id2)
    Output: - [type1](/reports/id1)
            - [type2](/reports/id2)
    """
    if not types_text:
        return ""

    lines = []
    entries = types_text.split("; ")
    for entry in entries:
        entry = entry.strip()
        if entry:
            lines.append(f'- {convert_internal_links(entry)}')
    return "\n".join(lines)

# ─── Formatting Helpers ──────────────────────────────────────────────────────

def get_thumbnails(term_data):
    """Extract thumbnail URLs from Images (individuals) or Examples (classes).

    Returns list of dicts: {url, label, template_id}
    """
    thumbnails = []

    # Individual terms have Images
    images = term_data.get("Images", {})
    if images:
        for template_id, image_list in images.items():
            for img in image_list:
                if img.get("thumbnail"):
                    thumbnails.append({
                        "url": img["thumbnail"],
                        "label": img.get("label", term_data.get("Name", "")),
                        "template_id": template_id,
                    })

    # Class terms have Examples
    examples = term_data.get("Examples", {})
    if examples and not thumbnails:
        for template_id, example_list in examples.items():
            for ex in example_list:
                if ex.get("thumbnail"):
                    thumbnails.append({
                        "url": ex["thumbnail"],
                        "label": ex.get("label", term_data.get("Name", "")),
                        "template_id": template_id,
                    })

    return thumbnails[:4]  # Limit to 4

def format_tags_badges(tags):
    """Format tags as Bootstrap badge HTML spans."""
    if not tags:
        return ""
    badges = []
    for tag in tags:
        display_tag = tag.replace('_', ' ')
        badges.append(f'<span class="badge bg-secondary">{display_tag}</span>')
    return " ".join(badges)

def format_synonyms_table(synonyms):
    """Format Synonyms array as a markdown table."""
    if not synonyms:
        return ""

    lines = [
        "| Synonym | Scope | Reference |",
        "|---------|-------|-----------|",
    ]
    for syn in synonyms:
        label = syn.get("label", "")
        scope = syn.get("scope", "").replace("has_", "").replace("_", " ")
        pub = syn.get("publication", "")
        pub_converted = convert_internal_links(pub) if pub else ""
        lines.append(f'| {label} | {scope} | {pub_converted} |')
    return "\n".join(lines)

def format_query_preview(query, term_id):
    """Format a Query's preview_results as an HTML table with thumbnails.

    Emitted as a complete raw HTML <table> rather than a markdown table wrapped
    in <div class="table-responsive">. Hugo's Goldmark does not process markdown
    nested inside a raw HTML block, so the wrapped-markdown form leaked every
    `[label](id)` cell as literal text and never rendered as a table. A full
    HTML table renders verbatim under unsafe=true. The `###` heading and the
    "View all" button stay outside the block, separated by blank lines so
    Goldmark closes each HTML block cleanly.
    """
    preview = query.get("preview_results", {})
    rows = preview.get("rows", [])
    if not rows:
        return ""

    label = query.get("label", "Query")
    count = query.get("count", 0)
    query_name = query.get("query", "")

    lines = []
    lines.append(f'### {label} ({count} total)')
    lines.append("")
    lines.append('<div class="table-responsive">')
    lines.append('<table class="table">')
    lines.append('<thead><tr><th>Thumbnail</th><th>Name</th><th>Tags</th></tr></thead>')
    lines.append('<tbody>')

    for row in rows:
        # Name — may be `[label](id)` markdown from the API; emit as an anchor
        # because it lives inside a raw HTML block (Goldmark won't linkify it).
        name_raw = row.get("label", row.get("name", ""))
        name_md = convert_internal_links(name_raw)
        row_id = row.get("id", "")
        if row_id and is_known_id(row_id) and name_md == name_raw and name_raw:
            name_md = f'[{name_raw}]({get_report_url(row_id)})'
        name_html = linkify_html(name_md) if "](" in name_md else name_md

        # Tags
        tags_raw = row.get("tags", "")
        tags_display = tags_raw.replace("|", ", ") if tags_raw else ""

        # Thumbnail — pull the URL out of `[![alt](url 'title')](link)` markdown.
        thumb_raw = row.get("thumbnail", "")
        thumb_html = ""
        if thumb_raw:
            img_match = re.search(r'!\[[^\]]*\]\(([^\s)]+)', thumb_raw)
            if img_match:
                thumb_url = img_match.group(1)
                thumb_html = (f'<a href="{VFB_BROWSER_BASE}?id={row_id}">'
                              f'<img src="{thumb_url}" width="80" style="background:#000; border-radius:2px;"/></a>')

        lines.append(f'<tr><td>{thumb_html}</td><td>{name_html}</td><td>{tags_display}</td></tr>')

    lines.append('</tbody>')
    lines.append('</table>')
    lines.append('</div>')
    lines.append("")
    lines.append(f'<a href="{get_query_results_url(term_id, query_name)}" class="btn btn-outline-primary btn-sm">View all {count} results in VFB &rarr;</a>')
    lines.append("")

    return "\n".join(lines)

def format_downloads(images):
    """Format download links from Images entries."""
    if not images:
        return ""

    lines = []
    for template_id, image_list in images.items():
        for img in image_list:
            template_label = template_id
            has_downloads = any(img.get(k) for k in ("nrrd", "obj", "swc", "wlz"))
            if not has_downloads:
                continue

            lines.append(f'Image files aligned to {img.get("label", template_label)}:')
            lines.append("")
            if img.get("obj"):
                lines.append(f'- [Pointcloud (OBJ)]({img["obj"]})')
            if img.get("swc"):
                lines.append(f'- [Skeleton (SWC)]({img["swc"]})')
            if img.get("wlz"):
                lines.append(f'- [Slices (Woolz)]({img["wlz"]})')
            if img.get("nrrd"):
                lines.append(f'- [Signal (NRRD)]({img["nrrd"]})')
            lines.append("")

    return "\n".join(lines)

def format_licenses(licenses):
    """Format Licenses dict into markdown."""
    if not licenses:
        return ""

    lines = []
    for key, lic in licenses.items():
        label = lic.get("label", "Unknown License")
        source = lic.get("source", "")
        source_iri = lic.get("source_iri", "")
        if source and source_iri:
            lines.append(f'- **{label}** — Source: [{source}]({source_iri})')
        elif source:
            lines.append(f'- **{label}** — Source: {source}')
        else:
            lines.append(f'- **{label}**')
    return "\n".join(lines)

def format_publications(publications):
    """Format Publications array into markdown with external links."""
    if not publications:
        return ""

    lines = []
    for pub in publications:
        core = pub.get("core", {})
        label = core.get("label", core.get("symbol", ""))
        short_form = core.get("short_form", "")

        parts = [f'- {convert_internal_links(f"[{label}]({short_form})")}']

        ext_links = []
        if pub.get("DOI"):
            ext_links.append(f'[DOI](https://doi.org/{pub["DOI"]})')
        if pub.get("PubMed"):
            ext_links.append(f'[PubMed](https://pubmed.ncbi.nlm.nih.gov/{pub["PubMed"]})')
        if pub.get("FlyBase"):
            ext_links.append(f'[FlyBase](https://flybase.org/reports/{pub["FlyBase"]})')

        if ext_links:
            parts.append(f' ({" | ".join(ext_links)})')

        lines.append("".join(parts))
    return "\n".join(lines)

def format_xrefs(xrefs, term_name):
    """Format Xrefs (external cross-references) into markdown links.

    Each xref is {label, accession, link, icon}. The cached get_term_info
    endpoint resolves the full external URL in `link`, so we link to it
    directly rather than rebuilding from a link_base/accession template
    (cf. VFBProcessTermInfoJson.xref.getLink). Link text mirrors the VFB
    browser's "Cross References" section: "<term> on <site>".
    """
    if not xrefs:
        return ""

    lines = []
    for xref in xrefs:
        link = xref.get("link", "")
        if not link:
            continue
        label = xref.get("label", "")
        text = f'{term_name} on {label}' if (term_name and label) else (label or link)
        accession = xref.get("accession", "")
        suffix = f' ({accession})' if accession and accession not in ("None", "") else ""
        lines.append(f'- [{text}]({link}){suffix}')
    return "\n".join(lines)

def format_related_tools(tools, term_id):
    """Format RelatedTools into the VFB browser's "Graphs For" links.

    Each tool is {tool, label, default_args}. These launch graph/hierarchy
    tools on the term inside the 3D browser; link to the term there so the
    user can run them (the browser exposes the tool set once the term loads).
    """
    if not tools:
        return ""

    lines = []
    for t in tools:
        label = t.get("label", t.get("tool", ""))
        if not label:
            continue
        lines.append(f'- [{label}]({VFB_BROWSER_BASE}?id={term_id})')
    return "\n".join(lines)

def build_hero_card(name, term_id, tags_badges, description_html, comment_html, thumbnails):
    """Build the hero card without blank lines that break Markdown HTML blocks."""
    lines = [
        '<div class="card mb-4 border-primary">',
        '<div class="card-body">',
        '<div class="row">',
        '<div class="col-md-4 text-center">',
    ]

    for thumb in thumbnails:
        lines.append(
            f'    <a href="{VFB_BROWSER_BASE}?id={term_id}">'
            f'<img src="{thumb["url"]}" alt="{name}" class="img-fluid rounded" '
            f'style="max-width:200px; background:#000; margin:4px;"/></a>'
        )

    lines.extend([
        '</div>',
        '<div class="col-md-8">',
        f'    <h4>{name}</h4>',
        f'    <p class="text-muted"><strong>ID:</strong> {term_id}</p>',
        f'    <div class="mb-2">{tags_badges}</div>',
    ])

    if description_html:
        lines.append(f'    {description_html}')
    if comment_html:
        lines.append(f'    {comment_html}')

    lines.extend([
        f'    <a href="{VFB_BROWSER_BASE}?id={term_id}" class="btn btn-primary btn-lg mt-2">Open in VFB 3D Browser &rarr;</a>',
        '</div>',
        '</div>',
        '</div>',
        '</div>',
    ])

    return "\n".join(lines)

# ─── Page Generation ─────────────────────────────────────────────────────────

def generate_page(term_data):
    """Generate the complete Hugo markdown page from API term data."""
    name = term_data.get("Name", "Unknown")
    term_id = term_data.get("Id", "")
    meta = term_data.get("Meta", {})
    tags = term_data.get("Tags", [])
    synonyms = term_data.get("Synonyms", [])
    queries = term_data.get("Queries", [])
    licenses = term_data.get("Licenses", {})
    publications = term_data.get("Publications", [])
    technique = term_data.get("Technique", [])
    images = term_data.get("Images", {})
    examples = term_data.get("Examples", {})
    xrefs = term_data.get("Xrefs", [])
    related_tools = term_data.get("RelatedTools", [])

    # Description for front matter
    description = meta.get("Description", "")
    if not description:
        # Fallback to Types text
        description = meta.get("Types", "")
    # Strip markdown link syntax to plain labels: the front-matter description
    # becomes the <meta name="description"> tag and page summary, where raw
    # `[label](id)` syntax would show literally.
    description = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', description)
    # Clean for YAML
    description = description.replace('"', '\\"').replace("\n", " ").replace("\r", " ").strip()

    # Comment
    comment = meta.get("Comment", "")

    # URL slug
    url_slug = get_term_url(name, term_id)

    # Tags for front matter
    # Build a clean list and drop empties, otherwise a term with no Tags
    # yields a leading comma (e.g. "[,VFB]") which is invalid YAML flow syntax
    tag_list = list(tags)
    if "_" in term_id:
        tag_list.append(term_id.split("_")[0])
    elif term_id.startswith("FB"):
        tag_list.append(term_id[0:4])
    tags_csv = ",".join(t for t in tag_list if t)

    # Thumbnails
    thumbnails = get_thumbnails(term_data)

    # Build the page
    sections = []

    # ── Front matter ──
    sections.append(f'''---
title: "{name.replace(chr(92), "&bsol;")} [{term_id}]"
linkTitle: "{name.replace(chr(92), "&bsol;")}"
tags: [{tags_csv}]
content: [term]
date: 2022-01-01
description: >
    {description}
weight: 10000
sitemap_exclude: true
canonicalUrl: "https://www.virtualflybrain.org/term/{url_slug}/"
---
''')

    # ── Hero section ──
    tags_badges = format_tags_badges(tags)

    desc_html = ""
    if meta.get("Description"):
        desc_html = f'<p>{linkify_html(meta["Description"])}</p>'

    comment_html = ""
    if comment:
        comment_html = f'<p class="text-muted"><em>{linkify_html(comment)}</em></p>'

    sections.append(build_hero_card(name, term_id, tags_badges, desc_html, comment_html, thumbnails))

    # ── Classification ──
    types_text = meta.get("Types", "")
    if types_text:
        types_md = format_types_section(types_text)
        sections.append(f'## Classification\n\n{types_md}\n')

    # ── Relationships ──
    rels_text = meta.get("Relationships", "")
    if rels_text:
        rels_md = format_relationships_section(rels_text)
        sections.append(f'## Relationships\n\n{rels_md}\n')

    # ── Synonyms ──
    if synonyms:
        syn_md = format_synonyms_table(synonyms)
        sections.append(f'## Alternative Names\n\n{syn_md}\n')

    # ── Cross references (external databases) ──
    if xrefs:
        xref_md = format_xrefs(xrefs, name)
        if xref_md.strip():
            sections.append(f'## Cross References\n\n{xref_md}\n')

    # ── Technique ──
    if technique:
        tech_lines = "\n".join(f'- {t}' for t in technique)
        sections.append(f'## Imaging Technique\n\n{tech_lines}\n')

    # ── Licenses ──
    if licenses:
        lic_md = format_licenses(licenses)
        sections.append(f'## License\n\n{lic_md}\n')

    # ── Downloads (individual Images and class Examples) ──
    # Class terms carry their downloadable volumes under Examples (one list
    # per template), individuals under Images. Merge both so class pages get
    # download links too, matching the browser's Available Images downloads.
    download_sources = {}
    for tpl, img_list in images.items():
        download_sources.setdefault(tpl, []).extend(img_list)
    for tpl, ex_list in examples.items():
        download_sources.setdefault(tpl, []).extend(ex_list)
    if download_sources:
        dl_md = format_downloads(download_sources)
        if dl_md.strip():
            sections.append(f'## Downloads\n\n{dl_md}\n')

    # ── Query Previews ──
    for q in queries:
        preview = q.get("preview_results", {})
        rows = preview.get("rows", [])
        if rows:
            q_md = format_query_preview(q, term_id)
            sections.append(q_md)

    # ── Graphs For (related graph/hierarchy tools) ──
    if related_tools:
        tools_md = format_related_tools(related_tools, term_id)
        if tools_md.strip():
            sections.append(f'## Graphs For\n\n{tools_md}\n')

    # ── Publications ──
    if publications:
        pub_md = format_publications(publications)
        sections.append(f'## References\n\n{pub_md}\n')

    # Join with a blank line between every section. Goldmark keeps a raw HTML
    # block (e.g. the hero card) open until a blank line, so without this the
    # first heading after the hero ("## Classification") gets swallowed into
    # the HTML block and printed literally instead of rendered as a heading.
    return "\n\n".join(sections)

# ─── Term Saving ─────────────────────────────────────────────────────────────

def get_vfb_connect():
    """Lazy-initialize VfbConnect (only needed for batch ID listing)."""
    global _vc
    if '_vc' not in globals() or _vc is None:
        from vfb_connect.cross_server_tools import VfbConnect
        _vc = VfbConnect()
    return _vc

def fetch_ids(label, query):
    """Fetch and log IDs for one query."""
    print(f"Fetching ID list for {label}...")
    data = get_vfb_connect().nc.commit_list([query])
    ids = data[0]['data'][0]['row'][0]
    print(f"  Retrieved {len(ids)} IDs for {label}")
    return ids

def process_group(base_path, relative_dir, label, query):
    """Change directory, fetch IDs, and generate pages for one ontology group."""
    target_dir = os.path.normpath(join(base_path, relative_dir))
    print(f"\n[{label}] {target_dir}")
    chdir(target_dir)
    save_terms(fetch_ids(label, query))

def process_term(term_id):
    """Fetch, render and write one term page. Returns a status string.

    Runs inside a worker thread. Writes to a temp file then atomically renames
    so a killed build never leaves a half-written page. Throttling against the
    server's capacity happens inside fetch_term_info via throttle().
    """
    filename = term_id + "_v" + str(version) + ".md"
    if os.path.isfile(filename):
        return "skip"

    term_data = fetch_term_info(term_id)
    if term_data is None:
        return "fail"

    page_content = generate_page(term_data)

    tmp = f"{filename}.{os.getpid()}.{threading.get_ident()}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(page_content)
    os.replace(tmp, filename)

    # Clean up previous version
    old_filename = term_id + "_v" + str(version - 1) + ".md"
    if os.path.isfile(old_filename):
        try:
            os.remove(old_filename)
        except OSError:
            pass
    return "ok"

def save_terms(ids):
    """Fetch and save term pages for a list of IDs, concurrently.

    A bounded ThreadPoolExecutor keeps up to MAX_WORKERS requests in flight so
    the server's ~20 query slots stay busy, instead of the old one-at-a-time
    loop that left them idle. The in-flight window is capped so building the
    future set for a 600k-id group doesn't balloon memory.
    """
    total = len(ids)
    counts = {"ok": 0, "skip": 0, "fail": 0}
    done = 0
    window = MAX_WORKERS * 4
    progress_every = max(100, window)

    def record(fut, tid):
        nonlocal done
        try:
            status = fut.result()
        except Exception as e:
            status = "fail"
            print(f"ERROR processing {tid}: {e}")
            print(traceback.format_exc())
        counts[status] = counts.get(status, 0) + 1
        done += 1
        if status == "fail" or done % progress_every == 0:
            print(f"  {done}/{total} processed "
                  f"(created={counts['ok']} skipped={counts['skip']} failed={counts['fail']}) "
                  f"last={tid}:{status}")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        inflight = {}
        for term_id in ids:
            inflight[ex.submit(process_term, term_id)] = term_id
            if len(inflight) >= window:
                finished, _ = wait(set(inflight), return_when=FIRST_COMPLETED)
                for fut in finished:
                    record(fut, inflight.pop(fut))
        for fut in as_completed(set(inflight)):
            record(fut, inflight[fut])

    print(f"\nBatch complete: {counts['ok']} created, {counts['skip']} skipped (existing), "
          f"{counts['fail']} failed out of {total} total")

# ─── Testing ─────────────────────────────────────────────────────────────────

def test_term_page(term_id, term_type="class"):
    """Test page generation for a single term."""
    print(f"Fetching {term_id} from VFBquery API...")
    term_data = fetch_term_info(term_id)

    if term_data is None:
        print(f"ERROR: Could not fetch {term_id}")
        return False

    print(f"  Name: {term_data.get('Name')}")
    print(f"  IsClass: {term_data.get('IsClass')}")
    print(f"  IsIndividual: {term_data.get('IsIndividual')}")
    print(f"  Tags: {term_data.get('Tags')}")
    print(f"  Queries: {len(term_data.get('Queries', []))}")
    print(f"  Images: {len(term_data.get('Images', {}))}")
    print(f"  Examples: {len(term_data.get('Examples', {}))}")
    print(f"  Synonyms: {len(term_data.get('Synonyms', []))}")
    print(f"  Licenses: {len(term_data.get('Licenses', {}))}")

    print(f"\nGenerating {term_type} page...")
    page_content = generate_page(term_data)

    filename = f"{term_id}_v{version}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_content)

    print(f"  Written to {filename} ({len(page_content)} bytes)")

    # Verify key sections
    checks = {
        "Front matter": "canonicalUrl:" in page_content,
        "Hero card": 'class="card mb-4' in page_content,
        "VFB browser link": VFB_BROWSER_BASE in page_content,
        "Tags badges": 'badge bg-secondary' in page_content,
    }

    if term_data.get("Meta", {}).get("Types"):
        checks["Classification"] = "## Classification" in page_content
    if term_data.get("Meta", {}).get("Relationships"):
        checks["Relationships"] = "## Relationships" in page_content
    if term_data.get("Synonyms"):
        checks["Synonyms"] = "## Alternative Names" in page_content
    if term_data.get("Xrefs"):
        checks["Cross References"] = "## Cross References" in page_content
    if term_data.get("Licenses"):
        checks["Licenses"] = "## License" in page_content
    if term_data.get("Images") or term_data.get("Examples"):
        checks["Downloads"] = "## Downloads" in page_content
    if any(q.get("preview_results", {}).get("rows") for q in term_data.get("Queries", [])):
        checks["Query previews"] = "table-responsive" in page_content
    if term_data.get("RelatedTools"):
        checks["Graphs For"] = "## Graphs For" in page_content

    all_pass = True
    for check_name, result in checks.items():
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {check_name}")

    return all_pass

def test_hero_card_regression():
    """Ensure optional empty fields do not turn the hero CTA into a code block."""
    print("=" * 60)
    print("Test 0: Hero card CTA markdown regression")
    print("=" * 60)

    term_data = {
        "Name": "adult intercalary segment",
        "Id": "FBbt_00003013",
        "Meta": {
            "Description": "Any intercalary segment of the adult.",
            "Comment": "",
            "Types": "[adult procephalic segment](FBbt_00003010); [intercalary segment](FBbt_00000010)",
        },
        "Tags": ["Adult", "Anatomy"],
        "Synonyms": [],
        "Queries": [],
        "Licenses": {},
        "Publications": [],
        "Technique": [],
        "Images": {},
        "Examples": {},
    }

    page_content = generate_page(term_data)
    hero_cta = f'<a href="{VFB_BROWSER_BASE}?id=FBbt_00003013" class="btn btn-primary btn-lg mt-2">Open in VFB 3D Browser &rarr;</a>'

    checks = {
        "Hero CTA present": hero_cta in page_content,
        "No blank line before hero CTA": "\n    \n    <a href=" not in page_content,
        "Description directly precedes hero CTA": (
            '<p>Any intercalary segment of the adult.</p>\n'
            f'    {hero_cta}'
        ) in page_content,
    }

    all_pass = True
    for check_name, result in checks.items():
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {check_name}")

    return all_pass

def test_report_link_regression():
    """Ensure generated term links point at VFB report URLs."""
    print("=" * 60)
    print("Test 1: Report link regression")
    print("=" * 60)

    converted = convert_internal_links("[DNb08](FBbt_20011340)")
    query_preview = format_query_preview(
        {
            "label": "Neurons with some part in adult intercalary segment",
            "count": 2,
            "preview_results": {
                "rows": [
                    {
                        "label": "[DNb08](FBbt_20011340)",
                        "id": "FBbt_20011340",
                        "tags": "Adult|Cholinergic|Nervous_system|primary_neuron",
                        "thumbnail": '[![DNb08](https://www.virtualflybrain.org/data/VFB/i/jrmc/37nx/VFB_00101567/thumbnail.png)](FBbt_20011340)',
                    },
                    {
                        "label": "DNp45",
                        "id": "FBbt_20011346",
                        "tags": "Adult|Cholinergic|Nervous_system|primary_neuron",
                    },
                ]
            },
        },
        "FBbt_00003013",
    )

    checks = {
        "Markdown links use report path": converted == "[DNb08](/reports/FBbt_20011340)",
        "Query preview preserves report link": '<a href="/reports/FBbt_20011340">DNb08</a>' in query_preview,
        "Plain row labels get report link": '<a href="/reports/FBbt_20011346">DNp45</a>' in query_preview,
    }

    all_pass = True
    for check_name, result in checks.items():
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {check_name}")

    return all_pass

def test_query_button_regression():
    """Ensure query preview buttons open the matching VFB query."""
    print("=" * 60)
    print("Test 2: Query button regression")
    print("=" * 60)

    query_preview = format_query_preview(
        {
            "label": "Neurons with some part in adult intercalary segment",
            "query": "NeuronsPartHere",
            "count": 666,
            "preview_results": {
                "rows": [
                    {
                        "label": "[DNb08](FBbt_20011340)",
                        "id": "FBbt_20011340",
                        "tags": "Adult|Cholinergic|Nervous_system|primary_neuron",
                    },
                ]
            },
        },
        "FBbt_00003013",
    )

    expected_query_url = f'{VFB_BROWSER_BASE}?q=FBbt_00003013,NeuronsPartHere'
    fallback_url = f'{VFB_BROWSER_BASE}?id=FBbt_00003013'

    checks = {
        "Query button uses VFB query URL": expected_query_url in query_preview,
        "Query button no longer uses term-only URL": fallback_url not in query_preview,
        "Helper falls back to term URL when missing query": get_query_results_url("FBbt_00003013", "") == fallback_url,
    }

    all_pass = True
    for check_name, result in checks.items():
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {check_name}")

    return all_pass

def test_medulla_page():
    """Test page generation for medulla (class) and fru-M-200266 (individual)."""
    result0 = test_hero_card_regression()
    result1 = test_report_link_regression()
    result2 = test_query_button_regression()

    print()
    print("=" * 60)
    print("Test 3: Class term — medulla (FBbt_00003748)")
    print("=" * 60)
    result3 = test_term_page("FBbt_00003748", "class")

    print()
    print("=" * 60)
    print("Test 4: Individual term — fru-M-200266 (VFB_00000001)")
    print("=" * 60)
    result4 = test_term_page("VFB_00000001", "individual")

    print()
    if result0 and result1 and result2 and result3 and result4:
        print("All tests PASSED")
        return True
    else:
        print("Some tests FAILED")
        return False

# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) > 1:
        mypath = sys.argv[1]
        print("Updating all files in " + mypath)
        groups = [
            ('fbbt/', 'FBbt classes', "MATCH (n:Class) WHERE n.short_form starts with 'FBbt' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('fbbi/', 'FBbi classes', "MATCH (n:Class) WHERE n.short_form starts with 'FBbi' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('fbcv/', 'FBcv classes', "MATCH (n:Class) WHERE n.short_form starts with 'FBcv' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('fbdv/', 'FBdv classes', "MATCH (n:Class) WHERE n.short_form starts with 'FBdv' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('vfb/', 'VFB individuals', "MATCH (n:Individual) WHERE n.short_form starts with 'VFB_' AND NOT n.short_form starts with 'VFB_internal' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('vfb/', 'VFBexp classes', "MATCH (n:Class) WHERE n.short_form starts with 'VFBexp_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('datasets/', 'Datasets', "MATCH (n:DataSet) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('go/', 'GO classes', "MATCH (n:Class) WHERE n.short_form starts with 'GO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('so/', 'SO classes', "MATCH (n:Class) WHERE n.short_form starts with 'SO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('ioa/', 'IAO classes', "MATCH (n:Class) WHERE n.short_form starts with 'IAO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('geno/', 'GENO classes', "MATCH (n:Class) WHERE n.short_form starts with 'GENO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('pato/', 'PATO classes', "MATCH (n:Class) WHERE n.short_form starts with 'PATO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('pco/', 'PCO classes', "MATCH (n:Class) WHERE n.short_form starts with 'PCO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('uberon/', 'UBERON classes', "MATCH (n:Class) WHERE n.short_form starts with 'UBERON_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('ro/', 'RO classes', "MATCH (n:Class) WHERE n.short_form starts with 'RO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('obi/', 'OBI classes', "MATCH (n:Class) WHERE n.short_form starts with 'OBI_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('ncbitaxon/', 'NCBITaxon classes', "MATCH (n:Class) WHERE n.short_form starts with 'NCBITaxon_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('zp/', 'ZP classes', "MATCH (n:Class) WHERE n.short_form starts with 'ZP_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('wbphenotype/', 'WBPhenotype classes', "MATCH (n:Class) WHERE n.short_form starts with 'WBPhenotype_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('caro/', 'CARO classes', "MATCH (n:Class) WHERE n.short_form starts with 'CARO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('bfo/', 'BFO classes', "MATCH (n:Class) WHERE n.short_form starts with 'BFO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
            ('flybase/', 'FlyBase classes', "MATCH (n:Class) WHERE n.short_form starts with 'FB' AND NOT n.short_form contains '_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"),
        ]

        for relative_dir, label, query in groups:
            process_group(mypath, relative_dir, label, query)

    else:
        print("Testing term page generation...")
        success = test_medulla_page()
        if not success:
            sys.exit(1)
