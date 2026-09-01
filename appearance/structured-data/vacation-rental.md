---
type: Reference
title: Vacation rental (VacationRental) structured data
description: Vacation listing structured data can help people find your vacation listings on Search. Learn about how to add markup and which fields to add, such as location, images, and the rating of your vacation property.
resource: https://developers.google.com/search/docs/appearance/structured-data/vacation-rental
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-vacation-rental
  resource: https://developers.google.com/search/docs/appearance/structured-data/vacation-rental
  title: Vacation rental (VacationRental) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Vacation rental (VacationRental) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/vacation-rental](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-vacation-rental]

![An illustration of vacation rentals in Google Search](https://developers.google.com/static/search/docs/images/vacation-rental-rich-result.png)

When you add structured data to your vacation rental listing pages, Google Search can show your listing in richer ways. Users can see listing information, such as the name, description, images, location, rating, reviews and more right in search results.

## Before You Begin

These instructions are intended for sites that have already connected with a Google Technical Account Manager and have access to the [Hotel Center](https://hotelcenter.google.com/). If you're interested in integrating your vacation rental listings, you can fill out the [vacation rental interest form](https://services.google.com/fb/forms/googlevacationrentalsinterestform/). Filling out the form is an expression of interest and doesn't guarantee an invitation into the Early Adopters Program.

This feature is limited to sites that meet certain eligibility criteria and additional [steps are required](https://support.google.com/hotelprices/answer/11946837) to complete the integration. To learn more about how to list your vacation rentals on Google, visit the integration [starter guide](https://support.google.com/hotelprices/answer/12568039).

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Example

Here's an example of a simple vacation rental listing using JSON-LD.

  

``` devsite-click-to-copy
<html>
  <head>
    <title>My Beautiful Vacation Rental</title>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "VacationRental",
        "additionalType": "HolidayVillageRental",
        "brand": {
          "@type": "Brand",
          "name": "brandIdName"
        },
        "containsPlace": {
          "@type": "Accommodation",
          "additionalType": "EntirePlace",
          "bed": [{
            "@type": "BedDetails",
            "numberOfBeds" : 1,
            "typeOfBed": "Queen"
          },
          {
            "@type": "BedDetails",
            "numberOfBeds" : 2,
            "typeOfBed": "Single"
          }],
         "occupancy": {
            "@type": "QuantitativeValue",
            "value" : 2
          },
          "amenityFeature": [
            {
              "@type": "LocationFeatureSpecification",
              "name": "ac",
              "value": true
            },
            {
              "@type": "LocationFeatureSpecification",
              "name": "airportShuttle",
              "value": true
            },
            {
             "@type": "LocationFeatureSpecification",
              "name": "balcony",
              "value": true
            },
            {
              "@type": "LocationFeatureSpecification",
              "name": "beachAccess",
              "value": true
            },
            {
              "@type": "LocationFeatureSpecification",
              "name": "childFriendly",
              "value": true
            }
          ],
          "floorSize": {
            "@type": "QuantitativeValue",
            "value" : 75,
            "unitCode": "MTK"
          },
          "numberOfBathroomsTotal": 1,
          "numberOfBedrooms": 3,
          "numberOfRooms": 5
        },
        "identifier": "abc123",
        "latitude": "42.12345",
        "longitude": "101.12345",
        "name": "My Beautiful Vacation Rental",
        "address": {
          "addressCountry": "US",
          "addressLocality": "Mountain View",
          "addressRegion": "California",
          "postalCode": "94043",
          "streetAddress": "1600 Amphitheatre Pkwy, Unit 6E"
        },
        "aggregateRating": {
          "ratingValue": 4.5,
          "ratingCount": 10,
          "reviewCount": 3,
          "bestRating": 5
        },
        "image": [
          "https://example.com/mylisting/unit_image1.png",
          "https://example.com/mylisting/unit_image2.png",
          "https://example.com/mylisting/unit_image3.png",
          "https://example.com/mylisting/unit_image4.png",
          "https://example.com/mylisting/unit_image5.png",
          "https://example.com/mylisting/unit_image6.png",
          "https://example.com/mylisting/unit_image7.png",
          "https://example.com/mylisting/unit_image8.png"
        ],
        "checkinTime": "18:00:00+08:00",
        "checkoutTime": "11:00:00+08:00",
        "description": "A great Vacation Rental in the perfect neighborhood.",
        "knowsLanguage": ["en-US", "fr-FR"],
        "review": [{
          "@type": "Review",
          "reviewRating": {
            "@type": "Rating",
            "ratingValue": 4,
            "bestRating": 5
          },
          "author": {
            "@type": "Person",
            "name": "Lillian Ruiz"
          },
          "datePublished": "2024-12-01",
          "contentReferenceTime": "2024-11-17"
        },
        {
          "@type": "Review",
          "reviewRating": {
            "@type": "Rating",
            "ratingValue": 5,
            "bestRating": 5
          },
          "author": {
            "@type": "Person",
            "name": "John S."
          },
          "datePublished": "2024-10-01",
          "contentReferenceTime": "2024-09-28"
        }
      ]
      }
    </script>
  </head>
  <body></body>
  </html>
```

## Eligibility guidelines

You must follow these guidelines for your vacation rental structured data to be eligible for use in Google Search.

- [Vacation Rental Policies](https://support.google.com/hotelprices/topic/12028304)
- [Search Essentials](/essentials/overview.md)
- [General structured data guidelines](/appearance/structured-data/sd-policies.md)

> **Warning:** If your site violates one or more of these guidelines, then Google may take [manual action](https://support.google.com/webmasters/answer/2604824) against it. Once you have remedied the problem, you can submit your site for [reconsideration](https://support.google.com/webmasters/answer/35843).

## Structured data type definitions

The following tables list properties and usage for marking up vacation rental listings using [schema.org/VacationRental](https://schema.org/VacationRental). You must include the required properties for your structured data to be eligible for display. You can also include the recommended properties to add more information about your content, which will provide a better user experience.

### `VacationRental`

The full definition of `VacationRental` is available at [schema.org/VacationRental](https://schema.org/VacationRental).

<table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th colspan="2">Required properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>containsPlace</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Accommodation">Accommodation</a>
</code>
</p>
<p>
          A vacation rental listing must contain one
          <a href="https://schema.org/Accommodation">Accommodation</a>
          to markup additional details such as beds, occupancy, number of rooms, and
          <code>amenityFeature</code> properties.
        </p>
</td>
</tr>
<tr>
<td>
<code>containsPlace.occupancy</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/QuantitativeValue">QuantitativeValue</a>
</code>
</p>
<p>Information about the maximum number of guests allowed to stay at the vacation rental listing.</p>
<pre class="devsite-click-to-copy">"occupancy": {
  "@type": "QuantitativeValue",
  "value" : 5
  }</pre>
</td>
</tr>
<tr>
<td>
<code>containsPlace.occupancy.value</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Integer">Integer</a>
</code>
</p>
<p>The numerical value of guests allowed to stay at the vacation rental listing.</p>
</td>
</tr>
<tr>
<td>
<code>identifier</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>A unique identifier for the property.</p>
<p>
          Additional guidelines:
        </p>
<ul>
<li>
              The identifier must be independent of the listing content; for example, it won't
              change when the property owner updates the listing name or number of bedrooms.
            </li>
<li>The same identifier must be used for the same listing in different languages.</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>image</code>
</td>
<td>
<p>
          Repeated <code><a href="https://schema.org/URL">URL</a></code>
</p>
<p>One or more images of the listing. The listing must have a minimum of 8 photos (at
          least 1 image of each of the following: bedroom, bathroom, and common area).</p>
<p>
          Additionally, follow the
          <a href="https://developers.google.com/hotels/vacation-rentals/dev-guide/onboarding#property_listing_image_requirements">Property listing image requirements</a>.
        </p>
</td>
</tr>
<tr>
<td>
<code>latitude</code>  (or <code>geo.latitude</code>)
      </td>
<td>
<p>
<code>
<a href="https://schema.org/Number">Number</a>
</code>
</p>
<p>
          The latitude of the listing's location. Precision must be at least 5 decimal places.
        </p>
</td>
</tr>
<tr>
<td>
<code>longitude</code>  (or <code>geo.longitude</code>)
      </td>
<td>
<p>
<code>
<a href="https://schema.org/Number">Number</a>
</code>
</p>
<p>
          The longitude of the listing's location. Precision must be at least 5 decimal places.
        </p>
</td>
</tr>
<tr>
<td>
<code>name</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>The name of the vacation rental listing.</p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup>
<col/>
</colgroup>
<thead>
<tr>
<th colspan="2">Recommended properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>additionalType</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>
          The type of vacation rental listing. Here are some suggested values:
        </p>
<ul>
<li><code>Apartment</code></li>
<li><code>Bungalow</code></li>
<li><code>Cabin</code></li>
<li><code>Chalet</code></li>
<li><code>Cottage</code></li>
<li><code>Gite</code></li>
<li><code>HolidayVillageRental</code></li>
<li><code>House</code></li>
<li><code>Villa</code></li>
<li><code>VacationRental</code></li>
</ul>
<p>
          The full definitions of these values are in
          <a href="https://support.google.com/hotelprices/answer/9970971?ref_topic=10062823#VR">Categories for lodging businesses</a>.
        </p>
</td>
</tr>
<tr>
<td>
<code>address</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/PostalAddress">PostalAddress</a>
</code>
</p>
<p>The full, physical location of the vacation rental.</p>
<p>Provide the street address, city, state or region,
        and postal code for the vacation rental. If applicable, provide the unit or apartment number.</p>
<p>Note that P.O. boxes or other mailing-only addresses are not
        considered full, physical addresses.</p>
<pre class="devsite-click-to-copy">"address": {
  "addressCountry": "US",
  "addressLocality": "Mountain View",
  "addressRegion": "California",
  "postalCode": "94043",
  "streetAddress": "1600 Amphitheatre Pkwy, Apartment 4E"
}</pre>
</td>
</tr>
<tr>
<td>
<code>address.addressCountry</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>The country of your vacation listing, using the two-letter
        <a href="https://wikipedia.org/wiki/ISO_3166-1">ISO 3166-1 alpha-2 country code</a>.</p>
</td>
</tr>
<tr>
<td>
<code>address.addressLocality</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>The city of your vacation listing.</p>
</td>
</tr>
<tr>
<td>
<code>address.addressRegion</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>The name of the listings's state, region, or province.</p>
</td>
</tr>
<tr>
<td>
<code>address.postalCode</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>The postal code for your vacation listing.</p>
</td>
</tr>
<tr>
<td>
<code>address.streetAddress</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>The full street address of your vacation listing, including the unit or apartment
          number if applicable.</p>
</td>
</tr>
<tr>
<td>
<code>aggregateRating</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/AggregateRating">AggregateRating</a>
</code>
</p>
<p>
        The average vacation rental rating is based on multiple ratings or reviews. Follow the
        <a href="/appearance/structured-data/review-snippet.md">review snippet guidelines</a>
        and the list of required and recommended
        <a href="/appearance/structured-data/review-snippet.md">aggregate rating properties</a>.
      </p>
</td>
</tr>
<tr>
<td>
<code>brand</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Brand">Brand</a>
</code>
</p>
<p>
        The brand ID associated with this property. Read more about how to to associate your
        properties to brands and how link your brand icons and display names to respective
        brand IDs in the <a href="https://support.google.com/hotelprices/answer/9919249">Hotel Center documentation</a>.
      </p>
<pre class="devsite-click-to-copy">"brand": {
  "@type": "Brand",
  "name" : "<var>brandIdName</var>"
}</pre>
</td>
</tr>
<tr>
<td>
<code>checkinTime</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Time">Time</a>
</code>
</p>
<p>
        The earliest time someone may check into a lodging establishment in
        <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.
      </p>
<p>Example: <code>14:30:00+08:00</code></p>
</td>
</tr>
<tr>
<td>
<code>checkoutTime</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Time">Time</a>
</code>
</p>
<p>The latest time someone may check into a lodging establishment in <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.</p>
<p>Example: <code>14:30:00+08:00</code></p>
</td>
</tr>
<tr>
<td>
<code>containsPlace.additionalType</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>
        The type of room for this accommodation. Use one of the following values:
      </p>
<ul>
<li><code>EntirePlace</code></li>
<li><code>PrivateRoom</code></li>
<li><code>SharedRoom</code></li>
</ul>
</td>
</tr>
<tr>
<td>
<code>containsPlace.amenityFeature</code>
</td>
<td>
<p>
        Repeated
        <code><a href="https://schema.org/amenityFeature">amenityFeature</a></code>
</p>
<p>Whether the property has a certain feature or amenity. Boolean examples follow this pattern:</p>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "<var>featureName</var>",
  "value": true
}</pre>
<b>Boolean values</b>
<p>Use one of the following values for the <code>amenityFeature.name</code> property. The
      values must be in English, even for non-English listings.</p>
<table>
<colgroup>
<col/>
</colgroup>
<tr>
<td>
<code>ac</code>
</td>
<td>
<p>Whether the property has air conditioning.</p>
</td>
</tr>
<tr>
<td>
<code>airportShuttle</code>
</td>
<td>
<p>Whether the host provides transportation to and from airport or other terminals.</p>
</td>
</tr>
<tr>
<td>
<code>balcony</code>
</td>
<td>
<p>Whether the property has a balcony.</p>
</td>
</tr>
<tr>
<td>
<code>beachAccess</code>
</td>
<td>
<p>Whether the property has access to a public beach close to the property.</p>
</td>
</tr>
<tr>
<td>
<code>childFriendly</code>
</td>
<td>
<p>Whether the property is suitable for children.</p>
</td>
</tr>
<tr>
<td>
<code>crib</code>
</td>
<td>
<p>Whether the property provides a crib.</p>
</td>
</tr>
<tr>
<td>
<code>elevator</code>
</td>
<td>
<p>Whether the property has an elevator.</p>
</td>
</tr>
<tr>
<td>
<code>fireplace</code>
</td>
<td>
<p>Whether the property has a fireplace.</p>
</td>
</tr>
<tr>
<td>
<code>freeBreakfast</code>
</td>
<td>
<p>Whether the property has breakfast included.</p>
</td>
</tr>
<tr>
<td>
<code>gymFitnessEquipment</code>
</td>
<td>
<p>Whether the property has a gym or fitness equipment.</p>
</td>
</tr>
<tr>
<td>
<code>heating</code>
</td>
<td>
<p>Whether the property has heating.</p>
</td>
</tr>
<tr>
<td>
<code>hotTub</code>
</td>
<td>
<p>Whether the property has a hot tub.</p>
</td>
</tr>
<tr>
<td>
<code>instantBookable</code>
</td>
<td>
<p>
            Whether the property is instantly bookable through the checkout process. The alternative is waiting for approval.
          </p>
</td>
</tr>
<tr>
<td>
<code>ironingBoard</code>
</td>
<td>
<p>Whether the property has ironing boards available.</p>
</td>
</tr>
<tr>
<td>
<code>kitchen</code>
</td>
<td>
<p>Whether the property has a kitchen.</p>
</td>
</tr>
<tr>
<td>
<code>microwave</code>
</td>
<td>
<p>Whether the property has a microwave available.</p>
</td>
</tr>
<tr>
<td>
<code>outdoorGrill</code>
</td>
<td>
<p>Whether the property has a grill.</p>
</td>
</tr>
<tr>
<td>
<code>ovenStove</code>
</td>
<td>
<p>Whether the property has an oven or a stove.</p>
</td>
</tr>
<tr>
<td>
<code>patio</code>
</td>
<td>
<p>Whether the property has a patio.</p>
</td>
</tr>
<tr>
<td>
<code>petsAllowed</code>
</td>
<td>
<p>Whether the guest is allowed to bring a pet to the property.</p>
<blockquote>You can use the <code>containsPlace.petsAllowed</code> property
            instead of this field.
         </blockquote>
</td>
</tr>
<tr>
<td>
<code>pool</code>
</td>
<td>
<p>Whether the property has a pool.</p>
</td>
</tr>
<tr>
<td>
<code>privateBeachAccess</code>
</td>
<td>
<p>Whether the property has dedicated access to a non-public beach.</p>
</td>
</tr>
<tr>
<td>
<code>selfCheckinCheckout</code>
</td>
<td>
<p>Whether the property supports self checkin and checkout.</p>
</td>
</tr>
<tr>
<td>
<code>smokingAllowed</code>
</td>
<td>
<p>Whether smoking is allowed in the unit.</p>
<blockquote>You can use the <code>containsPlace.smokingAllowed</code> property
             instead of this field.
          </blockquote>
</td>
</tr>
<tr>
<tr>
<td>
<code>tv</code>
</td>
<td>
<p>Whether the property has a TV.</p>
</td>
</tr>
<tr>
<td>
<code>washerDryer</code>
</td>
<td>
<p>Whether the property has laundry appliances.</p>
</td>
</tr>
<tr>
<td>
<code>wheelchairAccessible</code>
</td>
<td>
<p>Whether the property is wheelchair accessible.</p>
</td>
</tr>
<tr>
<td>
<code>wifi</code>
</td>
<td>
<p>Whether the property has wifi.</p>
</td>
</tr>
</tr></table>
<p><b>Non-boolean values</b></p>
<p>We also support the following non-boolean <code>name</code> and <code>value</code> pairs for
       <code>amenityFeature</code>.  Both values must be in English, even for non-English listings.
    </p>
<p>Non-boolean values follow this pattern:</p>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "<var>featureName</var>",
  "value": "<var>detail</var>"
  }</pre>
<table>
<colgroup>
<col/>
</colgroup>
<tr>
<td>
<p>
<code>
                internetType
              </code>
</p>
</td>
<td>
<p>
              The type of internet available on the property. Here are some suggested values:
            </p>
<ul>
<li><code>Free</code></li>
<li><code>Paid</code></li>
<li><code>None</code></li>
</ul>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "internetType",
  "value": "Free"
}</pre>
</td>
</tr>
<tr>
<td>
<code>
<p>parkingType</p>
</code>
</td>
<td>
<p>
            The type of parking available on the property. Here are some suggested values:
            <ul>
<li><code>Free</code></li>
<li><code>Paid</code></li>
<li><code>None</code></li>
</ul>
</p>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "parkingType",
  "value": "Free"
}</pre>
</td>
</tr>
<tr>
<td>
<code>
            poolType
          </code>
</td>
<td>
<p>
            The type of pool available on the property. Here are some suggested values:
            <ul>
<li><code>Indoor</code></li>
<li><code>Outdoor</code></li>
<li><code>None</code></li>
</ul>
<blockquote>Only English strings are supported.</blockquote>
</p>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "poolType",
  "value": "Outdoor"
}</pre>
</td>
</tr>
<tr>
<td>
<code>
<p>licenseNum</p>
</code>
</td>
<td>
<p>
            The license number (tourist or business) required to be shown for properties in certain
            regions of the world. It could be repeated and, if multiple licenses exist, we suggest
            adding the authority of the license as context (for example: <code>Paris: 123456ABC</code>).
          </p>
<pre class="devsite-click-to-copy">"amenityFeature": {
  "@type": "LocationFeatureSpecification",
  "name" : "licenseNum",
  "value": "Paris: 123456ABC"
}</pre>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>containsPlace.bed</code>
</td>
<td>
<p>
        Repeated <code><a href="https://schema.org/BedDetails">BedDetails</a></code>
</p>
<p>
        Information about the type and number of beds in the listing.
      </p>
<pre class="devsite-click-to-copy">"bed": [{
  "@type": "BedDetails",
  "numberOfBeds" : 1,
  "typeOfBed": "Queen"
  },
  {
  "@type": "BedDetails",
  "numberOfBeds" : 2,
  "typeOfBed": "Single"
  }]</pre>
</td>
</tr>
<tr>
<td>
<code>containsPlace.bed.numberOfBeds</code>
</td>
<td>
<p>
<code><a href="https://schema.org/Integer">Integer</a></code>
</p>
<p>
        The number of beds in the listing.
      </p>
</td>
</tr>
<tr>
<td>
<code>containsPlace.bed.typeOfBed</code>
</td>
<td>
<p>
<code><a href="https://schema.org/Text">Text</a></code>
</p>
<p>
        The type of beds in the listing. Here are some suggested values:
        <ul>
<li><code>CaliforniaKing</code></li>
<li><code>King</code></li>
<li><code>Queen</code></li>
<li><code>Full</code></li>
<li><code>Double</code></li>
<li><code>SemiDouble</code></li>
<li><code>Single</code></li>
</ul>
</p>
</td>
</tr>
<tr>
<td>
<code>containsPlace.floorSize</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/QuantitativeValue">QuantitativeValue</a>
</code>
</p>
<p>Size of the accommodation. It must be specified using <code>unitCode</code> property values:
      </p>
<ul>
<li>For square feet: <code>FTK</code> or <code>SQFT</code></li>
<li>For square meters: <code>MTK</code> or <code>SQM</code></li>
</ul>
<pre class="devsite-click-to-copy">"floorSize": {
  "@type": "QuantitativeValue",
  "value" : 75,
  "unitCode": "MTK"
  }</pre>
</td>
</tr>
<tr>
<td>
<code>containsPlace.numberOfBathroomsTotal</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Integer">Integer</a>
</code>
</p>
<p>
      The total bathrooms in the listing. Follow real estate conventions as
      <a href="https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field">documented in RESO</a>
      and use the simple sum of the number of bathrooms. For example, for a property with two full
      bathrooms and one half bathroom, the total number of bathrooms is 2.5.
    </p>
</td>
</tr>
<tr>
<td>
<code>containsPlace.numberOfBedrooms</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Integer">Integer</a>
</code>
</p>
<p>The total number of bedrooms in the listing.</p>
</td>
</tr>
<tr>
<td>
<code>containsPlace.numberOfRooms</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Integer">Integer</a>
</code>
</p>
<p>The total number of rooms in the listing.</p>
</td>
</tr>
<tr>
<td>
<code>description</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>A description of the property.</p>
</td>
</tr>
<tr>
<td>
<code>knowsLanguage</code>
</td>
<td>
<p>
<code>
          Repeated <a href="https://schema.org/Text">Text</a>
</code>
</p>
<p>
        The languages the host can speak. Use language codes from the IETF BCP 47 standard, such
        as <code>en-US</code> or <code>fr-FR</code>.
      </p>
</td>
</tr>
<tr>
<td>
<code>review</code>
</td>
<td>
<p>
<code>
          Repeated <a href="https://schema.org/Review">Review</a>
</code>
</p>
<p>
        One or more user reviews of the listing. Follow the
        <a href="/appearance/structured-data/review-snippet.md">review snippet guidelines</a>
        and the list of required and recommended
        <a href="/appearance/structured-data/review-snippet.md">review properties</a>.
      </p>
<blockquote><b>Note</b>: For vacation rentals, the <code>review.datePublished</code> is a required field.</blockquote>
<pre class="devsite-click-to-copy">"review": {
  "@type": "Review",
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": 4,
    "bestRating": 5
  },
  "datePublished": "2023-02-09"
  "author": {
    "@type": "Person",
    "name": "Lillian R"
  }
}</pre>
</td>
</tr>
<tr>
<td>
<code>review.contentReferenceTime</code>
</td>
<td>
<p>
<code>
<a href="https://schema.org/DateTime">DateTime</a>
</code>
</p>
<blockquote>This property is <b>required for vacation listings located in France</b>.</blockquote>
<p>The start date of the author's stay.</p>
</td>
</tr>
</tbody>
</table>

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#troubleshooting).
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
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/vacation-rental/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-vacation-rental]: Google Search Central (2025). "Vacation rental (VacationRental) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/vacation-rental. Retrieved 2026-09-01.
