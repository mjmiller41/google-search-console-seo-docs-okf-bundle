---
name: crawling-indexing
description: Audits whether a site's pages can be crawled and indexed by Google — robots.txt, sitemaps, canonicalization, redirects, robots meta/X-Robots-Tag, JavaScript rendering, mobile-first readiness, URL structure, 404 handling, hreflang, AMP, and site moves. Triggers on "crawl audit", "indexing audit", "can Google crawl this", "robots.txt check", "sitemap check", "canonical tag audit", "redirect audit", "is my site indexable". Not for title/snippet/favicon/Core Web Vitals/SERP-appearance signals — use the search-appearance skill for those.
type: Skill
title: Crawling and indexing audit
tags: [skills, google-search, crawling]
status: stable
---

# Crawling and indexing audit

Router for the CRA check group. This file is a workflow, not a content
source — every threshold, valid-value list, and limit lives in the grounding
document named per check, not here. Read the grounding document before
writing any finding.

## Workflow

1. **Resolve the bundle root.** `ROOT="${CLAUDE_PLUGIN_ROOT}"`, or if unset,
   this file's directory two levels up. Verify with
   `ls "$ROOT/essentials/technical.md"`; quote `$ROOT` everywhere. Stop and
   tell the user if the bundle can't be found.

2. **Resolve the target and sample.** Follow `../shared/targets.md` to decide
   live / static / mixed mode and to pick the page sample (homepage, sitemap
   URLs, distinct path segments, capped at 10). Reuse any sample already
   gathered by the router this session instead of re-fetching.

3. **Read the contracts.** Read `../shared/report-format.md` for the finding
   schema and severities, and `./reference/checks.md` for the full CRA check
   matrix. Read each check's grounding document immediately before writing a
   finding that cites it — never state a limit, valid rule name, or threshold
   from memory.

4. **Gather signals once, live mode.**
   - `python3 "$ROOT/skills/shared/scripts/site_probe.py" --base <origin> --check-url <sampled URLs>` for robots.txt, sitemap, and per-URL robots verdicts.
   - `python3 "$ROOT/skills/shared/scripts/fetch_page.py" <URL>` for each sampled page, then pipe into `extract_signals.py --from-fetch -` for head/link/JS signals. Cache every result; a URL is fetched at most once across the whole audit.

5. **Gather signals once, static mode.** Use `site_probe.py --local DIR` for
   robots.txt/sitemap files in the build output, and run
   `extract_signals.py FILE --base-url <intended URL>` against each sampled
   HTML file. Note in the report anything static mode cannot test (HTTP
   status codes, redirects not in a config file, response headers) per
   `../shared/targets.md`.

6. **Evaluate the CRA-01 through CRA-20 checks** in `./reference/checks.md`
   against the gathered signals. Skip conditional checks whose trigger
   condition doesn't apply (no hreflang found, no `amphtml` detected, no
   crawler-abuse question asked, no site move mentioned) and list them under
   "Checks not run" with the reason, not as silent passes.

7. **Emit findings** in the `../shared/report-format.md` structure: one
   finding per check ID per affected page group, each with evidence, why it
   matters, a concrete fix, and a full grounding citation (path, upstream
   URL, both dates). If running standalone, emit the whole report document;
   if running under a router, emit only this category's findings, scorecard
   row, and "Checks not run" rows for the router to merge.

## Severity quick reference

| Severity | When it applies here |
| :--- | :--- |
| BLOCKER | Site-wide robots.txt block (CRA-02) — the site cannot be crawled at all. |
| WARNING | Everything else that works today but violates documented guidance. |
| INFO | AMP pairing, fake-Googlebot advisory, site-move guidance — advisory only, and each fires only when its trigger condition is met. |

See `./reference/checks.md` for the full matrix, live/static methods per
check, and grounding paths.
