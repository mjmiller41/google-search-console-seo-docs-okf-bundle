# Google Search Central Documentation — OKF Bundle

An [Open Knowledge Format (OKF) v0.2](https://github.com/mjmiller41/cli-agent-okf) knowledge bundle
mirroring the official **Google Search Central** documentation
(<https://developers.google.com/search/docs>).

157 documentation pages — every page linked from the site's left-hand navigation
(`nav.devsite-book-nav`) — converted into OKF concept documents with provenance
frontmatter, source citations, and bundle-relative cross-links.

## Contents

| Directory | Concepts | Covers |
| :--- | ---: | :--- |
| `essentials/` | 3 | Search Essentials, technical requirements, spam policies |
| `fundamentals/` | 9 | SEO starter guide, how Search works, helpful content, AI optimization |
| `crawling-indexing/` | 24 | Sitemaps, robots.txt, Googlebot, canonicalization, AMP, JavaScript SEO, redirects |
| `appearance/` | 31 | Search appearance, ranking systems, page experience, rich results |
| `appearance/structured-data/` | 40 | Every structured data type reference (Article, Product, Recipe, Event, …) |
| `monitor-debug/` | 7 | Search Console, traffic-drop debugging, search operators |
| `monitor-debug/security/` | 4 | Malware, social engineering, Safe Browsing |
| `specialty/` | 15 | Ecommerce, international sites, explicit-content guidelines |

Start at [`index.md`](index.md) for progressive disclosure, or open `viz.html`
in a browser for an interactive graph of all 157 concepts and 791 cross-links.

## Concept structure

Each concept is UTF-8 markdown with YAML frontmatter conforming to OKF v0.2:

```yaml
---
type: Reference
title: Introduction to robots.txt
description: Robots.txt is used to manage crawler traffic. …
resource: https://developers.google.com/search/docs/crawling-indexing/robots/intro
tags: [google-search, documentation, crawling-indexing]
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:30:00Z'
sources:
  - id: google-intro
    resource: https://developers.google.com/search/docs/crawling-indexing/robots/intro
    title: Introduction to robots.txt
    author: Google Search Central (Google LLC)
    last_modified: '2025-12-10T00:00:00Z'
---
```

Every concept records the upstream URL as its `resource`, carries the page's
own Google-reported last-updated date as `sources[].last_modified`, and closes
with a Wikipedia-style bibliographic footnote.

## Working with the bundle

Using the [`okf` CLI](https://github.com/mjmiller41/cli-agent-okf):

```bash
okf validate --bundle . --strict   # lint frontmatter, footnotes, and link targets
okf index --bundle .               # regenerate every index.md
okf viz --bundle .                 # rebuild the interactive graph
```

## Attribution and licensing

All documentation content in this bundle is **authored by Google LLC** and
mirrored from Google Search Central. It is reproduced here under the
[Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
that Google applies to developers.google.com content; code samples within the
documentation are licensed under the
[Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). See
Google's [Site Policies](https://developers.google.com/site-policies).

Google Search Central is a Google product; this mirror is unofficial and is not
affiliated with or endorsed by Google. **The canonical, authoritative, and
current source is always <https://developers.google.com/search/docs>** — pages
here reflect their state as retrieved on 2026-09-01 and will drift as Google
updates the originals.

The OKF structuring, frontmatter, indices, and graph in this repository are
provided under the same CC BY 4.0 terms.
