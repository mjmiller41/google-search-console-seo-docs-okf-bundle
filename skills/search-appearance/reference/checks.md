---
type: Skill Reference
title: Search appearance check matrix
description: The APP-01 through APP-13 checks this skill runs, their live and static methods, severities, and the grounding document that supplies each check's actual guidance — never the guidance itself.
tags: [skills, google-search, search-appearance]
status: stable
---

# Search appearance check matrix

None of these rows restate a best practice, a guideline, or a threshold.
Google changes those. Open the grounding document for the row before writing
a finding against it, and take the wording of the requirement from what you
just read there, not from this table.

| ID | Check | Live method | Static method | Severity | Grounding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| APP-01 | `<title>` present, unique per page, descriptive, not boilerplate or stuffed; consistent with on-page prominence | `extract_signals.py` `title`, `title_length`, `h1_count`; compare titles across the sampled set for duplication/near-duplication | Same fields on built/template files | WARNING | `appearance/title-link.md` |
| APP-02 | Meta description present, unique, page-specific; snippet controls (`nosnippet`, `max-snippet`, `data-nosnippet`) intentional | `extract_signals.py` `meta_description`, `meta_robots`/`meta_googlebot` for snippet rules; read the raw `body` for `data-nosnippet` attributes (no dedicated field) | Same, on built/template files | WARNING | `appearance/snippet.md`, `crawling-indexing/robots-meta-tag.md` |
| APP-03 | Favicon declared on the homepage, crawlable, meets the documented guidelines | `extract_signals.py` `favicons[]` on the homepage fetch; cross-check the icon URL and homepage against `site_probe.py` `robots_verdicts` for crawlability | `favicons[]` on the built homepage file; crawlability unverifiable, note this | WARNING | `appearance/favicon-in-search.md` |
| APP-04 | Site name signals: `WebSite` structured data on the homepage, consistent naming | `extract_signals.py` `jsonld` on the homepage for a `WebSite` type; compare `og`/`title` site-name fragments across sampled pages | Same, on built files | INFO | `appearance/site-names.md` |
| APP-05 | Sitelinks readiness: clear structure, informative link text (no direct control) | `extract_signals.py` `links{non_crawlable,empty_anchor,generic_anchor}` as a heuristic proxy for link-text quality | Same fields on built/template files | INFO | `appearance/sitelinks.md` |
| APP-06 | Publication/updated dates consistent between visible text and markup; no artificial freshness | Compare `extract_signals.py` `jsonld` date fields and any meta date tags against the visible date in `text_excerpt` | Same, on built/template files | WARNING | `appearance/publication-dates.md` |
| APP-07 | HTTPS served, no mixed content | `fetch_page.py` `final_url` scheme; `extract_signals.py` `mixed_content_urls[]` | Search built assets for hardcoded `http://` references; TLS itself is unverifiable, note this | WARNING | `appearance/page-experience.md` |
| APP-08 | Core Web Vitals: real field data when a key is configured, heuristics otherwise | With `CRUX_API_KEY` or `PSI_API_KEY` set (see `../../shared/integrations.md`): `cwv_field_data.py` on the origin plus 2–3 representative pages, reporting the API's own per-metric verdicts. Without a key: `extract_signals.py` `images.missing_dimensions`, `script_bytes` heuristics only, each labeled "heuristic, not a CWV measurement", and the check goes in Checks not run with the setup pointer | Field data still applies if the site is live and a key is set; template heuristics otherwise, same labeling | INFO | `appearance/core-web-vitals.md`, `appearance/page-experience.md` |
| APP-09 | No intrusive interstitial covering main content on entry (documented exceptions acceptable) | Model judgment reading the fetched body/DOM for full-viewport overlay patterns on load; `extract_signals.py` `inline_style_hidden_hints[]` as a supporting signal | Same, on built/template HTML | WARNING | `appearance/avoid-intrusive-interstitials.md` |
| APP-10 | Image preview settings and quality images for Discover/Images eligibility | `extract_signals.py` `meta_robots`/`meta_googlebot` for `max-image-preview`; `images{count,missing_alt}` | Same fields on built/template files | INFO | `appearance/google-discover.md`, `appearance/google-images.md` |
| APP-11 | Reviews content quality bar, only if the site publishes reviews | `extract_signals.py` `jsonld`/`microdata_itemtypes` for `Review`/`AggregateRating` types on sampled pages | Same, on built/template files | INFO | `appearance/reviews-system.md` |
| APP-12 | Ranking-systems context: name which systems plausibly apply; framing, not pass/fail | Model judgment from sampled content type and structure — no script signal | Same | INFO | `appearance/ranking-systems-guide.md`, `appearance/core-updates.md`, `appearance/spam-updates.md` |
| APP-13 | Which SERP visual elements this site could realistically earn, from what was detected | `extract_signals.py` `jsonld`/`microdata_itemtypes` across the sampled set, matched against what each grounding doc says is eligible | Same, on built/template files | INFO | `appearance/visual-elements-gallery.md`, `appearance/featured-snippets.md` |

## How to judge

**APP-01.** `appearance/title-link.md` documents specific named failure
patterns (half-empty titles, obsolete titles, inaccurate titles,
micro-boilerplate, no clear main title, site-name duplication) as well as
the best practices that prevent them. Match what you observe to the actual
pattern named in the doc rather than a generic "title could be better" —
read the "Common issues" section, not just "Best practices," before writing
the finding.

**APP-02.** `appearance/snippet.md` distinguishes a keyword-list description
from a genuine summary with worked bad/better examples — use that bar, not a
generic length check, to judge quality. Snippet-control intent (`nosnippet`,
`max-snippet`, `data-nosnippet`) is grounded in
`crawling-indexing/robots-meta-tag.md`; a description missing while a
`nosnippet`/`max-snippet:0` rule is present is expected behavior, not a
finding.

**APP-03.** `appearance/favicon-in-search.md` scopes a favicon to the
hostname's actual homepage, not a subdirectory home page — a favicon
declared correctly on `/blog/` doesn't make `example.com` eligible. Confirm
the `<link>` is on the sampled homepage specifically, and that both the icon
and the homepage are crawlable, before treating a missing favicon as a
finding.

**APP-06.** Read both the visible date in `text_excerpt` and the structured
date fields. A visible date newer than the structured date (or vice versa)
is the mismatch this check catches. A structured `dateModified` that updates
on every crawl with no corresponding content change is the artificial
freshness pattern — flag it as a judgment call, not a certainty.

**APP-08.** Never state or imply a measured Core Web Vitals score or a
pass/fail verdict — this audit has no field data. Every finding here is
prefixed as a heuristic risk (e.g., images missing dimensions can contribute
to layout shift) and closes by pointing the user at the Search Console Core
Web Vitals report, PageSpeed Insights, or CrUX for an actual assessment.

**APP-11 / APP-12 / APP-13.** APP-11 fires only when review or rating
structured data is actually detected on a sampled page — omit it entirely
otherwise. APP-12 and APP-13 are never pass/fail: report them as context
("this content type plausibly interacts with these systems," "this
structured data makes X visual element plausible") and say so explicitly in
the finding.
