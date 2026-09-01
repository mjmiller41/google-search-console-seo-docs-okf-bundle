---
name: traffic-drops
description: Diagnoses a reported drop in Google Search traffic by walking Search Console Performance data through the drop-pattern methodology in Google's own debugging guide — classify the shape, eliminate ranking-update, technical, security, spam, seasonal, migration, and reporting-artifact causes in order, then rank surviving hypotheses by evidence. Triggers on "traffic dropped", "clicks went down", "impressions fell", "lost rankings", "why did my traffic drop", or "debug Search Console drop". Not for a general site audit with no reported drop — route to google-search-audit or a specific skill such as search-essentials or structured-data. Not for on-page SEO improvement absent a drop — route to seo-fundamentals.
type: Skill
title: Traffic drop diagnosis
tags: [skills, google-search, traffic-drops]
status: stable
---

# Traffic drop diagnosis

This skill mirrors the methodology and section structure of
`monitor-debug/debugging-search-traffic-drops.md`: classify the drop pattern
first, then work through that doc's own list of causes in order, eliminating
each with evidence before moving to the next. It never restates a limit,
policy definition, or update date from memory — the checks in
`./reference/gsc-analysis.md` name the grounding document for each cause, and
the model reads it before writing a finding. See `../shared/grounding.md`.

**Every finding here is a hypothesis, not a verdict.** Search traffic drops
rarely have one clean cause, and this skill has no access to Google's internal
ranking signals — only to what Search Console and the site itself expose.

## Workflow

1. **Resolve the bundle root.** `ROOT="${CLAUDE_PLUGIN_ROOT}"`; if unset, use
   the directory containing this file, two levels up. Quote `$ROOT` always.
   Verify with `ls "$ROOT/essentials/technical.md"` — if it is missing, tell
   the user the documentation bundle could not be found and stop rather than
   diagnosing from memory.
2. **Resolve the target and sample.** Follow `../shared/targets.md` to decide
   live, static, or mixed mode for the site itself, in case a technical
   re-check (TRF-03) is needed on affected URLs. Cache every fetched URL and
   script result; never fetch a URL twice.
3. **Read before judging.** Read `../shared/report-format.md` and
   `./reference/gsc-analysis.md` (which carries the TRF check matrix, export
   shapes, and comparison technique). For each check, open its grounding
   document before writing any finding that cites it.
4. **Intake.** Before asking the user for exports, probe for direct access:
   `"$ROOT/skills/shared/scripts/gsc_probe.py" --list-sites` (see
   `../shared/integrations.md`). If the property is listed, pull Performance
   data yourself with `--analytics` (by date for the shape, by page and query
   for the deltas) and use `--inspect` on affected URLs for Google's own
   coverage verdicts. Otherwise ask the user: Do they have Search Console
   access or can they export Performance data? What is the drop's approximate
   start date? Have they made recent site changes (redesign, migration,
   template change, deploy)? Without at least an approximate start date, the
   rest of the workflow can only produce generic guidance.
5. **Classify the drop pattern (TRF-01).** Using exported or described data,
   determine whether clicks alone dropped or clicks and impressions dropped
   together, and the shape over time (sudden cliff, slow decay, seasonal
   wave) — see `./reference/gsc-analysis.md` for how to compute this from a
   Performance export.
6. **Eliminate causes in order**, following
   `monitor-debug/debugging-search-traffic-drops.md`'s own sequence: ranking
   update timing (TRF-02), technical causes (TRF-03), security issues
   (TRF-04), spam/manual-action exposure (TRF-05), seasonality (TRF-06), site
   move or migration (TRF-07), and reporting artifacts (TRF-08). For
   clicks-only drops, follow up with title and snippet competitiveness
   (TRF-09). Each check's method and grounding document are in
   `./reference/gsc-analysis.md`.
7. **Report hypotheses ranked by evidence.** For each surviving hypothesis,
   name the specific Search Console report the user should check next to
   confirm or rule it out. State plainly that these are hypotheses pending
   confirmation in Search Console, not a diagnosis.

## Scope boundary

This skill diagnoses a reported drop. It does not run a general audit absent a
reported drop, and technical checks it surfaces (TRF-03, TRF-04, TRF-05)
reuse `search-essentials` and `structured-data` findings rather than
duplicating that logic — run those skills for the full detail behind a
technical hypothesis.
