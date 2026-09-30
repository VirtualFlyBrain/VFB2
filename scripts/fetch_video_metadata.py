#!/usr/bin/env python3
"""Regenerate data/videos.json from YouTube.

The youtube shortcode emits schema.org VideoObject markup for any video ID
present in data/videos.json. Google needs name, description, thumbnailUrl and
uploadDate before it will treat an embed as anything more than an unlabelled
iframe; without them it guesses from layout, and it guesses inconsistently
(two structurally identical news posts, one indexed, one "not on a watch
page").

This scrapes the watch page rather than using the Data API: no key to manage,
and the JSON blob it reads (ytInitialPlayerResponse) carries everything the
schema needs. It must run somewhere that can reach youtube.com directly --
the Cowork cloud sandbox is proxied and gets a 403, a workstation is fine.

    python3 scripts/fetch_video_metadata.py            # refresh every ID in content/
    python3 scripts/fetch_video_metadata.py --only ID  # one video, repeatable

Descriptions are truncated to a single paragraph: schema.org wants a summary,
and a full YouTube description is mostly links and credits.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT = ROOT / "data" / "videos.json"

# Matches {{< youtube id="XXXXXXXXXXX" ... >}} and the positional {{< youtube XXXXXXXXXXX >}}.
SHORTCODE = re.compile(r'{{<\s*youtube\s+(?:id=")?([A-Za-z0-9_-]{11})"?')

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

DESC_MAX = 500


def discover_ids() -> list[str]:
    ids: list[str] = []
    for path in sorted(CONTENT.rglob("*.md")):
        for match in SHORTCODE.finditer(path.read_text(encoding="utf-8", errors="replace")):
            if match.group(1) not in ids:
                ids.append(match.group(1))
    return ids


def fetch(video_id: str) -> str:
    req = urllib.request.Request(
        f"https://www.youtube.com/watch?v={video_id}",
        headers={"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def player_response(html: str) -> dict:
    """Pull ytInitialPlayerResponse out of the watch page.

    The blob is assigned inline and followed by ';var' or ';</script>'. Brace
    matching is more reliable than a regex here: the JSON contains both.
    """
    marker = "ytInitialPlayerResponse = "
    start = html.find(marker)
    if start < 0:
        raise ValueError("ytInitialPlayerResponse not found")
    start += len(marker)
    depth = 0
    in_string = False
    escaped = False
    for i in range(start, len(html)):
        ch = html[i]
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue
        if ch == '"':
            in_string = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(html[start : i + 1])
    raise ValueError("ytInitialPlayerResponse never closed")


def iso_duration(seconds: int) -> str:
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    out = "PT"
    if hours:
        out += f"{hours}H"
    if minutes:
        out += f"{minutes}M"
    if secs or not (hours or minutes):
        out += f"{secs}S"
    return out


def summarise(description: str) -> str:
    """First paragraph, collapsed, capped at DESC_MAX characters on a word boundary."""
    first = description.strip().split("\n\n")[0]
    first = " ".join(first.split())
    if len(first) <= DESC_MAX:
        return first
    return first[:DESC_MAX].rsplit(" ", 1)[0].rstrip(",;:-") + "…"


def head_ok(url: str) -> bool:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except urllib.error.URLError:
        return False


def best_thumbnail(details: dict, video_id: str) -> str:
    """Largest JPEG thumbnail, in descending order of size.

    YouTube now serves WebP by default (i.ytimg.com/vi_webp/.../maxresdefault.webp)
    but Google's structured-data requirements accept only .jpg, .png and .gif for
    a VideoObject thumbnail, so a WebP URL here silently invalidates the markup.
    Every WebP derivative has a JPEG twin under /vi/ -- except maxresdefault,
    which does not exist for videos uploaded before 720p was standard. Hence the
    HEAD check rather than trusting the name. hqdefault.jpg is always present.
    """
    named = [t.get("url", "").split("?")[0]
             for t in sorted(details.get("thumbnail", {}).get("thumbnails", []),
                             key=lambda t: t.get("width", 0), reverse=True)]
    candidates = [u.replace("/vi_webp/", "/vi/").replace(".webp", ".jpg") for u in named]
    candidates.append(f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg")
    candidates.append(f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg")

    seen = set()
    for url in candidates:
        if not url or url in seen:
            continue
        seen.add(url)
        if head_ok(url):
            return url
    return f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"


def extract(video_id: str) -> dict:
    data = player_response(fetch(video_id))
    details = data.get("videoDetails", {})
    micro = data.get("microformat", {}).get("playerMicroformatRenderer", {})

    upload = micro.get("uploadDate") or micro.get("publishDate")
    if not upload:
        raise ValueError("no uploadDate")

    record = {
        "name": details.get("title") or micro.get("title", {}).get("simpleText", ""),
        "description": summarise(details.get("shortDescription", "")),
        "thumbnailUrl": best_thumbnail(details, video_id),
        "uploadDate": upload,
        "channel": details.get("author", ""),
    }
    length = details.get("lengthSeconds")
    if length and int(length) > 0:
        record["duration"] = iso_duration(int(length))
    if not record["description"]:
        # schema.org requires a description; fall back to the title so the
        # markup stays valid rather than emitting an empty string.
        record["description"] = record["name"]
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", action="append", metavar="ID",
                        help="refresh just this video ID (repeatable)")
    args = parser.parse_args()

    existing: dict[str, dict] = {}
    if OUT.exists():
        existing = json.loads(OUT.read_text(encoding="utf-8"))

    ids = args.only or discover_ids()
    print(f"{len(ids)} video ID(s) to fetch", file=sys.stderr)

    failures = []
    for video_id in ids:
        try:
            existing[video_id] = extract(video_id)
            print(f"  ok   {video_id}  {existing[video_id]['name'][:60]}", file=sys.stderr)
        except (urllib.error.URLError, ValueError, KeyError) as exc:
            failures.append(video_id)
            print(f"  FAIL {video_id}  {exc}", file=sys.stderr)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps(dict(sorted(existing.items())), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUT.relative_to(ROOT)} ({len(existing)} videos)", file=sys.stderr)

    if failures:
        print(f"could not fetch: {', '.join(failures)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
