---
type: Skill Reference
title: Target resolution and sampling
description: How audit skills decide whether they are auditing a live site or a codebase, which pages to sample, and what cannot be tested without a server.
tags: [skills, targets, sampling]
status: stable
---

# Target resolution and sampling

## Modes

| Input | Mode | What it means |
| :--- | :--- | :--- |
| `https://example.com`, or a bare domain | **live** | Fetch the real site. Every check is available. |
| A filesystem path | **static** | Analyze build output or source. Server behavior cannot be observed. |
| Both | **mixed** | Analyze the code, verify the deployed result. Label each finding with the mode that produced it. |

Ask which the user wants only when it is genuinely ambiguous. A path that
exists on disk is static; anything with a scheme or a dot-tld is live.

## Live mode

**Sampling.** Auditing every page of a real site is neither necessary nor
polite. Take:

1. the homepage, always;
2. the first 3 URLs from the sitemap;
3. up to 6 more chosen across *distinct* first path segments.

Cap at 10 pages unless the user asks for more. Template diversity matters more
than volume — ten pages spanning ten sections find far more than ten pages of
one blog. `site_probe.py` implements exactly this in its `sample` field.

**Politeness — these are requirements, not suggestions.**

- Sequential requests only. Never fetch in parallel.
- One second between requests (`--sleep`, the default).
- Each URL fetched at most once per audit. Cache results and share them across
  sub-skills; the router gathers signals once for all of them.
- 2 MB body cap.
- Identify honestly with the default user agent
  (`search-audit-skill/1.0`). Use a Googlebot user-agent string only for the
  cloaking comparison, and see the caveat on that check.
- `site_probe.py` fetches only robots.txt and sitemaps, never page bodies.

## Static mode

**Find the built output first.** Analyzing rendered HTML is far more accurate
than analyzing templates. Look, in order, for: `_site/`, `out/`, `dist/`,
`build/`, `public/`.

`.next/` is not plain HTML. Ask the user to run their production build and
point at the exported output; if that is not possible, fall back to
template-level analysis and say so in the report.

If there is no build output at all, analyze the source templates and pages, and
state clearly in the report that this is template-level analysis: what ships to
Google may differ.

**Framework detection.** Use it to know where the answers live, and to give
fixes in the user's own stack:

| Marker file | Framework | Where robots/sitemap/redirects/head live |
| :--- | :--- | :--- |
| `next.config.*` | Next.js | `app/robots.ts`, `app/sitemap.ts`, `redirects()` in config, Metadata API |
| `astro.config.*` | Astro | `public/robots.txt`, `@astrojs/sitemap`, `<head>` in layouts |
| `_config.yml` | Jekyll | `robots.txt` at source root, `jekyll-sitemap`, `_includes/head.html` |
| `hugo.toml`/`config.toml` + `content/` | Hugo | `static/robots.txt`, built-in sitemap, `layouts/partials/head.html` |
| `gatsby-config.*` | Gatsby | `static/`, `gatsby-plugin-sitemap`, `react-helmet`/Head API |
| `svelte.config.*` | SvelteKit | `static/`, `+layout.svelte` head, hooks for redirects |
| `nuxt.config.*` | Nuxt | `public/`, `@nuxtjs/sitemap`, `useHead` |
| `.eleventy.js` | 11ty | `public/`/passthrough copy, sitemap template, layout head |
| bare `index.html` | plain static | files as they are |

Deployment redirects also live in `vercel.json`, `netlify.toml`, `_redirects`,
or `.htaccess` — check these before reporting a redirect as missing.

**Mapping URLs to files** (for mixed mode): `/about/` is `about/index.html`,
`/about` may be `about.html`, and extensionless routes depend on the framework.

## What static mode cannot test

Put every one of these that applies in the report's **Checks not run** table,
with the reason. Never report them as passes or failures.

- HTTP status codes, including whether missing pages really return 404
- Server-side redirects not visible in a config file
- Response headers: `X-Robots-Tag`, HSTS, caching, content type
- TLS and certificate validity
- Core Web Vitals field data
- Whether robots.txt or the sitemap are generated at deploy time

A missing `robots.txt` or `sitemap.xml` in a build directory is reported as
*possibly generated at deploy — verify on the live site*, not as a failure.

## Disclosure

The report states what was sampled: mode, framework and analyzed directory in
static mode, and "N of M pages sampled" in live mode. A reader who cannot tell
how much of their site was examined cannot judge the result.
