---
type: Skill Reference
title: Search Essentials check matrix
description: The eligibility-gate and spam-policy checks the search-essentials skill runs, their methods per mode, severities, and grounding documents.
tags: [skills, google-search, compliance]
status: stable
---

# Search Essentials check matrix

Read the grounding document(s) for a check before writing any finding that
cites it — see `../../shared/grounding.md`. Do not copy thresholds, policy
wording, or definitions from this table into a report; it names the source,
it is not the source.

## Eligibility gate (ESS-01–ESS-06)

Grounded in `essentials/technical.md`'s three requirements: Googlebot isn't
blocked, the page works, the page has indexable content.

| ID | Check | Live method | Static method | Severity | Grounding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ESS-01 | Googlebot not blocked by robots.txt for sampled URLs | `site_probe.py --base URL --check-url <sampled URLs>`, read the `allow`/robots verdict for each, using the Googlebot user agent | Read `robots.txt` (or the framework's `robots.ts`/config per `../../shared/targets.md`) and evaluate the sampled URL paths against its rules by hand | BLOCKER | `essentials/technical.md`, `crawling-indexing/robots/intro.md` |
| ESS-02 | Page returns HTTP 200, not 4xx/5xx or a redirect to a login page | `fetch_page.py URL`, read `status` and `redirect_chain`; a redirect landing on a login/auth path is a fail even if the final status is 200 | N/A — no server to respond; list under Checks not run | BLOCKER | `essentials/technical.md` |
| ESS-03 | Indexable textual content in a supported file type | `extract_signals.py --from-fetch -`, read `text_chars` (near-zero fails) and the response `Content-Type` from `fetch_page.py` against supported types | `extract_signals.py FILE`, same `text_chars` check; content type inferred from the file extension/build output | BLOCKER | `essentials/technical.md`, `crawling-indexing/indexable-file-types.md` |
| ESS-04 | No unintended `noindex`, via meta tag or `X-Robots-Tag` header | `extract_signals.py --from-fetch -`, read `meta_robots`/`meta_googlebot`, and `fetch_page.py`'s `x_robots_tag` header | `extract_signals.py FILE`, read `meta_robots`/`meta_googlebot`; the `X-Robots-Tag` header cannot be observed statically — note as Checks not run for that half of the check | BLOCKER | `crawling-indexing/block-indexing.md`, `crawling-indexing/robots-meta-tag.md` |
| ESS-05 | Publicly accessible, not login-gated | `fetch_page.py URL` with no auth; a redirect to a login/auth flow or a 401/403 fails this | Read the route/middleware config for auth gates; cannot confirm what an anonymous request actually receives | BLOCKER (live) / INFO (static) | `essentials/technical.md`, `crawling-indexing/control-what-you-share.md` |
| ESS-06 | robots.txt block and `noindex` conflict on the same URL | Cross-reference the ESS-01 robots verdict with the ESS-04 `meta_robots` value for the same URL | Same cross-reference against the static robots rules and page `meta_robots` | WARNING | `essentials/technical.md`, `crawling-indexing/block-indexing.md` |

**How to judge ESS-06.** A page can carry a `noindex` tag and still rank or
linger in the index if robots.txt blocks Googlebot from ever crawling it to
see that tag. `essentials/technical.md` states this directly: blocking with
robots.txt prevents crawling but a blocked URL can still appear in results,
and the correct way to keep a page out of the index is `noindex` *combined
with* allowing the crawl. Flag any sampled URL that is both robots-disallowed
and carries `noindex`.

## Spam policy indicators (ESS-10–ESS-19)

Grounded in the named sections of `essentials/spam-policies.md`. These are
indicators for human review, not manual-action determinations — only Google's
own systems and reviewers make that call.

| ID | Check | Live method | Static method | Severity | Grounding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| ESS-10 | Cloaking indicators | `fetch_page.py URL` with the default UA, then again with a Googlebot UA string; diff `title`/`text_excerpt` from `extract_signals.py` on both | N/A — no server to compare responses against; list under Checks not run | INFO ONLY | `essentials/spam-policies.md` (Cloaking), `crawling-indexing/crawlers-fetchers/verifying-googlebot.md` |
| ESS-11 | Hidden text and link abuse | `extract_signals.py`'s `inline_style_hidden_hints`, plus the model reading the page markup/CSS for off-screen positioning, zero opacity/font-size, or single-character links | Same, on the source/built HTML and CSS | BLOCKER if clear, WARNING if ambiguous | `essentials/spam-policies.md` (Hidden text and link abuse) |
| ESS-12 | Keyword stuffing | Model reads `text_excerpt`/full sampled text and judges against the policy's examples (unnatural repetition, list-like keyword blocks) | Same, on the rendered/source text | WARNING | `essentials/spam-policies.md` (Keyword stuffing) |
| ESS-13 | Sneaky redirects | `fetch_page.py`'s `redirect_chain` and `meta_refresh`; model checks whether the destination content matches what the origin URL promised, and scans for JS-based redirects in the page script | Read redirect config (`vercel.json`, `_redirects`, `.htaccess`, framework redirects per `../../shared/targets.md`) and any JS redirect in source | BLOCKER | `essentials/spam-policies.md` (Sneaky redirects) |
| ESS-14 | Unqualified paid/affiliate outbound links | `extract_signals.py`'s `links.sponsored`/`links.nofollow` counts vs. the model's read of commercial context (affiliate disclosures, "buy now" language) in the surrounding text | Same, on source/built markup | WARNING | `essentials/spam-policies.md` (Link spam), `crawling-indexing/qualify-outbound-links.md` |
| ESS-15 | Scaled content abuse, scraping, or thin affiliation | Model reviews sampled pages for templated/boilerplate structure repeated with minor substitutions, and for product copy that matches merchant listings verbatim | Same, across sampled source files/templates | WARNING | `essentials/spam-policies.md` (Scaled content abuse, Scraping, Thin affiliation) |
| ESS-16 | Doorway abuse | Compare sitemap URL patterns (`site_probe.py` sitemap parse) and sampled page titles/text for near-identical pages varying only by a city/query token | Same, across the static site's route list/generated pages | WARNING | `essentials/spam-policies.md` (Doorway abuse) |
| ESS-17 | Hacked-content indicators | Model scans `extract_signals.py` output for unfamiliar injected links, obfuscated `<script>` blocks (`script_bytes` spikes), or sitemap URLs unrelated to the site's stated topic | Same, on source files, plus a check for unfamiliar files in the build output | BLOCKER | `essentials/spam-policies.md` (Hacked content), `monitor-debug/security/malware.md` |
| ESS-18 | Misleading functionality, malicious practices, or unmoderated UGC spam | Model reads sampled pages for functionality claims that don't work as described, and for unmoderated comment/forum sections with spam links | Same, on source templates for UGC surfaces (comment forms, forums) | INFO | `essentials/spam-policies.md` (Misleading functionality, Malicious practices, User-generated spam) |
| ESS-19 | Expired-domain abuse or site-reputation abuse exposure | Ask the user about the domain's history (previously registered to an unrelated entity) and check for third-party content sections (sponsored/affiliate hubs) integrated inconsistently with the rest of the site | Same questions; cannot verify domain history statically | INFO | `essentials/spam-policies.md` (Expired domain abuse, Site reputation policy) |

**How to judge ESS-10.** CDNs, WAFs, and bot-mitigation layers routinely serve
different responses to unfamiliar user agents for reasons unrelated to
cloaking, so a diff alone is not proof. Report a diff as INFO only, and point
the user at Google's reverse-DNS verification method in
`crawling-indexing/crawlers-fetchers/verifying-googlebot.md` for a real
determination.

**How to judge ESS-11.** The policy explicitly excludes common, legitimate UI
patterns — accordions, tabs, sliders, tooltips, and screen-reader-only text.
Read the "not a violation" list in `essentials/spam-policies.md` before
flagging anything that toggles visibility; only flag content with no visible,
interactive path to being seen.

**How to judge ESS-12, ESS-15, ESS-16, ESS-18.** These require the model to
read sampled content and compare it against the policy's own illustrative
examples rather than run a mechanical test. Quote the specific text or markup
that triggered the finding as evidence; do not flag on a vague impression.
