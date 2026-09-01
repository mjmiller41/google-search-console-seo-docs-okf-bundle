---
type: Reference
title: Fact check (ClaimReview) structured data
description: Discover how you can use ClaimReview structured data to enable a summarized fact check to display in Google Search results.
resource: https://developers.google.com/search/docs/appearance/structured-data/factcheck
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-factcheck
  resource: https://developers.google.com/search/docs/appearance/structured-data/factcheck
  title: Fact check (ClaimReview) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Fact check (ClaimReview) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/factcheck](https://developers.google.com/search/docs/appearance/structured-data/factcheck). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-factcheck]

> We're phasing out support for `ClaimReview` markup in Google Search. However, this markup remains supported by the Factcheck Explorer Tool.

If you have a web page that reviews a claim made by others, you can include `ClaimReview` structured data on your web page. `ClaimReview` structured data can enable a summarized version of your fact check to display in Google Search results when your page appears in search results for that claim.

This guide describes the details on how to implement `ClaimReview` structured data. If you don't want to add structured data manually, you can check out the [Fact Check Markup Tool](https://toolbox.google.com/factcheck/markuptool). To learn more, visit [About the Fact Check Markup Tool](https://toolbox.google.com/factcheck/about#fcmt).

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Example

Imagine a page that evaluates the claim that the earth is flat. Here is what a search for "the world is flat" might look like in Google Search results if the page provides a `ClaimReview` element (note that the actual visual design may change):

![Single claim review associated with a page](https://developers.google.com/static/search/docs/images/factcheck-example-result.png)

> **Note**: The actual appearance in search results might be different. You can preview most features with the [Rich Results Test](https://support.google.com/webmasters/answer/7445569).

Here's an example of structured data on the page that hosts this fact check:

  

``` devsite-click-to-copy
<html>
  <head>
    <title>The world is flat</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "ClaimReview",
      "url": "https://example.com/news/science/worldisflat.html",
      "claimReviewed": "The world is flat",
      "itemReviewed": {
        "@type": "Claim",
        "author": {
          "@type": "Organization",
          "name": "Square World Society",
          "sameAs": "https://example.flatworlders.com/we-know-that-the-world-is-flat"
        },
        "datePublished": "2024-06-20",
        "appearance": {
          "@type": "OpinionNewsArticle",
          "url": "https://example.com/news/a122121",
          "headline": "Square Earth - Flat earthers for the Internet age",
          "datePublished": "2024-06-22",
          "author": {
            "@type": "Person",
            "name": "T. Tellar"
          },
          "image": "https://example.com/photos/1x1/photo.jpg",
          "publisher": {
            "@type": "Organization",
            "name": "Skeptical News",
            "logo": {
              "@type": "ImageObject",
              "url": "https://example.com/logo.jpg"
            }
          }
        }
      },
      "author": {
        "@type": "Organization",
        "name": "Example.com science watch"
      },
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": 1,
        "bestRating": 5,
        "worstRating": 1,
        "alternateName": "False"
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

## Eligibility guidelines

Google doesn't guarantee that fact checks will be shown in search results, even if your page is marked up correctly according to the [Rich Result Test](https://search.google.com/test/rich-results). Using structured data *enables* a feature to be present, it does not *guarantee* that it will be present. The Google algorithm programmatically determines the eligibility for fact check rich results, depending on many variables, including the following guidelines.

For your fact check content to be eligible to display as a fact check rich result on Google Search, you must meet the following guidelines:

- Your site must have several pages marked with `ClaimReview` structured data.
- You must follow all the [structured data guidelines](/appearance/structured-data/sd-policies.md) and [Search Essentials](/essentials/overview.md).
- There must not be any mismatch between the structured data and page content (for example, if the structured data indicated that the claim is true, but the content on the page said the claim was false). Instead, make sure that both the content and structured data match (for example, both indicate that the claim is true).
- You must meet the standards for accountability, transparency, readability, and site misrepresentation, as articulated in our [Google News General Guidelines](https://support.google.com/news/publisher-center/answer/6204050).
- You must have a corrections policy or have a mechanism for users to report errors.
- Websites for political entities (such as campaigns, parties, or elected officials) aren't eligible for this feature.
- Your readers can easily identify the claims and checks in the body of the article. Your readers are able to understand what was checked and what conclusions were reached.
- You must clearly attribute the specific claim that you're assessing to a distinct origin (separate from your website), whether it's another website, public statement, social media, or other traceable source.
- Your fact check analysis must be traceable and transparent about sources and methods, with citations and references to primary sources.

### Technical guidelines

- To be eligible for the single fact check rich result, a page must only have one `ClaimReview` element. If you add multiple `ClaimReview` elements per page, the page won't be eligible for the single fact check rich result.
- The page hosting the `ClaimReview` element must have at least a brief summary of the fact check and the evaluation, if not the full text.
- A specific `ClaimReview` must only be on one page on your site. Do not repeat the same fact check on multiple pages, unless they are variations of the same page (for example, you can post the same `ClaimReview` on the mobile and desktop versions of a page).
- If your website aggregates fact-check articles, ensure that all articles match the [criteria](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#guidelines) and that you provide an open and publicly available list of all fact-check websites you aggregate.

## Structured data type definitions

The following structured data types are required to implement fact checks:

- [`ClaimReview`](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#claimreview)
- [`Claim`](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#claim)
- [`Rating`](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#rating)

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

### `ClaimReview`

The full definition of `ClaimReview` is available at [schema.org/ClaimReview](https://schema.org/ClaimReview). The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>claimReviewed</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A short summary of the claim being evaluated. Try to keep this less than 75 characters
          to minimize wrapping when displayed on a mobile device.</p>
<blockquote>Don't include the rating in the <code>claimReviewed</code> field.
          Instead, specify the rating in the <code>reviewRating</code> field.</blockquote>
</td>
</tr>
<tr>
<td><code>reviewRating</code></td>
<td><p><code><a href="https://schema.org/Rating">Rating</a></code></p>
<p>The assessment of the claim. This object supports both a numeric and a textual assessment.
         The textual value is currently the only value shown in search results.</p>
<p>Different fact-checking projects have a variety of rating schemes which can have subtle differences,
          particularly for intermediate values. It is important to document such rating schemes to clarify
          the meaning of the numeric ratings. Minimally, there must be a number to text rating system
          for all your fact checks that carry numeric scores.</p>
<ul>
<li>1 = "False"</li>
<li>2 = "Mostly false"</li>
<li>3 = "Half true"</li>
<li>4 = "Mostly true"</li>
<li>5 = "True"</li>
</ul>
<p>For more information, see <a href="https://developers.google.com/search/docs/appearance/structured-data/factcheck/#rating">Rating</a>.</p></td>
</tr>
<tr>
<td><code>url</code></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>Link to the page hosting the full article of the fact check.</p>
<p>The domain of this URL value must be the same domain as, or a subdomain of, the
        page hosting this <code>ClaimReview</code> element. Redirects or shortened URLs (such
        as g.co/searchconsole) are not resolved, and so will not work here.</p></td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>author</code></td>
<td>
<p><code><a href="https://schema.org/Organization">Organization</a></code> or <code><a href="https://schema.org/Person">Person</a></code></p>
<p>The publisher of the fact check article, not the publisher of the
           claim. The <code>author</code> must be an organization or a person. The
           <code>author</code> have at least one of the following properties:</p>
<table>
<colgroup>
<col/>
</colgroup>
<tbody>
<tr>
<td>
<code>name</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Name of the organization that is publishing the fact check.</p>
</td>
</tr>
<tr>
<td><code>url</code>
</td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The URL of the publisher of the fact check. This can be a home page, contact page,
                 or other appropriate page.</p>
</td>
</tr>
</tbody>
</table>
<p>
           To help Google best
            understand authors across various features, consider following the
            <a href="/appearance/structured-data/article.md">author markup best practices</a>.
         </p>
</td>
</tr>
<tr>
<td><code>itemReviewed</code></td>
<td><p><code><a href="https://schema.org/Claim">Claim</a></code></p>
<p>An object describing the claim being made. For more information, see
          <a href="https://developers.google.com/search/docs/appearance/structured-data/factcheck/#claim"><code>Claim</code>.</a></p>
<blockquote><b>Backwards compatibility</b>: Upon the initial launch
            of fact check, Google Search recommended <code>CreativeWork</code> as the
            <code>itemReviewed</code>. Google Search continues to support earlier markup patterns.
            Here's an example that shows the original markup style:
            <br/>
<form><input><textarea>&lt;html&gt;
  &lt;head&gt;
    &lt;title&gt;The world is flat&lt;/title&gt;
    &lt;script type="application/ld+json"&gt;
    {
      "@context": "https://schema.org",
      "@type": "ClaimReview",
      "datePublished": "2024-06-22",
      "url": "https://example.com/news/science/worldisflat.html",
      "itemReviewed":
      {
        "@type": "CreativeWork",
        "author":
        {
          "@type": "Organization",
          "name": "Square World Society",
          "sameAs": "https://example.flatworlders.com/we-know-that-the-world-is-flat"
        },
        "datePublished": "2024-06-20"
      },
      "claimReviewed": "The world is flat",
      "author":
      {
        "@type": "Organization",
        "name": "Example.com science watch"
      },
      "reviewRating":
      {
        "@type": "Rating",
        "ratingValue": 1,
        "bestRating": 5,
        "worstRating": 1,
        "alternateName" : "False"
      }
    }
    &lt;/script&gt;
  &lt;/head&gt;
  &lt;body&gt;
  &lt;/body&gt;
&lt;/html&gt;</textarea></input></form></blockquote>
</td>
</tr>
</tbody>
</table>

### `Claim`

The full definition of `Claim` is available at [schema.org/Claim](https://schema.org/Claim).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>appearance</code></td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code> or
            <code><a href="https://schema.org/CreativeWork">CreativeWork</a></code></p>
<p>A link to, or inline description of, a <code>CreativeWork</code> in which this claim
            appears.</p>
<p>We recommend that you add either <code>appearance</code> or <code>firstAppearance</code>.
            You don't need to add both.</p>
</td>
</tr>
<tr>
<td><code>author</code></td>
<td><p>
<code><a href="https://schema.org/Organization">Organization</a></code> or
          <code><a href="https://schema.org/Person">Person</a></code></p>
<p>The author of the claim, not the author of the fact check. Don't include
            the <code>author</code> property if the claim doesn't have an author. If you add
            <code>author</code>, define the following properties:</p>
<table>
<colgroup>
<col/>
</colgroup>
<tbody>
<tr>
<td><code>name</code></td><td><code><a href="https://schema.org/Text">Text</a></code>, required
                <p>The publisher of the claim. The publisher can be a person or organization.</p></td></tr>
<tr><td><code>sameAs</code></td>
<td><code><a href="https://schema.org/URL">URL</a></code>, recommended
                  <p>Indicates the party that is making the claim, regardless of whether the party
                    is a <code><a href="https://schema.org/Person">Person</a></code> or
                    <code><a href="https://schema.org/Organization">Organization</a></code>. When multiple publishers
                    report on the same claim, the <code>appearance</code> property can be repeated. When
                    multiple parties are making essentially the same claim, the <code>author</code>
                    property can be repeated.</p>
<p>The URL can be:</p>
<ul>
<li>The home page of the organization that is making the claim. </li>
<li>Another definitive URL that provides information about the party that is making
                      the claim, such as a person or organization's Wikipedia or Wikidata entry.</li>
</ul>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><code>datePublished</code></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code>
          or <code><a href="https://schema.org/Date">Date</a></code></p>
<p>The date when the claim was made or entered public discourse (for example, when it became
          popular in social networks).</p>
</td>
</tr>
<tr>
<td><code>firstAppearance</code></td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code> or
          <code><a href="https://schema.org/CreativeWork">CreativeWork</a></code></p>
<p>A link to, or inline description of, a <code>CreativeWork</code> in which this specific
          claim first appears.</p>
<p>We recommend that you add either <code>appearance</code> or <code>firstAppearance</code>.
            You don't need to add both.</p>
</td>
</tr>
</tbody>
</table>

### `Rating`

The full definition of `Rating` is available at [schema.org/Rating](https://schema.org/Rating).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>alternateName</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The truthfulness rating assigned to <code>ClaimReview.reviewRating</code>, as a human-readible
        short word or phrase. This value is displayed
        in the fact check in search results. <b>Examples:</b> "True" or
        "Mostly true".</p>
<p>If using a longer sentence, be sure that the beginning of the sentence
        expresses the meaning, in case the sentence is truncated to fit the display. For example:
        "Mostly true in the specifics, although the overall claim is somewhat misleading"</p></td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>bestRating</code></td>
<td>
<p>
<code><a href="https://schema.org/Number">Number</a></code>
</p>
<p>For numeric ratings, the best value possible in the scale from worst to best. Must be greater than
      <code>worstRating</code>. Must be able to be evaluated as a number. <b>Example</b>:  4</p>
</td>
</tr>
<tr>
<td><code>name</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Same as <code>alternateName</code>, and used when <code>alternateName</code> is not
        provided, but we recommend that you specify <code>alternateName</code> instead of <code>name</code>.
      </p>
</td>
</tr>
<tr>
<td><code>ratingValue</code></td>
<td><p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>A numeric rating of this claim, in the range <code>worstRating</code> —
        <code>bestRating</code> inclusive. Integer values are recommended but not required. The closer the numeric
        rating is to <code>bestRating</code>, the more true it is; the closer this value is to
        <code>worstRating</code>, the more false it is. The numeric rating must be able to
        be evaluated as a number. <b>Example</b>: 4 </p>
</td>
</tr>
<tr>
<td><code>worstRating</code></td>
<td><p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>For numeric ratings, the worst value possible in a scale from worst to best. Must be less than
         <code>bestRating</code>. Must be able to be evaluated as a number. Must have a minimum value
           of 1. <b>Example</b>: 1</p>
</td>
</tr>
</tbody>
</table>

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#troubleshooting).
2.  [Inspect a live URL](https://support.google.com/webmasters/answer/9012289#test_live_page) to check if the issue persists.
3.  [Request validation](https://support.google.com/webmasters/answer/13300208) using the status report.

### After releasing new templates or updating your code

When you make significant changes to your website, monitor for increases in structured data invalid items.

- If you see an **increase in invalid items**, perhaps you rolled out a new template that doesn't work, or your site interacts with the existing template in a new and bad way.
- If you see a **decrease in valid items** (not matched by an increase in invalid items), perhaps you are no longer embedding structured data in your pages. Use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to learn what is causing the issue.

### Analyzing traffic periodically

Analyze your Google Search traffic using the [Performance Report](https://support.google.com/webmasters/answer/7576553). The data will show you how often your page appears as a rich result in Search, how often users click on it and what is the average position you appear on search results. You can also automatically pull these results with the [Search Console API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/factcheck/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-factcheck]: Google Search Central (2025). "Fact check (ClaimReview) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/factcheck. Retrieved 2026-09-01.
