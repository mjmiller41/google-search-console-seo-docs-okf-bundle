#!/usr/bin/env python3
"""Fetch one URL and report the HTTP behavior Google Search cares about.

Follows redirects manually so the full chain is captured, records headers
(including X-Robots-Tag), and returns everything as JSON on stdout.

    python3 fetch_page.py URL [--ua STRING] [--timeout 15] [--max-bytes 2000000]
                              [--head] [--no-body]

Stdlib only. Never writes files. Exit 0 on success, 2 on fetch failure.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_UA = "Mozilla/5.0 (compatible; search-audit-skill/1.0; local site audit)"
MAX_REDIRECTS = 10


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(url: str, ua: str, timeout: int, max_bytes: int, head: bool,
          want_body: bool) -> dict:
    opener = urllib.request.build_opener(NoRedirect)
    chain = []
    current = url
    started = time.monotonic()

    for _ in range(MAX_REDIRECTS + 1):
        request = urllib.request.Request(
            current,
            headers={"User-Agent": ua, "Accept-Encoding": "gzip"},
            method="HEAD" if head else "GET",
        )
        try:
            response = opener.open(request, timeout=timeout)
            status = response.status
        except urllib.error.HTTPError as exc:
            response = exc
            status = exc.code
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            return {"requested_url": url, "error": str(exc), "redirect_chain": chain}

        headers = {k.lower(): v for k, v in response.headers.items()}
        location = headers.get("location")
        if status in (301, 302, 303, 307, 308) and location:
            resolved = urllib.parse.urljoin(current, location)
            chain.append({"url": current, "status": status, "location": resolved})
            response.close()
            current = resolved
            continue

        raw = b"" if head or not want_body else response.read(max_bytes + 1)
        response.close()
        truncated = len(raw) > max_bytes
        raw = raw[:max_bytes]
        if headers.get("content-encoding") == "gzip" and raw:
            try:
                raw = gzip.decompress(raw)
            except OSError:
                pass

        body = raw.decode("utf-8", errors="replace") if raw else ""
        return {
            "requested_url": url,
            "final_url": current,
            "status": status,
            "redirect_chain": chain,
            "headers": headers,
            "x_robots_tag": headers.get("x-robots-tag"),
            "content_type": headers.get("content-type"),
            "body_bytes": len(raw),
            "truncated": truncated,
            "body": body if want_body and not head else None,
            "elapsed_ms": int((time.monotonic() - started) * 1000),
            "retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }

    return {
        "requested_url": url,
        "error": f"more than {MAX_REDIRECTS} redirects",
        "redirect_chain": chain,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--ua", default=DEFAULT_UA)
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--max-bytes", type=int, default=2_000_000)
    parser.add_argument("--head", action="store_true", help="HEAD request, no body")
    parser.add_argument("--no-body", action="store_true", help="GET but drop the body")
    parser.add_argument("--json", action="store_true", help="accepted for symmetry; output is always JSON")
    args = parser.parse_args()

    url = args.url
    if not urllib.parse.urlparse(url).scheme:
        url = "https://" + url

    result = fetch(url, args.ua, args.timeout, args.max_bytes, args.head,
                   want_body=not args.no_body)
    json.dump(result, sys.stdout, indent=1)
    print()
    return 2 if "error" in result else 0


if __name__ == "__main__":
    sys.exit(main())
