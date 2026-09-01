#!/usr/bin/env python3
"""Probe a site's robots.txt and sitemaps, live or from a build directory.

Deliberately narrow: it makes at most one request for robots.txt plus one per
sitemap. Fetching page bodies is fetch_page.py's job, so an audit never
double-fetches a URL.

    python3 site_probe.py --base https://example.com [--ua Googlebot]
                          [--check-url URL ...] [--sample 10] [--no-sitemaps]
    python3 site_probe.py --local ./dist [--check-url /about/index.html ...]

Stdlib only. Never writes files. JSON on stdout.
"""
from __future__ import annotations

import argparse
import gzip
import io
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser
import xml.etree.ElementTree as ET
from pathlib import Path

DEFAULT_UA = "Mozilla/5.0 (compatible; search-audit-skill/1.0; local site audit)"
ROBOTS_MAX_BYTES = 500 * 1024  # robots-txt-spec.md: Google parses the first 500 KiB
SITEMAP_MAX_URLS = 50_000      # sitemaps/build-sitemap.md limits
SITEMAP_MAX_BYTES = 50 * 1024 * 1024
KNOWN_DIRECTIVES = {"user-agent", "disallow", "allow", "sitemap", "crawl-delay",
                    "host", "noindex", "clean-param", "request-rate", "visit-time"}
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def _get(url: str, ua: str, timeout: int = 15, max_bytes: int = SITEMAP_MAX_BYTES):
    request = urllib.request.Request(
        url, headers={"User-Agent": ua, "Accept-Encoding": "gzip"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read(max_bytes)
            if response.headers.get("Content-Encoding") == "gzip" or url.endswith(".gz"):
                try:
                    raw = gzip.decompress(raw)
                except OSError:
                    pass
            return response.status, raw, None
    except urllib.error.HTTPError as exc:
        return exc.code, b"", None
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return None, b"", str(exc)


def lint_robots(text: str, size: int) -> dict:
    """Structural lint of a robots.txt against the documented parsing rules."""
    issues: list[str] = []
    if size > ROBOTS_MAX_BYTES:
        issues.append(f"exceeds 500 KiB ({size} bytes); Google ignores content past the limit")
    if text.startswith("﻿"):
        issues.append("starts with a UTF-8 BOM")

    groups: list[dict] = []
    current: dict | None = None
    sitemaps: list[str] = []
    unknown: list[str] = []

    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.split("#", 1)[0].strip()
        if not stripped:
            continue
        if ":" not in stripped:
            issues.append(f"line {number}: no directive separator — {stripped[:60]!r}")
            continue
        field, value = stripped.split(":", 1)
        field, value = field.strip().lower(), value.strip()
        if field not in KNOWN_DIRECTIVES:
            unknown.append(f"line {number}: {field}")
            continue
        if field == "sitemap":
            sitemaps.append(value)
        elif field == "user-agent":
            if current is None or current.get("_rules_seen"):
                current = {"user_agents": [], "disallow": [], "allow": [], "_rules_seen": False}
                groups.append(current)
            current["user_agents"].append(value)
        elif field in ("disallow", "allow"):
            if current is None:
                issues.append(f"line {number}: {field} before any user-agent group")
                continue
            current[field].append(value)
            current["_rules_seen"] = True

    for group in groups:
        group.pop("_rules_seen", None)

    blocks_everything = any(
        ("*" in g["user_agents"] or any("googlebot" in u.lower() for u in g["user_agents"]))
        and "/" in g["disallow"]
        for g in groups
    )
    return {"issues": issues, "unknown_directives": unknown, "groups": groups,
            "sitemaps": sitemaps, "blocks_entire_site": blocks_everything}


def parse_sitemap(raw: bytes, url: str) -> dict:
    result = {"url": url, "bytes": len(raw), "over_50mb": len(raw) > SITEMAP_MAX_BYTES,
              "urls": [], "sitemap_refs": [], "parse_error": None, "type": None}
    try:
        root = ET.parse(io.BytesIO(raw)).getroot()
    except ET.ParseError as exc:
        result["parse_error"] = str(exc)
        return result

    tag = root.tag.replace(SITEMAP_NS, "")
    result["type"] = tag
    if tag == "sitemapindex":
        result["sitemap_refs"] = [e.text.strip() for e in root.iter(f"{SITEMAP_NS}loc")
                                  if e.text]
    else:
        result["urls"] = [e.text.strip() for e in root.iter(f"{SITEMAP_NS}loc") if e.text]
    result["url_count"] = len(result["urls"])
    result["over_50k_urls"] = len(result["urls"]) > SITEMAP_MAX_URLS
    return result


def sample_urls(urls: list[str], limit: int) -> list[str]:
    """Homepage-ish first, then spread across distinct path prefixes so the
    sample covers templates rather than one section."""
    if len(urls) <= limit:
        return list(urls)
    chosen: list[str] = urls[:3]
    seen_prefixes = {urllib.parse.urlparse(u).path.strip("/").split("/")[0] for u in chosen}
    for url in urls[3:]:
        if len(chosen) >= limit:
            break
        prefix = urllib.parse.urlparse(url).path.strip("/").split("/")[0]
        if prefix not in seen_prefixes:
            seen_prefixes.add(prefix)
            chosen.append(url)
    for url in urls[3:]:
        if len(chosen) >= limit:
            break
        if url not in chosen:
            chosen.append(url)
    return chosen


def probe_live(base: str, ua: str, check_urls: list[str], limit: int,
               want_sitemaps: bool, sleep: float) -> dict:
    parsed = urllib.parse.urlparse(base)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = f"{origin}/robots.txt"
    status, raw, error = _get(robots_url, ua, max_bytes=ROBOTS_MAX_BYTES * 2)
    text = raw.decode("utf-8", errors="replace")

    robots = {"url": robots_url, "status": status, "fetch_error": error,
              "bytes": len(raw)}
    if status == 200:
        robots.update(lint_robots(text, len(raw)))
        robots["interpretation"] = "rules apply"
    elif status in (401, 403):
        robots["interpretation"] = ("4xx auth status: Google treats the site as fully "
                                    "disallowed for 401/403 — verify intent")
    elif status is not None and 400 <= status < 500:
        robots["interpretation"] = "not found (4xx): no crawl restrictions"
    elif status is not None and status >= 500:
        robots["interpretation"] = ("5xx: Google may stop crawling the site; "
                                    "serve 200 or 404 instead")
    else:
        robots["interpretation"] = "unreachable"

    verdicts = []
    if status == 200 and check_urls:
        parser = urllib.robotparser.RobotFileParser()
        parser.parse(text.splitlines())
        for target in check_urls:
            absolute = urllib.parse.urljoin(origin, target)
            verdicts.append({"url": absolute, "user_agent": ua,
                             "allowed": parser.can_fetch(ua, absolute)})

    sitemaps: list[dict] = []
    all_urls: list[str] = []
    if want_sitemaps:
        candidates = list(dict.fromkeys(
            robots.get("sitemaps", []) + [f"{origin}/sitemap.xml", f"{origin}/sitemap_index.xml"]
        ))
        seen: set[str] = set()
        queued_refs: set[str] = set()
        queue = candidates[:]
        while queue and len(sitemaps) < 6:
            url = queue.pop(0)
            if url in seen:
                continue
            seen.add(url)
            time.sleep(sleep)
            # Sitemaps can be tens of MB; give them longer than a page fetch.
            sm_status, sm_raw, sm_error = _get(url, ua, timeout=30)
            if sm_status != 200 or not sm_raw:
                # Only note a miss for sitemaps the site actually advertised;
                # probing /sitemap.xml on a site without one is not a finding.
                if url in robots.get("sitemaps", []) or url in queued_refs:
                    sitemaps.append({"url": url, "status": sm_status,
                                     "fetch_error": sm_error,
                                     "parse_error": "not retrievable"})
                continue
            parsed_sm = parse_sitemap(sm_raw, url)
            parsed_sm["status"] = sm_status
            sitemaps.append(parsed_sm)
            all_urls.extend(parsed_sm["urls"])
            refs = parsed_sm["sitemap_refs"][:5]
            queued_refs.update(refs)
            queue.extend(refs)

    return {
        "mode": "live", "origin": origin, "robots": robots,
        "robots_verdicts": verdicts, "sitemaps": sitemaps,
        "sitemap_url_total": len(all_urls),
        "sample": sample_urls(all_urls, limit) or [base],
        "sampled_from": "sitemap" if all_urls else "base url only",
        "probed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def probe_local(directory: str, check_urls: list[str], limit: int) -> dict:
    root = Path(directory).resolve()
    robots_path = next((p for p in (root / "robots.txt", root / "public" / "robots.txt",
                                    root / "static" / "robots.txt") if p.is_file()), None)
    robots: dict = {"path": str(robots_path) if robots_path else None}
    if robots_path:
        text = robots_path.read_text(encoding="utf-8", errors="replace")
        robots.update(lint_robots(text, robots_path.stat().st_size))
        robots["bytes"] = robots_path.stat().st_size
    else:
        robots["interpretation"] = ("no robots.txt in the build output; it may be "
                                    "generated at deploy time — verify on the live site")

    sitemaps = []
    for path in sorted(root.rglob("sitemap*.xml"))[:6]:
        parsed = parse_sitemap(path.read_bytes(), str(path.relative_to(root)))
        sitemaps.append(parsed)
    if not sitemaps:
        robots.setdefault("notes", []).append("no sitemap*.xml found in build output")

    html_files = [p for p in sorted(root.rglob("*.html"))
                  if not any(part.startswith(".") for part in p.parts)]
    sample = [str(p.relative_to(root)) for p in html_files]
    indexes = [s for s in sample if Path(s).name == "index.html"]
    ordered = ([s for s in indexes if s.count("/") == 0]
               + [s for s in indexes if s.count("/") > 0]
               + [s for s in sample if s not in indexes])

    return {
        "mode": "static", "root": str(root), "robots": robots, "sitemaps": sitemaps,
        "html_file_total": len(html_files),
        "sample": ordered[:limit],
        "sampled_from": "build output html files",
        "probed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--base", help="site origin or URL (live mode)")
    group.add_argument("--local", help="build output directory (static mode)")
    parser.add_argument("--ua", default=DEFAULT_UA,
                        help="user agent for fetching and robots allow-checks")
    parser.add_argument("--check-url", action="append", default=[],
                        help="URL or path to test against robots rules; repeatable")
    parser.add_argument("--sample", type=int, default=10, help="max pages to sample")
    parser.add_argument("--sleep", type=float, default=1.0,
                        help="seconds between network requests")
    parser.add_argument("--no-sitemaps", action="store_true")
    parser.add_argument("--json", action="store_true",
                        help="accepted for symmetry; output is always JSON")
    args = parser.parse_args()

    if args.base:
        base = args.base if urllib.parse.urlparse(args.base).scheme else "https://" + args.base
        result = probe_live(base, args.ua, args.check_url, args.sample,
                            not args.no_sitemaps, args.sleep)
    else:
        if not Path(args.local).is_dir():
            json.dump({"error": f"not a directory: {args.local}"}, sys.stdout)
            print()
            return 2
        result = probe_local(args.local, args.check_url, args.sample)

    json.dump(result, sys.stdout, indent=1)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
