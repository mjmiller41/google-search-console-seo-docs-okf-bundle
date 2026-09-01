---
name: search-appearance
description: Audits how a site's pages present themselves in Google Search results — title links, snippets/meta descriptions, favicon, site name signals, sitelinks readiness, publication dates, HTTPS/mixed content, Core Web Vitals heuristics, intrusive interstitials, image preview/Discover eligibility, reviews content, ranking-systems context, and SERP visual-element eligibility. Triggers on "search appearance audit", "SERP audit", "title tag check", "meta description audit", "favicon check", "snippet audit", "how will this look in search results". Not for crawlability, robots.txt, sitemaps, canonicalization, or JavaScript-rendering checks — use the crawling-indexing skill for those.
type: Skill
title: Search appearance audit
tags: [skills, google-search, search-appearance]
status: stable
---

# Search appearance audit

Router for the APP check group. This file is a workflow, not a content
source — every best-practice detail, guideline, and threshold lives in the
grounding document named per check, not here. Read the grounding document
before writing any finding.

## Workflow

1. **Resolve the bundle root.** `ROOT="${CLAUDE_PLUGIN_ROOT}"`, or if unset,
   this file's directory two levels up. Verify with
   `ls "$ROOT/essentials/technical.md"`; quote `$ROOT` everywhere. Stop and
   tell the user if the bundle can't be found.

2. **Resolve the target and sample.** Follow `../shared/targets.md` to decide
   live / static / mixed mode and to pick the page sample (homepage, sitemap
   URLs, distinct path segments, capped at 10). Reuse any sample already
   gathered by the router or by the crawling-indexing skill this session —
   this skill mostly reuses the same fetches, it doesn't refetch pages.

3. **Read the contracts.** Read `../shared/report-format.md` for the finding
   schema and severities, and `./reference/checks.md` for the full APP check
   matrix. Read each check's grounding document immediately before writing a
   finding that cites it — never state a best practice, threshold, or
   guideline from memory.

4. **Gather signals once, live mode.** For each sampled page, cache
   `python3 "$ROOT/skills/shared/scripts/fetch_page.py" <URL>` output and
   pipe it into `extract_signals.py --from-fetch -` for title, meta
   description, favicons, structured data, images, and mixed-content
   signals. A URL is fetched at most once across the whole audit — check the
   shared cache before fetching.

5. **Gather signals once, static mode.** Run
   `extract_signals.py FILE --base-url <intended URL>` against each sampled
   HTML file in the build output. Note in the report what static mode can't
   assess: HTTP/TLS, response headers, and any field-data check (Core Web
   Vitals) per `../shared/targets.md`.

6. **Evaluate the APP-01 through APP-13 checks** in `./reference/checks.md`
   against the gathered signals. Checks that require a judgment call (APP-05
   sitelinks readiness, APP-12 ranking-systems context, APP-13 SERP visual
   elements) are framing, not pass/fail — say so in the finding. Checks that
   are conditional on content type (APP-11 reviews) fire only when the
   condition is met; list the rest under "Checks not run" with the reason.

7. **Emit findings** in the `../shared/report-format.md` structure: one
   finding per check ID per affected page group, each with evidence, why it
   matters, a concrete fix, and a full grounding citation (path, upstream
   URL, both dates). Report Core Web Vitals verdicts only from real field
   data via `cwv_field_data.py` when a key is configured (see
   `../shared/integrations.md`); without one, APP-08 is heuristic-only and
   every such finding must be labeled a heuristic, never a measurement.
   If running standalone, emit the whole report document; if running under a
   router, emit only this category's findings, scorecard row, and "Checks
   not run" rows for the router to merge.

## Severity quick reference

| Severity | When it applies here |
| :--- | :--- |
| WARNING | Title/description/favicon/dates/HTTPS/interstitial checks that work today but go against documented guidance. |
| INFO | Site name, sitelinks, Core Web Vitals heuristics, image/Discover eligibility, reviews, ranking-systems framing, SERP visual elements — advisory or judgment calls, never pass/fail. |

See `./reference/checks.md` for the full matrix, live/static methods per
check, and grounding paths.
