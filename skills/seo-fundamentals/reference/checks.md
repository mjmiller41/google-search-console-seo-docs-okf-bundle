---
type: Skill Reference
title: SEO Fundamentals check matrix
description: The checks the seo-fundamentals skill runs, keyed to the SEO Starter Guide's own sections, their methods per mode, severities, and grounding documents.
tags: [skills, google-search, seo]
status: stable
---

# SEO Fundamentals check matrix

Read the grounding document(s) for a check before writing any finding that
cites it — see `../../shared/grounding.md`. Do not copy the guide's advice,
examples, or wording into this table or into a report; it names the source,
it is not the source. Check IDs below are keyed 1:1 to the H2/H3 sections of
`fundamentals/seo-starter-guide.md`.

| ID | Check | Live method | Static method | Severity | Grounding |
| :--- | :--- | :--- | :--- | :--- | :--- |
| FUN-01 | "Help Google find your content" — internal links and a sitemap, especially on large or new sites | `site_probe.py`'s sitemap parse (presence, URL count) plus `extract_signals.py`'s `links.internal` count on sampled pages | Check for a sitemap file or the framework's sitemap generator per `../../shared/targets.md`, and `links.internal` from the same script on source/built pages | WARNING | `fundamentals/seo-starter-guide.md` ("Help Google find your content"), `crawling-indexing/sitemaps/overview.md` |
| FUN-02 | "Organize your site" — descriptive, readable URLs and logical directory grouping | Model reads the sampled URL paths (from `site_probe.py`'s sample and the sitemap) and judges them against the guide's own examples | Model reads the route list or file-based routing paths | WARNING | `fundamentals/seo-starter-guide.md` ("Organize your site" / "Use descriptive URLs" / "Group topically similar pages in directories"), `crawling-indexing/url-structure.md` |
| FUN-03 | "Reduce duplicate content" — one canonical per piece of content, via redirect or `rel="canonical"` | `extract_signals.py`'s `canonical` field on sampled pages; flag pages with no canonical and content that duplicates another sampled URL | Same, on source/built pages; redirect consolidation cannot be confirmed without a server — note under Checks not run for that half | WARNING | `fundamentals/seo-starter-guide.md` ("Reduce duplicate content"), `crawling-indexing/consolidate-duplicate-urls.md` |
| FUN-04 | "Make your site interesting and useful" — organized, unique, useful content that anticipates readers' search terms | Model reads `text_excerpt`/sampled page text and judges readability, organization, and uniqueness against the guide's attributes list, and separately against `fundamentals/creating-helpful-content.md` | Same, on source/rendered text | WARNING/INFO | `fundamentals/seo-starter-guide.md` ("Make your site interesting and useful" / "Expect your readers' search terms"), `fundamentals/creating-helpful-content.md` |
| FUN-05 | "Avoid distracting advertisements" — ads and interstitials don't block or distract from content | Model reads the fetched page body/rendered markup for interstitial overlays, popups, or ad density that obscures content; live mode only, since rendering behavior isn't visible statically | Model reads source templates for interstitial/popup components, flagged as lower-confidence since rendered behavior can't be confirmed | WARNING | `fundamentals/seo-starter-guide.md` ("Avoid distracting advertisements"), `appearance/avoid-intrusive-interstitials.md` |
| FUN-06 | "Link to relevant resources" — crawlable links, descriptive anchor text, qualified external links | `extract_signals.py`'s `links.non_crawlable[]`, `empty_anchor`, `generic_anchor` counts, and `links.sponsored`/`nofollow` vs. external link context | Same, on source/built markup | WARNING | `crawling-indexing/links-crawlable.md`, `crawling-indexing/qualify-outbound-links.md` |
| FUN-07 | "Influence how your site looks in Google Search" — unique, accurate titles and useful meta descriptions | `extract_signals.py`'s `title`, `title_length`, `meta_description` per sampled page; flag duplicates across the sample | Same, on source/built pages | WARNING | `fundamentals/seo-starter-guide.md` ("Influence your title links" / "Control your snippets"), `appearance/title-link.md` |
| FUN-08 | "Add images to your site, and optimize them" — alt text, placement near relevant text, descriptive filenames | `extract_signals.py`'s `images.missing_alt` count, plus model review of image placement relative to surrounding text and of filename patterns in the markup | Same, on source/built markup | WARNING | `fundamentals/seo-starter-guide.md` ("Add images to your site, and optimize them"), `appearance/google-images.md` |
| FUN-09 | "Optimize your videos" — only if video content is detected in the sample | Model checks for `<video>` elements, video embeds, or `jsonld` `VideoObject` entries in `extract_signals.py` output; if none found, mark not applicable | Same, on source/built markup | INFO | `appearance/video.md` |
| FUN-10 | "Promote your website" — promotion channels | Conversational only: ask the user what promotion channels they use (social, community engagement, advertising, word of mouth). No automated test. | Same | INFO | `fundamentals/seo-starter-guide.md` ("Promote your website") |
| FUN-11 | "Things we believe you shouldn't focus on" — anti-myth scan | `extract_signals.py`'s `meta_keywords_present` field for the meta-keywords myth; model reads `title`/`text_excerpt` for keyword-repetition or artificial word-count padding | Same, on source/built pages | INFO | `fundamentals/seo-starter-guide.md` ("Things we believe you shouldn't focus on") |
| FUN-12 | "How long until I see impact in search results?" — expectation setting | No test. Report the guide's own timeline guidance to set the user's expectations after any fixes are applied. | Same | INFO | `fundamentals/seo-starter-guide.md` ("How long until I see impact in search results?") |

## How to judge

**FUN-01.** The guide treats a sitemap as optional technical work, useful
mainly for large or newly-published sites, not a universal requirement — read
the section's own framing before flagging a missing sitemap as more than a
WARNING on a small, well-linked site.

**FUN-04.** This check and `fundamentals/creating-helpful-content.md` overlap
by design; the starter guide explicitly defers to that document for what
"helpful, reliable, people-first" means. Read both before writing the
finding, and cite whichever document's wording the finding actually rests on.

**FUN-05.** Static analysis of ad/interstitial behavior is unreliable — popups
and overlays are often injected at runtime. Report static-mode findings here
at reduced confidence and say so explicitly.

**FUN-07.** If an `appearance` skill's `APP-01`/`APP-02` checks already ran in
this audit, do not duplicate the finding — reference it and move on. Only run
this check standalone if no appearance skill is in scope for the audit.

**FUN-09.** Do not invent a finding when no video content exists in the
sample; list it as not applicable rather than forcing a judgment.

**FUN-11.** Flag only the specific myths the guide itself names: the meta
keywords tag, keyword stuffing, keywords in the domain/URL path, minimum or
maximum content length, subdomains vs. subdirectories, PageRank, the
duplicate-content "penalty", heading order/count, and E-E-A-T as a ranking
factor. Quote the guide's own framing rather than treating any of these as a
hard rule on your own authority.
