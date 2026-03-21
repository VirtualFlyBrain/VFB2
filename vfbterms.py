#!/usr/bin/env python3

import sys
from os import listdir, chdir
from os.path import isfile, join
import os
import warnings
import re
import json
import datetime
import traceback
import time

# Suppress the urllib3 warning about OpenSSL
warnings.filterwarnings('ignore', category=Warning)

# Set environment variable to skip GUI dependencies
os.environ['VFB_SKIP_GUI'] = '1'

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

version = 7

API_BASE = "https://v3-cached.virtualflybrain.org/get_term_info"
VFB_BROWSER_BASE = "https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto"

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
        total=2,
        backoff_factor=120,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=10, pool_maxsize=10)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session

session = create_session()

# ─── Data Fetching ───────────────────────────────────────────────────────────

def fetch_term_info(term_id):
    """Fetch term info from VFBquery API. Returns dict or None on error."""
    try:
        resp = session.get(API_BASE, params={"id": term_id}, timeout=9000)
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

def is_known_id(identifier):
    """Check if an identifier matches a known VFB prefix."""
    return any(identifier.startswith(p) for p in KNOWN_PREFIXES)

def convert_internal_links(text):
    """Convert API markdown links [label](ID) to site inter-page links.

    Handles:
    - Simple links: [medulla](FBbt_00003748) → [medulla](/term/slug/)
    - IDs that aren't known prefixes are left as-is
    """
    if not text:
        return ""

    def replace_link(match):
        label = match.group(1)
        identifier = match.group(2)
        if is_known_id(identifier):
            slug = get_term_url(label, identifier)
            return f'[{label}](/term/{slug}/)'
        return match.group(0)

    # Use a pattern that handles nested brackets in labels (e.g. gene names with [allele])
    # Match: [ ... ]( ID ) where the ID part has no spaces or parens
    return re.sub(r'\[([^\]]*(?:\[[^\]]*\][^\]]*)*)\]\(([^)\s]+)\)', replace_link, text)

def format_relationships_section(relationships_text):
    """Format Meta.Relationships into markdown bullets.

    Input format: [rel_name](rel_id): [target1](id1), [target2](id2); [rel2](id): [target](id)
    Output: - **rel_name**: [target1](/term/...), [target2](/term/...)
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
    Output: - [type1](/term/slug1/)
            - [type2](/term/slug2/)
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
    """Format a Query's preview_results as a markdown table with thumbnails."""
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
    lines.append("")
    lines.append("| Thumbnail | Name | Tags |")
    lines.append("|-----------|------|------|")

    for row in rows:
        # Extract name — may be markdown link like [name](id)
        name_raw = row.get("label", row.get("name", ""))
        name_converted = convert_internal_links(name_raw)

        # Extract tags
        tags_raw = row.get("tags", "")
        tags_display = tags_raw.replace("|", ", ") if tags_raw else ""

        # Extract thumbnail — may be markdown image like [![alt](url)](link)
        thumb_raw = row.get("thumbnail", "")
        thumb_html = ""
        if thumb_raw:
            # Extract URL from markdown image: [![alt](url "title")](link)
            img_match = re.search(r'!\[[^\]]*\]\(([^\s)]+)', thumb_raw)
            if img_match:
                thumb_url = img_match.group(1)
                row_id = row.get("id", "")
                thumb_html = f'<a href="{VFB_BROWSER_BASE}?id={row_id}"><img src="{thumb_url}" width="80" style="background:#000; border-radius:2px;"/></a>'

        lines.append(f'| {thumb_html} | {name_converted} | {tags_display} |')

    lines.append("")
    lines.append("</div>")
    lines.append("")
    lines.append(f'<a href="{VFB_BROWSER_BASE}?id={term_id}" class="btn btn-outline-primary btn-sm">View all {count} results in VFB &rarr;</a>')
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

    # Description for front matter
    description = meta.get("Description", "")
    if not description:
        # Fallback to Types text (stripped of markdown links)
        types_text = meta.get("Types", "")
        description = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', types_text)
    # Clean for YAML
    description = description.replace('"', '\\"').replace("\n", " ").replace("\r", " ").strip()

    # Comment
    comment = meta.get("Comment", "")

    # URL slug
    url_slug = get_term_url(name, term_id)

    # Tags for front matter
    tags_csv = ",".join(tags)
    if "_" in term_id:
        tags_csv += "," + term_id.split("_")[0]
    elif term_id.startswith("FB"):
        tags_csv += "," + term_id[0:4]

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
    thumb_html = ""
    if thumbnails:
        thumb_imgs = []
        for t in thumbnails:
            thumb_imgs.append(
                f'<a href="{VFB_BROWSER_BASE}?id={term_id}">'
                f'<img src="{t["url"]}" alt="{name}" class="img-fluid rounded" '
                f'style="max-width:200px; background:#000; margin:4px;"/></a>'
            )
        thumb_html = "\n    ".join(thumb_imgs)

    tags_badges = format_tags_badges(tags)

    desc_html = ""
    if meta.get("Description"):
        desc_html = f'<p>{convert_internal_links(meta["Description"])}</p>'

    comment_html = ""
    if comment:
        comment_html = f'<p class="text-muted"><em>{convert_internal_links(comment)}</em></p>'

    sections.append(f'''<div class="card mb-4 border-primary">
<div class="card-body">
<div class="row">
<div class="col-md-4 text-center">
    {thumb_html}
</div>
<div class="col-md-8">
    <h4>{name}</h4>
    <p class="text-muted"><strong>ID:</strong> {term_id}</p>
    <div class="mb-2">{tags_badges}</div>
    {desc_html}
    {comment_html}
    <a href="{VFB_BROWSER_BASE}?id={term_id}" class="btn btn-primary btn-lg mt-2">Open in VFB 3D Browser &rarr;</a>
</div>
</div>
</div>
</div>
''')

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

    # ── Technique ──
    if technique:
        tech_lines = "\n".join(f'- {t}' for t in technique)
        sections.append(f'## Imaging Technique\n\n{tech_lines}\n')

    # ── Licenses ──
    if licenses:
        lic_md = format_licenses(licenses)
        sections.append(f'## License\n\n{lic_md}\n')

    # ── Downloads ──
    if images:
        dl_md = format_downloads(images)
        if dl_md.strip():
            sections.append(f'## Downloads\n\n{dl_md}\n')

    # ── Query Previews ──
    for q in queries:
        preview = q.get("preview_results", {})
        rows = preview.get("rows", [])
        if rows:
            q_md = format_query_preview(q, term_id)
            sections.append(q_md)

    # ── Publications ──
    if publications:
        pub_md = format_publications(publications)
        sections.append(f'## References\n\n{pub_md}\n')

    return "\n".join(sections)

# ─── Term Saving ─────────────────────────────────────────────────────────────

def get_vfb_connect():
    """Lazy-initialize VfbConnect (only needed for batch ID listing)."""
    global _vc
    if '_vc' not in globals() or _vc is None:
        from vfb_connect.cross_server_tools import VfbConnect
        _vc = VfbConnect()
    return _vc

def save_terms(ids):
    """Fetch and save term pages for a list of IDs."""
    total = len(ids)
    success_count = 0
    skip_count = 0
    fail_count = 0
    for i, term_id in enumerate(ids):
        try:
            filename = term_id + "_v" + str(version) + ".md"
            if os.path.isfile(filename):
                skip_count += 1
                continue

            print(f"Processing {term_id} ({i+1}/{total})...")
            term_data = fetch_term_info(term_id)
            if term_data is None:
                fail_count += 1
                continue

            page_content = generate_page(term_data)

            with open(filename, "w", encoding="utf-8") as f:
                f.write(page_content)

            success_count += 1

            # Clean up previous version
            old_filename = term_id + "_v" + str(version - 1) + ".md"
            if os.path.isfile(old_filename):
                os.remove(old_filename)
                print(f'Removed: {old_filename}')

            # Brief pause to avoid overwhelming the API
            time.sleep(0.5)

        except Exception as e:
            fail_count += 1
            print(f"ERROR processing {term_id}: {str(e)}")
            print(traceback.format_exc())

    print(f"\nBatch complete: {success_count} created, {skip_count} skipped (existing), {fail_count} failed out of {total} total")

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
    if term_data.get("Licenses"):
        checks["Licenses"] = "## License" in page_content
    if term_data.get("Images"):
        checks["Downloads"] = "## Downloads" in page_content
    if any(q.get("preview_results", {}).get("rows") for q in term_data.get("Queries", [])):
        checks["Query previews"] = "table-responsive" in page_content

    all_pass = True
    for check_name, result in checks.items():
        status = "PASS" if result else "FAIL"
        if not result:
            all_pass = False
        print(f"  [{status}] {check_name}")

    return all_pass

def test_medulla_page():
    """Test page generation for medulla (class) and fru-M-200266 (individual)."""
    print("=" * 60)
    print("Test 1: Class term — medulla (FBbt_00003748)")
    print("=" * 60)
    result1 = test_term_page("FBbt_00003748", "class")

    print()
    print("=" * 60)
    print("Test 2: Individual term — fru-M-200266 (VFB_00000001)")
    print("=" * 60)
    result2 = test_term_page("VFB_00000001", "individual")

    print()
    if result1 and result2:
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
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        chdir(mypath + 'fbbt/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbt' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
        chdir(mypath + 'fbbi/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbi' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
        chdir(mypath + 'fbcv/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBcv' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
        chdir(mypath + 'fbdv/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBdv' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
        chdir(mypath + 'vfb/')
        vfb = get_vfb_connect().nc.commit_list(["MATCH (n:Individual) WHERE n.short_form starts with 'VFB_' AND NOT n.short_form starts with 'VFB_internal' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0]
        save_terms(vfb)
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'VFBexp_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + '../datasets/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:DataSet) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'go/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'GO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'so/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'SO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'ioa/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'IAO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'geno/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'GENO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'pato/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'PATO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'pco/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'PCO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'uberon/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'UBERON_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'ro/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'RO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'obi/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'OBI_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'ncbitaxon/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'NCBITaxon_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'zp/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'ZP_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'wbphenotype/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'WBPhenotype_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'caro/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'CARO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'bfo/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'BFO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

        chdir(mypath + 'flybase/')
        save_terms(get_vfb_connect().nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FB' AND NOT n.short_form contains '_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

    else:
        print("Testing term page generation...")
        success = test_medulla_page()
        if not success:
            sys.exit(1)
