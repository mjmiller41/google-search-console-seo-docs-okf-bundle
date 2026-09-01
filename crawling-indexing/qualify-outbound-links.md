---
type: Reference
title: Qualify your outbound links to Google
description: You might want to tell Google your relationship with outbound links on your site. Discover how to qualify outbound links with rel attribute values.
resource: https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-qualify-outbound-links
  resource: https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links
  title: Qualify your outbound links to Google
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Qualify your outbound links to Google

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-qualify-outbound-links]

For certain links on your site, you might want to tell Google your relationship with the linked page. In order to do that, use one of the following `rel` attribute values in the `<a>` tag.

For regular links that you expect Google to fetch and parse without any qualifications, you don't need to add a `rel` attribute. For example:

``` devsite-click-to-copy
<p>My favorite horse is the <a href="https://horses.example.com/Palomino">palomino</a>.</p>
```

For other links, use one or more of the following values:

<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th colspan="2"><code>rel</code> values</th>
</tr>
</thead>
<tbody>
<tr>
<td><h3><code>rel="sponsored"</code></h3></td>
<td>
<p>Mark links that are advertisements or paid placements (commonly called <i>paid
              links</i>) with the <code>sponsored</code> value. Read more about <a href="/essentials/spam-policies.md">Google's stance on paid links</a>.</p>
<pre class="devsite-click-to-copy">&lt;a <b>rel="sponsored"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt;</pre>
<blockquote><b>Note:</b> The <code>nofollow</code> attribute was
              <a href="https://developers.google.com/search/blog/2019/09/evolving-nofollow-new-ways-to-identify">previously recommended</a>
              for these types of links and is still an acceptable way to flag
              them, though <code>sponsored</code> is preferred. </blockquote>
</td>
</tr>
<tr>
<td><h3><code>rel="ugc"</code></h3></td>
<td>
<p>We recommend marking user-generated content (UGC) links, such as comments and forum
              posts, with the <code>ugc</code> value.</p>
<pre class="devsite-click-to-copy">&lt;a <b>rel="ugc"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt;</pre>
<p>If you want to recognize and reward trustworthy contributors, you might remove this
              attribute from links posted by members or users who have consistently made
              high-quality contributions over time. Read more about how to
              <a href="/monitor-debug/prevent-abuse.md">prevent user-generated spam on your site and platform</a>.</p>
</td>
</tr>
<tr>
<td><h3><code>rel="nofollow"</code></h3></td>
<td>
<p>Use the <code>nofollow</code> value when other values don't apply, and you'd rather
              Google not associate your site with, or crawl the linked page from, your site. For
              links within your own site, use the
      <a href="https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt#disallow">robots.txt <code>disallow</code> rule</a>.</p>
<pre class="devsite-click-to-copy">&lt;a <b>rel="nofollow"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt;</pre>
</td>
</tr>
<tr>
<td><h3><i>Multiple values</i></h3></td>
<td>
<p>You may specify multiple <code>rel</code> values as a space- or comma-separated
              list. <b>Examples:</b></p>
<pre class="devsite-click-to-copy">&lt;p&gt;I love &lt;a <b>rel="ugc nofollow"</b> href="https://cheese.example.com/Appenzeller_cheese"&gt;Appenzeller&lt;/a&gt; cheese.&lt;/p&gt;</pre>
<pre class="devsite-click-to-copy">&lt;p&gt;I hate &lt;a <b>rel="ugc,nofollow"</b> href="https://cheese.example.com/blue_cheese"&gt;Blue&lt;/a&gt; cheese.&lt;/p&gt;</pre>
</td>
</tr>
</tbody>
</table>

Links marked with these `rel` attributes will generally not be followed. Remember that the linked pages may be found through other means, such as sitemaps or links from other sites, and thus they may still be crawled. These `rel` attributes are used only in [`<a>` elements that Google can crawl](/crawling-indexing/links-crawlable.md), except `nofollow`, which is also available as [robots `meta` tag](/crawling-indexing/special-tags.md).

If you need to prevent Google from fetching a link to a page on your own site, use the [robots.txt `disallow` rule](https://developers.google.com/search/docs/crawling-indexing/robots/robots_txt#disallow).

To prevent Google from indexing a page, allow crawling and use the [`noindex` robots rule](/crawling-indexing/block-indexing.md).

# References & Citations

[^google-qualify-outbound-links]: Google Search Central (2025). "Qualify your outbound links to Google". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links. Retrieved 2026-09-01.
