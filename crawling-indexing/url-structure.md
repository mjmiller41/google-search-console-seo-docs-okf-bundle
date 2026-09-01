---
type: Reference
title: URL structure best practices for Google Search
description: It's a good idea to keep your site's URL structure as simple as possible. Learn more about the URL format recommended by Google, such as the use of hyphens, underscores, and domain structure.
resource: https://developers.google.com/search/docs/crawling-indexing/url-structure
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-url-structure
  resource: https://developers.google.com/search/docs/crawling-indexing/url-structure
  title: URL structure best practices for Google Search
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# URL structure best practices for Google Search

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/url-structure](https://developers.google.com/search/docs/crawling-indexing/url-structure). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-url-structure]

To make sure Google Search can crawl your site effectively, use a crawlable URL structure that meets the following requirements. If your URLs don't meet the following criteria, Google Search will likely crawl your site inefficiently — including but not limited to extremely high crawl rates, or not at all.

<table>
<thead>
<colgroup><col/></colgroup>
<tr><th colspan="2"><h2>Requirements for a crawlable URL structure</h2></th></tr>
</thead>
<tbody>
<tr>
<td><h3>Follow <a href="https://datatracker.ietf.org/doc/std66/">IETF STD 66</a></h3>
</td>
<td>
<p>Google Search supports URLs as defined by
          <a href="https://datatracker.ietf.org/doc/std66/">IETF STD 66</a>. Characters defined by
          the standard as <a href="https://www.rfc-editor.org/rfc/rfc3986#section-2.2">reserved</a>
          must be <a href="https://developer.mozilla.org/docs/Glossary/Percent-encoding">percent encoded</a>.
        </p>
</td>
</tr>
<tr>
<td><h3>Don't use URL fragments to change content</h3>
</td>
<td>
<p>
          Don't use <a href="https://wikipedia.org/wiki/URI_fragment">fragments</a> to change the
          content of a page, as Google Search generally doesn't support URL fragments. Here's an
          example of a URL fragment:
        </p>
<pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/#/potatoes</pre>
<p>
          If you're using JavaScript to change content, <a href="/crawling-indexing/javascript/javascript-seo-basics.md">use the History API</a>
          instead.
        </p>
</td>
</tr>
<tr>
<td><h3>Use a common encoding for URL parameters</h3>
</td>
<td>
<p>When specifying URL parameters, use the following common encoding: an equal sign
          (<code>=</code>) to separate key-value pairs and add additional parameters with an
          ampersand (<code>&amp;</code>). To list multiple values for the same key within a key-value
          pair, you can use any character that doesn't conflict with
          <a href="https://datatracker.ietf.org/doc/std66/">IETF STD 66</a>, such as a comma
          (<code>,</code>).
        </p>
<table>
<tr>
<th>
Recommended
            </th>
<th>
Not recommended
            </th>
</tr>
<tr>
<td>
              Using an equal sign (<code>=</code>) to separate key-value pairs and an ampersand
              (<code>&amp;</code>) to add additional parameters:
            <pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/category?category=dresses&amp;sort=low-to-high&amp;sid=789</pre>
</td>
<td>
              Using a colon (<code>:</code>) to separate key-value pairs and brackets (<code>[ ]</code>)
              to add additional parameters:
              <pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/category?[category:dresses][sort:price-low-to-high][sid:789]</pre>
</td>
</tr>
<tr>
<td>
              Using a comma (<code>,</code>) to list multiple values for the same key, an equal sign
              (<code>=</code>) to separate key-value pairs, and an ampersand (<code>&amp;</code>) to add
              additional parameters:
              <pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/category?category=dresses&amp;color=purple,pink,salmon&amp;sort=low-to-high&amp;sid=789</pre>
</td>
<td>
              Using a single comma (<code>,</code>) to separate key-value pairs and double
              commas (<code>,,</code>) to add additional parameters:
              <pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/category?category,dresses,,sort,lowtohigh,,sid,789</pre>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>

## Make it easy to understand your URL structure

To help Google Search (and your users) better understand your site, we recommend creating a simple URL structure, applying the following best practices when possible.

> Consider organizing your content so that URLs are constructed logically and in a manner that is most intelligible to humans. For information on structuring your site as a whole, check out [this section of the SEO Starter Guide](/fundamentals/seo-starter-guide.md).

<table>
<thead>
<colgroup><col/></colgroup>
<tr><th colspan="2">Best practices</th></tr>
</thead>
<tbody>
<tr>
<td><h3>Use descriptive URLs</h3></td>
<td>
<p>When possible, use readable words rather than long ID numbers in your URLs.</p>
<table>
<tr>
<th>
Recommended (simple, descriptive words)
            </th>
<th>
Not recommended (unreadable, long ID numbers)
            </th>
</tr>
<tr>
<td>
<pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>wiki/Aviation</strong></pre>
</td>
<td>
<pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>index.php?topic=42&amp;area=3a5ebc944f41daa6f849f730f1</strong></pre>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td><h3>Use your audience's language</h3></td>
<td>
<p>Use words in your audience's language in the URL (and, if applicable, transliterated words).
          For example, if your audience is searching in German, use German words in the URL:
        </p>
<pre>https://example.com/<strong>lebensmittel/pfefferminz</strong></pre>
<p>
          Or if your audience is searching in Japanese, use Japanese words in the URL:
        </p>
<pre>https://example.com/<strong>ペパーミント</strong></pre>
</td>
</tr>
<tr>
<td><h3>Use percent encoding as necessary</h3></td>
<td>
<p>When <a href="/crawling-indexing/links-crawlable.md">linking to pages on your site</a>,
          use percent encoding in your links's <code>href</code> attributes as necessary. Unreserved
          ASCII characters may be left in the non-encoded form. Additionally, characters in the
          non-ASCII range should be percent encoded. For example:
        </p>
<table>
<tr>
<th>Recommended (percent encoding)</th>
<th>Not recommended (non-ASCII characters)</th>
</tr>
<tr>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>%D9%86%D8%B9%D9%86%D8%A7%D8%B9/%D8%A8%D9%82%D8%A7%D9%84%D8%A9</strong></pre>
</td>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>نعناع</strong></pre>
</td>
</tr>
<tr>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>%E6%9D%82%E8%B4%A7/%E8%96%84%E8%8D%B7</strong></pre>
</td>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>杂货/薄荷</strong></pre>
</td>
</tr>
<tr>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>gem%C3%BCse</strong></pre>
</td>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>gemüse</strong></pre>
</td>
</tr>
<tr>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>%F0%9F%A6%99%E2%9C%A8</strong></pre>
</td>
<td><pre class="devsite-disable-code-toggle wrap-code">https://example.com/<strong>🦙✨</strong></pre>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td><h3>Use hyphens to separate words</h3>
</td>
<td>
<p>We recommend separating words in your URLs, when possible. Specifically, we recommend using
        hyphens (<code>-</code>) instead of underscores (<code>_</code>) to
        separate words in your URLs, as it helps users and search engines better identify
        concepts in the URL. For historical reasons, we don't recommend using underscores, as
        this style is already commonly used for denoting concepts that should be kept together,
        for example, by various programming languages to name functions (such as <code>format_date</code>).
      </p>
<table>
<tr>
<th>
Recommended
          </th>
<th>
Not recommended
          </th>
</tr>
<tr>
<td>
<p>Using hyphens (<code>-</code>) to separate words:</p>
<pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/summer<strong>-</strong>clothing/filter?color<strong>-</strong>profile=dark<strong>-</strong>grey</pre>
</td>
<td>
<p>Using underscores (<code>_</code>) to separate words:</p>
<pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/summer<strong>_</strong>clothing/filter?color<strong>_</strong>profile=dark<strong>_</strong>grey</pre>
<p>Joining words together in the URL:</p>
<pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/<strong>greendress</strong></pre>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td><h3>Use as few parameters as you can</h3></td>
<td>Whenever possible, shorten URLs by trimming unnecessary parameters (meaning, parameters
      that don't change the content).
    </td>
</tr>
<tr>
<td><h3>Be aware that URLs are case sensitive</h3></td>
<td>Like any other HTTP client following IETF STD 66, Google Search's URL handling is case
      sensitive (for example, Google treats both <code>/APPLE</code> and <code>/apple</code> as
      distinct URLs with their own content). If upper and lower case text in a URL is treated
      the same by your web server, convert all text to the same case so it's easier for Google
      to determine that URLs reference the same page.
    </td>
</tr>
<tr>
<td><h3>For multi-regional sites</h3></td>
<td>
<p>If your site is multi-regional, consider using a URL structure that makes it easy to
        geotarget your site. For more examples of how you can structure your URLs, refer to
        <a href="/specialty/international/managing-multi-regional-sites.md">using locale-specific URLs</a>.
      </p>
<p>
Recommended (using a country-specific domain):
      </p>
<pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.de</pre>
<p>
Recommended (using a country-specific subdirectory with gTLD):
      </p>
<pre class="wrap-code devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/de/</pre>
</td>
</tr>
</tbody>
</table>

## Avoid common issues related to URLs

Overly complex URLs, especially those containing multiple parameters, can cause problems for crawlers by creating unnecessarily high numbers of URLs that point to identical or similar content on your site. As a result, Googlebot may consume much more bandwidth than necessary, or Google Search may be unable to completely index all the content on your site.

Unnecessarily high numbers of URLs can be caused by a number of issues. These include:

<table>
<thead>
<colgroup><col/></colgroup>
<tr><th colspan="2">Common issues</th></tr>
</thead>
<tbody>
<tr>
<td><h3>Additive filtering of a set of items</h3>
</td>
<td>
<p>Many sites provide different views of the same set of items or search results, often
       allowing the user to filter this set using defined criteria (for example: show me hotels on
       the beach). When filters can be combined in an additive manner (for example: hotels on the
       beach and with a fitness center), the number of URLs (views of data) in the sites explodes.
       Creating a large number of slightly different lists of hotels is redundant, as Googlebot
       only needs to see a small number of lists from which it can reach the page for each hotel.
       For example:
     </p>
<ul>
<li>Hotel properties at "value rates":
          <pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/hotel-search-results.jsp?Ne=292&amp;N=461</pre></li>
<li>Hotel properties at "value rates" on the beach:
          <pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/hotel-search-results.jsp?Ne=292&amp;N=461+4294967240</pre></li>
<li>Hotel properties at "value rates" on the beach and with a fitness center:
          <pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/hotel-search-results.jsp?Ne=292&amp;N=461+4294967240+4294967270</pre>
</li>
</ul>
</td>
</tr>
<tr>
<td><h3>Irrelevant parameters</h3>
</td>
<td>
<p>Irrelevant parameters in the URL can cause a large number of URLs, such as:</p>
<ul>
<li>Referral parameters:
          <pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/search/noheaders?click=6EE2BF1AF6A3D705D5561B7C3564D9C2&amp;clickPage=OPD+Product+Page&amp;cat=79</pre>
<pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/discuss/showthread.php?referrerid=249406&amp;threadid=535913</pre>
<pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/products/products.asp?N=200063&amp;Ne=500955&amp;ref=foo%2Cbar&amp;Cn=Accessories</pre>
</li>
<li>Shopping sorting parameters:
          <pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/results?search_type=search_videos&amp;search_query=tpb&amp;search_sort=relevance&amp;search_category=25</pre>
</li>
<li>Session IDs:
          <pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/search/noheaders?sessionid=6EE2BF1AF6A3D705D5561B7C3564D9C2</pre>
<blockquote>Wherever possible, avoid the use of session IDs in URLs and consider
            using cookies instead.</blockquote>
</li>
</ul>
<p>
          Consider using a <a href="/crawling-indexing/robots/intro.md">robots.txt file</a>
          to block Googlebot's access to these problematic URLs.</p>
</td>
</tr>
<tr>
<td><h3>Calendar issues</h3>
</td>
<td>
<p>A dynamically generated calendar might generate links to future and previous dates with
        no restrictions on start or end dates. For example:</p>
<pre class="devsite-disable-click-to-copy devsite-disable-code-toggle">https://example.com/calendar.php?d=13&amp;m=8&amp;y=2011</pre>
<p>
          If your site has an infinite calendar, add a <code><a href="/crawling-indexing/qualify-outbound-links.md">nofollow</a></code>
          attribute to links to dynamically created future calendar pages.
        </p>
</td>
</tr>
<tr>
<td><h3>Broken relative links</h3></td>
<td>Placing a <a href="https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references#parent-directory_relative">parent-relative link</a>
        on the wrong page may create infinite spaces if your server doesn't respond with the right
        HTTP status code for nonexistent pages. For example, a parent-relative link such as
        <code>&lt;a href="../../category/stuff"&gt;...&lt;/a&gt;</code> on <code>https://example.com/category/community/070413/html/FAQ.htm</code>
        may lead to bogus URLs such as <code>https://example.com/category/community/category/stuff</code>.
        To fix, use root-relative URLs in your links (instead of parent-relative).
      </td>
</tr>
</tbody>
</table>

## Fixing crawling-related URL structure problems

If you notice that Google Search is crawling these problematic URLs, we recommend the following:

- Consider using a [robots.txt file](/crawling-indexing/robots/intro.md) to block Googlebot's access to [problematic URLs](https://developers.google.com/search/docs/crawling-indexing/url-structure/#common-issues). Typically, consider blocking dynamic URLs, such as URLs that generate search results, or URLs that can create infinite spaces, such as calendars, and ordering and filtering functions.
- If your site has faceted navigation, learn how to [manage crawling of those faceted navigation URLs](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation#prevent-crawling-of-faceted-navigation-urls).

# References & Citations

[^google-url-structure]: Google Search Central (2025). "URL structure best practices for Google Search". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/url-structure. Retrieved 2026-09-01.
