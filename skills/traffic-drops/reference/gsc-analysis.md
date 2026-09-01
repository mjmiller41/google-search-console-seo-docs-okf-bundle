---
type: Skill Reference
title: Search Console Performance data analysis
description: The shapes of Search Console Performance exports, honest period comparison, per-page and per-query delta computation, the drop-shape taxonomy, the CTR-versus-position triage technique, and the TRF check matrix for the traffic-drops skill.
tags: [skills, google-search, traffic-drops, reference]
status: stable
---

# Search Console Performance data analysis

Read the grounding document(s) for a check before writing any finding that
cites it — see `../../shared/grounding.md`. Do not copy thresholds, dates, or
policy wording out of the named docs into a report; this file names the
source, it is not the source.

## Shapes of a Performance export

A Search Console Performance report exported for offline analysis (**Export**
> **Download CSV** or **Google Sheets**) comes as a set of per-tab CSVs, one
row per date/dimension combination with `Clicks`, `Impressions`, `CTR`, and
`Position` columns:

- **Dates** — one row per day (or the export's chosen granularity); the
  overall trend line.
- **Queries** — one row per search query.
- **Pages** — one row per landing URL.
- **Countries** — one row per country.
- **Devices** — one row per device category (desktop, mobile, tablet).
- **Search appearance** — one row per search feature (e.g. rich results,
  AMP) the property appeared in.

For longer or automated analysis, the **bulk data export** to BigQuery
(`support.google.com/webmasters/answer/12917675`, referenced in
`monitor-debug/debugging-search-traffic-drops.md`) exposes the same
dimensions as queryable tables without the UI's history limit, which is the
better source once a drop needs day-by-day, query-by-query reconciliation
beyond what a CSV comparison view shows.

## Comparing periods honestly

`monitor-debug/debugging-search-traffic-drops.md` gives two comparison
techniques; use both before concluding anything:

1. **Widen the date range to 16 months first.** Doing this before drawing any
   conclusion is what rules out a drop that happens every year around the
   same date — a click-through pattern that looks alarming at 28 days can be
   an annual pattern at 16 months. If 16 months isn't enough, the doc points
   to the Search Analytics API or bulk export to go back further.
2. **Then compare the drop period to a similar period**, both "previous
   period" and "year over year," and check every breakdown tab (queries,
   pages, countries, devices, search appearance) for where the change is
   concentrated, not only the total line.

## Computing deltas with stdlib Python

Do this work in a scratch directory, never inside this repository. Use only
the standard library `csv` module — no dependencies to install:

```python
import csv
from pathlib import Path

scratch = Path("/tmp/traffic-drop-analysis")  # or the session scratchpad
scratch.mkdir(parents=True, exist_ok=True)

def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return {row["Top pages"]: row for row in csv.DictReader(f)}

before = load(scratch / "pages-before.csv")
after = load(scratch / "pages-after.csv")

deltas = []
for page, row in after.items():
    prev_clicks = float(before.get(page, {}).get("Clicks", 0))
    cur_clicks = float(row["Clicks"])
    deltas.append((page, cur_clicks - prev_clicks, prev_clicks, cur_clicks))

deltas.sort(key=lambda d: d[1])  # largest loss first
for page, delta, prev, cur in deltas[:20]:
    print(f"{delta:+.0f}  {prev:.0f} -> {cur:.0f}  {page}")
```

The same pattern applies to the Queries tab (key on `Top queries`) to find
which search terms lost clicks, and to compute a per-page or per-query CTR
change (`Clicks / Impressions`) alongside the raw click delta — a click drop
with a stable CTR points to an impressions problem (visibility), while a
stable-impressions, falling-CTR pattern points to the result itself becoming
less appealing.

## Drop-shape taxonomy

`monitor-debug/debugging-search-traffic-drops.md`'s own sketches describe
what the Performance chart's shape over time suggests about the cause. Use
the shape as a starting hypothesis, not a conclusion — confirm it against the
specific cause checks below.

- **Sudden cliff (a sharp, single-day drop)** — consistent with a site-wide
  technical failure (server down, robots.txt change, sitewide `noindex`), a
  security issue, or a manual action taking effect. Check TRF-03, TRF-04, and
  TRF-05 first.
- **Slower decay over days or weeks** — consistent with a page-level
  technical issue (a `noindex` on a subset of pages, a broken template)
  playing out as Google recrawls and reindexes affected URLs over time, or
  with a ranking effect settling in. Check TRF-03 and TRF-02.
- **Seasonal wave (a dip that recurs at the same point each year)** — visible
  once the date range is widened to 16 months; consistent with genuine
  seasonality or changing interest rather than a site problem. Check TRF-06.

A drop that shows in clicks but not impressions, with position roughly
unchanged, points away from all of the above and toward the result becoming
less clickable — see TRF-09 and the CTR-versus-position technique below.

## CTR-versus-position triage

`monitor-debug/bubble-chart-analysis.md` describes a bubble-chart technique
for spotting exactly this pattern at the query level: plot average position
against CTR (with click volume as bubble size), and look at queries that sit
in the **top position, low CTR** quadrant. That doc names specific reasons a
top-ranking query can still underperform on CTR: competitors picking up rich
results the page isn't eligible for, a query the site ranks for but isn't
really a good match for user intent, or a result that already answers the
need (e.g. a store's hours) without a click. Apply the same quadrant logic to
the Queries tab data pulled above when a drop is clicks-only.

## TRF check matrix

| ID | Check | Severity | Grounding |
| :--- | :--- | :--- | :--- |
| TRF-01 | Classify the drop pattern: clicks only vs. clicks and impressions together, and the shape over time | INFO/diagnostic | `monitor-debug/debugging-search-traffic-drops.md` |
| TRF-02 | Timing against a known ranking update | WARNING | `monitor-debug/debugging-search-traffic-drops.md`, `appearance/core-updates.md`, `appearance/spam-updates.md` |
| TRF-03 | Technical causes on affected URLs | BLOCKER if found | `monitor-debug/debugging-search-traffic-drops.md`, `essentials/technical.md` |
| TRF-04 | Security issues (malware, social engineering warnings) | BLOCKER if found | `monitor-debug/security/overview.md`, `monitor-debug/security/malware.md`, `monitor-debug/security/social-engineering.md` |
| TRF-05 | Manual action or spam-policy exposure | BLOCKER if found | `essentials/spam-policies.md` |
| TRF-06 | Seasonality or genuinely changing interest | INFO | `monitor-debug/trends-start.md` |
| TRF-07 | Site move or migration fallout | WARNING | `crawling-indexing/site-move-with-url-changes.md` |
| TRF-08 | Reporting artifact rather than a real drop (data anomalies, analytics discrepancies) | INFO | `monitor-debug/google-analytics-search-console.md` |
| TRF-09 | Clicks-only drops: follow up on title and snippet competitiveness | WARNING | `appearance/title-link.md`, `appearance/snippet.md` |

**How to judge TRF-02.** Fetch the Google Search Status ranking-updates
history page (`status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history`,
linked from `monitor-debug/debugging-search-traffic-drops.md`) once per
session and cache it. If it can't be reached, give the user the URL directly
and compare the drop's start date against it manually rather than guessing at
update dates from memory.

**How to judge TRF-03.** Don't re-derive crawl, indexing, or robots findings
here — re-run the `search-essentials` skill's ESS-01 through ESS-06 gate
checks (and `structured-data`'s SD-05 where structured data is involved) on
the specific URLs the Pages-tab delta identified, and cite those findings.

**How to judge TRF-04 and TRF-05.** These are BLOCKER-if-found because they
each independently explain a drop and require remediation before anything
else matters. Check the Security Issues report and Manual Actions report in
Search Console directly if the user has access; both are named in
`monitor-debug/debugging-search-traffic-drops.md`.

**How to judge TRF-09.** Only pursue this once TRF-01 shows clicks fell while
impressions and average position held roughly steady — otherwise a title or
snippet change is unlikely to be the primary cause.
