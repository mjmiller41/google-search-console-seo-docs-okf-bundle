---
type: Reference
title: Define a favicon to show in search results
description: If your website has a favicon, it can be included in your Google Search results. Follow these favicon SEO instructions to make your site eligible.
resource: https://developers.google.com/search/docs/appearance/favicon-in-search
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-favicon-in-search
  resource: https://developers.google.com/search/docs/appearance/favicon-in-search
  title: Define a favicon to show in search results
  author: Google Search Central (Google LLC)
  last_modified: '2026-08-28T00:00:00Z'
---

# Define a favicon to show in search results

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/favicon-in-search](https://developers.google.com/search/docs/appearance/favicon-in-search). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-08-28.[^google-favicon-in-search]

If your site has a [favicon](https://www.google.com/search?q=what+is+a+favicon), it can be included in Google Search results for your site.

> This documentation is for organic search results. For logos on Google Ads results, visit the [business logo specifications](https://support.google.com/adspolicy/answer/12499303#business_logo).

## Implementation

Here's how to make your site eligible for a favicon in Google Search results:

1.  Create a favicon that follows the [guidelines](https://developers.google.com/search/docs/appearance/favicon-in-search/#guidelines).

2.  Add a `<link>` tag to the header of your [home page](https://developers.google.com/search/docs/appearance/favicon-in-search/#guidelines) with the following syntax:

    ``` devsite-click-to-copy
    <link rel="icon" href="/path/to/favicon.ico">
    ```

    To extract the favicon information, Google relies on the following attributes of the `link` element:

    <table>
<tr>
<th colspan="2">Attributes</th>
</tr>
<tr>
<td>
<code>rel</code>
</td>
<td>
<p>
            Google supports the following <code>rel</code> attribute values for specifying a favicon; use
            whichever one fits your use case:
          </p>
<table>
<tr>
<td>
<code>icon</code>
</td>
<td>
<p>
                  The icon that represents your site, as defined in the <a href="https://html.spec.whatwg.org/#rel-icon">HTML standard</a>.
                </p>
<blockquote>For historical reasons, we also support <code>shortcut icon</code>,
                    which is an earlier, alternative version of <code>icon</code>.
                  </blockquote>
</td>
</tr>
<tr>
<td>
<code>apple-touch-icon</code>
</td>
<td>
<p>An iOS-friendly icon that represents your site, per <a href="https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html">Apple's developer documentation</a>.</p>
</td>
</tr>
<tr>
<td>
<code>apple-touch-icon-precomposed</code>
</td>
<td>
<p>An alternative icon for earlier versions of iOS, per <a href="https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html">Apple's developer documentation</a>.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>href</code>
</td>
<td>
<p>
            The URL of the favicon. The URL can be a relative path (<code>/smile.ico</code>) or
            absolute path (<code>https://example.com/smile.ico</code>). The URL doesn't need to be
            hosted on your site (for example, your favicon could be hosted on a content delivery
            network (CDN)).
          </p>
</td>
</tr>
</table>

3.  Allow time for Google to recrawl and process the new information on your home page. Remember that crawling can take anywhere from several days to several weeks, depending on how often our systems determine content needs to be refreshed. You can [request indexing](/crawling-indexing/ask-google-to-recrawl.md) of your site's home page by using the URL Inspection tool.

## Guidelines

You must follow these guidelines to be eligible for a favicon in Google Search results.

> A favicon isn't guaranteed to appear in Google Search results, even if all guidelines are met.

- Google Search only supports one favicon per site, where a *site* is defined by the hostname. For example, `https://www.example.com/` and `https://code.example.com/` are two different hostnames, and therefore can have two different favicons. However, `https://www.example.com/sub-site` is a subdirectory of a site, and you can only set one favicon for `https://www.example.com/`, which applies to the site and its subdirectories.  
  **Supported**: `https://example.com` (this is a domain-level home page)  
  **Supported**: `https://news.example.com` (this is a subdomain-level home page)  
  **Not supported**: `https://example.com/news` (this is a subdirectory-level home page)
- Googlebot-Image must be able to crawl the favicon file and Googlebot must be able to crawl the home page; they cannot be [blocked](/crawling-indexing/control-what-you-share.md) for crawling.
- To help people quickly identify your site when they scan through search results, make sure your favicon is visually representative of your website's brand.
- Your favicon must be a square (1:1 aspect ratio) that's at least 8x8px. While the minimum size requirement is 8x8px, we recommend using a favicon that's larger than 48x48px so that it looks good on various surfaces. Google Search supports the following favicon file formats: BMP, GIF, ICO, PNG, JPEG, PPM, and TIFF.
- The favicon URL must be stable (don't change the URL frequently).
- Google won't show any favicon that it deems inappropriate, including pornography or hate symbols (for example, swastikas). If this type of imagery is discovered within a favicon, Google replaces it with a default icon.

## Submit feedback about favicons in search results

If you have feedback about Google's handling of favicons in search results, [fill out our favicon feedback form](https://forms.gle/KVBeuGWTg1yTwy7p9). Note that feedback submitted here is designed to help our teams to improve the systems in Google Search overall and doesn't guarantee it will be acted upon individually.

# References & Citations

[^google-favicon-in-search]: Google Search Central (2026). "Define a favicon to show in search results". *Google for Developers*. https://developers.google.com/search/docs/appearance/favicon-in-search. Retrieved 2026-09-01.
