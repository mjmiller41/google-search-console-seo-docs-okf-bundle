---
type: Skill Reference
title: Audit report format
description: The shared report structure, finding schema, and severity rules every audit skill emits so results merge into one document.
tags: [skills, reporting]
status: stable
---

# Audit report format

A skill run on its own emits this whole document. Run under the
`google-search-audit` router, it emits only its findings and verdict line, and
the router merges them.

## Severity

| Severity | Meaning |
| :--- | :--- |
| **BLOCKER** | The page or site cannot appear in Google Search, or violates a spam policy. |
| **WARNING** | Works today, but goes against documented guidance or risks demotion. |
| **INFO** | Advisory, opportunity, or a judgment call needing human confirmation. |

Category verdict: any blocker is **FAIL**; otherwise any warning is **WARN**;
otherwise **PASS**.

Overall verdict: **Not eligible** if any eligibility blocker fired,
**Eligible with issues** if anything else fired, **Good standing** if nothing did.

Do not invent numeric scores. A "72/100" implies a precision this audit does
not have, and Google publishes no such scale. Verdicts and counts only.

## Structure

```markdown
# Google Search Audit — <target> — <YYYY-MM-DD>

**Mode:** live | static (Next.js, analyzed `out/`) | mixed
**Sample:** 8 of 1,240 sitemap URLs (listed in the appendix)
**Grounding:** Google Search Central documentation mirrored <bundle sync date>.
The live documentation at developers.google.com is authoritative and may have
changed since.

## Scorecard

| Category | Verdict | Blockers | Warnings | Info |
| :--- | :--- | ---: | ---: | ---: |
| Search Essentials (ESS) | FAIL | 1 | 2 | 3 |
| Crawling & Indexing (CRA) | WARN | 0 | 4 | 2 |

**Overall: Eligible with issues** — one sentence saying why.

## Findings

### [ESS-04] Unintended noindex on /pricing — BLOCKER

- **Evidence:** `<meta name="robots" content="noindex">` in `out/pricing/index.html`
- **Why it matters:** one sentence, paraphrased from the grounding document.
- **Fix:** the concrete action, in the user's own stack where known.
- **Grounding:** crawling-indexing/block-indexing.md —
  https://developers.google.com/search/docs/crawling-indexing/block-indexing
  (Google last updated 2025-12-10; mirrored 2026-09-01)

## Passed blocker checks

Brief confirmations that the gate checks passed (ESS-01 robots access, ESS-02
HTTP 200, ...). Users need to see what was verified, not only what failed.

## Checks not run

| Check | Reason |
| :--- | :--- |
| ESS-02 HTTP status | static mode — no server |
| APP-08 Core Web Vitals field data | requires CrUX or PageSpeed Insights |

## Methodology and limitations

Sampling, mode limits, the JavaScript-rendering caveat when it applies, and the
politeness settings used.
```

## Finding rules

- **One finding per check ID per affected page group.** Ten pages missing a
  canonical is one finding listing ten pages, not ten findings.
- **Cite always.** Every finding carries at least one bundle-relative document
  path, its upstream URL, and both dates. A finding you cannot ground is a
  finding you should not write. See [grounding.md](./grounding.md).
- **Evidence is concrete.** Quote the markup, the header, the URL, the file and
  location. "Title could be better" is not evidence; the title string is.
- **Check IDs are stable.** `ESS-04` means the same thing across runs, so users
  can diff audits over time and the router can deduplicate.
- **Say what you could not determine.** Silence reads as a pass.

## Attribution

Findings paraphrase Google's documentation, which is licensed CC BY 4.0. Close
standalone reports with:

> Guidance derived from Google Search Central documentation (CC BY 4.0),
> mirrored in this bundle. Google Search is a Google product; this audit is
> unofficial.
