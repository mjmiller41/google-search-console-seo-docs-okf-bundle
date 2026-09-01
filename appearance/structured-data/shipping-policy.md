---
type: Reference
title: Merchant shipping policy (ShippingService) structured data
description: Learn how to mark up shipping policies for products sold online or in stores.
resource: https://developers.google.com/search/docs/appearance/structured-data/shipping-policy
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-shipping-policy
  resource: https://developers.google.com/search/docs/appearance/structured-data/shipping-policy
  title: Merchant shipping policy (ShippingService) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-01-07T00:00:00Z'
---

# Merchant shipping policy (ShippingService) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/shipping-policy](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-01-07.[^google-shipping-policy]

![shopping knowledge panel with shipping information in search results](https://developers.google.com/static/search/docs/images/shipping-policy.png)

Many merchants have shipping policies that outline the process of shipping purchased products for customers. When you add `ShippingService` structured data to your site, Google Search can use this information to display shipping information alongside your products and in knowledge panels in Search results. `ShippingService` lets you specify details such as shipping costs and delivery times depending on product characteristics such as product weight, dimensions, or delivery location.

A standard shipping policy for your business that applies to most or all products you sell can be specified using the `ShippingService` structured data type nested under the `Organization` structured data type using the `hasShippingService` property.

> If you need to override your standard shipping policy for a specific product, specify one or more instances of the `OfferShippingDetails` type, which is nested under the `Offer` type using the `shippingDetails` property. For more information on shipping policies for individual products, refer to the [Merchant listing](/appearance/structured-data/merchant-listing.md) documentation. Shipping policies for individual products specified under `Offer` support a more limited set of properties than those described here for shipping policies specified under `Organization`.

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

This example shows for the US and Canada there is free 2-day shipping for orders over \$29.99, otherwise 3-day shipping for \$3.49. For Mexico, there is no shipping for orders under \$50, otherwise there is 4-day shipping with a 10% shipping cost.

``` devsite-click-to-copy
  <html>
  <head>
    <title>Our shipping policy</title>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "https://schema.org/Organization",
        "hasShippingService": {
            "@type": "ShippingService",
            "@id": "#us_ca_mx_standard_shipping",
            "name": "Standard shipping policies for US, Canada and Mexico",
            "description": "US and Canada: Free 2-day shipping for orders over $29.99,
                            otherwise 3-day shipping for $3.49.
                            Mexico: No shipping to Mexico for orders under $50,
                            otherwise 10% shipping cost and 4-day shipping.",
            "fulfillmentType": "FulfillmentTypeDelivery",
            "handlingTime": {
              "@type": "ServicePeriod",
              "cutoffTime": "14:30:00-07:00",
              "duration": {
                "@type": "QuantitativeValue",
                "minValue": 0,
                "maxValue": 1,
                "unitCode": "DAY"
              },
              "businessDays": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday"
              ]
            },
            "shippingConditions": [
              {
                "@type": "ShippingConditions",
                "shippingDestination": [
                  {
                    "@type": "DefinedRegion",
                    "addressCountry": "US"
                  },
                  {
                    "@type": "DefinedRegion",
                    "addressCountry": "CA"
                  }
                ],
                "orderValue": {
                  "@type": "MonetaryAmount",
                  "minValue": 0,
                  "maxValue": 29.99,
                  "currency": "USD"
                },
                "shippingRate": {
                  "@type": "MonetaryAmount",
                  "value": 3.49,
                  "currency": "USD"
                },
                "transitTime": {
                  "@type": "ServicePeriod",
                  "duration": {
                    "@type": "QuantitativeValue",
                    "minValue": 1,
                    "maxValue": 2,
                    "unitCode": "DAY"
                  },
                  "businessDays": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"
                  ]
                }
              },
              {
                "@type": "ShippingConditions",
                "shippingDestination": [
                  {
                    "@type": "DefinedRegion",
                    "addressCountry": "US"
                  },
                  {
                    "@type": "DefinedRegion",
                    "addressCountry": "CA"
                  }
                ],
                "orderValue": {
                  "@type": "MonetaryAmount",
                  "minValue": 30,
                  "currency": "USD"
                },
                "shippingRate": {
                  "@type": "MonetaryAmount",
                  "value": 0,
                  "currency": "USD"
                },
                "transitTime": {
                  "@type": "ServicePeriod",
                  "duration": {
                    "@type": "QuantitativeValue",
                    "minValue": 1,
                    "maxValue": 1,
                    "unitCode": "DAY"
                  },
                  "businessDays": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"
                  ]
                }
              },
              {
                "@type": "ShippingConditions",
                "shippingDestination": {
                  "@type": "DefinedRegion",
                  "addressCountry": "MX"
                },
                "orderValue": {
                  "@type": "MonetaryAmount",
                  "minValue": 0,
                  "maxValue": 49.99,
                  "currency": "USD"
                },
                "doesNotShip": true
              },
              {
                "@type": "ShippingConditions",
                "shippingDestination": {
                  "@type": "DefinedRegion",
                  "addressCountry": "MX"
                },
                "orderValue": {
                  "@type": "MonetaryAmount",
                  "minValue": 50,
                  "currency": "USD"
                },
                "shippingRate": {
                  "@type": "ShippingRateSettings",
                  "orderPercentage": 0.10
                },
                "transitTime": {
                  "@type": "ServicePeriod",
                  "duration": {
                    "@type": "QuantitativeValue",
                    "minValue": 2,
                    "maxValue": 3,
                    "unitCode": "DAY"
                  },
                  "businessDays": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"
                  ]
                }
              }
           ]
        }
        // Other Organization-level properties
        // ...
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

## Guidelines

For your shipping policy markup to be eligible for usage in Google Search, you must follow these guidelines:

- [General structured data guidelines](/appearance/structured-data/sd-policies.md)
- [Search Essentials](/essentials/overview.md)
- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#technical-guidelines)

### Technical guidelines

- We recommend placing shipping policy information on a single page on your site that describes the shipping policy of your business. You don't need to include it on every page of your site. Include the `ShippingService` structured data type under the `Organization` structured data type. For more information, see [Organization markup](/appearance/structured-data/organization.md).
- If you have a non-standard shipping policy for a specific product, specify the `OfferShippingDetails` structured data type directly under the `Offer` structured data type. Note that the properties supported for offer-level shipping policies are a subset of the properties supported for organization-level shipping policies. See [merchant listing markup](/appearance/structured-data/merchant-listing.md) for the subset of properties that are supported for product-level shipping policies.

## Structured data type definitions

You must include the required properties for your structured data to be eligible for usage in Google Search. You can also include recommended properties to add more information about your shipping policies, which could provide a better user experience.

### `ShippingService` (nested under `Organization` using the `hasShippingService` property)

Use the following properties to describe the standard shipping services for your business. <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>shippingConditions</code></td>
<td>
<p><code><a href="https://schema.org/ShippingConditions">ShippingConditions</a></code></p>
<p>
              Specify the shipping cost and/or delivery times that apply for a particular set of conditions, for example,
              a product weight range, product dimensions, order value, or delivery location. A <code>ShippingService</code> can have
              multiple <code>shippingConditions</code>. If more than one <code>ShippingConditions</code> applies to a product,
              we'll use the lowest shipping cost for the product for the given situation and display that rate and the associated
              shipping speed to customers. If the shipping cost is the same, we'll use the shipping information with the
              fastest shipping speed.
            </p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>
<p>
<code><a href="https://schema.org/Text">Text</a></code>
</p>
<p>A unique name for your shipping service, if applicable. For example, "Standard Shipping".</p>
</td>
</tr>
<tr>
<td><code>description</code></td>
<td>
<p>
<code><a href="https://schema.org/Text">Text</a></code>
</p>
<p>A description of your shipping service, if applicable. This is typically more comprehensive than the name.</p>
</td>
</tr>
<tr>
<td><code>fulfillmentType</code></td>
<td>
<p><code><a href="https://schema.org/FulfillmentTypeEnumeration">FulfillmentTypeEnumeration</a></code></p>
<p>How the product is delivered to the customer for this shipping service, if applicable.</p>
<ul>
<li><code>https://schema.org/FulfillmentTypeDelivery</code>: This service ships the product to the customer's address (this is the default if this property is not specified).</li>
<li><code>https://schema.org/FulfillmentTypeCollectionPoint</code>: The product is shipped to a collection point for customer pickup.</li>
</ul>
</td>
</tr>
<tr>
<td><code>handlingTime</code></td>
<td>
<p><code><a href="https://schema.org/ServicePeriod">ServicePeriod</a></code></p>
<p>Optional information about handling times (for example, in a warehouse) after receiving an order, if applicable.</p>
             See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-service-handling-time-properties"><code>ServicePeriod</code></a>
             properties under the <code>ShippingService</code> type supported by Google.</td></tr></tbody></table>

`validForMemberTier`

[`MemberProgramTier`](https://schema.org/MemberProgramTier)

The loyalty program and tier that this shipping service is valid for, if applicable. You can specify multiple member tiers if the shipping settings are the same for all of the tiers.

If you use the `validForMemberTier` property to designate member shipping benefits, you must also provide at least one regular (non-member) shipping service.

The loyalty programs and tiers that you offer for your business can either be defined in your Merchant Center account or using the `MemberProgram` structured data type nested under `Organization` structured data on a separate page that defines your organization's administrative details and policies. See [loyalty program markup](/appearance/structured-data/loyalty-program.md) for information on how to define the member programs and tiers for your organization.

Here's an example of the `validForMemberTier` property referencing a member program (*member-plus*) and tier (*silver*) defined in Merchant Center:

``` devsite-click-to-copy
"validForMemberTier": {
  "@type": "MemberProgramTier",
  "name": "silver",
  "isTierOf": {
    "@type": "MemberProgram",
    "name": "member-plus"
  }
}
```

Here's an example of the `validForMemberTier` property referencing `MemberProgramTier` structured data nested under `MemberProgram` structured data, which is in turn nested under a `Organization` structured data type on a separate page. The `MemberProgramTier` instance is identified by the `@id` property specifying the unique resource identifier (URI) of its definition: `https://www.example.com/com/member-plus#tier_silver`:

``` devsite-click-to-copy
"validForMemberTier": {
  "@id": "https://www.example.com/com/member-plus#tier_silver"
}
```

> This property is still in beta. Off-page `MemberProgramTier` structured data might not show up in Google Search right away.

#### `ServicePeriod` (for handling times)

> The `ServicePeriod` type is also used to specify transit times. When specifying transit times, the `cutoffTime` property is not used. For more information, see [`ServicePeriod` for transit times](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-service-transit-time-properties).

To specify shipping handling times, use the `ServicePeriod` type.

Here's an example of a `ServicePeriod` type where orders are processed Monday through Friday, with a cutoff time of 10:30 PM Eastern Standard Time. The duration of the handling time is between 0 and 2 days (where a handling time of 0 means orders are processed the same day if received before the cutoff time).

``` devsite-click-to-copy
"handlingTime": {
  "@type": "ServicePeriod",
  "businessDays": [
    "https://schema.org/Monday",
    "https://schema.org/Tuesday",
    "https://schema.org/Wednesday",
    "https://schema.org/Thursday",
    "https://schema.org/Friday"
  ],
  "cutoffTime": "22:30:00-05:00",
  "duration": {
    "@type": "QuantitativeValue",
    "minValue": 0,
    "maxValue": 2,
    "unitCode": "DAY"
  }
}
```

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>businessDays</code></td>
<td>
<p><code><a href="https://schema.org/DayOfWeek">DayOfWeek</a></code></p>
<p>The days of the week when received orders are processed, if applicable.</p>
</td>
</tr>
<tr>
<td><code>cutoffTime</code></td>
<td>
<p><code><a href="https://schema.org/Time">Time</a></code></p>
<p>The time after which orders received on a day are not processed that same day, if applicable.
                For orders processed after cutoff time, one day gets added to the delivery time estimate.
                The time is indicated using the ISO-8601 time format, for example "23:30:00-05:00"
                represents 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated
                Universal Time (UTC).</p>
</td>
</tr>
<tr>
<td><code>duration</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code></p>
<p>The delay between the receipt of an order and the goods leaving the warehouse, if applicable.</p>
</td>
</tr>
</tbody>
</table>

#### `QuantitativeValue` (for shipping handling times)

Use the `QuantitativeValue` type to represent minimum and maximum order handling times. You must provide either `value` (for a fixed handling time) or `maxValue` (for an upper bound for handling time) together with the `unitCode`. `minValue` can optionally be provided to specify a lower bound for handling time.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>maxValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The maximum number of days. The value must be a non-negative, whole number.</p>
</td>
</tr>
<tr>
<td><code>minValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The minimum number of days, if applicable. The value must be a non-negative, whole number.</p>
</td>
</tr>
<tr>
<td><code>unitCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The units of the minimum/maximum values. The value must be <code>DAY</code> or <code>d</code>.</p>
</td>
</tr>
<tr>
<td><code>value</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The exact number of handling days, if known. The value must be a non-negative, whole number.
                If provided, <code>minValue</code> and <code>maxValue</code> must not be specified.
              </p>
</td>
</tr>
</tbody>
</table>

### `ShippingConditions` (nested under `ShippingService` using the `shippingConditions` property)

Use the following properties to describe the conditions and associated costs and transit times for a shipping service.

If no shipping destination is specified, the shipping conditions are applicable to all shipping destinations worldwide.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>doesNotShip</code></td>
<td>
<p><code><a href="https://schema.org/Boolean">Boolean</a></code></p>
<p>If applicable, set this to <code>true</code> if shipping from a location in the specified <code>shippingOrigin</code>
            to a location in the specified <code>shippingDestination</code> isn't available for orders with the specified
            combination of <code>weight</code>, <code>numItems</code>, and <code>orderValue</code> conditions.</p>
</td>
</tr>
<tr>
<td><code>numItems</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code></p>
<p>The range of the number of products in the order for this shipping conditions object, if applicable.
            See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-quantitative-value-properties"><code>QuantitativeValue</code></a> properties
            related to the <code>ShippingConditions</code> type supported by Google.</p>
</td>
</tr>
<tr>
<td><code>orderValue</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code></p>
<p>The range of the cost of the order for this shipping conditions object, if applicable.
            See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-conditions-monetary-amount-properties"><code>MonetaryAmount</code></a>
            properties related to the <code>ShippingConditions</code> type supported by Google.</p>
</td>
</tr>
<tr>
<td><code>shippingDestination</code></td>
<td>
<p>
<code><a href="https://schema.org/DefinedRegion">DefinedRegion</a></code>
</p>
<p>Indicates shipping destination, if applicable. See the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#defined-region-properties"><code>DefinedRegion</code></a>
            properties under the <code>shippingDestination</code> property supported by Google.</p>
</td>
</tr>
<tr>
<td><code>shippingOrigin</code></td>
<td>
<p>
<code><a href="https://schema.org/DefinedRegion">DefinedRegion</a></code>
</p>
<p>Indicates shipping origin, if applicable. See the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#defined-region-properties"><code>DefinedRegion</code></a>
            properties under the <code>shippingOrigin</code> property supported by Google.</p>
</td>
</tr>
<tr>
<td><code>seasonalOverride</code></td>
<td>
<p><code><a href="https://schema.org/OpeningHoursSpecification">OpeningHoursSpecification</a></code></p>
<p>If applicable, use this property to specify a limited time period for which this shipping conditions object is valid.
                See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-seasonal-override-properties"><code>OpeningHoursSpecification</code></a>
                properties supported for the <code>ShippingConditions</code> type by Google.</p>

</td>
</tr>
<tr>
<td><code>shippingRate</code></td>
<td>
<p><code><a href="https://schema.org/ShippingRateSettings">ShippingRateSettings</a></code> or
                <code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code>
</p>
<p>If applicable, use this property to specify the shipping cost for
                shipments from a location in the specified <code>shippingOrigin</code> to a location
                in the specified <code>shippingDestination</code> for orders with the
                specified combination of <code>weight</code>, <code>numItems</code>, and <code>orderValue</code> conditions.
                See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-rate-settings-properties"><code>ShippingRateSettings</code>
</a> properties and <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-monetary-amount-properties"><code>MonetaryAmount</code>
</a> properties supported for the <code>ShippingConditions</code> type by Google. This property
                should only be specified if <code>doesNotShip</code> is absent or set to <code>false</code>.</p>

</td>
</tr>
<tr>
<td><code>transitTime</code></td>
<td>
<p><code><a href="https://schema.org/ServicePeriod">ServicePeriod</a></code></p>
<p>If applicable, use to specify the expected transit time between leaving the shipping origin (typically a warehouse)
                and arriving at the shipping destination (typically the customer). Applies to
                shipments from a location in the specified <code>shippingOrigin</code> property to a location
                in the specified <code>shippingDestination</code> property for orders with the
                specified combination of <code>weight</code>, <code>numItems</code>, and <code>orderValue</code> conditions.
                See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-service-transit-time-properties"><code>ServicePeriod</code></a>
                properties supported by Google. This property should only be specified if the <code>doesNotShip</code> property
                is absent or set to <code>false</code>.</p>

</td>
</tr>
<tr>
<td><code>weight</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code></p>
<p>The package's weight range for this shipping conditions object, if applicable.
              See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-quantitative-value-properties"><code>QuantitativeValue</code></a>
              properties related to the <code>ShippingConditions</code> type supported by Google.</p>
</td>
</tr>
</tbody>
</table>

#### `DefinedRegion`

Use the `DefinedRegion` type to create custom areas so that accurate shipping costs and transit times can be set across multiple shipping services.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>addressCountry</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The two-letter country code, in <a href="https://en.wikipedia.org/wiki/ISO_3166-1">
                 ISO 3166-1 alpha-2</a> format.</p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>addressRegion</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The country-specific region code, if applicable. The region must be a 2- or 3-character ISO 3166-2
                subdivision code, without country prefix. Google Search only supports
                the US, Australia, and Japan. Examples: <code>NY</code> (for US, state of New York),
                <code>NSW</code> (for Australia, state of New South Wales), or <code>03</code>
                (for Japan, Iwate prefecture).</p>
<p>Don't provide both a region and postal code information.</p>
</td>
</tr>
<tr>
<td><code>postalCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The country-specific postal code, if applicable. For example, <code>94043</code>. Postal codes are supported for
                Australia, Canada, and the US.</p>
</td>
</tr>
</tbody>
</table>

#### `ServicePeriod` (for transit times)

Use the `ServicePeriod` type to represent ranges of transit times for an order.

> You can also use the `ServicePeriod` type to specify handling times. For more information on handling times, see [`ServicePeriod`](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-service-handling-time-properties).

Example:

``` devsite-click-to-copy
"transitTime": {
  "@type": "ServicePeriod",
  "businessDays": [
    "https://schema.org/Monday",
    "https://schema.org/Tuesday",
    "https://schema.org/Wednesday",
    "https://schema.org/Thursday",
    "https://schema.org/Friday"
  ],
  "duration": {
    "@type": "QuantitativeValue",
    "minValue": 0,
    "maxValue": 2,
    "unitCode": "DAY"
  }
}
```

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>businessDays</code></td>
<td>
<p><code><a href="https://schema.org/DayOfWeek">DayOfWeek</a></code></p>
<p>The days of the week when an order is an active transit, if applicable. If your organization's
                business days are Monday through Saturday, you don't need to add this property.
            </p></td>
</tr>
<tr>
<td><code>duration</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code></p>
<p>The number of business days in transit, if applicable.
                See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-quantitative-value-properties"><code>QuantitativeValue</code></a> properties
                for transit times supported by Google.</p>
</td>
</tr>
</tbody>
</table>

#### `QuantitativeValue` (for shipping transit times)

Use the `QuantitativeValue` type to represent minimum and maximum order transit times. You must provide either `value` (for a fixed transit time) or `maxValue` (for an upper bound for transit time) together with the `unitCode`. `minValue` can optionally be provided to specify a lower bound for transit time.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>maxValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The maximum number of days. The value must be a non-negative, whole number.</p>
</td>
</tr>
<tr>
<td><code>minValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The minimum number of days, if applicable. The value must be a non-negative, whole number.</p>
</td>
</tr>
<tr>
<td><code>unitCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The transit time unit. The value must be <code>DAY</code> or <code>d</code>.</p>
</td>
</tr>
<tr>
<td><code>value</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The exact number of transit days, if known. The value must be a non-negative, whole number.
                If provided, <code>minValue</code> and <code>maxValue</code> must not be specified.
              </p>
</td>
</tr>
</tbody>
</table>

#### `QuantitativeValue` (in the context of shipping packing dimensions)

In the context of `ShippingConditions`, use the `QuantitativeValue` type to represent ranges of values of shipping packing dimensions (`weight` and `numItems`) for which a particular shipping rate and transit time apply. Either the `minValue` or `maxValue` property must be provided. The `minValue` property defaults to 0 and the `maxValue` property defaults to infinity when not provided.

> You can also use the `QuantitativeValue` type to specify handling times under the `ShippingService` type as well as transit times under the `ShippingConditions` type. For more information, see [`QuantitativeValue` for handling times](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#handling-time-quantitative-value-properties) and [`QuantitativeValue` for transit times](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#transit-time-quantitative-value-properties).

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>maxValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The maximum number for the dimension (<code>weight</code> or <code>numItems</code>), if applicable.
                 Defaults to infinity when not provided.
              </p>
</td>
</tr>
<tr>
<td><code>minValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The minimum number for the dimension (<code>weight</code> or <code>numItems</code>), if applicable.
                Must be less than <code>maxValue</code>. Defaults to 0 when not provided.</p>
</td>
</tr>
<tr>
<td><code>unitCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A unit relevant to the dimension (<code>weight</code> or <code>numItems</code>), if applicable.
                in UN/CEFACT Common Code (three characters) format:
                <ul>
<li>For weight units, the value must be <code>LBR</code> (pound) or <code>KGM</code> (kilogram)</li>
<li>For number of items, <code>unitCode</code> can be omitted. Alternatively, you can use UN/CEFACT Common Code name <code>H87</code>.</li>
</ul>
</p></td>
</tr>
</tbody>
</table>

#### `MonetaryAmount` (in the context of shipping conditions)

In the context of shipping conditions, use the `MonetaryAmount` type to represent ranges of order values for which a particular shipping rate and delivery time apply. Either the `minValue` or `maxValue` property must be provided. When not provided, the `minValue` property defaults to 0 and the `maxValue` property defaults to infinity. Note that you can also use the `MonetaryAmount` type in a different format to [specify shipping costs](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#shipping-monetary-amount-properties).

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>currency</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The currency code for the order value in <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format.</p>
</td>
</tr>
<tr>
<td><code>maxValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The maximum value of the order. Defaults to infinity when not provided.</p>
</td>
</tr>
<tr>
<td><code>minValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The minimum value of the order. Defaults to 0 when not provided.</p>
</td>
</tr>
</tbody>
</table>

#### `MonetaryAmount` (in the context of shipping rate)

In the context of shipping rates, use the `MonetaryAmount` type to specify a specific or maximum shipping rate for a given shipping condition. You can use the `MonetaryAmount` type as a simpler alternative to the more complex `ShippingRateSettings` and it can be used when you just need to specify a specific or maximum shipping rate. Either the `maxValue` or `value` property must be provided together with the `currency` property.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>currency</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The currency code for the shipping cost in <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format.</p>
</td>
</tr>
<tr>
<td><code>maxValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The maximum shipping cost for the given shipping condition. If you specify the
                <code>maxValue</code> property, don't specify the <code>value</code> property.</p>
</td>
</tr>
<tr>
<td><code>value</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The fixed shipping cost for the given shipping condition. For free shipping, use <code>0</code> as the value.</p>
</td>
</tr>
</tbody>
</table>

#### `ShippingRateSettings` (in the context of shipping rate)

In the context of shipping rates, use the `ShippingRateSettings` type to specify the shipping rate for a given shipping condition as a percentage of the order value or weight of the ordered goods. Either the `orderPercentage` or `weightPercentage` property must be provided when using the `ShippingRateSettings` type.

> The `MonetaryAmount` type is a simpler alternative to the more complex `ShippingRateSettings` type, and can be used when you just need to specify a fixed shipping rate.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>orderPercentage</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The shipping cost for the given shipping condition as a fraction of the order value.
                 Use a value between <code>0</code> and <code>1</code>.</p>
</td>
</tr>
<tr>
<td><code>weightPercentage</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The shipping cost for the given shipping condition as a fraction of the weight of the shipped goods.
                 Use a value between <code>0</code> and <code>1</code>.</p>
</td>
</tr>
</tbody>
</table>

#### `OpeningHoursSpecification` (in the context of seasonal shipping overrides)

In the context of shipping conditions, use the `OpeningHoursSpecification` type to represent when the condition is valid, for example due to seasonal holidays. At least one of the `validFrom` and `validThrough` properties must be provided when using the `OpeningHoursSpecification` type.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>validFrom</code></td>
<td>
<p><code><a href="https://schema.org/Date">Date</a></code></p>
<p>The first date when the shipping condition is valid, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.</p>
</td>
</tr>
<tr>
<td><code>validThrough</code></td>
<td>
<p><code><a href="https://schema.org/Date">Date</a></code></p>
<p>The last date when the shipping condition is valid, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.</p>
</td>
</tr>
</tbody>
</table>

## Alternative approach to configuring shipping settings with Google

Retailer shipping policies can get complicated and may change frequently. If you're having trouble indicating and keeping your shipping details up-to-date with markup and have a Google Merchant Center account, consider configuring your [delivery settings](https://support.google.com/merchants/answer/12577710) in Google Merchant Center. You can alternatively configure account-level [shipping policies in Search Console](https://support.google.com/webmasters/answer/14907594), which get automatically added to Merchant Center.

### Combining multiple shipping configurations

If you're combining various shipping configurations, keep in mind how you can override your policy information based on the order of precedence. For example, if you provide both shipping policy markup on your site and shipping policy settings in Search Console, Google will only use the information provided in Search Console.

Google uses the following order of precedence (from strongest to weakest):

- Content API for Shopping ([account level shipping settings](https://developers.google.com/shopping-content/guides/how-tos/account-level-tax-shipping))
- Settings in [Merchant Center](https://support.google.com/merchants/answer/12577710) or [Search Console](https://support.google.com/webmasters/answer/14907594)
- [Product-level merchant listing markup](/appearance/structured-data/merchant-listing.md)
- Organization-level markup

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/shipping-policy/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-shipping-policy]: Google Search Central (2026). "Merchant shipping policy (ShippingService) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/shipping-policy. Retrieved 2026-09-01.
