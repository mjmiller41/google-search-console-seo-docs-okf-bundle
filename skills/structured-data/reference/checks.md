---
type: Skill Reference
title: Structured data check matrix
description: The structured data checks the structured-data skill runs, their methods per mode, severities, and grounding documents.
tags: [skills, structured-data, reference]
status: stable
---

# Structured data check matrix

Read the grounding document(s) for a check before writing any finding that
cites it — see `../../shared/grounding.md`. Do not copy required or
recommended property lists, thresholds, or policy wording out of the docs
named here (or out of `./type-index.md`'s target docs) into a report; this
table names the source, it is not the source.

| ID | Check | Live method | Static method | Severity | Grounding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| SD-01 | JSON-LD parses as valid JSON with `@context` and `@type` | `extract_signals.py --from-fetch -`; read each `jsonld[]` entry's `raw_ok`, `parsed`, and `parse_error` | `extract_signals.py FILE`; same fields | BLOCKER for the feature | `appearance/structured-data/intro-structured-data.md` |
| SD-02 | Required properties present, per the mapped type doc's definitions table | Model reads the parsed JSON-LD / `microdata_itemtypes` against the "Structured data type definitions" table in the doc mapped by `./type-index.md` | Same, on the parsed static markup | BLOCKER for the feature | The mapped type doc, via `./type-index.md` |
| SD-03 | Recommended properties missing | Same comparison as SD-02, against the doc's recommended-properties table; list as enhancement opportunities, not failures | Same | INFO | The mapped type doc, via `./type-index.md` |
| SD-04 | Markup describes the page it is on and matches visible content; no invisible or fabricated data (e.g. ratings not shown to users) | Model compares parsed structured data values (name, author, rating, price, and so on) against `title`, `text_excerpt`, and `images` from `extract_signals.py` | Same, on the parsed static page content | BLOCKER | `appearance/structured-data/sd-policies.md` |
| SD-05 | The marked-up page is itself crawlable and indexable | Reuse the `search-essentials` skill's ESS-01 and ESS-04 signals for the same URL rather than re-deriving them | Same reuse, on static-mode signals | WARNING | `appearance/structured-data/sd-policies.md` |
| SD-06 | Format sanity: JSON-LD preferred; conflicting duplicate entities across JSON-LD and microdata | Diff `jsonld[].parsed` `@type`/identity values against `microdata_itemtypes` for the same page | Same | INFO | `appearance/structured-data/intro-structured-data.md` |
| SD-07 | JS-injected structured data cannot be confirmed statically; flag for Rich Results Test verification | If `jsonld` is empty but the page's markup or bundle suggests client-side rendering, note the markup as unconfirmed rather than absent | Static analysis never observes post-render JS injection; always list as unconfirmed when analyzing source/templates | INFO | `appearance/structured-data/generate-structured-data-with-javascript.md` |
| SD-08 | Site-level markup: `Organization` on the homepage, `WebSite` site name, `BreadcrumbList` on deep pages | Run `extract_signals.py` on the homepage and on deep sampled pages; check `jsonld`/`microdata_itemtypes` for each expected type | Same, on the static homepage and deep sampled pages | INFO | `appearance/structured-data/organization.md`, `appearance/site-names.md`, `appearance/structured-data/breadcrumb.md` |

**How to judge SD-02 and SD-03.** Read the mapped doc's "Structured data type
definitions" section in full before comparing — required and recommended
properties differ by type and by nested object (for example `Recipe` vs.
`HowToStep` vs. `ItemList` within the same doc). Quote the specific property
that is missing or present as evidence.

**How to judge SD-04.** This is a judgment call, not a mechanical diff. A
`Product` price that matches the page, and a fabricated `aggregateRating` the
page never shows to users, are both covered by this check; the second is a
policy violation even when it passes SD-01 through SD-03 cleanly.

**How to judge SD-05.** This check exists so a structured-data audit doesn't
silently imply eligibility for a page that can't be indexed at all. Don't
re-run the crawl/index checks here — cite the `search-essentials` finding for
the same URL.
