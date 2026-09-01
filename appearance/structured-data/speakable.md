---
type: Reference
title: Speakable (Article, WebPage) structured data (BETA)
description: Speakable schema markup can be used to identify content that is best suited for audio playback. Learn about SEO for voice search with this guide.
resource: https://developers.google.com/search/docs/appearance/structured-data/speakable
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-speakable
  resource: https://developers.google.com/search/docs/appearance/structured-data/speakable
  title: Speakable (Article, WebPage) structured data (BETA)
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Speakable (Article, WebPage) structured data (BETA)

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/speakable](https://developers.google.com/search/docs/appearance/structured-data/speakable). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-speakable]

> This feature is in beta and subject to change. We're currently developing this feature and you may see changes in requirements or guidelines.

The `speakable` [schema.org](https://schema.org/) property identifies sections within an article or webpage that are best suited for audio playback using text-to-speech (TTS). Adding markup allows search engines and other applications to identify content to read aloud on Google Assistant-enabled devices using TTS. Web pages with `speakable` structured data can use the Google Assistant to distribute the content through new channels and reach a wider base of users.

The Google Assistant uses `speakable` structured data to answer topical news queries on smart speaker devices. When users ask for news about a specific topic, the Google Assistant returns up to three articles from around the web and supports audio playback using TTS for sections in the article with `speakable` structured data. When the Google Assistant reads aloud a `speakable` section, it attributes the source and sends the full article URL to the user's mobile device through the Google Assistant app.

## Example

The following is an example of `speakable` structured data using JSON-LD code and the xPath `content-locator` value:

``` devsite-click-to-copy
<html>
  <head>
    <title>Speakable markup example</title>
    <meta name="description" content="This page is all about the quick brown fox" />
    <script type="application/ld+json">
    {
     "@context": "https://schema.org/",
     "@type": "WebPage",
     "name": "Quick Brown Fox",
     "speakable":
     {
      "@type": "SpeakableSpecification",
      "xPath": [
        "/html/head/title",
        "/html/head/meta[@name='description']/@content"
        ]
      },
     "url": "https://www.example.com/quick-brown-fox"
     }
    </script>
  </head>
  <body>
  </body>
</html>
```

## Country and language availability

The `speakable` property works for users in the U.S. that have Google Home devices set to English, and publishers that publish content in English. We hope to launch in other countries and languages as soon as sufficient number of publishers have implemented `speakable`.

## Getting started

For your news content to be eligible as answers to topical news queries, follow these steps:

1.  Make sure that you follow [our guidelines](https://developers.google.com/search/docs/appearance/structured-data/speakable/#guidelines).
2.  Add [`speakable` structured data](https://developers.google.com/search/docs/appearance/structured-data/speakable/#structured-data-type-definitions) to your web page.

## Guidelines

You must follow these guidelines for `speakable` content to be eligible to appear in news results.

- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/speakable/#technical-guidelines)
- [Content guidelines](https://developers.google.com/search/docs/appearance/structured-data/speakable/#content-guidelines)
- [Search Essentials](/essentials/overview.md)
- [Structured data general guidelines](/appearance/structured-data/sd-policies.md)

### Technical guidelines

Follow these guidelines when implementing `speakable` markup for Google Assistant.

- Don't add `speakable` structured data to content that may sound confusing in voice-only and voice-forward situations, like datelines (location where the story was reported), photo captions, or source attributions.
- Rather than highlighting an entire article with `speakable` structured data, focus on key points. This allows listeners to get an idea of the story and not have the TTS readout cut off important details.

### Content guidelines

Follow these guidelines when writing content that you intend to mark up with `speakable` structured data.

- Content indicated by `speakable` structured data must have concise headlines and/or summaries that provide users with comprehensible and useful information.
- If you include the top of the story in `speakable` structured data, we suggest that you rewrite the top of the story to break up information into individual sentences so that it reads more clearly for TTS.
- For optimal audio user experiences, we recommend around 20-30 seconds of content per section of `speakable` structured data, or roughly two to three sentences.

## Structured data type definitions

[Speakable](https://pending.schema.org/speakable) is used by the [`Article`](https://pending.schema.org/Article) or [`Webpage`](https://pending.schema.org/WebPage) object. The full definition of `speakable` is available at [schema.org/speakable](https://schema.org/speakable). You must include the required properties for your content to be eligible for this feature.

The `speakable` property can be repeated an arbitrary number of times, with two kinds of possible `content-locator` values: CSS selectors and xPaths. Use one of the following properties:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>cssSelector</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Addresses content in the annotated pages (such as class attribute). Use either
            <code>cssSelector</code> or <code>xPath</code>; don't use both. For example:</p>
<pre class="devsite-click-to-copy">"speakable":
  {
  "@type": "SpeakableSpecification",
  "cssSelector": [
    ".headline",
    ".summary"
  ]
}</pre>
</td>
</tr>
<tr>
<td><code>xPath</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code>
<p>Addresses content using xPaths (assuming an XML view of the content). Use either
               <code>cssSelector</code> or <code>xPath</code>; don't use both. For example:</p>
<pre class="devsite-click-to-copy">"speakable":
  {
  "@type": "SpeakableSpecification",
  "xPath": [
    "/html/head/title",
    "/html/head/meta[@name='description']/@content"
  ]
}</pre>
</p></td>
</tr>
</tbody>
</table>

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/speakable/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

### Can't trigger content

*error* **Problem**: You can't trigger your content through the Google Assistant using TTS audio.

*done* **Fix the issue**

1.  Try the following voice commands:
    - "What's the latest news about \$topic?"
    - "What's the latest on \$topic?"
    - "Play news about \$topic."
2.  If you're still having trouble, it may be because ranking is determined algorithmically. The Google Assistant provides up to three articles from different news publications through TTS audio playback. For more information about how Google ranks articles, see [How Search works](https://www.google.com/search/howsearchworks/).

## More audio solutions

In addition to `speakable` structured data, you can use other Google Assistant audio solutions for your news content, such as advanced integration of Google Assistant for your own custom applications. For example, allowing users to interact with the app through Google Assistant. For more information, see the [Actions on Google developer guide](https://developers.google.com/actions).

# References & Citations

[^google-speakable]: Google Search Central (2025). "Speakable (Article, WebPage) structured data (BETA)". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/speakable. Retrieved 2026-09-01.
