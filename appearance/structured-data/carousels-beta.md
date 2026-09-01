---
type: Reference
title: Structured data carousels (beta)
description: This guide focuses on a new carousel rich result that's in beta, which is a list-like rich result that people can scroll horizontally to see more entities from a given site (also known as a host carousel).
resource: https://developers.google.com/search/docs/appearance/structured-data/carousels-beta
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-carousels-beta
  resource: https://developers.google.com/search/docs/appearance/structured-data/carousels-beta
  title: Structured data carousels (beta)
  author: Google Search Central (Google LLC)
  last_modified: '2026-01-21T00:00:00Z'
---

# Structured data carousels (beta)

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/carousels-beta](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-01-21.[^google-carousels-beta]

Google uses [structured data](/appearance/structured-data/intro-structured-data.md) to understand the content on the page and show that content in a richer appearance in search results, which is called a *rich result*. This guide focuses on a [new carousel rich result that's in beta](https://developers.google.com/search/blog/2024/02/search-experiences-in-eea), which is a list-like rich result that people can scroll horizontally to see more entities from a given site (also known as a host carousel). Each tile in the carousel may have information from your site about the price, rating, and images for entities on the page.

To be eligible for this beta rich result, add `ItemList` structured data in combination with at least one one of the following supported structured data items:

- [`LocalBusiness`](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#localbusiness) and its subtypes, for example:
  - [`Restaurant`](https://schema.org/Restaurant)
  - [`Hotel`](https://schema.org/Hotel)
  - [`VacationRental`](https://schema.org/VacationRental)
- [`Product`](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#product)
- [`Event`](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#event)

Here's how carousels can look in Google Search when you add `ItemList` markup in combination with a supported content type:

![New carousel rich result](https://developers.google.com/static/search/blog/images/new-carousel-rich-result.png)

## Feature availability

This feature is in beta and you may see changes in requirements or guidelines, as we develop this feature. This feature is also only available in [European Economic Area](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Glossary:European_Economic_Area_(EEA)#:~:text=See%20EEA%20disambiguation%20page%20for,and%20Norway%3B%20excluding%20Switzerland).) (EEA) countries, Turkey, and South Africa, on both desktop and mobile devices. In EEA countries, this experience is available for queries related to hotels, vacation rentals, ground transportation, flights, local businesses, things to do (events, tours, and activities), and shopping. In Turkey, this experience is only available for queries related to hotels, vacation rentals, and local businesses. In South Africa, this experience is available for queries related to hotels, vacation rentals, things to do (events, tours, and activities), flights, shopping, food delivery, car hire, and bus booking.

If your business is based in the EEA or Turkey, or serves users in the EEA or Turkey, fill out the applicable form:

- For queries related to ground transportation, hotels, vacation rentals, local business, and things to do (for example, events, tours, and activities), use this [Google Search aggregator features interest form](https://support.google.com/websearch/contact/search_dma)
- For flight features, use this [flight queries interest form](https://support.google.com/travel/contact/flight_queries_interest)
- For shopping queries in [CSS Program countries](https://support.google.com/css-center/answer/7524491#Supported_countries), get started with the [Comparison Shopping Services (CSS) program](https://support.google.com/css-center/answer/7524491)

If your business is based in South Africa, fill out the [Google Search South African Badging and Refinement Chips Interest Form](https://docs.google.com/forms/d/e/1FAIpQLSeio2rTpaGNFohJQNKRDLQENyfK5avJFGJSx1nguoRwqsocIQ/viewform).

## Add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to add structured data to your site.

1.  Pick a single summary page that contains some information about every entity in the list. For example, a category page that lists the "Top hotels in Paris", with links out to specific detail pages on your site for more information about each hotel. You can mix and match different types of entities (for example, hotels, restaurants), if needed for your scenario. For example, if you have a "Things to do in Switzerland" article that lists both local events and local businesses.

2.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#structured-data-type-definitions) to that summary page. You don't need to add markup to the detail pages in order to be eligible for this beta feature. Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

3.  Add the required and recommended properties for the specific content type that the carousel is about:

    - [`LocalBusiness`](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#localbusiness) and its subtypes, for example:
      - [`Restaurant`](https://schema.org/Restaurant)
      - [`Hotel`](https://schema.org/Hotel)
      - [`VacationRental`](https://schema.org/VacationRental)
    - [`Product`](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#product)
    - [`Event`](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#event)

    Depending on your scenario, you may choose the best type to use. For example, if you have a list of hotels and vacation rentals on your page, use both `Hotel` and `VacationRental` types. While it's ideal to use the type that's closest to your scenario, you can choose to use a more generic type (for example, `LocalBusiness`).

4.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#guidelines).

5.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results).

6.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

7.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/sitemaps).

## Guidelines

For your page to be eligible for carousel rich results (beta), you must follow the [Search Essentials](/essentials/overview.md) and [general structured data guidelines](https://developers.google.com/search/docs/guides/sd-policies). In addition, the following guidelines apply to carousel rich results (beta):

- Use of generic types is allowed. However, to use recommended properties, you must use the respective types. For example, to use `amenityFeature`, use the `LodgingBusiness` type.
- Use of additional or extra fields is allowed, but may not appear in the rich result.
- Your site must have a summary page and multiple detail pages. Currently, this feature isn't designed to support other scenarios, such as an all-in-one page where the "details" are anchor points within the same page.
- The markup must be on a summary or category page, which is a list-like page that contains information about at least three entities and then links out to other pages on your site for more information on those entities. While you don't need to add markup to the detail pages, you must include the detail page URLs in your summary page's markup.
- Mark up all items that are on the summary or category page. For paginated categories, add an `ItemList` to each subsequent page and include the entities that are listed on that page. For infinite scroll, focus on marking up the entities that are initially loaded in the viewport.

## Examples

The following is a high level structure of the carousel. The order specified in the markup is the order that will be used to order the tiles in the carousel rich result.

  

``` devsite-click-to-copy
  <html>
    <head>
      <title>Top 5 Restaurants in Italy</title>
      <script type="application/ld+json">
        {
        "@context": "https://schema.org",
        "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
                "position": 1,
                "item": {
                  "@type": "Restaurant",
                  "name": "Trattoria Luigi",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$",
                  "servesCuisine": "Italian",
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.5,
                    "reviewCount": 250
                  },
                "url": "https://www.example.com/trattoria-luigi"
              }
            },
            {
              "@type": "ListItem",
                "position": 2,
                "item": {
                  "@type": "Restaurant",
                  "name": "La Pergola",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$",
                  "servesCuisine": "Italian",
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.9,
                    "reviewCount": 1150
                  },
                "url": "https://www.example.com/la-pergola"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Restaurant",
                "name": "Pasta e Basta",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.2,
                  "reviewCount": 690
                },
              "url": "https://www.example.com/pasta-e-basta"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
  
```

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

### `ItemList`

`ItemList` is the container item that holds all elements in the list. All URLs of the elements in the list must point to different pages on the same domain.

The full definition of `ItemList` is available at [schema.org/ItemList](https://schema.org/ItemList).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>itemListElement</code></td>
<td>
<p><a href="https://schema.org/ListItem"><code>ListItem</code></a>
</p>
<p>
          List of items. To specify a list, define an <code>ItemList</code> that contains at least
          three <code>itemListElement.item</code> elements.
        </p>
</td>
</tr>
<tr>
<td><code>itemListElement.item</code>
</td>
<td>
<p>Subtype of <code>LocalBusiness</code>, <code>Product</code>, or <code>Event</code>
</p>
<p>
          An individual item in a list. Populate this object with:
        </p>
<ul>
<li>The <a href="https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#common">general properties</a> that all carousels must have (<code>image</code>,
            <code>url</code>, <code>name</code>)</li>
<li>Any other properties required for this data type, as described for your content type:
            <ul>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#localbusiness"><code>LocalBusiness</code> and its subtypes</a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#product"><code>Product</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#event"><code>Event</code></a></li>
</ul>
</li>
</ul>
<p>
<b>Example</b>: For a hotel, provide <code>priceRange</code> and <code>amenityFeature</code> properties.
        </p>
</td>
</tr>
<tr>
<td><code>itemListElement.position</code>
</td>
<td>
<p>
<a href="https://schema.org/Integer"><code>Integer</code></a>
</p>
<p>
          The item's position in the carousel. This is a 1-based number.
        </p>
</td>
</tr>
</tbody>
</table>

### Common list item properties (`LocalBusiness`, `Product,` or `Event`)

All of the carousel item types have the following properties in common.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>image</code></td>
<td>
<p>Repeated <code><a href="https://schema.org/URL">URL</a></code> or
          <code><a href="https://schema.org/ImageObject">ImageObject</a></code>
</p>
<p>
          One or more images of the entity or item (for example, an image of the hotel). Don't include
          logos in this image property.
        </p>
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
<tr>
<td><code>name</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
          The string name of the entity or item. For example, the name of a hotel or a vacation
          listing. The <code>item.name</code> is displayed as the title of an individual item in
          the carousel. HTML formatting is ignored.
        </p>
</td>
</tr>
<tr>
<td><code>url</code></td>
<td>
<p>
<a href="https://schema.org/URL"><code>URL</code></a>
</p>
<p>
          The canonical URL of the item detail page (for example, the standalone page for a single
          hotel or vacation listing that was referenced in the summary page). All URLs in the
          list must be unique, but live on the same domain (the same domain, or sub or super domain
          as the summary page).
        </p>
<blockquote>Anchor links within a summary or category page aren't supported; your
          site must have standalone detail pages for each item in the list.</blockquote>
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
<code>aggregateRating.bestRating</code>
</td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The highest value allowed in this rating system (for example, <code>5 / 10</code>). If
          <code>bestRating</code> is omitted, <code>5</code> is assumed.
        </p>
</td>
</tr>
<tr>
<td>
<code>aggregateRating.ratingCount</code>
</td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The total number of ratings for the item on your site.
        </p>
</td>
</tr>
<tr>
<td>
<code>aggregateRating.ratingValue</code>
</td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code> or
          <code><a href="https://schema.org/Text">Text</a></code></p>
<p>A numerical quality rating for the item, either a number, fraction, or percentage (for
          example, <code>4</code>, <code>60%</code>, or <code>6 / 10</code>).
          Google understands the scale for fractions and percentages, since the scale is
          implied in the fraction itself or the percentage. The default scale for numbers is a
          5-point scale, where 1 is the lowest value and 5 is the highest value.  If another scale is
          intended, use <code>bestRating</code> and <code>worstRating</code>.</p>
<p>For decimal numbers, use a dot instead of a comma to specify the value (for example
          <code>4.4</code> instead of <code>4,4</code>). In Microdata and RDFa, you can use
          <code>content</code> attributes to override the visible content. That way, you can show
          the user whatever style convention you want, while also satisfying the dot requirement
          for structured data. For example:</p>
<pre class="devsite-click-to-copy">&lt;span itemprop="ratingValue" content="4.4"&gt;4,4&lt;/span&gt; stars</pre>
</td>
</tr>
</tbody>
</table>

### Additional type-specific properties definitions

#### `LocalBusiness` (and subtypes)

In addition to the [`ListItem` properties](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#listitem), Google supports the following `LocalBusiness` properties (including its subtypes) for carousel rich results Nest these properties under `itemListElement.item`.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>amenityFeature</code></td>
<td>
<p>
<a href="https://schema.org/LocationFeatureSpecification"><code>LocationFeatureSpecification</code></a>
</p>
<p><b>For <code>LodgingBusiness</code> only</b>: An amenity feature (for example, a
          characteristic or service) of the accommodation.</p>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "beachAccess",
  "value": true
}</pre>
</td>
</tr>
<tr>
<td><code>priceRange</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
          The relative price range of a business, commonly specified by a normalized number of
          currency signs. Provide the price range in either of the following formats:
        </p>
<ul>
<li><b>Price level:</b> for example, "$", "$$", "$$$"</li>
<li><b>Range:</b> for example, "$-$$"</li>
</ul>
<p>
            This field must be shorter than 12 characters. If it's longer than 12 characters, Google
            won't show a price range for the business.
          </p>
</td>
</tr>
<tr>
<td><code>servesCuisine</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p><b>For restaurants only</b>: The type of cuisine the restaurant serves.</p>
</td>
</tr>
</tbody>
</table>

#### `Product`

In addition to the [`ListItem` properties](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#listitem), Google supports the following `Product` properties for carousel rich results. Nest these properties under `itemListElement.item`.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>offers</code></td>
<td>
<p><a href="https://schema.org/Offer"><code>Offer</code></a> or
          <a href="https://schema.org/AggregateOffer"><code>AggregateOffer</code></a></p>
<p>A nested <code>Offer</code> or <code>AggregateOffer</code> to sell the product. Include
           the recommended properties for either <code>Offer</code> or <code>AggregateOffer</code>
          (whichever is applicable to your content).</p>
<p>If you're using <code>Offer</code>, including the following properties:</p>
<ul>
<li><code>offers.price</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
<p>If you're using <code>AggregateOffer</code>, including the following properties:</p>
<ul>
<li><code>offers.highPrice</code></li>
<li><code>offers.lowPrice</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>offers.highPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The highest price of all offers available. If you're specifying a single price with
          <code>price</code>, don't need to include the <code>highPrice</code> and <code>lowPrice</code>
          properties.
          </p>
</td>
</tr>
<tr>
<td><code>offers.lowPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The lowest price of all offers available. If you're specifying a single price with
          <code>price</code>, don't need to include the <code>highPrice</code> and <code>lowPrice</code>
          properties.
        </p>
</td>
</tr>
<tr>
<td><code>offers.price</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The offer price of a product, or of a price component when attached to <code>PriceSpecification</code>
          and its subtypes. If you're specifying a price range with <code>lowPrice</code> and <code>highPrice</code>,
          don't include the <code>price</code> property.
          </p>
</td>
</tr>
<tr>
<td><code>offers.priceCurrency</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
          The currency used to describe the product price, in three-letter
          <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format. If a currency is
          not provided, Google defaults to <code>USD</code>.
        </p>
</td>
</tr>
</tbody>
</table>

#### `Event`

In addition to the [`ListItem` properties](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#listitem), Google supports the following `Event` properties for carousel rich results. Nest these properties under `itemListElement.item`.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>offers</code></td>
<td>
<p><code>Offer</code> or <code>AggregateOffer</code></p>
<p>A nested <code>Offer</code> or <code>AggregateOffer</code> to sell the event. Include
           the recommended propeties for either <code>Offer</code> or <code>AggregateOffer</code>
          (whichever is applicable to your content).</p>
<p>If you're using <code>Offer</code>, including the following properties:</p>
<ul>
<li><code>offers.price</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
<p>If you're using <code>AggregateOffer</code>, including the following properties:</p>
<ul>
<li><code>offers.highPrice</code></li>
<li><code>offers.lowPrice</code></li>
<li><code>offers.priceCurrency</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>offers.highPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The highest price of all offers available. If you're specifying a single price with
          <code>price</code>, don't need to include the <code>highPrice</code> and <code>lowPrice</code>
          properties.
          </p>
</td>
</tr>
<tr>
<td><code>offers.lowPrice</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The lowest price of all offers available. If you're specifying a single price with
          <code>price</code>, don't need to include the <code>highPrice</code> and <code>lowPrice</code>
          properties.
        </p>
</td>
</tr>
<tr>
<td><code>offers.price</code></td>
<td>
<p>
<a href="https://schema.org/Number"><code>Number</code></a>
</p>
<p>
          The price for your tickets, including service charges and fees. Don't forget to update it
          as prices change or tickets sell out. If you're specifying a price range with
          <code>lowPrice</code> and <code>highPrice</code>, don't include the <code>price</code> property.
        </p>
<p>
          If the event is available without payment, fees, or service charges, set the
          <code>price</code> to <code>0</code>.
        </p>
<pre class="devsite-click-to-copy">"offers": {
  "@type": "Offer",
  "price": 0
}</pre>
</td>
</tr>
<tr>
<td><code>offers.priceCurrency</code></td>
<td>
<p>
<a href="https://schema.org/Text"><code>Text</code></a>
</p>
<p>
          The currency used to describe the event price, in three-letter
          <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format. If a currency is
          not provided, Google defaults to <code>USD</code>.
        </p>
</td>
</tr>
</tbody>
</table>

## Examples for common scenarios

### `Restaurant` example

Here is an example of a restaurant carousel in JSON-LD.

  

``` devsite-click-to-copy
<html>
    <head>
      <title>Top 5 Restaurants in Paris</title>
      <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "item": {
                "@type": "Restaurant",
                "name": "Trattoria Luigi",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.5,
                  "reviewCount": 250
                },
                "url": "https://www.example.com/restaurant-location-1"
              }
            },
            {
              "@type": "ListItem",
              "position": 2,
              "item": {
                "@type": "Restaurant",
                "name": "La Pergola",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 1150
                },
                "url": "https://www.example.com/restaurant-location-2"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Restaurant",
                "name": "Pasta e Basta",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$$$",
                "servesCuisine": "Italian",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.2,
                  "reviewCount": 690
                },
                "url": "https://www.example.com/restaurant-location-3"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
```

### Lodging (`Hotels` and `VacationRental`) example

Here is an example of a lodging carousel in JSON-LD.

  

``` devsite-click-to-copy
<html>
    <head>
      <title>Top 5 Hotels in Paris</title>
      <script type="application/ld+json">
        {
        "@context": "https://schema.org",
        "@type": "ItemList",
            "itemListElement": [
              {
                "@type": "ListItem",
                "position": 1,
                "item": {
                  "@type": "Hotel",
                  "name": "Four Seasons Hotel George V, Paris",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$$",
                  "amenityFeature": {
                      "@type": "LocationFeatureSpecification",
                      "name" : "internetType",
                      "value": "Free"
                  },
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.9,
                    "reviewCount": 50
                  },
                  "url": "https://www.example.com/four-seasons"
                }
              },
              {
                "@type": "ListItem",
                "position": 2,
                "item": {
                  "@type": "VacationRental",
                  "name": "Downtown Condo",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$",
                  "amenityFeature": {
                    "@type": "LocationFeatureSpecification",
                    "name" : "instantBookable",
                    "value": true
                  },
                  "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": 4.7,
                    "reviewCount": 827
                  },
                  "url": "https://www.example.com/downtown-condo"
                }
              },
              {
                "@type": "ListItem",
                "position": 3,
                "item": {
                  "@type": "Hotel",
                  "name": "Ritz Paris",
                  "image": [
                    "https://example.com/photos/1x1/photo.jpg",
                    "https://example.com/photos/4x3/photo.jpg",
                    "https://example.com/photos/16x9/photo.jpg"
                  ],
                  "priceRange": "$$$$",
                  "amenityFeature": {
                    "@type": "LocationFeatureSpecification",
                    "name" : "freeBreakfast",
                    "value": true
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 1290
                },
                "url": "https://www.example.com/ritz-paris"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
```

### Things to do example example

Here is an example of a things to do carousel in JSON-LD.

  

``` devsite-click-to-copy
<html>
    <head>
      <title>Top 5 Things To Do in Paris</title>
      <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "item": {
                "@type": "Event",
                "name": "Paris Seine River Dinner Cruise",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "Offer",
                  "price": 45.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.2,
                  "reviewCount": 690
                },
                "url": "https://www.example.com/event-location1"
              }
            },
            {
              "@type": "ListItem",
              "position": 2,
              "item": {
                "@type": "LocalBusiness",
                "name": "Notre-Dame Cathedral",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "priceRange": "$",
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.8,
                  "reviewCount": 4220
                },
                "url": "https://www.example.com/localbusiness-location"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Event",
                "name": "Eiffel Tower With Host Summit Tour",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "Offer",
                  "price": 59.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 652
                },
                "url": "https://www.example.com/event-location2"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
  
```

### `Product` example

Here is an example of a product carousel in JSON-LD.

  

``` devsite-click-to-copy
<html>
    <head>
      <title>Top coats of the season</title>
      <script type="application/ld+json">
        {
          "@context": "https://schema.org",
          "@type": "ItemList",
          "itemListElement": [
            {
              "@type": "ListItem",
              "position": 1,
              "item": {
                "@type": "Product",
                "name": "Puffy Coat Series by Goat Coat",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "AggregateOffer",
                  "lowPrice": 45.00,
                  "highPrice": 60.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 50
                },
                "url": "https://www.example.com/puffy-coats"
              }
            },
            {
              "@type": "ListItem",
              "position": 2,
              "item": {
                "@type": "Product",
                "name": "Wool Coat Series by Best Coats Around",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "AggregateOffer",
                  "lowPrice": 189.00,
                  "highPrice": 200.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.7,
                  "reviewCount": 827
                },
                "url": "https://www.example.com/wool-coats"
              }
            },
            {
              "@type": "ListItem",
              "position": 3,
              "item": {
                "@type": "Product",
                "name": "Antarctic Coat by Cold Coats",
                "image": [
                  "https://example.com/photos/1x1/photo.jpg",
                  "https://example.com/photos/4x3/photo.jpg",
                  "https://example.com/photos/16x9/photo.jpg"
                ],
                "offers": {
                  "@type": "Offer",
                  "price": 45.00,
                  "priceCurrency": "EUR"
                },
                "aggregateRating": {
                  "@type": "AggregateRating",
                  "ratingValue": 4.9,
                  "reviewCount": 1290
                },
                "url": "https://www.example.com/antarctic-coat"
              }
            }
          ]
        }
      </script>
    </head>
    <body>
    </body>
  </html>
  
```

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/carousels-beta/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-carousels-beta]: Google Search Central (2026). "Structured data carousels (beta)". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/carousels-beta. Retrieved 2026-09-01.
