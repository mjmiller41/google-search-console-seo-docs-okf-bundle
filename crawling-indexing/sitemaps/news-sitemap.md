---
type: Reference
title: News sitemaps
description: Learn how to create and submit a News sitemap by reviewing the requirements, example entries, and news-specific tag definitions.
resource: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-news-sitemap
  resource: https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap
  title: News sitemaps
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# News sitemaps

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-news-sitemap]

If you are a news publisher, use news sitemaps to tell Google about your news articles and additional information about them. You can either extend your existing sitemap with news specific tags, or create a separate news sitemap that's reserved just for your news articles. Either option is fine with Google, however creating a separate sitemap just for your news articles may enable better tracking of your content in Search in Search Console.

## News sitemap best practices

News sitemaps are based on generic sitemaps, so the [general sitemap best practices](/crawling-indexing/sitemaps/build-sitemap.md) also apply to news sitemaps.

Update your news sitemap with fresh articles as they're published. Don't create a new sitemap with each update. Google News crawls news sitemaps as often as it crawls the rest of your site.

Only include recent URLs for articles that were created in the last two days. Once the articles are older than two days, either remove those URLs from the news sitemap or remove the `<news:news>` metadata in your sitemap from the older URLs.

If you choose the method of removing old URLs from your news sitemap, this could mean that your sitemap becomes empty for a period of time (for example, if you haven't published articles in the last few days). You may see an Empty Sitemap warning in Search Console, but this is just to make sure it was intentional on your behalf. It won't cause any problems with Google Search if the file is empty.

## Example news sitemap

The following example shows a regular sitemap with news extension. It contains one `<url>` tag and a single `<news:news>` tag with its required child tags:

``` devsite-click-to-copy
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">
  <url>
  <loc>http://www.example.org/business/article55.html</loc>
  <news:news>
    <news:publication>
      <news:name>The Example Times</news:name>
      <news:language>en</news:language>
    </news:publication>
    <news:publication_date>2008-12-23</news:publication_date>
    <news:title>Companies A, B in Merger Talks</news:title>
  </news:news>
  </url>
</urlset>
```

## News sitemap reference

The `news` tags are defined in the news sitemap namespace: [`http://www.google.com/schemas/sitemap-news/0.9`](http://www.google.com/schemas/sitemap-news/0.9)

To make sure Google can use your news sitemap, you must use the following required tags:

<table>
<tr>
<th colspan="2">Required tags</th>
</tr>
<tr>
<td><code>&lt;news:news&gt;</code></td>
<td>
      The parent tag of other tags in the <code>news:</code> namespace. Each <code>url</code>
      sitemap tag can have only one <code>news:news</code> tag (plus the respective closing tag)
      and a sitemap may have up to 1,000 <code>news:news</code> tags. If there are more than
      1,000 <code>&lt;news:news&gt;</code> tags in a news sitemap,
      <a href="/crawling-indexing/sitemaps/large-sitemaps.md">split your sitemap into several smaller sitemaps</a>.
    </td>
</tr>
<tr>
<td><code>&lt;news:publication&gt;</code></td>
<td>
<p>
        The parent tag for the <code>&lt;news:name&gt;</code> and
        <code>&lt;news:language&gt;</code> tags. Each <code>&lt;news:news&gt;</code> parent tag
        may only have one <code>&lt;news:publication&gt;</code> tag.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;news:name&gt;</code></td>
<td>
<p>
        The <code>&lt;news:name&gt;</code> tag is the name of the news publication. It must
        exactly match the name as it appears on your articles on
        <a href="https://news.google.com/">news.google.com</a>, omitting
        anything in parentheses.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;news:language&gt;</code></td>
<td>
<p>
        The <code>&lt;news:language&gt;</code> tag is the language of your publication. Use an
        <a href="http://www.loc.gov/standards/iso639-2/php/code_list.php">ISO 639 language code</a>
        (two or three letters).
      </p>
<p>
<b>Exception</b>: For Simplified Chinese, use <code>zh-cn</code> and for Traditional
        Chinese, use <code>zh-tw</code>.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;news:publication_date&gt;</code></td>
<td>
<p>
        The article publication date in
        <a href="http://www.w3.org/TR/NOTE-datetime">W3C format</a>. Use
        either the "complete date" format (<code>YYYY-MM-DD</code>) or the "complete date plus
        hours, minutes, and seconds" format with time zone designator format
        (<code>YYYY-MM-DDThh:mm:ssTZD</code>). Specify the original date and time when the
        article was first published on your site. Don't specify the time when you added the
        article to your sitemap.
      </p>
<p>Google accepts any of the following formats:</p>
<ul>
<li>Complete date: <code>YYYY-MM-DD (1997-07-16)</code></li>
<li>
          Complete date plus hours and minutes:
          <code>YYYY-MM-DDThh:mmTZD (1997-07-16T19:20+01:00)</code>
</li>
<li>
          Complete date plus hours, minutes, and seconds:
          <code>YYYY-MM-DDThh:mm:ssTZD (1997-07-16T19:20:30+01:00)</code>
</li>
<li>
          Complete date plus hours, minutes, seconds, and a decimal fraction of a second:
          <code>YYYY-MM-DDThh:mm:ss.sTZD</code> (<code>1997-07-16T19:20:30.45+01:00</code>)
        </li>
</ul>
</td>
</tr>
<tr>
<td><code>&lt;news:title&gt;</code></td>
<td>
<p>The title of the news article.</p>
<blockquote>
<b>Tip:</b> Google may shorten the title of the news article for space reasons when
        displaying the article on various devices. Include the title of the article as it
        appears on your site. Don't include the author name, publication name, or publication
        date in the <code>&lt;news:title&gt;</code> tag. Learn more about
        <a href="/appearance/title-link.md">creating better titles</a>.
      </blockquote>
</td>
</tr>
</table>

## Troubleshooting sitemaps

If you're having trouble with your sitemap, you can investigate the errors with Google Search Console. See Search Console's [sitemaps troubleshooting guide](https://support.google.com/webmasters/answer/7451001#errors) for help.

## Additional resources

Want to learn more? Check out the following resources:

- [Submit your sitemap to Google](/crawling-indexing/sitemaps/build-sitemap.md)
- [Learn how to combine sitemap extensions](/crawling-indexing/sitemaps/combine-sitemap-extensions.md)

# References & Citations

[^google-news-sitemap]: Google Search Central (2025). "News sitemaps". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap. Retrieved 2026-09-01.
