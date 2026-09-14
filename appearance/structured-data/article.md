---
type: Reference
title: Article (Article, NewsArticle, BlogPosting) structured data
description: Learn how adding article schema markup to your news articles and blogs can enhance their appearance in Google Search results.
resource: https://developers.google.com/search/docs/appearance/structured-data/article
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-article
  resource: https://developers.google.com/search/docs/appearance/structured-data/article
  title: Article (Article, NewsArticle, BlogPosting) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Article (Article, NewsArticle, BlogPosting) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/article](https://developers.google.com/search/docs/appearance/structured-data/article). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-article]

Adding `Article` structured data to your news, blog, and sports article pages can help Google understand more about the web page and show better [title text](/appearance/title-link.md), images, and [date information](/appearance/publication-dates.md) for the article in search results on Google Search and other properties (for example, Google News and the [Google Assistant](https://developers.google.com/assistant/content/overview)). While there's no markup requirement to be eligible for Google News features like [Top stories](https://support.google.com/news/publisher-center/answer/9607026), you can add `Article` to more explicitly tell Google what your content is about (for example, that it's a news article, who the author is, or what the title of the article is).

![Article rich result](https://developers.google.com/static/search/docs/images/article-rich-result.png)

## Example

Here's an example of a page with `Article` structured data.

#### JSON-LD

  

``` devsite-click-to-copy
<html>
  <head>
    <title>Title of a News Article</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "Title of a News Article",
      "image": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "datePublished": "2024-01-05T08:00:00+08:00",
      "dateModified": "2024-02-05T09:20:00+08:00",
      "author": [{
          "@type": "Person",
          "name": "Jane Doe",
          "url": "https://example.com/profile/janedoe123"
        },{
          "@type": "Person",
          "name": "John Doe",
          "url": "https://example.com/profile/johndoe123"
      }]
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

#### Microdata

  

``` devsite-click-to-copy
<html>
  <head>
    <title>Title of a News Article</title>
  </head>
  <body>
    <div itemscope itemtype="https://schema.org/NewsArticle">
      <div itemprop="headline">Title of News Article</div>
      <meta itemprop="image" content="https://example.com/photos/1x1/photo.jpg" />
      <meta itemprop="image" content="https://example.com/photos/4x3/photo.jpg" />
      <img itemprop="image" src="https://example.com/photos/16x9/photo.jpg" />
      <div>
        <span itemprop="datePublished" content="2024-01-05T08:00:00+08:00">
          January 5, 2024 at 8:00am
        </span>
        (last modified
        <span itemprop="dateModified" content="2024-02-05T09:20:00+08:00">
          February 5, 2024 at 9:20am
        </span>
        )
      </div>
      <div>
        by
        <span itemprop="author" itemscope itemtype="https://schema.org/Person">
          <a itemprop="url" href="https://example.com/profile/janedoe123">
            <span itemprop="name">Jane Doe</span>
          </a>
        </span>
        and
        <span itemprop="author" itemscope itemtype="https://schema.org/Person">
          <a itemprop="url" href="https://example.com/profile/johndoe123">
            <span itemprop="name">John Doe</span>
          </a>
        </span>
      </div>
    </div>
  </body>
</html>
```

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add as many [recommended properties](https://developers.google.com/search/docs/appearance/structured-data/article/#structured-data-type-definitions) that apply to your web page. There are no required properties; instead, add the properties that apply to your content. Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/article/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Guidelines

You must follow these guidelines to enable structured data to be eligible for inclusion in Google Search results.

> **Warning:** If your site violates one or more of these guidelines, then Google may take [manual action](https://support.google.com/webmasters/answer/2604824) against it. Once you have remedied the problem, you can submit your site for [reconsideration](https://support.google.com/webmasters/answer/35843).

- [Search Essentials](/essentials/overview.md)
- [General structured data guidelines](/appearance/structured-data/sd-policies.md)
- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/article/#technical-guidelines)

### Technical guidelines

- For multi-part articles, make sure that the `rel=canonical` points at either each individual page or a "view-all" page (and not to page 1 of a multi-part series). Learn more about [canonicalization](/crawling-indexing/consolidate-duplicate-urls.md).
- If you offer subscription-based access to your website content, or if users must register for access, consider adding structured data for [subscription and paywalled content](/appearance/structured-data/paywalled-content.md).

## Structured data type definitions

To help Google better understand your page, include as many recommended properties that apply to your web page. There are no required properties; instead, add the properties that apply to your content.

### `Article` objects

Article objects must be based on one of the following schema.org types: [`Article`](https://schema.org/Article), [`NewsArticle`](https://schema.org/NewsArticle), [`BlogPosting`](https://schema.org/BlogPosting).

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>author</code></td>
<td><p><code><a href="https://schema.org/Person">Person</a></code> or <code><a href="https://schema.org/Organization">Organization</a></code></p>
<p>The author of the article. To help Google best understand authors across various features,
      we recommend following the <a href="https://developers.google.com/search/docs/appearance/structured-data/article/#author-bp">author markup best practices</a>.
      </p>
</td>
</tr>
<tr>
<td><code>author.name</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The name of the author.</p></td>
</tr>
<tr>
<td><code>author.url</code></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>A link to a web page that uniquely identifies the author of the article. For example, the
      author's social media page, an "about me" page, or a bio page.</p>
<p>If the URL is an internal profile page, we recommend marking up that author using
      <a href="/appearance/structured-data/profile-page.md">profile page structured data</a>.</p>
<blockquote>You can use the <code>sameAs</code> property as an alternative. Google can
       understand both <code>sameAs</code> and <code>url</code> when disambiguating authors.</blockquote></td>
</tr>
<tr>
<td><code>dateModified</code></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the article was most recently modified, in <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.
      We recommend that you provide timezone information; otherwise, we will default to <a href="/crawling-indexing/googlebot.md">the timezone used by Googlebot</a>.</p>
<p>Add the <code>dateModified</code> property if you want to provide more accurate date information to Google.
    The <a href="https://search.google.com/test/rich-results">Rich Results Test</a> doesn't show a warning for this property,
    as it's only recommended if you decide that it's applicable to your site.</p></td>
</tr>
<tr>
<td><code>datePublished</code></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the article was first published, in
      <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.
      We recommend that you provide timezone information; otherwise, we will default to <a href="/crawling-indexing/googlebot.md">the timezone used by Googlebot</a>.</p>
<p>Add the <code>datePublished</code> property if you want to provide more
      accurate date information to Google. The
      <a href="https://search.google.com/test/rich-results">Rich Results Test</a> doesn't show a
      warning for this property, as it's only recommended if you decide that it's applicable to your site.</p></td>
</tr>
<tr>
<td><code>headline</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The title of the article. Consider using a concise title, as long titles may be truncated on some devices.</p></td>
</tr>
<tr>
<td><code>image</code></td>
<td><p>Repeated <code><a href="https://schema.org/ImageObject">ImageObject</a></code> or <code><a href="https://schema.org/URL">URL</a></code></p>
<p>The URL to an image that is representative of the article. Use images that are relevant
        to the article, rather than logos or captions.</p>
<p>Additional image guidelines:
  <ul>
<li>Image URLs must be crawlable and indexable. To check if Google can access your URLs, use
      the <a href="https://support.google.com/webmasters/answer/9012289">URL Inspection tool</a>.</li>
<li>Images must represent the marked up content.</li>
<li>Images must be in a file format that's <a href="/appearance/google-images.md">supported by Google Images</a>.</li>
<li>For best results, we recommend providing multiple high-resolution images (minimum of 50K pixels when
      multiplying width and height) with the following aspect ratios: 16x9, 4x3, and 1x1.</li>
</ul>
<p>For example:</p>
<pre class="devsite-click-to-copy">"image": [
  "https://example.com/photos/1x1/photo.jpg",
  "https://example.com/photos/4x3/photo.jpg",
  "https://example.com/photos/16x9/photo.jpg"
]</pre>
</p></td>
</tr>
</tbody>
</table>

## Author markup best practices

To help Google best understand and represent the author of the content, we recommend following these best practices when specifying authors in markup:

<table>
<thead>
<tr>
<th colspan="2">Best practices for author markup</th>
</tr>
</thead>
<tbody>
<tr>
<td><h3>
        Include all authors in the markup
        </h3></td>
<td>
<p>
          Make sure that all the authors that are presented as authors on the web page are also included in markup.
        </p>
</td>
</tr>
<tr>
<td><h3>
        Specifying multiple authors
        </h3></td>
<td>
<p>
          When specifying multiple authors, list each author in their own <code>author</code> field:
        </p>
<pre class="devsite-click-to-copy">"author": [
  {"name": "Willow Lane"},
  {"name": "Regula Felix"}
]</pre>
<p>
Don't merge multiple authors in the same <code>author</code> field:
        </p>
<pre class="devsite-click-to-copy">"author": {
  "name": "Willow Lane, Regula Felix"
}</pre>
</td>
</tr>
<tr>
<td><h3>
        Use additional fields
        </h3></td>
<td>
<p>
          To help Google better understand who the author is, we strongly recommend using the
          <code>type</code> and <code>url</code> (or <code>sameAs</code>)
          properties. Use valid URLs for the <code>url</code> or <code>sameAs</code> properties.
        </p>
<p>
          For example, if the author is a person, you could link to an author's page that
          provides more information about the author:
        </p>
<pre class="devsite-click-to-copy">"author": [
  {
    "@type": "Person",
    "name": "Willow Lane",
    "url": "https://www.example.com/staff/willow_lane"
  }
]</pre>
<p>
          If the author is an organization, you could link to the organization's home page.
        </p>
<pre class="devsite-click-to-copy">"author":
  [
    {
      "@type":"Organization",
      "name": "Some News Agency",
      "url": "https://www.example.com/"
  }
]</pre>
</td>
</tr>
<tr>
<td><h3>
        Only specify the author's name in the <code>author.name</code> property
        </h3></td>
<td>
<p>
          In the <code>author.name</code> property, only specify the name of the author. Don't add
          any other piece of information. More specifically, don't add the following information:
        </p>
<ul>
<li>The name of the publisher. Instead, use the <code>publisher</code> property.</li>
<li>The author's job title. Instead, use the appropriate property if you want to specify
            that information (<a href="https://schema.org/jobTitle"><code>jobTitle</code></a>).</li>
<li>Honorific prefix or suffix. Instead, use the appropriate property if you want to
            specify that information (<a href="https://schema.org/honorificPrefix"><code>honorificPrefix</code></a>
            or <a href="https://schema.org/honorificSuffix"><code>honorificSuffix</code></a>).</li>
<li>Introductory words (for example, don't include words like "posted by").</li>
</ul>
<pre class="devsite-click-to-copy">"author":
  [
    {
      "@type": "Person",
      "name": "Echidna Jones",
      "honorificPrefix": "Dr",
      "jobTitle": "Editor in Chief"
    }
  ],
"publisher":
  [
    {
      "@type": "Organization",
      "name": "Bugs Daily"
    }
  ]
}</pre>
</td>
</tr>
<tr>
<td><h3>
        Use the appropriate <code>Type</code>
</h3></td>
<td>
<p>
          Use the <code>Person</code> type for people, and the <code>Organization</code> type
          for organizations. Don't use the <code>Thing</code> type, and don't use the wrong type
          (for example, using the <code>Organization</code> type for a person).</p>
</td>
</tr>
</tbody>
</table>

Here's an example that applies the author markup best practices:

``` devsite-click-to-copy
"author":
  [
    {
      "@type": "Person",
      "name": "Willow Lane",
      "jobTitle": "Journalist",
      "url": "https://www.example.com/staff/willow-lane"
    },
    {
      "@type": "Person",
      "name": "Echidna Jones",
      "jobTitle": "Editor in Chief",
      "url": "https://www.example.com/staff/echidna-jones"
    }
  ],
"publisher":
  {
    "@type": "Organization",
    "name": "The Daily Bug",
    "url": "https://www.example.com"
  },
  // + Other fields related to the article...
}
```

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/article/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-article]: Google Search Central (2026). "Article (Article, NewsArticle, BlogPosting) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/article. Retrieved 2026-09-14.
