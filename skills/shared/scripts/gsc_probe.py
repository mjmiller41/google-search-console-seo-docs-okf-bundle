#!/usr/bin/env python3
"""Query Google Search Console for the checks a crawl cannot answer.

What this unlocks, per audit check:

- URL Inspection: Google's own index coverage verdict per URL (what Google
  actually kept, not what a crawl predicts) and its rich-results verdict —
  the same assessments the Page Indexing report and Rich Results Test surface.
- Search analytics: clicks/impressions by page or query, for traffic-drop work.
- Site list: confirms the property is verified and which form it takes.

Manual Actions and Security Issues have no API; check those two reports in the
Search Console UI directly. This script prints their URLs with --reports.

Auth, in order: ``GSC_ACCESS_TOKEN`` env var if set, else
``gcloud auth application-default print-access-token``. The token must carry
the Search Console scope — grant it once with:

    gcloud auth application-default login \
      --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters.readonly

Set ``GOOGLE_CLOUD_QUOTA_PROJECT`` to bill quota to a specific project.

    python3 gsc_probe.py --list-sites
    python3 gsc_probe.py --site sc-domain:example.com --inspect https://example.com/page
    python3 gsc_probe.py --site https://example.com/ --analytics --days 28 --dimension page
    python3 gsc_probe.py --site sc-domain:example.com --reports

Stdlib only. Never writes files. JSON on stdout. Exit 0 on success, 2 on
auth/API failure (the JSON says which).
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://searchconsole.googleapis.com"


def access_token() -> tuple[str | None, str | None]:
    token = os.environ.get("GSC_ACCESS_TOKEN")
    if token:
        return token.strip(), None
    try:
        result = subprocess.run(
            ["gcloud", "auth", "application-default", "print-access-token"],
            capture_output=True, text=True, timeout=30)
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        return None, f"no GSC_ACCESS_TOKEN and gcloud unavailable: {exc}"
    if result.returncode != 0:
        return None, ("no GSC_ACCESS_TOKEN and gcloud returned an error: "
                      + result.stderr.strip()[:300])
    return result.stdout.strip(), None


def call(token: str, method: str, path: str, payload: dict | None = None,
         timeout: int = 30) -> tuple[int, dict]:
    headers = {"Authorization": f"Bearer {token}"}
    quota_project = os.environ.get("GOOGLE_CLOUD_QUOTA_PROJECT")
    if quota_project:
        headers["x-goog-user-project"] = quota_project
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(f"{API}{path}", data=data,
                                     headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, json.loads(response.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as exc:
        try:
            return exc.code, json.loads(exc.read().decode("utf-8"))
        except Exception:
            return exc.code, {}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"error": {"message": str(exc)}}


def api_error(status: int, body: dict) -> dict:
    message = body.get("error", {}).get("message", f"HTTP {status}")
    hint = None
    if status in (401, 403):
        hint = ("Token lacks the Search Console scope or the account has no "
                "access to this property. Re-run the application-default login "
                "with the webmasters.readonly scope (see --help), and confirm "
                "the property with --list-sites.")
    return {"ok": False, "status": status, "error": message,
            **({"hint": hint} if hint else {})}


def reports_urls(site: str) -> dict:
    encoded = urllib.parse.quote(site, safe="")
    base = "https://search.google.com/search-console"
    return {
        "ok": True,
        "note": "Manual Actions and Security Issues are not exposed by any API; "
                "open these reports directly.",
        "manual_actions": f"{base}/manual-actions?resource_id={encoded}",
        "security_issues": f"{base}/security-issues?resource_id={encoded}",
        "page_indexing": f"{base}/index?resource_id={encoded}",
        "core_web_vitals": f"{base}/core-web-vitals?resource_id={encoded}",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--site", default=None,
                        help="property, e.g. sc-domain:example.com or https://example.com/")
    parser.add_argument("--list-sites", action="store_true")
    parser.add_argument("--inspect", metavar="URL", action="append", default=[],
                        help="URL to inspect (repeatable; needs --site)")
    parser.add_argument("--analytics", action="store_true",
                        help="search analytics summary (needs --site)")
    parser.add_argument("--dimension", default="page",
                        choices=["page", "query", "date", "country", "device"])
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--row-limit", type=int, default=25)
    parser.add_argument("--reports", action="store_true",
                        help="print Search Console UI report URLs (needs --site)")
    parser.add_argument("--json", action="store_true",
                        help="accepted for symmetry; output is always JSON")
    args = parser.parse_args()

    if not (args.list_sites or args.inspect or args.analytics or args.reports):
        parser.error("nothing to do: pass --list-sites, --inspect, --analytics or --reports")
    if (args.inspect or args.analytics or args.reports) and not args.site:
        parser.error("--site is required for --inspect/--analytics/--reports")

    if args.reports and not (args.inspect or args.analytics or args.list_sites):
        json.dump(reports_urls(args.site), sys.stdout, indent=1)
        print()
        return 0

    token, error = access_token()
    if token is None:
        json.dump({"ok": False, "error": error}, sys.stdout, indent=1)
        print()
        return 2

    output: dict = {"ok": True}
    failed = False

    if args.list_sites:
        status, body = call(token, "GET", "/webmasters/v3/sites")
        if status != 200:
            output["sites"] = api_error(status, body)
            failed = True
        else:
            output["sites"] = [
                {"site_url": entry.get("siteUrl"),
                 "permission": entry.get("permissionLevel")}
                for entry in body.get("siteEntry", [])
            ]

    for url in args.inspect:
        status, body = call(token, "POST", "/v1/urlInspection/index:inspect",
                            {"inspectionUrl": url, "siteUrl": args.site},
                            timeout=60)
        key = f"inspect:{url}"
        if status != 200:
            output[key] = api_error(status, body)
            failed = True
            continue
        result = body.get("inspectionResult", {})
        index = result.get("indexStatusResult", {})
        rich = result.get("richResultsResult", {})
        output[key] = {
            "coverage_state": index.get("coverageState"),
            "verdict": index.get("verdict"),
            "indexing_state": index.get("indexingState"),
            "robots_txt_state": index.get("robotsTxtState"),
            "page_fetch_state": index.get("pageFetchState"),
            "last_crawl_time": index.get("lastCrawlTime"),
            "google_canonical": index.get("googleCanonical"),
            "user_canonical": index.get("userCanonical"),
            "rich_results": {
                "verdict": rich.get("verdict"),
                "detected_items": [
                    {"type": item.get("richResultType"),
                     "issues": [issue.get("issueMessage")
                                for issue in (entry.get("issues") or [])]}
                    for item in (rich.get("detectedItems") or [])
                    for entry in (item.get("items") or [{}])
                ],
            } if rich else None,
            "inspection_link": result.get("inspectionResultLink"),
        }

    if args.analytics:
        end = datetime.date.today() - datetime.timedelta(days=2)  # GSC data lags
        start = end - datetime.timedelta(days=args.days)
        status, body = call(
            token, "POST",
            f"/webmasters/v3/sites/{urllib.parse.quote(args.site, safe='')}/searchAnalytics/query",
            {"startDate": start.isoformat(), "endDate": end.isoformat(),
             "dimensions": [args.dimension], "rowLimit": args.row_limit})
        if status != 200:
            output["analytics"] = api_error(status, body)
            failed = True
        else:
            output["analytics"] = {
                "start": start.isoformat(), "end": end.isoformat(),
                "dimension": args.dimension,
                "rows": [
                    {"key": row.get("keys", [None])[0],
                     "clicks": row.get("clicks"),
                     "impressions": row.get("impressions"),
                     "ctr": round(row.get("ctr", 0), 4),
                     "position": round(row.get("position", 0), 1)}
                    for row in body.get("rows", [])
                ],
            }

    if args.reports:
        output["reports"] = reports_urls(args.site)

    output["ok"] = not failed
    json.dump(output, sys.stdout, indent=1)
    print()
    return 0 if output["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
