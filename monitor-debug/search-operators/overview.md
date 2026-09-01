---
type: Reference
title: Overview of Google search operators
description: Learn about the different Google Search operators that we support and discover how they can help you monitor and debug your website.
resource: https://developers.google.com/search/docs/monitor-debug/search-operators
tags:
- google-search
- documentation
- monitor-debug
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-search-operators
  resource: https://developers.google.com/search/docs/monitor-debug/search-operators
  title: Overview of Google search operators
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Overview of Google search operators

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/monitor-debug/search-operators](https://developers.google.com/search/docs/monitor-debug/search-operators). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-search-operators]

Google Search supports [several search operators](https://support.google.com/websearch/answer/2466433) that you can use to refine or target your searches. The following search operators may also be useful for debugging your website.

For example, the `site:` search operator may be useful to monitor comment spam on your website, and the image search `imagesize:` operator may be helpful to find images on your site that are small.

> Because search operators are bound by indexing and retrieval limits, the [URL Inspection](https://support.google.com/webmasters/answer/9012289) tool in Search Console is more reliable for debugging purposes.

The following table contains the search operators that you can use to inspect different aspects of your pages in Search:

<table>
<thead>
<tr>
<th colspan="2">Search operators</th>
</tr>
</thead>
<tbody>
<tr>
<td><h2><code>filetype:</code></h2></td>
<td>
<p>
            Find search results in a
            <a href="/crawling-indexing/indexable-file-types.md">specific file type</a>
            as defined by the <code>content-type</code> HTTP header, or file extension.
            For example, you can search for RTF files and URLs ending in <code>.rtf</code> whose
            content contains the term "galway":
          </p>
<pre>filetype:rtf galway</pre>
</td>
</tr>
<tr>
<td><h2><a href="/monitor-debug/search-operators/image-search.md"><code>imagesize:</code></a></h2></td>
<td>
<p>
            Find pages that contain images of a specific dimension. This search operator only works on Google Images. For example:
          </p>
<pre>imagesize:1200x800</pre>
</td>
</tr>
<tr>
<td><h2><a href="/monitor-debug/search-operators/all-search-site.md"><code>site:</code></a></h2></td>
<td>
<p>
            Find search results from a particular domain, URL, or URL prefix. For example:
          </p>
<pre>site:https://www.google.com/</pre>
</td>
</tr>
<tr>
<td><h2><a href="/monitor-debug/search-operators/image-search.md"><code>src:</code></a></h2></td>
<td>
<p>Find pages that reference a particular image URL in the <code>src</code> attribute. This search operator only works on Google Images. For example:</p>
<pre>src:https://www.example.com/images/peanut-butter.png</pre>
</td>
</tr>
</tbody>
</table>

# References & Citations

[^google-search-operators]: Google Search Central (2025). "Overview of Google search operators". *Google for Developers*. https://developers.google.com/search/docs/monitor-debug/search-operators. Retrieved 2026-09-01.
