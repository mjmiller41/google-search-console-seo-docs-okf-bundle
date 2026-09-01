---
type: Skill Reference
title: Crawling and indexing check matrix
description: The CRA-01 through CRA-20 checks this skill runs, their live and static methods, severities, and the grounding document that supplies each check's actual rules — never the rules themselves.
tags: [skills, google-search, crawling]
status: stable
---

# Crawling and indexing check matrix

None of these rows restate a threshold, a valid-value list, or a limit.
Google changes those. Open the grounding document for the row before writing
a finding against it, and take the wording of the requirement from what you
just read there, not from this table.

| ID | Check | Live method | Static method | Severity | Grounding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CRA-01 | robots.txt present at origin root, parseable, within the documented size limit, no malformed lines or unknown directives | `site_probe.py` `robots{status,issues,unknown_directives}` | Same fields via `site_probe.py --local DIR` | WARNING | `crawling-indexing/robots-txt/robots-txt-spec.md`, `crawling-indexing/robots/intro.md` |
| CRA-02 | robots.txt does not block the whole site or critical CSS/JS assets | `robots.blocks_entire_site`, `robots_verdicts[]` for sampled pages and their known asset paths | Same, `--local` | BLOCKER (site-wide) / WARNING (assets) | `crawling-indexing/robots/intro.md`, `crawling-indexing/javascript/javascript-seo-basics.md` |
| CRA-03 | Sitemap exists, valid XML, within the documented URL/size limits, index file used when needed | `site_probe.py` `sitemaps[]` (`url_count`, `over_50k_urls`, `bytes`, `over_50mb`, `parse_error`), `sitemap_url_total` | Same, `--local`; note if generation at deploy time is possible | WARNING | `crawling-indexing/sitemaps/overview.md`, `crawling-indexing/sitemaps/build-sitemap.md`, `crawling-indexing/sitemaps/large-sitemaps.md` |
| CRA-04 | Sitemap URLs are canonical, absolute, and resolve (sample) | Fetch a sample of `sitemaps[].sitemap_refs`/entries with `fetch_page.py`; compare final status and `canonical` from `extract_signals.py` | Resolve sample entries against build output files; cannot confirm live status | WARNING | `crawling-indexing/sitemaps/build-sitemap.md` |
| CRA-05 | `rel=canonical` present, absolute, self-consistent, one per page, targets an indexable 200 URL | `extract_signals.py` `canonical`; verify target with a cached `fetch_page.py` result | `extract_signals.py canonical` on the built file; target status unverifiable | WARNING | `crawling-indexing/canonicalization.md`, `crawling-indexing/canonicalization-troubleshooting.md` |
| CRA-06 | Permanent moves use server-side 301/308; no long chains or loops; meta-refresh/JS redirects only as a last resort | `fetch_page.py` `redirect_chain[]` | Deployment redirect config (`vercel.json`, `netlify.toml`, `_redirects`, `.htaccess`) per `../shared/targets.md`; framework config for server-side redirects | WARNING | `crawling-indexing/301-redirects.md` |
| CRA-07 | http→https and www/non-www variants consolidate to one origin | Fetch each variant origin with `fetch_page.py`, compare `redirect_chain[]`/`final_url` | Check redirect config for variant-consolidation rules | WARNING | `crawling-indexing/canonicalization.md`, `crawling-indexing/301-redirects.md` |
| CRA-08 | robots meta and `X-Robots-Tag` use valid rule names with the intended effect; conflicts resolve most-restrictive | `extract_signals.py` `meta_robots`, `meta_googlebot`; `fetch_page.py` `x_robots_tag` | `extract_signals.py meta_robots`/`meta_googlebot` on the built file; no HTTP header available | WARNING | `crawling-indexing/robots-meta-tag.md` |
| CRA-09 | Right tool for the intent: `noindex` to keep a page out of the index, robots.txt to manage crawl load | Cross-reference `meta_robots`/`x_robots_tag` against `robots_verdicts` for the same URL — a disallowed URL with `noindex` in its head is the tell | Cross-reference the head against robots.txt rules | WARNING | `crawling-indexing/block-indexing.md`, `crawling-indexing/robots/intro.md` |
| CRA-10 | Content present without JS execution, or clearly renderable; empty app-shell detection | `extract_signals.py` `app_shell_suspect`, `app_shell_container`, `text_chars`, `script_bytes` on the raw fetch | Same fields against source/build HTML; flag as template-level if no build output | WARNING | `crawling-indexing/javascript/javascript-seo-basics.md`, `crawling-indexing/javascript/fix-search-javascript.md` |
| CRA-11 | No fragment-based routing; dynamic rendering not relied on | Inspect sampled URLs for `#!`/hash-route patterns; check for user-agent-conditional serving in `fetch_page.py` headers | Inspect router config and framework markers from `../shared/targets.md` | WARNING | `crawling-indexing/javascript/dynamic-rendering.md`, `crawling-indexing/javascript/fix-search-javascript.md` |
| CRA-12 | Lazy-loaded content loads without user interaction | `extract_signals.py` `images.lazy_native`, `inline_style_hidden_hints[]` | Same, on built HTML | WARNING | `crawling-indexing/javascript/lazy-loading.md` |
| CRA-13 | Mobile-first readiness: viewport present, mobile/desktop content parity | `extract_signals.py` `viewport`; compare `text_chars`/`h1_count` between a mobile-UA and default fetch if the site serves separate mobile URLs | `extract_signals.py viewport` on built file; parity across templates only | WARNING | `crawling-indexing/mobile/mobile-sites-mobile-first-indexing.md` |
| CRA-14 | `<head>` contains only valid elements; no invalid element truncating metadata | `extract_signals.py` `head_validity{invalid_elements,metadata_after_invalid}` | Same, on built or template HTML | WARNING | `crawling-indexing/valid-page-metadata.md` |
| CRA-15 | URL structure readable; no uncontrolled parameter/facet explosion | Inspect sampled URLs and `sitemap_url_total` vs. sampled path-segment diversity | Inspect route/URL-generation config | WARNING | `crawling-indexing/url-structure.md` |
| CRA-16 | Missing pages return a real 404/410, not a soft 200 | `fetch_page.py` a deliberately invented path under the target; compare `status` and rendered content to a known real page | Not testable — list under Checks not run | WARNING | `crawling-indexing/troubleshoot-crawling-errors.md` |
| CRA-17 | hreflang, if present: valid codes, absolute URLs, reciprocal, self-referencing, x-default | `extract_signals.py` `hreflang[]`; cross-check reciprocity across the sampled set | Same field on built/template files | WARNING | `specialty/international/localized-versions.md` |
| CRA-18 | AMP, only if `amphtml` detected: pairing and canonical correctness | `extract_signals.py` `amphtml`; fetch the AMP URL and check its `canonical` points back | Same, if the AMP file exists in build output | INFO | `crawling-indexing/amp/overview.md`, `crawling-indexing/amp/validate-amp.md` |
| CRA-19 | Fake-Googlebot advisory, only if the user suspects crawler abuse in logs | Not a probe — advise the reverse-DNS verification method from the grounding doc | Same | INFO | `crawling-indexing/crawlers-fetchers/verifying-googlebot.md` |
| CRA-20 | Site move, only if one happened: 1:1 redirect mapping, old and new sitemaps, no mass 404 | Sample old URLs (from the user or an old sitemap) against `fetch_page.py`/`redirect_chain[]` | Compare old-to-new URL list against redirect config | WARNING | `crawling-indexing/site-move-with-url-changes.md` |

## How to judge

**CRA-01 / CRA-03.** "Documented size limit" and "documented URL limit" mean
exactly that — read `crawling-indexing/robots-txt/robots-txt-spec.md` and
`crawling-indexing/sitemaps/large-sitemaps.md` for the current numbers before
flagging a file as oversized. Do not compare against a remembered number.

**CRA-08.** `crawling-indexing/robots-meta-tag.md` documents two lists: the
rules Google currently honors, and a separate list of historical rules that
Google no longer uses and silently ignores. A value from the second list
isn't a syntax error — it's a no-op the page owner probably still thinks is
working. Read both lists before judging a value invalid, and say which list
it fell into. Also check the doc's own note on multi-crawler combination
(named-crawler rules add to, not replace, unnamed `robots` rules) before
calling a combination a conflict.

**CRA-09.** A URL that is both disallowed in robots.txt and carries
`noindex` in its head is the specific anti-pattern this check catches:
robots.txt disallow prevents the crawl that would ever let Google see the
`noindex` rule, so the page can still be indexed without a snippet. Ground
this in `crawling-indexing/block-indexing.md`, which explains the intended
division of labor between the two mechanisms.

**CRA-16.** Live mode only. In static mode this is unverifiable — no server
to return a status code — and belongs in "Checks not run," not a pass.

**CRA-18.** Only evaluate when `extract_signals.py` reports a non-empty
`amphtml` field on at least one sampled page. Otherwise omit the row from
findings and don't mention AMP at all.

**CRA-19 / CRA-20.** Both are advisory-only and conditional on what the user
actually asked about — CRA-19 fires only if the user raises suspected
crawler impersonation, CRA-20 only if the user mentions a completed or
in-progress site move. Do not run either speculatively.
