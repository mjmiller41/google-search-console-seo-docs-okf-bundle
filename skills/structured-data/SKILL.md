---
name: structured-data
description: Audits structured data (JSON-LD, Microdata, RDFa) on sampled pages against Google Search Central's per-type documentation — required and recommended properties, general guidelines, and rich-result eligibility. Triggers on "structured data audit", "schema markup check", "is my JSON-LD valid", "rich results eligibility", "check my Product/Recipe/Article/JobPosting schema", or "why isn't my rich result showing". Not for indexing eligibility, robots.txt, or spam policies — route to search-essentials. Not for titles, snippets, favicons, or page experience — route to search-appearance.
type: Skill
title: Structured data audit
tags: [skills, google-search, structured-data]
status: stable
---

# Structured data audit

This skill validates structured data markup against the Google Search Central
documentation for the specific `@type` detected on each sampled page. It never
restates a required or recommended property list, a threshold, or a policy
definition from memory: the model reads the mapped type doc — looked up in
`./reference/type-index.md` — at run time, and that document is the entire
source of truth. This is deliberate. Google revises property tables often, and
copying them into this skill would drift out of date the moment it changed.
See `../shared/grounding.md` for the full rule.

## Workflow

1. **Resolve the bundle root.** `ROOT="${CLAUDE_PLUGIN_ROOT}"`; if unset, use
   the directory containing this file, two levels up. Quote `$ROOT` always.
   Verify with `ls "$ROOT/essentials/technical.md"` — if it is missing, tell
   the user the documentation bundle could not be found and stop rather than
   auditing from memory.
2. **Resolve the target and sample.** Follow `../shared/targets.md` to decide
   live, static, or mixed mode and to pick the page sample. Cache every
   fetched URL and script result for the session; never fetch a URL twice.
3. **Read before judging.** Read `../shared/report-format.md`,
   `./reference/checks.md`, and `./reference/type-index.md`. For each check
   you are about to run, open its grounding document(s) first and take the
   wording for the finding from what you just read, per `../shared/grounding.md`.
4. **Extract markup from each sampled page.** Run `extract_signals.py` (from a
   cached fetch or a static file) and read its `jsonld` array (each entry's
   `raw_ok`, `parsed`, `parse_error`, `excerpt`), `microdata_itemtypes`, and
   the page context fields (`title`, `text_excerpt`, `images`, `meta_robots`).
5. **Map each detected `@type` to a doc.** Look it up in
   `./reference/type-index.md`. For `Product`, apply the product-snippet vs.
   merchant-listing vs. product-variants routing nuance documented there.
6. **Validate against the mapped doc.** Read that doc's "Structured data type
   definitions" section in full, then check the parsed markup against its
   required properties (SD-02) and recommended properties (SD-03).
7. **Run the generic checks (SD-01, SD-04 through SD-08)** from
   `./reference/checks.md` against all detected markup, regardless of type.
8. **Opportunity pass.** For each sampled page, classify what the visible
   content actually is (article, product, recipe, event, job posting, and so
   on) and check `./reference/type-index.md` for a matching feature the page
   doesn't currently mark up. Only suggest markup the content genuinely
   supports — never suggest marking up something not visible on the page, per
   SD-04.
9. **Report.** Emit findings in the shared report structure. Every finding
   names the type doc it came from. Close with a recommendation to verify
   final markup in the [Rich Results Test](https://search.google.com/test/rich-results) —
   this audit is a snapshot against a mirrored doc set, not a live validator.

## Scope boundary

This skill validates the presence, correctness, and eligibility of structured
data markup. It does not determine whether a page is indexable at all (that's
`search-essentials`) or evaluate titles, meta descriptions, or other visual
search appearance elements (that's `search-appearance`). SD-05 reuses those
skills' signals rather than re-deriving them; run `search-essentials` alongside
this skill for a complete picture.
