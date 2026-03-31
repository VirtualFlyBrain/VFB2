#!/usr/bin/env python3
"""Check external image URLs in content (optionally themes) and report failures."""

from __future__ import annotations
import argparse
import pathlib
import re
import sys
import ssl
import socket
import urllib.request
import urllib.error

IMAGE_PATTERN = re.compile(r'https?://[^\s"\')]+\.(?:png|jpg|jpeg|gif|svg)', re.IGNORECASE)
DEFAULT_EXTENSIONS = ['.md', '.html', '.yml', '.yaml', '.toml', '.json', '.js', '.ts', '.scss', '.css']


def collect_image_urls(base_dir: pathlib.Path, ext_filter=None):
    ext_filter = ext_filter or DEFAULT_EXTENSIONS
    matches = []
    for path in base_dir.rglob('*'):
        if not path.is_file() or path.suffix.lower() not in ext_filter:
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        for m in IMAGE_PATTERN.finditer(text):
            matches.append((str(path), m.group(0)))
    return matches


def check_url(url: str, timeout: float = 8.0):
    socket.setdefaulttimeout(timeout)
    ctx = ssl.create_default_context()
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; image-link-checker/1.0)'}
    try:
        req = urllib.request.Request(url, method='HEAD', headers=headers)
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
            return response.status, None
    except urllib.error.HTTPError as he:
        if 300 <= he.code < 400 and he.headers.get('Location'):
            return he.code, None
        try:
            req = urllib.request.Request(url, method='GET', headers=headers)
            with urllib.request.urlopen(req, timeout=timeout, context=ctx) as response:
                return response.status, None
        except Exception as inner_e:
            return he.code, str(inner_e)
    except Exception as e:
        return None, str(e)


def main() -> int:
    parser = argparse.ArgumentParser(description='Check external image URLs in a static site repo')
    parser.add_argument('--base', default='content', help='Base directory to scan (default: content)')
    parser.add_argument('--include-themes', action='store_true', help='Also include themes directory')
    parser.add_argument('--timeout', type=float, default=8.0, help='HTTP timeout in seconds')
    args = parser.parse_args()

    dirs = [pathlib.Path(args.base)]
    if args.include_themes:
        dirs.append(pathlib.Path('themes'))

    all_urls = []
    for d in dirs:
        if not d.exists():
            continue
        all_urls.extend(collect_image_urls(d))

    if not all_urls:
        print('No external image URLs found')
        return 0

    unique = list(dict.fromkeys(all_urls))
    print(f'Found {len(all_urls)} references, {len(unique)} unique URLs')

    failures = []
    for i, (path, url) in enumerate(unique, 1):
        status, err = check_url(url, timeout=args.timeout)
        if status is None or status >= 400:
            failures.append((path, url, status, err))
        if i % 20 == 0:
            print(f'Checked {i}/{len(unique)}')

    if failures:
        print(f'FAILED {len(failures)} URLs')
        for p, u, s, e in failures:
            print(f'{p} {s or "ERR"} {e or ""} {u}')
        return 1

    print('All URLs OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
