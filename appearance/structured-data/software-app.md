---
type: Reference
title: Software app (SoftwareApplication) structured data
description: Learn how to add software application schema to a web page so you can better display your app details in Google Search.
resource: https://developers.google.com/search/docs/appearance/structured-data/software-app
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-software-app
  resource: https://developers.google.com/search/docs/appearance/structured-data/software-app
  title: Software app (SoftwareApplication) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Software app (SoftwareApplication) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/software-app](https://developers.google.com/search/docs/appearance/structured-data/software-app). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-software-app]

Mark up software application information in the body of a web page to better display your app details in Google Search results.

![Software application rich result in Google Search results](https://developers.google.com/static/search/docs/images/software-apps.png)

> **Note**: The actual appearance in search results might be different. You can preview most features with the [Rich Results Test](https://support.google.com/webmasters/answer/7445569).

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/software-app/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/software-app/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

JSON-LD

Here's an example of a software app in JSON-LD:

  

``` devsite-click-to-copy
<html>
  <head>
    <title>Angry Birds</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Angry Birds",
      "operatingSystem": "ANDROID",
      "applicationCategory": "GameApplication",
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 4.6,
        "ratingCount": 8864
      },
      "offers": {
        "@type": "Offer",
        "price": 1.00,
        "priceCurrency": "USD"
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

RDFa

Here's an example of a software app in RDFa:

  

``` devsite-click-to-copy
<div vocab="https://schema.org/" typeof="SoftwareApplication">
  <span property="name">Angry Birds</span> -

  REQUIRES <span property="operatingSystem">ANDROID</span>
  TYPE: <span property="applicationCategory" content="GameApplication">Game</span>

  RATING:
  <div property="aggregateRating" typeof="AggregateRating">
    <span property="ratingValue">4.6</span> (
    <span property="ratingCount">8864</span> ratings )
  </div>

  <div property="offers" typeof="Offer">
    Price: $<span property="price">1.00</span>
    <meta property="priceCurrency" content="USD" />
  </div>
</div>
  
```

Microdata

Here's an example of a software app in Microdata:

  

``` devsite-click-to-copy
<div itemscope itemtype="https://schema.org/SoftwareApplication">
  <span itemprop="name">Angry Birds</span> -

  REQUIRES <span itemprop="operatingSystem">ANDROID</span>
  TYPE: <span itemprop="applicationCategory" content="GameApplication">Game</span>

  RATING:
  <div itemprop="aggregateRating" itemscope itemtype="https://schema.org/AggregateRating">
    <span itemprop="ratingValue">4.6</span> (
    <span itemprop="ratingCount">8864</span> ratings )
  </div>

  <div itemprop="offers" itemscope itemtype="https://schema.org/Offer">
    Price: $<span itemprop="price">1.00</span>
    <meta itemprop="priceCurrency" content="USD" />
  </div>
</div>
  
```

## Guidelines

You must follow these guidelines for your app to be eligible to appear as a rich result.

> **Warning:** If your site violates one or more of these guidelines, then Google may take [manual action](https://support.google.com/webmasters/answer/2604824) against it. Once you have remedied the problem, you can submit your site for [reconsideration](https://support.google.com/webmasters/answer/35843).

- [Search Essentials](/essentials/overview.md)
- [General structured data guidelines](/appearance/structured-data/sd-policies.md)

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

### `SoftwareApplication`

The full definition of `SoftwareApplication` is available at [schema.org/SoftwareApplication](https://schema.org/SoftwareApplication).

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>name</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The name of the app.</p>
</td>
</tr>
<tr>
<td>
<code>offers.price</code>
</td>
<td>
<p><code><a href="https://schema.org/Offer">Offer</a></code></p>
<p>An offer to sell the app. For developers, <code>offers</code> can indicate the
              marketplaces that carry the application. For marketplaces, use <code>offers</code> to
              indicate the price of the app for a specific app instance.</p>
<p>
              If the app is available without payment, set <code>offers.price</code> to <code>0</code>. For example:
            </p>
<pre class="devsite-click-to-copy">"offers": {
  "@type": "Offer",
  "price": 0
}</pre>
<p>
              If the app has a price greater than 0, we recommend also including the <code>offers.priceCurrency</code> property (or Google will try to find the right currency).
              For example:
            </p>
<pre class="devsite-click-to-copy">"offers": {
  "@type": "Offer",
  "price": 1.00,
  "priceCurrency": "USD"
}</pre>
</td>
</tr>
<tr>
<td>
            Rating or review
          </td>
<td>
<p>
              A rating or review of the app. You must include one of the following properties:
            </p>
<table>
<tr>
<td>
<code>aggregateRating</code>
</td>
<td><p><code><a href="https://schema.org/AggregateRating">AggregateRating</a></code></p>
<p>The average review score of the app. Follow the
              <a href="/appearance/structured-data/review-snippet.md">Review snippet
                guidelines</a> and list of required and recommended
              <a href="/appearance/structured-data/review-snippet.md">AggregateRating properties</a>.</p>
</td>
</tr>
<tr>
<td>
<code>review</code>
</td>
<td><p><code><a href="https://schema.org/Review">Review</a></code></p>
<p>A single review of the app. Follow the
              <a href="/appearance/structured-data/review-snippet.md">Review snippet
                guidelines</a> and list of required and recommended
              <a href="/appearance/structured-data/review-snippet.md">Review properties</a>.</p>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>applicationCategory</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The type of app (for example, <code>BusinessApplication</code> or
              <code>GameApplication</code>). The value must be a supported app type.</p>
<p><b>List of supported app types</b></p>
<ul>
<li><code>GameApplication</code></li>
<li><code>SocialNetworkingApplication</code></li>
<li><code>TravelApplication</code></li>
<li><code>ShoppingApplication</code></li>
<li><code>SportsApplication</code></li>
<li><code>LifestyleApplication</code></li>
<li><code>BusinessApplication</code></li>
<li><code>DesignApplication</code></li>
<li><code>DeveloperApplication</code></li>
<li><code>DriverApplication</code></li>
<li><code>EducationalApplication</code></li>
<li><code>HealthApplication</code></li>
<li><code>FinanceApplication</code></li>
<li><code>SecurityApplication</code></li>
<li><code>BrowserApplication</code></li>
<li><code>CommunicationApplication</code></li>
<li><code>DesktopEnhancementApplication</code></li>
<li><code>EntertainmentApplication</code></li>
<li><code>MultimediaApplication</code></li>
<li><code>HomeApplication</code></li>
<li><code>UtilitiesApplication</code></li>
<li><code>ReferenceApplication</code></li>
</ul>
</td>
</tr>
<tr>
<td>
<code>operatingSystem</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The operating system(s) required to use the app (for example, <code>Windows 7</code>,
              <code>OSX 10.6</code>, <code>Android 1.6</code>)</p>
</td>
</tr>
</tbody>
</table>

### Extended properties for app subtypes

For mobile applications and web applications, Google also supports [`MobileApplication`](https://schema.org/MobileApplication) and [`WebApplication `](https://schema.org/WebApplication).

Google doesn't show a rich result for Software Apps that only have the [`VideoGame`](https://schema.org/VideoGame) type. To make sure that your Software App is eligible for display as a rich result, co-type the [`VideoGame`](https://schema.org/VideoGame) type with another type. For example:

``` devsite-click-to-copy
{
  "@context": "https://schema.org",
  "@type": ["VideoGame", "MobileApplication"],
  ....
}
```

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/software-app/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-software-app]: Google Search Central (2025). "Software app (SoftwareApplication) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/software-app. Retrieved 2026-09-01.
