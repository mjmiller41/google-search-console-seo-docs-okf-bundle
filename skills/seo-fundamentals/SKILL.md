---
name: seo-fundamentals
description: Audits a page or site against Google's SEO Starter Guide fundamentals — findability (links, sitemap), URL structure and directory organization, duplicate-content consolidation, content quality and usefulness, distracting ads/interstitials, crawlable links and anchor text, titles and meta descriptions, image optimization, video best practices, and promotion. Also flags SEO myths the guide itself warns against (meta keywords, keyword-stuffed titles, word-count padding). Triggers on "seo fundamentals", "seo starter guide check", "is my content seo friendly", "review my site structure", "check my titles and meta descriptions", or "seo myths check". Not for eligibility/spam-policy gating (robots blocking, noindex, cloaking, link spam) — route those to search-essentials. Not for structured-data markup validation — route to an appearance/structured-data skill.
type: Skill
title: SEO Fundamentals audit
tags: [skills, google-search, seo]
status: stable
---

# SEO Fundamentals audit

This skill checks a page or site against the practices in
`fundamentals/seo-starter-guide.md`, section by section. It never restates
the guide's advice, examples, or wording from memory — the check matrix in
`./reference/checks.md` names which grounding document answers each check,
and the model reads that document before writing any finding that cites it.
See `../shared/grounding.md` for the full rule.

## Workflow

1. **Resolve the bundle root.** `ROOT="${CLAUDE_PLUGIN_ROOT}"`; if unset, use
   the directory containing this file, two levels up. Quote `$ROOT` always.
   Verify with `ls "$ROOT/essentials/technical.md"` — if it is missing, tell
   the user the documentation bundle could not be found and stop rather than
   auditing from memory.
2. **Resolve the target and sample.** Follow `../shared/targets.md` to decide
   live, static, or mixed mode and to pick the page sample. Cache every
   fetched URL and script result for the session; never fetch a URL twice —
   if `search-essentials` already ran in this audit, reuse its fetches.
3. **Read before judging.** Read `../shared/report-format.md` for the output
   contract and `./reference/checks.md` for the full check matrix. For each
   check, open its grounding document(s) first and take the wording for the
   finding from what you just read, per `../shared/grounding.md`.
4. **Run FUN-01 through FUN-09** using the sampled pages, the scripts named
   in `./reference/checks.md`, and model judgment where the check is
   qualitative. Skip FUN-09 (video) entirely and note it as not applicable if
   no video content is detected in the sample.
5. **Run FUN-10 through FUN-12.** FUN-10 (promotion) is conversational — ask
   the user about their promotion channels rather than testing anything.
   FUN-11 (anti-myth scan) flags practices the guide itself calls wasted or
   harmful effort. FUN-12 states the guide's own expectation-setting guidance
   on how long changes take to show results.
6. **Report.** Emit findings in the shared report structure. FUN-07 (titles
   and meta descriptions) overlaps with a full audit's `APP-01`/`APP-02`
   checks if an appearance skill also ran; note the overlap rather than
   duplicating the finding.

## Scope boundary

This skill answers "is this content well-built by Google's own SEO
guidance," assuming it already passed the eligibility gate. It does not
determine whether a page is indexable, blocked, or in spam-policy violation
— that is `search-essentials`, and should run first or alongside this skill.
It does not validate structured data markup. Run both skills for a full
audit; the router merges their findings into one report per
`../shared/report-format.md`.
