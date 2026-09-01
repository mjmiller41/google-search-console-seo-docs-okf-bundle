#!/usr/bin/env python3
"""Fetch Core Web Vitals field data for a URL or origin (check APP-08).

Two sources, best first:

- Chrome UX Report API when ``CRUX_API_KEY`` is set (fast, field data only).
- PageSpeed Insights API otherwise (slower, works without a key at low volume;
  ``PSI_API_KEY`` raises the quota). PSI runs Lighthouse, so expect 30-60s.

Verdicts (good / needs improvement / poor) are taken from the API responses
themselves — CrUX returns the threshold bins per metric and PSI returns a
category per metric — so no threshold is hardcoded here.

    python3 cwv_field_data.py https://example.com/page [--origin] [--form-factor PHONE]
    python3 cwv_field_data.py https://example.com --source psi

Stdlib only. Never writes files. JSON on stdout. Exit 0 on success, 2 when no
data or the request failed (the JSON says which).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

CRUX_ENDPOINT = "https://chromeuxreport.googleapis.com/v1/records:queryRecord"
PSI_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
CORE_METRICS = (
    "largest_contentful_paint",
    "interaction_to_next_paint",
    "cumulative_layout_shift",
)


def _post_json(url: str, payload: dict, timeout: int) -> tuple[int, dict]:
    request = urllib.request.Request(
        url, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        try:
            return exc.code, json.loads(exc.read().decode("utf-8"))
        except Exception:
            return exc.code, {}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"error": {"message": str(exc)}}


def _get_json(url: str, timeout: int) -> tuple[int, dict]:
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        try:
            return exc.code, json.loads(exc.read().decode("utf-8"))
        except Exception:
            return exc.code, {}
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"error": {"message": str(exc)}}


def _crux_metric(name: str, data: dict) -> dict:
    """Reduce one CrUX metric to p75 + a verdict derived from the API's own
    threshold bins (first bin = good, middle = needs improvement, last = poor)."""
    p75_raw = data.get("percentiles", {}).get("p75")
    p75 = float(p75_raw) if p75_raw is not None else None
    bins = data.get("histogram", [])
    verdict = None
    if p75 is not None and len(bins) == 3:
        labels = ("good", "needs improvement", "poor")
        verdict = labels[-1]
        for i, histogram_bin in enumerate(bins):
            end = histogram_bin.get("end")
            if end is not None and p75 < float(end):
                verdict = labels[i]
                break
    return {
        "p75": p75,
        "verdict": verdict,
        "densities": [round(float(b.get("density", 0)), 4) for b in bins],
        "bin_ends": [b.get("end") for b in bins],
    }


def query_crux(target: str, api_key: str, form_factor: str | None,
               as_origin: bool, timeout: int) -> dict:
    payload: dict = {"origin" if as_origin else "url": target,
                     "metrics": list(CORE_METRICS)}
    if form_factor:
        payload["formFactor"] = form_factor
    status, body = _post_json(f"{CRUX_ENDPOINT}?key={urllib.parse.quote(api_key)}",
                              payload, timeout)
    if status == 404:
        return {"source": "crux", "target": target, "has_data": False,
                "note": "CrUX has no record for this "
                        + ("origin" if as_origin else "URL")
                        + " (not enough real-user traffic)."}
    if status != 200:
        return {"source": "crux", "target": target, "has_data": False,
                "error": body.get("error", {}).get("message", f"HTTP {status}")}
    record = body.get("record", {})
    return {
        "source": "crux",
        "target": record.get("key", {}).get("origin") or record.get("key", {}).get("url"),
        "form_factor": record.get("key", {}).get("formFactor", "ALL"),
        "has_data": True,
        "collection_period": record.get("collectionPeriod"),
        "metrics": {name: _crux_metric(name, metric)
                    for name, metric in record.get("metrics", {}).items()},
    }


def query_psi(target: str, api_key: str | None, form_factor: str | None,
              timeout: int) -> dict:
    params = {"url": target, "category": "performance",
              "strategy": "desktop" if form_factor == "DESKTOP" else "mobile"}
    if api_key:
        params["key"] = api_key
    status, body = _get_json(f"{PSI_ENDPOINT}?{urllib.parse.urlencode(params)}", timeout)
    if status != 200:
        return {"source": "psi", "target": target, "has_data": False,
                "error": body.get("error", {}).get("message", f"HTTP {status}")}

    def experience(section: dict | None) -> dict | None:
        if not section or not section.get("metrics"):
            return None
        return {
            "overall_category": section.get("overall_category"),
            "metrics": {name: {"percentile": metric.get("percentile"),
                               "category": metric.get("category")}
                        for name, metric in section["metrics"].items()},
        }

    lighthouse = body.get("lighthouseResult", {})
    performance = lighthouse.get("categories", {}).get("performance", {})
    return {
        "source": "psi",
        "target": target,
        "strategy": params["strategy"],
        "has_data": True,
        "field_data_url": experience(body.get("loadingExperience")),
        "field_data_origin": experience(body.get("originLoadingExperience")),
        "lab_performance_score": performance.get("score"),
        "lab_note": "Lighthouse lab score, not field data; field_data_* above "
                    "is what Google's page experience guidance is about.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="page URL, or origin with --origin")
    parser.add_argument("--origin", action="store_true",
                        help="query origin-level data instead of URL-level")
    parser.add_argument("--form-factor", choices=["PHONE", "DESKTOP", "TABLET"],
                        default=None, help="CrUX form factor (default: combined)")
    parser.add_argument("--source", choices=["auto", "crux", "psi"], default="auto")
    parser.add_argument("--api-key", default=None,
                        help="overrides CRUX_API_KEY / PSI_API_KEY")
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--json", action="store_true",
                        help="accepted for symmetry; output is always JSON")
    args = parser.parse_args()

    target = args.target
    if not urllib.parse.urlparse(target).scheme:
        target = "https://" + target

    crux_key = args.api_key or os.environ.get("CRUX_API_KEY")
    # One key can serve both APIs; PSI_API_KEY only needs setting when the
    # keys differ.
    psi_key = args.api_key or os.environ.get("PSI_API_KEY") or crux_key

    if args.source == "crux" or (args.source == "auto" and crux_key):
        if not crux_key:
            result = {"has_data": False,
                      "error": "CRUX_API_KEY is not set; use --source psi or set the key"}
        else:
            result = query_crux(target, crux_key, args.form_factor,
                                args.origin, args.timeout)
            if args.source == "auto" and not result.get("has_data") and "error" not in result:
                # No CrUX record; PSI may still return origin-level data.
                result = {"crux": result,
                          **query_psi(target, psi_key, args.form_factor, args.timeout)}
    else:
        result = query_psi(target, psi_key, args.form_factor, args.timeout)

    json.dump(result, sys.stdout, indent=1)
    print()
    return 0 if result.get("has_data") else 2


if __name__ == "__main__":
    sys.exit(main())
