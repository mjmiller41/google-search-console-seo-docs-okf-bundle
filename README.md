---
type: Bundle Guide
title: Google Search Central Documentation — OKF Bundle
description: How this bundle is structured, how each concept is shaped, and how to sync it with the upstream Google Search Central documentation.
resource: https://github.com/mjmiller41/google-search-console-seo-docs-okf-bundle
tags: [google-search, documentation, readme]
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T16:00:00Z'
---

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

## Keeping the bundle current

`sync_docs.py` re-crawls the upstream navigation and updates the bundle in
place. It rebuilds every page through the same pipeline that produced the
bundle, then writes only the concepts whose content actually changed — the
timestamps that move on every run (`generated.at`, the footnote's `Retrieved`
date) are excluded from the comparison, so an unchanged page is left untouched
and its original `generated.at` stands as the true date of last meaningful
change (OKF v0.2 §5.2).

```bash
pip install -r requirements.txt   # plus pandoc and the okf CLI

python3 sync_docs.py              # sync in place, then run the maintenance chain
python3 sync_docs.py --check      # report drift, write nothing (exit 2 if drift)
python3 sync_docs.py --force      # rewrite every concept
python3 sync_docs.py --only /search/docs/appearance/structured-data/recipe
```

| Flag | Effect |
| :--- | :--- |
| `--check` | Read-only drift report. Exits `2` when the bundle is behind, `0` when current — suitable as a CI gate. |
| `--force` | Rewrites every concept, regardless of whether content changed. |
| `--only PATH...` | Restricts the sync to specific upstream paths. Skips the deprecation scan. |
| `--jobs N` | Parallel fetches (default `4`). |
| `--record-verification` | Stamps unchanged concepts with a `process:google-docs-sync` `verified` event, raising them to the machine-confirmed trust tier (§5.3). |
| `--no-maintenance` | Skips the `validate`/`index`/`log`/`viz` chain. |
| `--bundle DIR` | Bundle root (defaults to the script's own directory). |

What the sync does with each kind of change:

* **Changed page** — the concept is rewritten with a fresh `generated.at`, and
  the upstream `Last updated` date is carried into `sources[].last_modified`.
* **New page in the navigation** — a new concept is created at the matching path.
* **Page dropped from the navigation** — the concept is marked
  `status: deprecated` with a `deprecated_at` timestamp and kept, per OKF v0.2
  §5.4, so inbound links and history survive.

Afterwards it runs `okf validate --strict`, `okf index`, `okf log`, and
`okf viz`. Set `OKF_CLI` if the CLI is not on `PATH`
(e.g. `OKF_CLI="python3 -m okf_cli.cli"`).

A [scheduled workflow](.github/workflows/sync-docs.yml) runs the sync weekly and
commits any resulting changes.

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
