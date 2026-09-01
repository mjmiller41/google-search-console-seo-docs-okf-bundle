---
type: Reference
title: Control what you share with Google
description: You can control what content Google sees on your site and what is shown in search results. Discover the main ways to remove site content from Google.
resource: https://developers.google.com/search/docs/crawling-indexing/control-what-you-share
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-control-what-you-share
  resource: https://developers.google.com/search/docs/crawling-indexing/control-what-you-share
  title: Control what you share with Google
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Control what you share with Google

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/control-what-you-share](https://developers.google.com/search/docs/crawling-indexing/control-what-you-share). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-control-what-you-share]

Google supports a variety of ways that allows site owners control what shows up in Google's search results. While most people focus on getting their pages indexed, sometimes it's important to do the opposite: prevent content from appearing in Search. There are a few reasons you might want to hide content from Google:

- **To restrict data**: You might have data hosted on your site that you want to show only to users who are already on your site. You can block Google from crawling such data so it doesn't show up in search results.  
  Also keep in mind that certain files published on your site may have metadata that can show up in Search. [Learn more about keeping redacted information out of Search](/crawling-indexing/keep-redacted-information-out.md).
- **To hide content of less value to your audience**: Your website might have low quality content that shouldn't show up in Search. For example, if your website allows users to create content, some of that content might be [low quality or even spam](/essentials/spam-policies.md). Allowing indexing of such content may have a negative effect on your site's ranking in Google's search results.
- **To have Google focus on your important content**: If you have a very large site (over hundreds of thousands of URLs) and pages with less important content, or if you have a lot of duplicate content, you might want to prevent Google from crawling the duplicate or less important pages in order to focus on your more important content.

## How to block content

Here are the main ways to block content from appearing in Google:

<table>
<tr><th colspan="2">Methods</th></tr>
<tr>
<td>
<h3>Remove the content from your site</h3>
</td>
<td>
<p>
<b>Applicable: all content types</b>
</p>
<p>
        Removing content from your site is the best way to ensure that it won't appear in
        Google Search and anywhere else on the Internet.
      </p>
</td>
</tr>
<tr>
<td>
<h3>Password-protect your files</h3>
</td>
<td>
<p>
<b>Applicable: all content types</b>
</p>
<p>
        If you have confidential or private content on your site, you need to password protect
        it to ensure only authorized users can access it. This will also prevent that content
        from appearing in Google Search, or if it already appears, it will eventually remove
        that content from our search results.
      </p>
</td>
</tr>
<tr>
<td><a href="/crawling-indexing/block-indexing.md"><code>noindex</code> rule</a></td>
<td>
<p>
<b>Applicable: all content types</b>
</p>
<p>
        The <code>noindex</code> robots <code>meta</code> tag is a
        rule that tells Google not to index your content or let it appear in Google search
        results. Your content can still be linked to and visited through other web pages, or
        directly visited by users with a link, but the content will not appear in Google search
        results.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Disallow crawling with
        <a href="/crawling-indexing/prevent-images-on-your-page.md">robots.txt</a>
</h3>
</td>
<td>
<p>
<b>Applicable: images and video</b>
</p>
<p>
        Google only indexes images and videos that Googlebot is allowed to crawl. To prevent
        Googlebot from accessing your media files, use
        <a href="/crawling-indexing/prevent-images-on-your-page.md">robots.txt rules to block the files</a>.
      </p>
</td>
</tr>
<tr>
<td>
<a href="https://support.google.com/webmasters/answer/3035947">Opt out of specific Google properties</a>
</td>
<td>
<p>
<b>Applicable: web pages</b>
</p>
<p>
        You can tell Google not to include content from your site in specific Google properties,
        such as
        <a href="https://www.google.com/shopping">Google Shopping</a>,
        <a href="https://www.google.com/travel/hotels">Google Hotels</a>, and vacation rentals.
      </p>
</td>
</tr>
</table>

## Remove existing content from Google

If the content hosted on your site is already appearing in Google, you can request the removal of those search results. Learn how to [remove a page hosted on your site from Google](/crawling-indexing/remove-information.md).

# References & Citations

[^google-control-what-you-share]: Google Search Central (2025). "Control what you share with Google". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/control-what-you-share. Retrieved 2026-09-01.
