---
name: search-essentials
description: Audits whether a page or site meets Google's Search Essentials — the eligibility gate (Googlebot access, HTTP 200, indexable content, no unintended noindex, public accessibility) and the spam policies that can get content demoted or removed (cloaking, hidden text, keyword stuffing, sneaky redirects, link spam, scaled content abuse, doorway abuse, hacked content, and related tactics). Triggers on "search essentials", "is this page eligible for Google", "spam policy check", "am I blocking Googlebot", "will this get penalized", "manual action risk", or "check indexing eligibility". Not for on-page SEO quality, titles/meta descriptions, image alt text, or promotion advice — route those to seo-fundamentals. Not for rich-result/structured-data eligibility — route to an appearance/structured-data skill.
type: Skill
title: Search Essentials audit
tags: [skills, google-search, compliance]
status: stable
---

# Search Essentials audit

This skill checks the bare-minimum eligibility gate defined in
`essentials/technical.md` and the spam policies defined in
`essentials/spam-policies.md`. It never restates thresholds, definitions, or
policy wording from memory — the check matrix in `./reference/checks.md` names
which grounding document answers each check, and the model reads that document
before writing any finding that cites it. See `../shared/grounding.md` for the
full rule.

## Workflow

1. **Resolve the bundle root.** `ROOT="${CLAUDE_PLUGIN_ROOT}"`; if unset, use
   the directory containing this file, two levels up. Quote `$ROOT` always.
   Verify with `ls "$ROOT/essentials/technical.md"` — if it is missing, tell
   the user the documentation bundle could not be found and stop rather than
   auditing from memory.
2. **Resolve the target and sample.** Follow `../shared/targets.md` to decide
   live, static, or mixed mode and to pick the page sample. Cache every
   fetched URL and script result for the session; never fetch a URL twice.
3. **Read before judging.** Read `../shared/report-format.md` for the output
   contract and `./reference/checks.md` for the full check matrix. For each
   check you are about to run, open its grounding document(s) first and take
   the wording for the finding from what you just read, per
   `../shared/grounding.md`.
4. **Run the gate checks (ESS-01 through ESS-06)** using `site_probe.py` and
   `fetch_page.py` + `extract_signals.py` as named in `./reference/checks.md`.
   These determine baseline eligibility.
5. **Run the spam-policy checks (ESS-10 through ESS-19)** against the sampled
   pages. Most of these need the model to read the page text, markup, and
   link structure and judge it against a named section of
   `essentials/spam-policies.md` — the "How to judge" notes in
   `./reference/checks.md` say what to look for. These are indicators for
   human review, not a manual-action determination.
6. **Report.** Emit findings in the shared report structure. If any BLOCKER
   fires, state plainly that the page is **not eligible** to appear in Google
   Search until it is fixed. Regardless of outcome, include this caveat from
   `essentials/technical.md` verbatim in the report: *"Just because a page
   meets these requirements doesn't mean that a page will be indexed;
   indexing isn't guaranteed."* Meeting the gate is necessary, not sufficient.

## Scope boundary

This skill answers "is this content allowed to appear in Google Search at
all." It does not evaluate title/description quality, content usefulness,
image optimization, or promotion — that is `seo-fundamentals`. It does not
validate structured data markup. Run both skills for a full audit; the router
merges their findings into one report per `../shared/report-format.md`.
