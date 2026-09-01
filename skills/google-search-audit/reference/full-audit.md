---
type: Skill Reference
title: Full audit pipeline
description: Execution order, the shared signal cache, check ownership for overlapping findings, and how sub-skill results merge into one report.
tags: [skills, audit, pipeline]
status: stable
---

# Full audit pipeline

## Gather signals once

The five audit skills need the same underlying data. Collect it once, before
running any of them, and pass the cached results down. A URL is fetched at most
once per audit.

1. **Site surface.** One `site_probe.py` run (`--base` live, `--local` static)
   gives robots.txt with its lint, the robots allow verdicts for the sampled
   URLs, the parsed sitemaps, and the page sample.
2. **Per page.** For each sampled page, one `fetch_page.py` (live) or direct
   file read (static), then one `extract_signals.py`. Keep both JSON results
   keyed by URL or path for the rest of the run.
3. **Variant probes, live only.** Fetch the http, https, www and non-www forms
   of the homepage once for CRA-07, and one URL certain not to exist for
   CRA-16. That is four or five extra requests, not a crawl.

Write cache files to a scratch directory, never into the repository.

## Order

Run the categories in this order, because each answers a question the next one
assumes:

1. **search-essentials (ESS)** — can this be indexed at all, and is it clean?
2. **crawling-indexing (CRA)** — can Google reach and consolidate it correctly?
3. **structured-data (SD)** — is the markup valid and honest?
4. **seo-fundamentals (FUN)** — does it follow the starter guide?
5. **search-appearance (APP)** — will it present well in results?

`traffic-drops` is not part of a full audit. It is a diagnosis of something
that already happened, and it is driven by Search Console data rather than by
crawling the site. Run it on its own, and only when there is a drop to explain.

## Early exit

If ESS blockers apply site-wide — robots.txt disallowing everything, a
site-wide `noindex`, the origin not resolving — stop and report those first.
Ask whether to continue. Ranking advice for a site Google cannot index wastes
the reader's attention on the wrong problem.

## Check ownership

Several conditions are visible from more than one category. Exactly one check
owns each, and the others defer. Report the owner's ID only.

| Condition | Owner | Defers |
| :--- | :--- | :--- |
| Unintended `noindex` | ESS-04 | CRA-08, CRA-09 |
| robots.txt blocking sampled pages | ESS-01 | CRA-02 (which keeps site-wide blocks and blocked assets) |
| Title quality | APP-01 | FUN-07 |
| Meta description quality | APP-02 | FUN-07 |
| Duplicate or missing canonical | CRA-05 | FUN-03 |
| Non-crawlable links, anchor text | FUN-06 | — |
| Intrusive interstitials | APP-09 | FUN-05 |
| Structured data present but invalid | SD-01, SD-02 | — |
| Markup contradicting visible content | SD-04 | ESS-11 |

When a skill runs standalone, it reports its own checks normally; ownership
only applies to merging.

## Merge

1. Concatenate findings in category order, keeping each finding's ID.
2. Drop deferred duplicates per the ownership table.
3. Collapse repeats: one finding per check ID, listing every affected page,
   rather than one finding per page.
4. Compute each category verdict — any blocker means FAIL, otherwise any
   warning means WARN, otherwise PASS.
5. Overall: **Not eligible** if any ESS blocker fired, **Eligible with issues**
   if anything else did, **Good standing** if nothing did.
6. Merge each skill's "checks not run" rows into one table, deduplicated.

## Ordering findings

Within the report, order by severity first (blockers, warnings, then info) and
by breadth second: a warning affecting every sampled page outranks one
affecting a single page. The reader should be able to act on the first three
findings and get most of the available benefit.
