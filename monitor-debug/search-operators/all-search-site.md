---
type: Reference
title: site:search operator
description: 'Learn all about the site: search operator and how it can help with debugging and understanding how Google sees your website.'
resource: https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site
tags:
- google-search
- documentation
- monitor-debug
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-all-search-site
  resource: https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site
  title: site:search operator
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# site:search operator

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site](https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-all-search-site]

A `site:` query is a search operator that allows you to request search results from the particular domain, URL, or URL prefix specified in the operator. For example:

<table>
<thead>
<tr>
<th colspan="2"><code>site:</code> examples</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>site:example.com</code></td>
<td>Show results only from the <code>example.com</code> domain (<code>www.example.com</code> and <code>recipes.example.com</code>).</td>
</tr>
<tr>
<td><code>site:https://www.example.com/ramen</code> tsukemen</td>
<td>Shows results for pages that contain URLs that start with <code>https://www.example.com/ramen</code> and are relevant to the term tsukemen.</td>
</tr>
</tbody>
</table>

The `site:` search operator is available on all Google Search properties.

> If a URL is indexed in Google, it can show up in search results for `site:` queries that are related to the URL, however it's not guaranteed. If a URL doesn't show in a `site:` query, use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to make sure the URL can be indexed and to submit the URL to indexing. Also, double-check the query is correct; `site:https://www.example.com` doesn't return the same results as `site:https://example.com/`.

## Uses for site owners

A `site:` query can help in a few ways with debugging a site. A few examples:

<table>
<thead>
<tr>
<th colspan="2"><code>site:</code> examples</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>site:example.com</code></td>
<td><p>Returns a list of indexed and serving URLs.</p>
<blockquote>
              The list of URLs returned is not always exhaustive. Bigger sites shouldn't expect to
              see all their URLs in the results. A more specific prefix in the query may yield more
              results than broader prefixes.
            </blockquote>
</td>
</tr>
<tr>
<td><code>site:https://example.com/recipes/tsukemen.html</code></td>
<td>May help you understand whether a specific URL is indexed and served.</td>
</tr>
<tr>
<td><code>site:example.com viagra casino</code></td>
<td>Helps with identifying and monitoring spam problems on your site.</td>
</tr>
<tr>
<td><code>site:https://example.com/</code> lemon</td>
<td>Shows which URLs on the site can show up for the term "lemon".</td>
</tr>
<tr>
<td><code>site:https://example.com/recipes/tsukemen.html</code> lemon</td>
<td>Shows whether the specific URL is indexed for the term "lemon".</td>
</tr>
</tbody>
</table>

## Limitations

The `site:` operator was designed primarily for search users and so it has some restrictions that site owners might find limiting. Specifically:

- The `site:` operator doesn't necessarily return all the URLs that are indexed under the prefix specified in the query. Keep this in mind if you want to use the `site:` operator for tasks like identifying how many URLs are indexed and serving under a prefix.
- A `site:` operator without a query (for example `site:example.com`) doesn't rank the results. It will generally show the shortest URL for the prefix at the top, but otherwise the results are relatively random.

# References & Citations

[^google-all-search-site]: Google Search Central (2025). "site:search operator". *Google for Developers*. https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site. Retrieved 2026-09-01.
