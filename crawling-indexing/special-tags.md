---
type: Reference
title: metatags and attributes that Google supports
description: Google supports both page-level meta tags and tag attributes. Explore a list of the special tags that Google Search can support.
resource: https://developers.google.com/search/docs/crawling-indexing/special-tags
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-special-tags
  resource: https://developers.google.com/search/docs/crawling-indexing/special-tags
  title: metatags and attributes that Google supports
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# metatags and attributes that Google supports

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/special-tags](https://developers.google.com/search/docs/crawling-indexing/special-tags). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-special-tags]

This page explains what `meta` tags are, which `meta` tags and HTML attributes Google supports to control indexing, and other important points to note when implementing `meta` tags on your site.

## `meta` tags

`meta` tags are HTML tags used to provide additional information about a page to search engines and other clients. Clients process the `meta` tags and ignore those they don't support. `meta` tags are added to the `<head>` section of your HTML page and generally look like this:

``` devsite-click-to-copy
<!DOCTYPE html>
  <html>
  <head>
    <meta charset="utf-8">
    <meta name="description" content="Author: A.N. Author, Illustrator: P. Picture, Category: Books, Price:  £9.24, Length: 784 pages">
    <meta name="google-site-verification" content="+nxGUDJ4QpAZ5l9Bsjdi102tLVC21AIh5d1Nl23908vVuFHs34=">
    <title>Example Books - high-quality used books for children</title>
    <meta name="robots" content="noindex,nofollow">
  </head>
</html>
```

> **If you use a CMS, such as Wix, WordPress, or Blogger**, you might not be able to edit your HTML directly, or you might prefer not to. Instead, your CMS might have a search engine settings page or some other mechanism to tell search engines about `meta` tags.
>
> If you want to add a `meta` tag to your website, search for instructions about modifying the `<head>` of your page on your CMS (for example, search for "wix add meta tags").

Google supports the following `meta` tags:

<table>
<thead>
<tr><th colspan="2">List of <code>meta</code> tags that Google supports</th></tr>
</thead>
<tbody>
<tr>
<td><h3>description</h3>
</td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="description" content="A description of the page"&gt;</pre>
        Use this tag to provide a short description of the page. In some situations, this
        description is used in the
        <a href="/appearance/snippet.md">snippet shown in search results</a>.</td>
</tr>
<tr>
<td><h3>robots and googlebot</h3></td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="robots" content="..., ..."&gt;</pre>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="googlebot" content="..., ..."&gt;</pre>
<p>
          These <code>meta</code> tags control the behavior of search engine crawling and
          indexing.
        </p>
<p>The <code>&lt;meta name="robots" ...</code> tag applies to all search engines, while
          the <code>&lt;meta name="googlebot ...</code> tag is specific to Google.</p>
<p>In the case of conflicting <code>robots</code> (or <code>googlebot</code>)
          <code>meta</code> tags, the more restrictive tag applies. For example, if a page has
          both the <code>max-snippet:50</code> and <code>nosnippet</code> tags, the
          <code>nosnippet</code> tag will apply.</p>
<p>The default values are <code>index, follow</code> and don't need to be specified.
          For a full list of values that Google supports, see the
          <a href="/crawling-indexing/robots-meta-tag.md">list of valid rules</a>.
        </p>
<p>You can also specify this information in the header of your pages using the
          <code>X-Robots-Tag</code> HTTP header rule. This is particularly useful if you wish to limit
          indexing of non-HTML files like graphics or other kinds of documents.
          <a href="/crawling-indexing/robots-meta-tag.md">More information about robots <code>meta</code> tags</a>.</p>
</td>
</tr>
<tr>
<td>
<h3>notranslate</h3>
</td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="googlebot" content="notranslate"&gt;</pre>
<p>
          When Google recognizes that the contents of a page aren't in the language that the
          user likely wants to read, Google may provide a <a href="/appearance/translated-results.md">translated title link and snippet</a> in search results.
          If the user clicks the translated title link, all further user interaction with the page
          is through Google Translate, which will automatically translate any links followed. In
          general, this gives you the chance to provide your unique and
          compelling content to a much larger group of users. However, there may be situations
          where this is not desired. This <code>meta</code> tag tells Google that you don't want
          us to provide a translation for this page.
        </p>
</td>
</tr>
<tr>
<td><h3>nopagereadaloud</h3></td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="google" content="nopagereadaloud"&gt;</pre>
<p>Prevents various <a href="https://developers.google.com/search/docs/crawling-indexing/read-aloud-user-agent">Google text-to-speech services</a>
           from reading aloud web pages using text-to-speech (TTS).</p>
</td>
</tr>
<tr>
<td><h3>google-site-verification</h3></td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="google-site-verification" content="..."&gt;</pre>
<p>
          You can use this tag on the top-level page of your site to <a href="https://support.google.com/webmasters/answer/9008080">verify ownership for Search Console</a>.
          Note that while the values of the <code>name</code> and
          <code>content</code> attributes must match exactly what is provided to you (including
          upper and lower case), it doesn't matter if you change the tag from XHTML to HTML or
          if the format of the tag matches the format of your page.
        </p>
</td>
</tr>
<tr>
<td>
<h3>Content-Type and charset</h3>
</td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta http-equiv="Content-Type" content="...; charset=..."&gt;</pre>
<pre class="devsite-click-to-copy wrap-code">&lt;meta charset="..."&gt;</pre>
<p>
          These tags define the page's content type and character set respectively. Make sure that you
          surround the value of the <code>content</code> attribute in the
          <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#attr-http-equiv"><code>http-equiv</code></a>
<code>meta</code> tag with quotes—otherwise the
          <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta#charset"><code>charset</code></a>
          attribute may be interpreted incorrectly. We recommend using Unicode/UTF-8 where possible.
        </p>
</td>
</tr>
<tr>
<td><h3>refresh</h3></td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta http-equiv="refresh" content="...;url=..."&gt;</pre>
<p>
          This tag, commonly called meta-refresh, sends the user to a new URL after a certain
          amount of time, and is sometimes used as a simple form of redirection. However, it is
          <a href="https://www.w3.org/TR/WCAG10-HTML-TECHS/#meta-element">not supported by all browsers and can be confusing to the user</a>.
          We recommend using a server-side
          <a href="/crawling-indexing/301-redirects.md"><code>301</code> redirect</a>
          instead.
        </p>
</td>
</tr>
<tr>
<td><h3>viewport</h3></td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="viewport" content="..."&gt;</pre>
<p>
          This tag tells the browser how to render a page on a mobile device. Presence of this tag
          indicates to Google that the page is mobile friendly.
          <a href="https://web.dev/articles/responsive-web-design-basics#size-content">Read more about how to configure the <code>viewport</code> <code>meta</code> tag.</a>
</p>
</td>
</tr>
<tr>
<td>
<h3>rating</h3>
</td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="rating" content="adult"&gt;</pre>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="rating" content="RTA-5042-1996-1400-1577-RTA"&gt;</pre>
<p>
          Labels a page as containing sexually-explicit adult content, to signal that it be filtered by SafeSearch
          results. <a href="https://developers.google.com/search/docs/crawling-indexing/safesearch">Learn more about labeling SafeSearch pages.</a>
</p>
</td>
</tr>
</tbody>
</table>

## HTML tag attributes

[HTML tag attributes](https://developer.mozilla.org/docs/Web/HTML/Attributes) are additional values of HTML tags that configure the parent tag. For example, the `href` attribute of the `<a>` tag configures the resource the anchor tag points to: `<a `**`href="https://example.com/"`**`...>`.

Google Search supports a limited number of HTML attributes for indexing purposes. Attributes like `src` and `href` are used for discovering resources such as images and URLs. Google also supports various [`rel` attributes](/crawling-indexing/qualify-outbound-links.md) that allow site owners to qualify outbound links.

The [`data-nosnippet` attribute](/crawling-indexing/robots-meta-tag.md) of `div`, `span`, and `section` tags allow you to exclude parts of an HTML page from snippets.

## Other points to note

- Google can read both HTML and XHTML-style `meta` tags, regardless of the code used on the page.
- To ensure machine readability, the `head` section must be [valid HTML](/crawling-indexing/valid-page-metadata.md) and in case of attributes, all parent tags closed accordingly.
- With the exception of `google-site-verification`, letter case is generally not important in `meta` tags.
- You can use other `meta` tags if they are important to your site, but Google will ignore `meta` tags that it doesn't support.
- If you're considering using JavaScript to inject or change `meta` tags, proceed with caution. We recommend that you avoid using JavaScript to inject or change `meta` tags whenever possible, and if you must use it, [test your implementations](/crawling-indexing/javascript/fix-search-javascript.md) thoroughly.
- To check the `meta` tags and attributes on your pages, use the [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289).

## Unsupported tags and attributes

The following tags and attributes aren't supported by Google Search and are ignored. We're including them here because they're either very common in HTML or we used to support them.

<table>
<tbody>
<tr>
<th colspan="2">Unsupported tags and attributes</th>
</tr>
<tr>
<td>meta-keyword tag</td>
<td>
<code>&lt;meta name="keywords" content="..."&gt;</code>
        The meta-keyword tag is not used by Google Search, and it has no effect on indexing and
        ranking at all.</td>
</tr>
<tr>
<td>HTML tag <code>lang</code> attributes</td>
<td>Google Search detects the language of a page
      based on the textual content of the page. It doesn't rely on code annotations such as the
      <code>lang</code>.</td>
</tr>
<tr>
<td>
<code>next</code> and <code>prev</code> <code>rel</code> attribute values
      </td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;link rel="next" href="..."&gt;</pre>
<pre class="devsite-click-to-copy wrap-code">&lt;link rel="prev" href="..."&gt;</pre>
<p>
          Google no longer uses these HTML <code>&lt;link&gt;</code> tags, and they have no effect on
          indexing.
        </p>
</td>
</tr>
<tr>
<td>
<h3>nositelinkssearchbox</h3>
</td>
<td>
<pre class="devsite-click-to-copy wrap-code">&lt;meta name="google" content="nositelinkssearchbox"&gt;</pre>
<p>
          The <code>nositelinkssearchbox</code> rule is no longer used by Google Search to control
          whether the sitelink search box is shown for a given page, as the feature no longer exists.
        </p>
</td>
</tr>
</tbody>
</table>

# References & Citations

[^google-special-tags]: Google Search Central (2025). "metatags and attributes that Google supports". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/special-tags. Retrieved 2026-09-01.
