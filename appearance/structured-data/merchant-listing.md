---
type: Reference
title: Merchant listing (Product, Offer) structured data
description: Discover how you can add merchant listing structured data to attract potential buyers while they are searching for items to purchase on Google.
resource: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:55:35Z'
sources:
- id: google-merchant-listing
  resource: https://developers.google.com/search/docs/appearance/structured-data/merchant-listing
  title: Merchant listing (Product, Offer) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-07-07T00:00:00Z'
---

# Merchant listing (Product, Offer) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/merchant-listing](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-07-07.[^google-merchant-listing]

![shopping knowledge panel presentation in search results](https://developers.google.com/static/search/docs/images/shopping-knowledge-panel.png)

When you add `Product` markup to your page, it can be eligible for display in merchant listing experiences on Google Search, including the shopping knowledge panel, Google Images, popular product results, and product snippets. Merchant listings can highlight more specific data about a product, such as its price, availability, and shipping and return information.

This guide focuses on the `Product` structured data requirements for merchant listings. If you're not sure which markup to use, read our [intro to `Product` markup](/appearance/structured-data/product.md).

> **Do you have editorial product review pages?** Consider adding [product snippet markup](/appearance/structured-data/product-snippet.md).

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

The following examples illustrate how to include structured data on your web pages for different situations.

### Product page with an offer

Here's an example of a product page selling a product, with product reviews.

#### JSON-LD

  

``` devsite-click-to-copy
 <html>
  <head>
    <title>Executive Anvil</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Product",
      "name": "Executive Anvil",
      "image": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "description": "Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height.",
      "sku": "0446310786",
      "mpn": "925872",
      "brand": {
        "@type": "Brand",
        "name": "ACME"
      },
      "review": {
        "@type": "Review",
        "reviewRating": {
          "@type": "Rating",
          "ratingValue": 4,
          "bestRating": 5
        },
        "author": {
          "@type": "Person",
          "name": "Fred Benson"
        }
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 4.4,
        "reviewCount": 89
      },
      "offers": {
        "@type": "Offer",
        "url": "https://example.com/anvil",
        "priceCurrency": "USD",
        "price": 119.99,
        "priceValidUntil": "2024-11-20",
        "itemCondition": "https://schema.org/UsedCondition",
        "availability": "https://schema.org/InStock"
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

#### RDFa

  

``` devsite-click-to-copy
 <html>
  <head>
    <title>Executive Anvil</title>
  </head>
  <body>
    <div typeof="schema:Product">
        <div rel="schema:review">
          <div typeof="schema:Review">
            <div rel="schema:reviewRating">
              <div typeof="schema:Rating">
                <div property="schema:ratingValue" content="4"></div>
                <div property="schema:bestRating" content="5"></div>
              </div>
            </div>
            <div rel="schema:author">
              <div typeof="schema:Person">
                <div property="schema:name" content="Fred Benson"></div>
              </div>
            </div>
          </div>
        </div>
        <div rel="schema:image" resource="https://example.com/photos/4x3/photo.jpg"></div>
        <div property="schema:mpn" content="925872"></div>
        <div property="schema:name" content="Executive Anvil"></div>
        <div property="schema:description" content="Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height."></div>
        <div rel="schema:image" resource="https://example.com/photos/1x1/photo.jpg"></div>
        <div rel="schema:brand">
          <div typeof="schema:Brand">
            <div property="schema:name" content="ACME"></div>
          </div>
        </div>
        <div rel="schema:aggregateRating">
          <div typeof="schema:AggregateRating">
            <div property="schema:reviewCount" content="89"></div>
            <div property="schema:ratingValue" content="4.4"></div>
          </div>
        </div>
        <div rel="schema:offers">
          <div typeof="schema:Offer">
            <div property="schema:price" content="119.99"></div>
            <div property="schema:availability" content="https://schema.org/InStock"></div>
            <div property="schema:priceCurrency" content="USD"></div>
            <div property="schema:priceValidUntil" datatype="xsd:date" content="2024-11-20"></div>
            <div rel="schema:url" resource="https://example.com/anvil"></div>
            <div property="schema:itemCondition" content="https://schema.org/UsedCondition"></div>
          </div>
        </div>
        <div rel="schema:image" resource="https://example.com/photos/16x9/photo.jpg"></div>
        <div property="schema:sku" content="0446310786"></div>
      </div>
  </body>
</html>
```

#### Microdata

  

``` devsite-click-to-copy
 <html>
  <head>
    <title>Executive Anvil</title>
  </head>
  <body>
  <div>
    <div itemtype="https://schema.org/Product" itemscope>
      <meta itemprop="mpn" content="925872" />
      <meta itemprop="name" content="Executive Anvil" />
      <link itemprop="image" href="https://example.com/photos/16x9/photo.jpg" />
      <link itemprop="image" href="https://example.com/photos/4x3/photo.jpg" />
      <link itemprop="image" href="https://example.com/photos/1x1/photo.jpg" />
      <meta itemprop="description" content="Sleeker than ACME's Classic Anvil, the Executive Anvil is perfect for the business traveler looking for something to drop from a height." />
      <div itemprop="offers" itemtype="https://schema.org/Offer" itemscope>
        <link itemprop="url" href="https://example.com/anvil" />
        <meta itemprop="availability" content="https://schema.org/InStock" />
        <meta itemprop="priceCurrency" content="USD" />
        <meta itemprop="itemCondition" content="https://schema.org/UsedCondition" />
        <meta itemprop="price" content="119.99" />
        <meta itemprop="priceValidUntil" content="2024-11-20" />
      </div>
      <div itemprop="aggregateRating" itemtype="https://schema.org/AggregateRating" itemscope>
        <meta itemprop="reviewCount" content="89" />
        <meta itemprop="ratingValue" content="4.4" />
      </div>
      <div itemprop="review" itemtype="https://schema.org/Review" itemscope>
        <div itemprop="author" itemtype="https://schema.org/Person" itemscope>
          <meta itemprop="name" content="Fred Benson" />
        </div>
        <div itemprop="reviewRating" itemtype="https://schema.org/Rating" itemscope>
          <meta itemprop="ratingValue" content="4" />
          <meta itemprop="bestRating" content="5" />
        </div>
      </div>
      <meta itemprop="sku" content="0446310786" />
      <div itemprop="brand" itemtype="https://schema.org/Brand" itemscope>
        <meta itemprop="name" content="ACME" />
      </div>
    </div>
  </div>
  </body>
</html>
```

### Pricing

Google recognizes three kinds of prices:

Active price  
The price at which the product is currently offered.

Strikethrough price  
During a sale, the higher regular price at which the product is normally offered. It may be displayed as a struck-through price to draw attention to a lowered active price.

Member price  
The price at which the product is offered to a member of a particular loyalty program.

These prices are encoded using price specifications under the `Offer` object (with the exception of the active price, which can also be encoded at the offer level). The respective price specifications are identified by the price specification properties `priceType` and `validForMemberTier`, which must not be used together:

- Active prices have neither a `priceType` nor a `validForMemberTier` property.
- Strikethrough prices set the `priceType` property to `StrikethroughPrice` (for a transition period, `ListPrice` is also allowed) and cannot have a `validForMemberTier` property.
- Member prices are marked with a `validForMemberTier` property and cannot have a `priceType` property.

Price specifications containing both of these properties are ignored.

### Active price

Here are two examples of encoding the active price in JSON-LD. The active price can be specified using the `price` property as follows:

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "price": 10.00,
  "priceCurrency": "USD",
  ...
}
```

Alternatively, the active price can be specified using the `priceSpecification` property.

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "price": 10.00,
    "priceCurrency": "USD"
  },
  ...
}
```

> If you use both the `offers.price` and `offers.priceSpecification` properties to encode an active price, Google will use the price provided through the `offers.price` property and ignore the `offers.priceSpecification` property.

### Sale pricing

The following example shows a product with a sale price. The current, active price automatically becomes a sale price when you provide a second price with the original, strikethrough price and mark it with a [`priceType`](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#pricetype) property of value `https://schema.org/StrikethroughPrice`. Don't mark the active price with a `priceType` property.

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Nice trinket",
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/trinket_offer",
    "price": 10.00,
    "priceCurrency": "GBP",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "priceType": "https://schema.org/StrikethroughPrice",
      "price": 15.00,
      "priceCurrency": "GBP"
    }
  }
}
```

Alternatively, you can use two `UnitPriceSpecification` objects to specify the sale price and the strikethrough price:

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Nice trinket",
  "offers": {
    "@type": "Offer",
    "priceSpecification": [
      {
        "@type": "UnitPriceSpecification",
        "price": 10.00,
        "priceCurrency": "GBP"
      },
      {
        "@type": "UnitPriceSpecification",
        "priceType": "https://schema.org/StrikethroughPrice",
        "price": 15.00,
        "priceCurrency": "GBP"
      }
    ]
  }
}
```

### Sale duration

To specify the period when a sale price is active, use the following schema.org properties in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (for example, `2025-12-31T23:59:59+01:00`):

- **Start date and time:** Use the [`validFrom`](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#validFrom) property.
- **End date and time:** Use *either* the [`validThrough`](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#validThrough) property *or* the [`priceValidUntil`](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#priceValidUntil) property.

#### Best practices:

- Provide both a start and an end date/time to clearly define the sale period.
- Ensure the start date/time (from the `validFrom` property) is earlier than or equal to the end date/time (from the `validThrough` property or the `priceValidUntil` property).
- We recommend including the time and timezone in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format for accuracy in Google systems.

#### Where to place the properties:

- **On the `Offer` node:** You can add the `validFrom` property and (the `validThrough` property or the `priceValidUntil` property) directly to the `Offer` node. These dates apply when the `price` property on the `Offer` node represents the current active sale price.
- **On a `PriceSpecification` node:** If the sale price is defined within a `PriceSpecification` node (typically one without the `priceType` property when a `StrikethroughPrice` value is also present), add the `validFrom` property and the `validThrough` property to that specific `PriceSpecification` node. Note that the `priceValidUntil` property isn't applicable to the `PriceSpecification` type.

The following example shows a product with a sale price. The duration properties are added to the `Offer` node, as the `price` property on the `Offer` node holds the sale price.

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Nice trinket",
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/trinket_offer",
    "price": 10.00,
    "priceCurrency": "GBP",
    "validFrom": "2025-11-20T08:00:00+00:00",
    "priceValidUntil": "2025-11-30T23:59:59+00:00",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "priceType": "https://schema.org/StrikethroughPrice",
      "price": 15.00,
      "priceCurrency": "GBP"
    }
  }
}
```

Alternatively, you can use two `UnitPriceSpecification` objects to specify the sale price and the strikethrough price. The duration properties are added to the `UnitPriceSpecification` object that contains the sale price:

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "Nice trinket",
  "offers": {
    "@type": "Offer",
    "priceSpecification": [
      {
        "@type": "UnitPriceSpecification",
        "price": 10.00,
        "priceCurrency": "GBP",
        "validFrom": "2025-11-20T08:00:00+00:00",
        "validThrough": "2025-11-30T23:59:59+00:00"
      },
      {
        "@type": "UnitPriceSpecification",
        "priceType": "https://schema.org/StrikethroughPrice",
        "price": 15.00,
        "priceCurrency": "GBP"
      }
    ]
  }
}
```

### Member prices

Here are four examples of encoding a member price. In the first example, the active price is specified with the `price` property at the offer level, and the member price is given in a price specification marked with the [`validForMemberTier`](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#validForMemberTier) property:

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "url": "https://www.example.com/trinket_offer",
  "price": 10.00,
  "priceCurrency": "GBP",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "price": 8.00,
    "priceCurrency": "GBP",
    "validForMemberTier": {
      "@type": "MemberProgramTier",
      "@id": "https://www.example.com/com/members#tier_gold"
    }
  }
}
```

The second example shows both the active price and the member price encoded with price specifications:

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "url": "https://www.example.com/trinket_offer",
  "priceSpecification": [
    {
      "@type": "UnitPriceSpecification",
      "price": 10.00,
      "priceCurrency": "GBP"
    },
    {
      "@type": "UnitPriceSpecification",
      "price": 8.00,
      "priceCurrency": "GBP",
      "validForMemberTier": {
        "@type": "MemberProgramTier",
        "@id": "https://www.example.com/com/members#tier_gold"
      }
    }
  ]
}
```

The third example demonstrates how to encode a sale price, a strikethrough price, and member prices for several loyalty program tiers in a single offer:

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "url": "https://www.example.com/trinket_offer",
  "priceSpecification": [
    {
      "@type": "UnitPriceSpecification",
      "price": 9.00,
      "priceCurrency": "GBP"
    },
    {
      "@type": "UnitPriceSpecification",
      "priceType": "https://schema.org/StrikethroughPrice",
      "price": 10.00,
      "priceCurrency": "GBP"
    },
    {
      "@type": "UnitPriceSpecification",
      "price": 8.00,
      "priceCurrency": "GBP",
      "validForMemberTier": {
        "@type": "MemberProgramTier",
        "@id": "https://www.example.com/com/members#tier_silver"
      }
    },
    {
      "@type": "UnitPriceSpecification",
      "price": 7.00,
      "priceCurrency": "GBP",
      "validForMemberTier": [
        {
          "@type": "MemberProgramTier",
          "@id": "https://www.example.com/com/members#tier_gold"
        },
        {
          "@type": "MemberProgramTier",
          "@id": "https://www.example.com/com/members#tier_platinum"
        }
      ]
    }
  ]
}
```

The active price could also be encoded at the offer level, as shown in the first example.

In the fourth example, the member price specification shows membership points instead of a member price:

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "url": "https://www.example.com/trinket_offer",
  "price": 10.00,
  "priceCurrency": "GBP",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "membershipPointsEarned": 20,
    "validForMemberTier": {
      "@type": "MemberProgramTier",
      "@id": "https://www.example.com/com/members#tier_gold"
    }
  }
}
```

### Pricing with unit pricing measures

Here is an example of how to specify a price for 200 ml of a product that is customarily sold in multiples of 100 ml. For example, if you were selling a 200 ml bottle of perfume, you could show customers how much your perfume costs per 100 ml. The following example shows that the perfume costs €100 per 100 ml, which means a 200 ml bottle of perfume would cost €200. This form of pricing is particularly important in the EU, New Zealand, and Australia for products sold by volume, length, or weight.

When the [unit pricing measure](https://support.google.com/merchants/answer/6324455) and [unit pricing base measure](https://support.google.com/merchants/answer/6324490) are present, specify the active price inside a `UnitPriceSpecification` and use the [`referenceQuantity`](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#referenceQuantity) property to provide the unit pricing.

``` devsite-click-to-copy
"offers": {
  "@type": "Offer",
  "url": "https://www.example.com/perfume_offer",
  "priceSpecification": {
    "@type": "UnitPriceSpecification",
    "price": 200.00,
    "priceCurrency": "EUR",
    "referenceQuantity": {
      "@type": "QuantitativeValue",
      "value": "200",
      "unitCode": "ML",
      "valueReference": {
        "@type": "QuantitativeValue",
        "value": "100",
        "unitCode": "ML"
      }
    }
  }
}
```

### Shipping details

Here's an example of a product page with shipping details. This example would result in a shipping rate of \$3.49 for all users that live in the US. For more examples, review the [Shipping](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#shipping) section.

#### JSON-LD

  

``` devsite-click-to-copy
 <html>
  <head>
    <title>Nice trinket</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "Product",
      "sku": "trinket-12345",
      "gtin14": "00012345600012",
      "image": [
        "https://example.com/photos/16x9/trinket.jpg",
        "https://example.com/photos/4x3/trinket.jpg",
        "https://example.com/photos/1x1/trinket.jpg"
      ],
      "name": "Nice trinket",
      "description": "Trinket with clean lines",
      "brand": {
        "@type": "Brand",
        "name": "MyBrand"
      },
      "offers": {
        "@type": "Offer",
        "url": "https://www.example.com/trinket_offer",
        "itemCondition": "https://schema.org/NewCondition",
        "availability": "https://schema.org/InStock",
        "price": 39.99,
        "priceCurrency": "USD",
        "priceValidUntil": "2024-11-20",
        "shippingDetails": {
          "@type": "OfferShippingDetails",
          "shippingRate": {
            "@type": "MonetaryAmount",
            "value": 3.49,
            "currency": "USD"
          },
          "shippingDestination": {
            "@type": "DefinedRegion",
            "addressCountry": "US"
          },
          "deliveryTime": {
            "@type": "ShippingDeliveryTime",
            "handlingTime": {
              "@type": "QuantitativeValue",
              "minValue": 0,
              "maxValue": 1,
              "unitCode": "DAY"
            },
            "transitTime": {
              "@type": "QuantitativeValue",
              "minValue": 1,
              "maxValue": 5,
              "unitCode": "DAY"
            }
          }
        }
      },
      "review": {
        "@type": "Review",
          "reviewRating": {
            "@type": "Rating",
            "ratingValue": 4,
            "bestRating": 5
          },
          "author": {
            "@type": "Person",
            "name": "Fred Benson"
          }
        },
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": 4.4,
          "reviewCount": 89
        }
      }
    </script>
  </head>
  <body>
  </body>
</html>
```

#### RDFa

  

``` devsite-click-to-copy
 <html>
  <head>
    <title>Nice trinket</title>
  </head>
  <body>
    <div typeof="schema:Product">
      <div property="schema:sku" content="trinket-12345"></div>
      <div property="schema:gtin14" content="00012345600012"></div>
      <div property="schema:name" content="Nice trinket"></div>
      <div rel="schema:image" resource="https://example.com/photos/16x9/trinket.jpg"></div>
      <div rel="schema:image" resource="https://example.com/photos/4x3/trinket.jpg"></div>
      <div rel="schema:image" resource="https://example.com/photos/1x1/trinket.jpg"></div>
      <div property="schema:description" content="Trinket with clean lines"></div>
      <div rel="schema:brand">
        <div typeof="schema:Brand">
          <div property="schema:name" content="MyBrand"></div>
        </div>
      </div>
      <div rel="schema:offers">
        <div typeof="schema:Offer">
          <div rel="schema:url" resource="https://example.com/trinket_offer"></div>
          <div property="schema:itemCondition" content="https://schema.org/NewCondition"></div>
          <div property="schema:availability" content="https://schema.org/InStock"></div>
          <div property="schema:price" content="39.99"></div>
          <div property="schema:priceCurrency" content="USD"></div>
          <div property="schema:priceValidUntil" datatype="xsd:date" content="2024-11-20"></div>
          <div rel="schema:shippingDetails">
            <div typeof="schema:OfferShippingDetails">
              <div rel="schema:shippingRate">
                <div typeof="schema:MonetaryAmount">
                  <div property="schema:value" content="3.49"></div>
                  <div property="schema:currency" content="USD"></div>
                </div>
              </div>
              <div rel="schema:shippingDestination">
                <div typeof="schema:DefinedRegion">
                  <div property="schema:addressCountry" content="US"></div>
                </div>
              </div>
              <div rel="schema:deliveryTime">
                <div typeof="schema:ShippingDeliveryTime">
                  <div rel="schema:handlingTime">
                    <div typeof="schema:QuantitativeValue">
                      <div property="schema:minValue" content="0"></div>
                      <div property="schema:maxValue" content="1"></div>
                      <div property="schema:unitCode" content="DAY"></div>
                    </div>
                  </div>
                  <div rel="schema:transitTime">
                    <div typeof="schema:QuantitativeValue">
                      <div property="schema:minValue" content="1"></div>
                      <div property="schema:maxValue" content="5"></div>
                      <div property="schema:unitCode" content="DAY"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div rel="schema:review">
        <div typeof="schema:Review">
          <div rel="schema:reviewRating">
            <div typeof="schema:Rating">
              <div property="schema:ratingValue" content="4"></div>
              <div property="schema:bestRating" content="5"></div>
            </div>
          </div>
          <div rel="schema:author">
            <div typeof="schema:Person">
              <div property="schema:name" content="Fred Benson"></div>
            </div>
          </div>
        </div>
      </div>
      <div rel="schema:aggregateRating">
        <div typeof="schema:AggregateRating">
          <div property="schema:reviewCount" content="89"></div>
          <div property="schema:ratingValue" content="4.4"></div>
        </div>
      </div>
    </div>
  </body>
</html>
```

#### Microdata

  

``` devsite-click-to-copy
 <html>
  <head>
    <title>Nice trinket</title>
  </head>
  <body>
  <div>
    <div itemtype="https://schema.org/Product" itemscope>
      <meta itemprop="sku" content="trinket-12345" />
      <meta itemprop="gtin14" content="00012345600012" />
      <meta itemprop="name" content="Nice trinket" />
      <link itemprop="image" href="https://example.com/photos/16x9/trinket.jpg" />
      <link itemprop="image" href="https://example.com/photos/4x3/trinket.jpg" />
      <link itemprop="image" href="https://example.com/photos/1x1/trinket.jpg" />
      <meta itemprop="description" content="Trinket with clean lines" />
      <div itemprop="brand" itemtype="https://schema.org/Brand" itemscope>
        <meta itemprop="name" content="MyBrand" />
      </div>
      <div itemprop="offers" itemtype="https://schema.org/Offer" itemscope>
        <link itemprop="url" href="https://www.example.com/trinket_offer" />
        <meta itemprop="itemCondition" content="https://schema.org/NewCondition" />
        <meta itemprop="availability" content="https://schema.org/InStock" />
        <meta itemprop="price" content="39.99" />
        <meta itemprop="priceCurrency" content="USD" />
        <meta itemprop="priceValidUntil" content="2024-11-20" />
        <div itemprop="shippingDetails" itemtype="https://schema.org/OfferShippingDetails" itemscope>
          <div itemprop="shippingRate" itemtype="https://schema.org/MonetaryAmount" itemscope>
            <meta itemprop="value" content="3.49" />
            <meta itemprop="currency" content="USD" />
          </div>
          <div itemprop="shippingDestination" itemtype="https://schema.org/DefinedRegion" itemscope>
            <meta itemprop="addressCountry" content="US" />
          </div>
          <div itemprop="deliveryTime" itemtype="https://schema.org/ShippingDeliveryTime" itemscope>
            <div itemprop="handlingTime" itemtype="https://schema.org/QuantitativeValue" itemscope>
              <meta itemprop="minValue" content="0" />
              <meta itemprop="maxValue" content="1" />
              <meta itemprop="unitCode" content="DAY" />
            </div>
            <div itemprop="transitTime" itemtype="https://schema.org/QuantitativeValue" itemscope>
              <meta itemprop="minValue" content="1" />
              <meta itemprop="maxValue" content="5" />
              <meta itemprop="unitCode" content="DAY" />
            </div>
          </div>
        </div>
      </div>
      <div itemprop="review" itemtype="https://schema.org/Review" itemscope>
        <div itemprop="author" itemtype="https://schema.org/Person" itemscope>
          <meta itemprop="name" content="Fred Benson" />
        </div>
        <div itemprop="reviewRating" itemtype="https://schema.org/Rating" itemscope>
          <meta itemprop="ratingValue" content="4" />
          <meta itemprop="bestRating" content="5" />
        </div>
      </div>
      <div itemprop="aggregateRating" itemtype="https://schema.org/AggregateRating" itemscope>
        <meta itemprop="reviewCount" content="89" />
        <meta itemprop="ratingValue" content="4.4" />
      </div>
    </div>
  </div>
  </body>
</html>
```

### Free shipping

Here's an example of providing free shipping to buyers in the US state of New York.

``` devsite-click-to-copy
"shippingDetails": {
  "@type": "OfferShippingDetails",
  "shippingRate": {
    "@type": "MonetaryAmount",
    "value": "0",
    "currency": "USD"
  },
  "shippingDestination": [
    {
      "@type": "DefinedRegion",
      "addressCountry": "US",
      "addressRegion": ["NY"]
    }
  ]
}
```

### Return details

Here is an example of a product page with return details. The markup matches a return policy that requires products sold in Switzerland to be returned by mail within 60 days and charges a return fee of 3.49 Swiss Francs.

> If you have a standard return policy that applies to most or all of your products, we recommend nesting the `MerchantReturnPolicy` markup under the `Organization` type, as documented under [merchant return policies](/appearance/structured-data/return-policy.md). Product-level return policies should only be used to override a standard merchant-level return policy or when there is no standard return policy as product-level return policies support only a subset of the properties available for merchant-level return policies.

``` devsite-click-to-copy
    {
      "@context": "https://schema.org/",
      "@type": "Product",
      "sku": "trinket-12345",
      "gtin14": "00012345600012",
      "image": [
        "https://example.com/photos/16x9/trinket.jpg",
        "https://example.com/photos/4x3/trinket.jpg",
        "https://example.com/photos/1x1/trinket.jpg"
      ],
      "name": "Nice trinket",
      "description": "Trinket with clean lines",
      "brand": {
        "@type": "Brand",
        "name": "MyBrand"
      },
      "offers": {
        "@type": "Offer",
        "url": "https://www.example.com/trinket_offer",
        "itemCondition": "https://schema.org/NewCondition",
        "availability": "https://schema.org/InStock",
        "priceSpecification": {
          "@type": "PriceSpecification",
          "price": 39.99,
          "priceCurrency": "CHF"
        },
        "hasMerchantReturnPolicy": {
          "@type": "MerchantReturnPolicy",
          "applicableCountry": "CH",
          "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 60,
          "returnMethod": "https://schema.org/ReturnByMail",
          "returnFees": "https://schema.org/ReturnShippingFees",
          "returnShippingFeesAmount": {
            "@type": "MonetaryAmount",
            "value": 3.49,
            "currency": "CHF"
          }
        }
      }
    }
  
```

### Certifications

The following examples illustrate how to specify certification information using structured data. The first example specifies the German CO2 emissions class "D" for a vehicle.

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "sku": "1234-5678",
  "image": "https://www.example.com/vehicle.jpg",
  "name": "Big Car",
  "description": "Passenger vehicle with combustion engine",
  "gtin14": "00012345600012",
  "mpn": "WH1234",
  "brand": {
    "@type": "Brand",
    "name": "ExampleCarBrand"
  },
  "hasCertification": {
    "@type": "Certification",
    "issuedBy": {
      "@type": "Organization",
      "name": "BMWK"
    },
    "name": "Vehicle_CO2_Class",
    "certificationRating": {
      "@type": "Rating",
      "ratingValue": "D"
    }
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/vehicle",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock",
    "price": 17999.00,
    "priceCurrency": "EUR"
  }
}
```

The second example specifies an EPREL energy efficiency label for an LED:

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "sku": "1234-5678",
  "image": "https://www.example.com/led.jpg",
  "name": "LED",
  "description": "Dimmable LED",
  "gtin14": "00012345600012",
  "mpn": "WH1234",
  "brand": {
    "@type": "Brand",
    "name": "ExampleLightingBrand"
  },
  "hasCertification": {
    "@type": "Certification",
    "issuedBy": {
      "@type": "Organization",
      "name": "European_Commission"
    },
    "name": "EPREL",
    "certificationIdentification": "123456"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/led",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock",
    "price": 2.30,
    "priceCurrency": "EUR"
  }
}
```

### 3D model

This example shows how to link a 3D model to a product with the `subjectOf` property and the `3DModel` type.

``` devsite-click-to-copy
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "sku": "1234-5678",
  "image": "https://www.example.com/sofa.jpg",
  "name": "Water heater",
  "description": "White 3-Seat Sofa",
  "gtin14": "00012345600012",
  "mpn": "S1234W3",
  "brand": {
    "@type": "Brand",
    "name": "ExampleSofaBrand"
  },
  "subjectOf": {
    "@type": "3DModel",
    "encoding": {
      "@type": "MediaObject",
      "contentUrl": "https://example.com/sofa.gltf"
    }
  },
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/whitechaiselongue",
    "itemCondition": "https://schema.org/NewCondition",
    "availability": "https://schema.org/InStock",
    "price": 1299.00,
    "priceCurrency": "USD"
  }
}
```

## Guidelines

For your `Product` markup to be eligible for merchant listing experiences, you must follow these guidelines:

- [General structured data guidelines](/appearance/structured-data/sd-policies.md)
- [Search Essentials](/essentials/overview.md)
- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#technical-guidelines)
- [Content guidelines](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#content-guidelines)
- [Free listings guidelines](https://support.google.com/merchants/answer/12073010) (for merchant listing experiences)

### Technical guidelines

Only pages where a shopper can purchase a product are eligible for merchant listing experiences, not pages with links to other sites that sell the product. Google may attempt to verify merchant listing product data before showing the information in search results.

Product rich results only support pages that focus on a single product (or multiple variants of the same product). For example, "shoes in our shop" is not a specific product. This includes product variants where [each product variant has a distinct URL](/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites.md). We recommend focusing on adding markup to product pages instead of pages that list products or a category of products.

For details about how to mark up product variants, refer to [product variant structured data documentation](/appearance/structured-data/product-variants.md).

When offering products for sale in multiple currencies, have a distinct URL per currency. For example, if a product is available for sale in Canadian and US dollars, use two distinct URLs, one per currency.

[`Car`](https://schema.org/Car) isn't supported automatically as a subtype of Product. For now, include both [`Car`](https://schema.org/Car) and [`Product`](https://schema.org/Product) types if you want to attach ratings to it and be eligible for the Search feature. For example in JSON-LD:

``` devsite-click-to-copy
{
  "@context": "https://schema.org",
  "@type": ["Product", "Car"],
  ...
}
    
```

If you're a merchant optimizing for all types of shopping results, we recommend putting `Product` structured data in the initial HTML for best results.

**For JavaScript-generated `Product` markup**: Be aware that [dynamically-generated markup](/appearance/structured-data/generate-structured-data-with-javascript.md) can make Shopping crawls less frequent and less reliable, which can be an issue for fast-changing content like product availability and price. If you're using JavaScript to generate `Product` markup, make sure your server has enough computing resources to handle increased traffic from Google.

### Content guidelines

- We don't allow content that promotes widely prohibited or regulated goods, services, or information that may facilitate serious, immediate, or long term harm to people. This includes content related to firearms and weapons, recreational drugs, tobacco and vaping products, and gambling-related products.

## Structured data type definitions

You must include the required properties for your content to be eligible for display as a rich result. You can also include the recommended properties to add more information to your structured data, which could provide a better user experience.

### Product information

#### `Product`

The full definition of `Product` is available at [schema.org/Product](https://schema.org/Product). When you mark up your content for product information, use the following properties of the `Product` type:

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The name of the product.</p>
</td>
</tr>
<tr>
<td><code>image</code></td>
<td>
<p>Repeated <code><a href="https://schema.org/ImageObject">ImageObject</a></code> or
                <code><a href="https://schema.org/URL">URL</a></code></p>
<p>The URL of a product photo. Pictures clearly showing the product (for example, against
                a white background) are preferred.</p>
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
<td><code>offers</code></td>
<td>
<p><code><a href="https://schema.org/Offer">Offer</a></code></p>
<p>A nested <code>Offer</code> to sell the product.</p>
<p>Product snippets accept an <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#offer-properties"><code>Offer</code></a>
                or <code>AggregateOffer</code>
                but merchant listings require an <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#offer-properties"><code>Offer</code></a>
                as the merchant has to be the seller of the product in order to be eligible
                for merchant listing experiences.
              </p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>aggregateRating</code></td>
<td>
<p><code><a href="https://schema.org/AggregateRating">AggregateRating</a></code></p>
<p>A nested <code>aggregateRating</code> of the product. Follow the
                <a href="/appearance/structured-data/review-snippet.md">Review snippet guidelines</a>
                and the list of required and recommended
                <a href="/appearance/structured-data/review-snippet.md"><code>AggregateRating</code> properties</a>.</p>
</td>
</tr>
<tr>
<td><code>audience</code></td>
<td>
<p><code><a href="https://schema.org/PeopleAudience">PeopleAudience</a></code></p>
<p>Optional information about the suggested audience for the product, such as the
                suggested gender and age group. Only the <code>PeopleAudience</code> type is supported.
                See the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#people-audience-properties"><code>PeopleAudience</code> properties</a>
                supported by Google.</p>
</td>
</tr>
<tr>
<td><code>brand.name</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Include the brand of the product in the
                <code><a href="https://schema.org/PeopleAudience">name</a></code>
                property of the
                <code><a href="https://schema.org/Brand">Brand</a></code>
                type if known. Include at most one brand name.</p>
</td>
</tr>
<tr>
<td><code>category</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/CategoryCode">CategoryCode</a></code></p>
<p>Specifies the product's categories. This property can accept an array of values, mixing plain text strings and <code>CategoryCode</code> objects.</p>
<ul>
<li><strong>Custom product types:</strong> Plain <code>Text</code> values represent your custom product category, similar to the <a href="https://support.google.com/merchants/answer/6324406"><code>product_type</code> attribute</a> in product feeds. We recommend keeping custom product types under the 750-character limit.</li>
<li><strong>Google Product Category (GPC):</strong> To specify a GPC, similar to the <a href="https://support.google.com/merchants/answer/6324436"><code>google_product_category</code> attribute</a> in product feeds, use the <code>CategoryCode</code> type.
                  <ul>
<li>Set <code>@type</code> to <code>CategoryCode</code>.</li>
<li>Set <code>inCodeSet</code> to a Google Product Taxonomy URL (for example, <code>"https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt"</code>).</li>
<li>Set <code>codeValue</code> to the GPC ID (for example, <code>"2271"</code>) or the full category path (for example, <code>"Apparel &amp; Accessories &gt; Clothing &gt; Dresses"</code>).</li>
<li>When using the path format, use <code>&gt;</code> as the separator between levels. Each segment in the path must contain at least one letter. Numeric IDs are also accepted.</li>
</ul>
</li>
</ul>
<p>You can provide multiple category values. For example, you can include several GPC codes or paths and several custom product type strings.</p>
<pre class="devsite-click-to-copy">"category": [
  {
    "@type": "CategoryCode",
    "inCodeSet": "https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt",
    "codeValue": "2271"
  },
  {
    "@type": "CategoryCode",
    "inCodeSet": "https://www.google.com/basepages/producttype/taxonomy-with-ids.en-US.txt",
    "codeValue": "Apparel &amp; Accessories &gt; Clothing &gt; Dresses"
  },
  "Dresses",
  "Special Occasion &gt; Wedding &amp; Bridal Party Dresses"
]
              </pre>
</td>
</tr>
<tr>
<td><code>color</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The color or color combination of the product (for example, "red" or "yellow/sky blue").
                See also the
                <a href="https://support.google.com/merchants/answer/6324487">Color attribute</a>
                in Google Merchant Center Help.</p>
</td>
</tr>
<tr>
<td><code>description</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The product description. While the product description is not mandatory, it is strongly recommended to
                provide a description of the product in this property.</p>
</td>
</tr>
<tr>
<td><code>gtin | gtin8 | gtin12 | gtin13 | gtin14 | isbn</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Include all applicable global identifiers; these are described at
                <a href="https://schema.org/Product">schema.org/Product</a>.
                While you can use the generic <code>gtin</code> property for all GTINs, we recommend that you
                use the most specific GTIN that applies to your product, as this is the most accurate
                representation of the product. Make sure the GTIN value is in the numerical form; we don't
                support the URL form for GTINs.</p>
<p><code>isbn</code> is only a valid property on
              <code><a href="https://schema.org/Book">Book</a></code>. For
              best results, use ISBN-13 format. To use <code>Book</code> correctly, co-type with the
              <code>Product</code>. This will let you
              use properties of both types on the node. For example:</p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": ["Product", "Book"],
  ...
}
              </pre>
</td>
</tr>
<tr>
<td><code>hasAdultConsideration</code></td>
<td><p><code><a href="https://schema.org/AdultOrientedEnumeration">AdultOrientedEnumeration</a></code></p>
<p>Indicates that the product is designated as adult-oriented for example, because it
              contains nudity or sexual content. If you sell products that are considered adult-oriented according to Google's
              <a href="https://support.google.com/merchants/answer/12073010#res">adult-oriented content policy</a>,
              you must use this property to label them as adult-oriented. While these products
              are eligible to be shown in Shopping ads and free listings, they are subject to age- and
              country-based restrictions. Labelling them ensures that Google can apply these
              restrictions and show appropriate and legally compliant content to people shopping online.
              While schema.org defines multiple values for <code>AdultOrientedEnumeration</code>,
              Google Search only supports the value <code>https://schema.org/SexualContentConsideration</code> for this property.</p>
</td>
</tr>
<tr>
<td><code>hasCertification</code></td>
<td><p><code><a href="https://schema.org/Certification">Certification</a></code></p>
<p>Certifications, such as energy efficiency ratings, associated with a product. Up to
              10 certifications can be specified. This property is particularly relevant in
              European countries. See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#certification-properties"><code>Certification</code> properties</a>
              supported by Google.</p>
<blockquote>
<b>Backwards compatibility</b>: Upon the initial launch of merchant listing, we recommended
                  the <code>hasEnergyConsumptionDetails</code> property. While we continue to support the
                  earlier markup pattern, we recommend using the new <code>hasCertification</code> property
                  instead, if possible, with the required <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#certification-properties"><code>Certification</code> properties</a>
                  supported by Google. Here's an example that shows the original markup style:
                <pre>"hasEnergyConsumptionDetails": {
  <strong>"@type": "EnergyConsumptionDetails",</strong>
  "hasEnergyEfficiencyCategory": "https://schema.org/EUEnergyEfficiencyCategoryC",
  "energyEfficiencyScaleMin": "https://schema.org/EUEnergyEfficiencyCategoryF",
  "energyEfficiencyScaleMax": "https://schema.org/EUEnergyEfficiencyCategoryA1Plus"
}</pre>
</blockquote>
</td>
</tr>
<tr>
<td><code>inProductGroupWithID</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The ID of a product group that this product variant belongs to. See also
                <a href="https://support.google.com/merchants/answer/6324507"><code>Item Group Id</code></a>
                in Google Merchant Center Help. Specify at most one value.</p>
                For details on how to add markup for product variants, refer to
              <a href="/appearance/structured-data/product-variants.md">product variant structured data documentation</a>.
            </td>
</tr>
<tr>
<td><code>isVariantOf</code></td>
<td>
<p><code><a href="https://schema.org/ProductGroup">ProductGroup</a></code></p>
<p>A product group that this product variant belongs to, if applicable. For details on
                how to add markup for product variants, refer to
                <a href="/appearance/structured-data/product-variants.md">product variant structured data documentation</a>.
              </p>
</td>
</tr>
<tr>
<td><code>material</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The material or material combination the product is made from, such as "Leather"
                or "Cotton/Polyester". See also
                <code><a href="https://support.google.com/merchants/answer/6324410">Material</a></code>
                in Google Merchant Center help.</p>
</td>
</tr>
<tr>
<td><code>mpn</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The manufacturer part number. This property uniquely identifies the product
                for a given manufacturer.</p>
</td>
</tr>
<tr>
<td><code>pattern</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The pattern of the product, such as "polka dots" or "striped". See also
                <code><a href="https://support.google.com/merchants/answer/6324483">Pattern</a></code>
                on the Google Merchant Center Product Data Specification page.</p>
</td>
</tr>
<tr>
<td><code>review</code></td>
<td>
<p><code><a href="https://schema.org/Review">Review</a></code></p>
<p>A nested <code>Review</code> of the product. Follow the
                <a href="/appearance/structured-data/review-snippet.md">Review snippet
                  guidelines</a> and the list of required and recommended
                <a href="/appearance/structured-data/review-snippet.md">review properties</a>.
                See also the list of additional <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#/search/docs/appearance/structured-data/product-snippet#review-properties"><code>Review</code> properties</a>
                specific to the <code>Product</code> schema.org type.</p>
<p>If you add a review for the product, the reviewer's name must be a valid name for a <code>Person</code> or
                <code>Team</code>.</p>
<p><b>Not recommended</b>: 50% off on Black Friday</p>
<p><b>Recommended</b>: "James Smith" or "CNET Reviewers"</p>
</td>
</tr>
<tr>
<td><code>size</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/SizeSpecification">SizeSpecification</a></code></p>
<p>The size of the product, such as "XL" or "medium". See also <code>size</code> in the
                <a href="https://support.google.com/merchants/answer/7052112">Google Merchant Center Product Data Specification page</a>.
                See the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#size-specification-properties"><code>SizeSpecification</code> properties</a>
                supported by Google. Specify at most one value.</p>
</td>
</tr>
<tr>
<td><code>sku</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The merchant-specific identifier for the product. Specify at most one value.</p>
<ul>
<li>The <code>sku</code> value must use unicode characters that are valid for interchange.</li>
<li>The <code>sku</code> value must not contain any whitespace characters (as defined by
                  the <a href="https://en.wikipedia.org/wiki/Unicode_character_property#Whitespace">Unicode whitespace property</a>).</li>
<li>We recommend that the <code>sku</code> value only contain ASCII characters.</li>
</ul>
</td>
</tr>
<tr>
<td><code>subjectOf</code></td>
<td>
<p><code><a href="https://schema.org/3DModel">3DModel</a></code></p>
<p>A 3D model for the product, if applicable. See the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#3d-model-properties"><code>3DModel</code> properties</a> properties supported by Google. Specify at most one <code>3DModel</code> value.</p>
</td>
</tr>
</tbody>
</table>

#### `3DModel`

The full definition of `3DModel` is available at [`schema.org/3DModel`](https://schema.org/3DModel).

Use the following properties to link to a 3D model. Currently only models in [glTF](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html) format are supported.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>encoding</code></td>
<td>
<p><code><a href="https://schema.org/MediaObject">MediaObject</a></code></p>
<p>The media for the 3D model.</p>
</td>
</tr>
<tr>
<td><code>encoding.contentUrl</code></td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The link to a 3D model definition file in <a href="https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html">glTF</a> format. The file must have a <code>.gltf</code> or <code>.glb</code> suffix.</p>
</td>
</tr>
</tbody>
</table>

### Offer details

#### `Offer`

The full definition of `Offer` is available at [schema.org/Offer](https://schema.org/Offer). When marking up offers within a product, use the following properties of the `schema.org` [`Offer`](https://schema.org/Offer) type.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>price</code> or <code>priceSpecification.price</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The current, active offer price of a product. Follow the
            <a href="https://schema.org/price">schema.org usage
              guidelines</a>.</p>
<p>
            Here's an example of the <code>price</code> property:
          </p>
<pre class="devsite-click-to-copy devsite-code-highlight">"offers": {
  "@type": "Offer",
  <strong>"price": 39.99,</strong>
  "priceCurrency": "USD"
}
          </pre>
<p>
            Unlike product snippets, merchant listing experiences require a price greater than zero.
          </p>
<p>
            The active price is required but may be nested inside a
            <code>priceSpecification</code> property instead of being provided at the
            <code>Offer</code> level.
          </p>
<blockquote>
      If you use both the <code>offers.price</code> and <code>offers.priceSpecification</code>
      properties to encode an active price, Google will use the price provided through
      the <code>offers.price</code> property and ignore the <code>offers.priceSpecification</code>
      property.
    </blockquote>
</td>
</tr>
<tr>
<td><code>priceCurrency</code> or <code>priceSpecification.priceCurrency</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The currency used to describe the product price, in three-letter
            <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format.</p>
<p>
<code>priceCurrency</code> is required if <code>price</code> is specified, otherwise
            <code>priceSpecification.priceCurrency</code> is required if
            <code>priceSpecification.price</code> is specified.
          </p>
</td>
</tr>
<tr>
<td><code>priceSpecification</code></td>
<td>
<p><code><a href="https://schema.org/UnitPriceSpecification">UnitPriceSpecification</a></code></p>
<p>The active price can also be specified using <code>price</code>
          and <code>priceCurrency</code> inside a <code>priceSpecification</code> property.</p>
<blockquote>
      If you use both the <code>offers.price</code> and <code>offers.priceSpecification</code>
      properties to encode an active price, Google will use the price provided through
      the <code>offers.price</code> property and ignore the <code>offers.priceSpecification</code>
      property.
    </blockquote>
<p>The <code>priceSpecification</code> property allows the specification of complex prices
            by using <code>UnitPriceSpecification</code> objects. See the list of supported
            <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#unit-price-specification-properties"><code>UnitPriceSpecification</code></a>
            properties and the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#pricing-examples">pricing examples</a> of how to mark up
            various kinds of prices.</p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>availability</code></td>
<td>
<p><code><a href="https://schema.org/ItemAvailability">ItemAvailability</a></code></p>
<p>The possible product availability options. The short names without the URL prefix
            are also supported (for example <code>BackOrder</code>).</p>
<ul>
<li><code>https://schema.org/BackOrder</code>: The item is on back order.</li>
<li><code>https://schema.org/Discontinued</code>: The item has been discontinued.</li>
<li><code>https://schema.org/InStock</code>: The item is in stock.</li>
<li><code>https://schema.org/InStoreOnly</code>: The item is only available for purchase in store.</li>
<li><code>https://schema.org/LimitedAvailability</code>: The item has limited availability.</li>
<li><code>https://schema.org/OnlineOnly</code>: The item is available online only.</li>
<li><code>https://schema.org/OutOfStock</code>: The item is currently out of stock.</li>
<li><code>https://schema.org/PreOrder</code>: The item is available for pre-order.</li>
<li><code>https://schema.org/PreSale</code>: The item is available for ordering and delivery before general availability.</li>
<li><code>https://schema.org/SoldOut</code>: The item has been sold out.</li>
</ul>
<p>
            Don't specify more than one value.
          </p>
</td>
</tr>
<tr>
<td><code>hasMerchantReturnPolicy</code></td>
<td>
<p><code><a href="https://schema.org/MerchantReturnPolicy">MerchantReturnPolicy</a></code></p>
<p>Nested information about the return policies associated with an <code>Offer</code>.
            Add the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#merchant-return-policy-properties">required and recommended
              <code>MerchantReturnPolicy</code> properties</a> for individual offers.</p>

<blockquote>
            We recommend you provide a global return policy for your business under <code>Organization</code> markup instead,
            as documented under the <a href="/appearance/structured-data/organization.md">Organization documentation</a> and
            the <a href="/appearance/structured-data/return-policy.md">Merchant return policy documentation</a>.
            Only if some of your products have specific return policies for which you need to override your
            global return policy, or if you don't provide standard return policy for your business, use
            this property under <code>Offer</code>. Note that the
            properties supported for offer-level return policies are a subset of the properties
            supported for organization-level return policies.
            To unambiguously reference your global return policy (located on a different page) from an <code>Offer</code>,
            using only the <code>@id</code> keyword. For example:
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Offer",
  "hasMerchantReturnPolicy": {
    "@id": "https://example.com/returns#policy"
  }
}</pre>

</blockquote>
</td>
</tr>
<tr>
<td><code>itemCondition</code></td>
<td>
<p><code><a href="https://schema.org/OfferItemCondition">OfferItemCondition</a></code></p>
<p>Condition of the item offered for sale. The short names without the URL prefix
            are also supported (for example <code>NewCondition</code>).</p>
<ul>
<li><code>https://schema.org/NewCondition</code>: The item is new.</li>
<li><code>https://schema.org/RefurbishedCondition</code>: The item has been refurbished.</li>
<li><code>https://schema.org/UsedCondition</code>: The item is used (it is not new).</li>
</ul>
<p>
            Don't specify more than one value.
          </p>
</td>
</tr>
<tr>
<td><code>priceValidUntil</code></td>
<td>
<p><code><a href="https://schema.org/Date">Date</a></code></p>
<p>The date and time after which the price will no longer be available, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. Your listing may not display if the <code>priceValidUntil</code> property indicates a past date. For details and markup examples, see <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#sale-duration">Sale duration</a>.</p>
</td>
</tr>
<tr>
<td><code>shippingDetails</code></td>
<td>
<p><code><a href="https://schema.org/OfferShippingDetails">OfferShippingDetails</a></code></p>
<p>Nested information about the shipping policy associated with an
            <code>Offer</code>. If you decide to add <code>shippingDetails</code>, add
            the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#offer-shipping-details-properties">required and recommended
              <code>OfferShippingDetails</code> properties</a>.</p>
<blockquote>
            We recommend you provide a global shipping policy for your business under <code>Organization</code> markup instead,
            as documented under the <a href="/appearance/structured-data/organization.md">Organization documentation</a> and
            the <a href="/appearance/structured-data/shipping-policy.md">Merchant shipping policy documentation</a>.
            Only if some of your products have specific shipping policies for which you need to override your
            global shipping policy, or if you don't provide a standard shipping policy for your business, use
            this property under <code>Offer</code>. Note that the
            properties supported for offer-level shipping policies are a subset of the properties
            supported for organization-level shipping policies.
            To unambiguously reference your global shipping policy (located on a different page) from an <code>Offer</code>, use only
            the <code>hasShippingService</code> property under the <code>OfferShippingDetails</code> type
            using only the <code>@id</code> keyword. For example:
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Offer",
  "shippingDetails": {
    "@type": "OfferShippingDetails",
    "hasShippingService": {
      "@id": "https://example.com/shipping#policy"
    }
  }
}</pre>
</blockquote>
</td>
</tr>
<tr>
<td><code>url</code></td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>A URL of the product web page from which a shopper can purchase the product.
            This URL may be the preferred URL for the current page with all variant options
            appropriately selected. The URL can be omitted. Don't provide multiple URLs.</p>
<p>For details on how to add markup for product variants, refer to
            <a href="/appearance/structured-data/product-variants.md">product variant structured data documentation</a>.
          </p>
</td>
</tr>
<tr>
<td><code>validFrom</code></td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code> or <code><a href="https://schema.org/Date">Date</a></code></p>
<p>The start date and time when the price is valid, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. For details and markup examples, see <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#sale-duration">Sale duration</a>.</p>
</td>
</tr>
<tr>
<td><code>validThrough</code></td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code> or <code><a href="https://schema.org/Date">Date</a></code></p>
<p>The end date and time when the price is valid, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. For details and markup examples, see <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#sale-duration">Sale duration</a>.</p>
</td>
</tr>
</tbody>
</table>

#### `UnitPriceSpecification`

The full definition of `UnitPriceSpecification` is available at [`schema.org/UnitPriceSpecification`](https://schema.org/UnitPriceSpecification). Use the following properties to capture more complex pricing schemes.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>price</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>
                The offer price of a product. See also the <code>price</code> property of <code>Offer</code>.
              </p>
</td>
</tr>
<tr>
<td><code>priceCurrency</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The currency used to describe the product price, in three-letter
                <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format.
                See also the <code>priceCurrency</code> property of <code>Offer</code>.</p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>membershipPointsEarned</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<blockquote><b>Beta</b>: This property is in beta, and you may not see an
                effect in Google Search right away.</blockquote>
<p>The (whole) number of points that members of a particular loyalty program earn with
              this purchase. Use this property only together with <code>validForMemberTier</code>.
              See the fourth example in <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#member-price-example">member price examples</a>
              and the article <a href="https://support.google.com/merchants/answer/12922446">Loyalty program</a> in Google Merchant Center Help.</p>
              Refer to
              <a href="/appearance/structured-data/loyalty-program.md">loyalty program markup</a> for
                information on how to define member programs and tiers for your organization.
            </td>
</tr>
<tr>
<td><code>priceType</code></td>
<td>
<p>
<code><a href="https://schema.org/PriceTypeEnumeration">PriceTypeEnumeration</a></code>
</p>
<p>
                The presence of this property marks the full, original listing price of a product,
                if applicable. Only use this property if you want Google to show sale pricing for
                your product. You must set the <code>priceType</code> to
                the <code>https://schema.org/StrikethroughPrice</code> value (no other values are
                supported).
              </p>
<p>
                If you use the <code>priceType</code> property to designate a list price,
                you must also provide a current sale price with the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#price"><code>price</code></a> or
                <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#pricespecification"><code>priceSpecification</code></a> property on
                the <code>Offer</code> object. Don't mark the current sale price with
                the <code>priceType</code> property. See the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#sale-pricing-example">sale
                price examples</a>.
              </p>
</td>
</tr>
<tr>
<td><code>referenceQuantity</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code>
              (for unit pricing)</p>
<p>The quantity of the product offered for the given price. See the
              example <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#unit-pricing-example">Pricing with unit pricing measures</a> and the
              article <a href="https://support.google.com/merchants/answer/6324455">Unit pricing measure</a> in Google Merchant Center Help for a
              detailed discussion of unit pricing.</p>
</td>
</tr>
<tr>
<td><code>validForMemberTier</code></td>
<td>
<p>
<code><a href="https://schema.org/MemberProgramTier">MemberProgramTier</a></code>
</p>
<p>
                The presence of this property indicates that this price is valid for members of a
                particular loyalty program. You can specify multiple member tiers if
                the price is the same for them and multiple price specifications with this property
                if the price is different for different member tiers.
              </p>
<p>
                If you use the <code>validForMemberTier</code> property to designate a member price,
                you must also provide a current regular price with
                the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#price"><code>price</code></a> or
                <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#pricespecification"><code>priceSpecification</code></a> property on
                the <code>Offer</code> object. See the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#member-price-example">member price
                examples</a>.
              </p>
<p>
                  The loyalty programs and tiers that you offer for your business should either be
                  defined in your Merchant Center account or using the <code>MemberProgram</code> structured
                  data type nested under <code>Organization</code> structured data on a separate page
                  that defines your Organization's administrative details and policies. See
                  <a href="/appearance/structured-data/loyalty-program.md">loyalty program markup</a> for
                  information on how to define the member programs and tiers for your organization.
              </p>
<p>Here's an example of the <code>validForMemberTier</code> property referencing a member
                program and tier defined in Merchant Center:
              </p>
<pre class="devsite-click-to-copy">"validForMemberTier": {
  "@type": "MemberProgramTier",
  "name": "silver",
  "isTierOf": {
    "@type": "MemberProgram",
    "name": "member-plus"
  }
}</pre>
<p>Here's an example of the <code>validForMemberTier</code> property referencing
              <code>MemberProgramTier</code> structured data nested under
              <code>MemberProgram</code> structured data, which is in turn nested under a <code>Organization</code> structured
              data type on a separate page. The <code>MemberProgramTier</code> instance is
              identified by the <code>@id</code> property specifying the unique resource identifier (URI) of its definition:
              <code>https://www.example.com/com/member-plus#tier_silver</code>:
            </p>
<pre class="devsite-click-to-copy">"validForMemberTier": {
  "@type": "MemberProgramTier",
  "@id": "https://www.example.com/com/member-plus#tier_silver"
}</pre>
<blockquote>
              This property is still in Beta. Off-page <code>MemberProgramTier</code>
              structured data might not show up in Google Search right away.
            </blockquote>
</td>
</tr>
<tr>
<td><code>validFrom</code></td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code> or <code><a href="https://schema.org/Date">Date</a></code></p>
<p>The start date and time when the price is valid, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. For details and markup examples, see <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#sale-duration">Sale duration</a>.</p>
</td>
</tr>
<tr>
<td><code>validThrough</code></td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code> or <code><a href="https://schema.org/Date">Date</a></code></p>
<p>The end date and time when the price is valid, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. For details and markup examples, see <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#sale-duration">Sale duration</a>.</p>
</td>
</tr>
</tbody>
</table>

If both `priceType` and `validForMemberTier` are used, the price specification is ignored.

#### `QuantitativeValue` (for unit pricing)

This section talks about using `QuantitativeValue` for the `referenceQuantity` property of a unit pricing specification. (`QuantitativeValue` is also used for shipping durations, but with different rules.) The full definition of `QuantitativeValue` is available at [`schema.org/QuantitativeValue`](https://schema.org/QuantitativeValue).

`QuantitativeValue` can be used for pricing that is based on a unit measure, such as buying flooring per square meter, or liquids per half gallon. See the example [Pricing with unit pricing measures](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#unit-pricing-example) and the article [Unit pricing measure](https://support.google.com/merchants/answer/6324455) in Google Merchant Center Help for a detailed discussion on unit pricing.

Use the following properties to capture unit pricing details.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>unitCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/URL">URL</a></code></p>
<p>
                The unit of measurement. Either the UN/CEFACT codes or their human-readable
                equivalents as listed in Google Merchant Center Help
                <a href="https://support.google.com/merchants/answer/6324455">Unit pricing measure</a>
                are supported (except <code>sheet</code> and <code>item</code>; these two codes are
                only supported by Merchant Center feeds).
              </p>
</td>
</tr>
<tr>
<td><code>value</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The numeric value of the unit sold.</p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>valueReference</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code></p>
<p>The base quantity in which the product is priced.</p>
</td>
</tr>
</tbody>
</table>

#### `SizeSpecification`

The `SizeSpecification` type is used to indicate the size of a product. The full definition of the type is available at [`schema.org/SizeSpecification`](https://schema.org/SizeSpecification).

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>name</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A human readable name for the size, such as "XL". See the
                <a href="https://support.google.com/merchants/answer/6324492">size attribute</a>
                in Google Merchant Center Help for more details.</p>
</td>
</tr>
<tr>
<td><code>sizeGroup</code></td>
<td>
<p><code><a href="https://schema.org/WearableSizeGroupEnumeration">WearableSizeGroupEnumeration</a></code> or <code><a href="https://schema.org/Text">Text</a></code></p>
<p>The suggested size group for the product, if applicable. The interpretation of
                the group is defined by the <code>sizeGroup</code> property.
                At most two size groups can be provided. Supported values are:</p>
<ul>
<li><code>https://schema.org/WearableSizeGroupRegular</code>: The item size is "regular".</li>
<li><code>https://schema.org/WearableSizeGroupPetite</code>: The item size is "petite".</li>
<li><code>https://schema.org/WearableSizeGroupPlus</code>: The item size is "plus".</li>
<li><code>https://schema.org/WearableSizeGroupTall</code>: The item size is "tall".</li>
<li><code>https://schema.org/WearableSizeGroupBig</code>: The item size is "big".</li>
<li><code>https://schema.org/WearableSizeGroupMaternity</code>: The item size is "maternity".</li>
</ul>
<p>The short names without the URL prefix are also supported (for example, <code>WearableSizeGroupRegular</code>).</p>
<p>See also <a href="https://support.google.com/merchants/answer/6324497"><code>size_type</code></a>
                in Google Merchant Center Help and
                <a href="https://support.google.com/merchants/answer/6386198">Supported structured data types and values</a>
                in Google Merchant Center Help for more information about supported size systems.
                Google understands the text values for <code>size_type</code> as well
                (<code>regular</code>, <code>petite</code>, <code>plus</code>, <code>tall</code>,
                <code>big</code>, and <code>maternity</code>), but other search engines may not,
                so it is recommended to use the standard <code>schema.org</code> enumeration values.</p>
</td>
</tr>
<tr>
<td><code>sizeSystem</code></td>
<td>
<p><code><a href="https://schema.org/WearableSizeSystemEnumeration">WearableSizeSystemEnumeration</a></code> or <code><a href="https://schema.org/Text">Text</a></code></p>
<p>The size system for the product, if applicable. Supported values are:</p>
<ul>
<li><code>https://schema.org/WearableSizeSystemAU</code>: The size system in Australia.</li>
<li><code>https://schema.org/WearableSizeSystemBR</code>: The size system in Brazil.</li>
<li><code>https://schema.org/WearableSizeSystemCN</code>: The size system in China.</li>
<li><code>https://schema.org/WearableSizeSystemDE</code>: The size system in Germany.</li>
<li><code>https://schema.org/WearableSizeSystemEurope</code>: The size system in Europe.</li>
<li><code>https://schema.org/WearableSizeSystemFR</code>: The size system in France.</li>
<li><code>https://schema.org/WearableSizeSystemIT</code>: The size system in Italy.</li>
<li><code>https://schema.org/WearableSizeSystemJP</code>: The size system in Japan.</li>
<li><code>https://schema.org/WearableSizeSystemMX</code>: The size system in Mexico.</li>
<li><code>https://schema.org/WearableSizeSystemUK</code>: The size system in the United Kingdom.</li>
<li><code>https://schema.org/WearableSizeSystemUS</code>: The size system in the United States.</li>
</ul>
<p>The short names without the URL prefix are also supported (for example, <code>WearableSizeSystemAU</code>).</p>
<p>See also <a href="https://support.google.com/merchants/answer/6324502"><code>size_system</code></a>
                in Google Merchant Center Help.
                Google understands the text values for <code>size_system</code> as well
                (for example, <code>UR</code>, <code>BR</code>, <code>CN</code>, <code>DE</code>, <code>EU</code>), but other search engines may not,
                so it is recommended to use the standard <code>schema.org</code> enumeration values.</p>
</td>
</tr>
</tbody>
</table>

#### `PeopleAudience`

The full definition of `PeopleAudience` is available at [`schema.org/PeopleAudience`](https://schema.org/PeopleAudience).

Use the following properties when indicating the recommended audience for a product. See also [Supported structured data attributes and values](https://support.google.com/merchants/answer/6386198) in Google Merchant Center Help.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>suggestedGender</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code> or <code><a href="https://schema.org/GenderType">GenderType</a></code></p>
<p>The suggested gender the product is suitable for. Must be one of the following values:</p>
<ul>
<li><code>https://schema.org/Male</code></li>
<li><code>https://schema.org/Female</code></li>
<li><code>Unisex</code>: This (case-insensitive) value is not in the schema.org standard and must not have a <code>https://schema.org/</code> prefix.</li>
</ul>
<p>See <a href="https://support.google.com/merchants/answer/6324479"><code>Gender</code></a> in
                Google Merchant Center Help for more details.</p>
<p>Note that Google will complete <code>GenderType</code> values without schema.org prefix,
                therefore raw <code>male</code> and <code>female</code> values are also accepted.</p>
</td>
</tr>
<tr>
<td><code>suggestedMaxAge</code> (or <code>suggestedAge.maxValue</code>)</td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The suggested maximum age for the product, in years. Google maps the maximum
                suggested ages for products onto the following fixed set of numerical values:</p>
<ul>
<li><code>0.25</code>: For newborns</li>
<li><code>1.0</code>: For infants</li>
<li><code>5.0</code>: For toddlers</li>
<li><code>13.0</code>: For kids</li>
</ul>
<blockquote>For adults, you don't need to provide the <code>suggestedMaxAge</code>
                (or <code>suggestedAge.maxValue</code>)
                property.</blockquote>
</td>
</tr>
<tr>
<td><code>suggestedMinAge</code> (or <code>suggestedAge.minValue</code>)</td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The suggested minimum age for the product, in years. Google maps the minimum suggested ages for
                products onto the following fixed set of numerical values:</p>
<ul>
<li><code>0</code>: For newborns</li>
<li><code>0.25</code>: For infants</li>
<li><code>1.0</code>: For toddlers</li>
<li><code>5.0</code>: For kids</li>
<li><code>13.0</code>: For adults</li>
</ul>
</td>
</tr>
</tbody>
</table>

#### `Certification`

The full definition of `Certification` is available at [`schema.org/Certification`](https://schema.org/Certification).

Use the following properties to specify the certification.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>issuedBy</code></td>
<td>
<p><code><a href="https://schema.org/Organization">Organization</a></code></p>
<p>The authority or certification body responsible for issuing the certification. Use the property <code>name</code> to specify the organization. At this time, we support the following names:</p>
<ul>
<li><code>EC</code> or <code>European_Commission</code> for energy labels in the EU</li>
<li><code>ADEME</code> for French CO2 emissions classes for vehicles</li>
<li><code>BMWK</code> for German CO2 emissions classes for vehicles</li>
</ul>
</td></tr>
<td><code>name</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The name of the certification. At this time, we support the following values:</p>
<ul>
<li><code>EPREL</code>, which represents energy efficiency certifications in the EU European Registry for Energy Labeling (EPREL) database.</li>
<li><code>Vehicle_CO2_Class</code> for the overall CO2 class of a vehicle</li>
<li><code>Vehicle_CO2_Class_Discharged_Battery</code> for the CO2 class of a vehicle with a discharged battery</li>
</ul>
</td>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>certificationIdentification</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The code of the certification. For example, for the EPREL certificate with the link
                <code>https://example.com/product/dishwashers2019/123456</code> the code is
                <code>123456.</code> The code is required for European Energy Labels.</p>
<blockquote>If you're a merchant serving customers in NO, CH, or the UK and
                you don't have EPREL codes, you can use the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#certification-rating"><code>certificationRating</code> property</a>
                instead of the <code>certificationIdentification</code> property.</blockquote>
</td>
</tr>
<tr>
<td><code>certificationRating</code></td>
<td>
<p><code><a href="https://schema.org/Rating">Rating</a></code></p>
<p>The value of the certification. This property is ignored for certifications that
                have the <code>certificationIdentification</code> property (for example, an EPREL
                code). You can use the <code>certificationRating</code> property to provide the CO2
                Emissions class that's required when listing vehicles in certain countries, or the
                energy efficiency rating when an EPREL code is not available. The following
                properties can be nested in the <code>certificationRating</code> property:</p>
<ul>
<li><code>ratingValue</code></li>
<li><code>bestRating</code></li>
<li><code>worstRating</code></li>
</ul>
<p>The <code>ratingValue</code> property is required when the <code>certificationRating</code>
                property is used. For EU energy efficiency ratings, the <code>bestRating</code> and
                <code>worstRating</code> properties are also required.</p>
<p>Here's an example of the <code>certificationRating</code> property with nested
                properties that specify an EU energy efficiency rating:</p>
<pre class="devsite-click-to-copy">hasCertification": {
  "@type": "Certification",
  "issuedBy": {
    "@type": "Organization",
    "name": "European_Commission"
  }
  "name": "EPREL",
  "url": "https://eprel.ec.europa.eu/screen/product/ovens/53553",
  "certificationIdentification": "53553",
  "certificationRating": {
    "@type": "Rating",
    "ratingValue": "A+",
    "bestRating": "A++",
    "worstRating": "D"
  }
}</pre>
<p>Here's an example of the <code>certificationRating</code> property with nested
                properties that specify a CO2 emissions class:</p>
<pre class="devsite-click-to-copy">"hasCertification": {
  "@type": "Certification",
  "issuedBy": {
    "@type": "Organization",
    "name": "ADEME"
  }
  "name": "Vehicle_CO2_Class",
  "certificationRating": {
    "@type": "Rating",
    "ratingValue": "E",
    "bestRating": "A",
    "worstRating": "G"
  }
}</pre>
</td>
</tr>
</tbody>
</table>

### Shipping

#### `OfferShippingDetails`

`OfferShippingDetails` enables people to see shipping costs and estimated delivery timeframes based on their location and your company's shipping policies. To make your products eligible for the shipping details enhancement, add the following `OfferShippingDetails` properties to your product pages in addition to `Product` structured data.

Sometimes merchants might have multiple options for users to select when shipping a product to a destination (for example, Express Overnight, Rushed 2-day, and Standard). You can indicate each of these by using multiple `shippingDetails` properties, each with different combinations of the `shippingRate` and `deliveryTime` properties.

While `OfferShippingDetails` isn't required, the following properties are required if you want your shipping details to be eligible for the shipping details enhancement.

The full definition of `OfferShippingDetails` is available at [schema.org/OfferShippingDetails](https://schema.org/OfferShippingDetails).

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>deliveryTime</code></td>
<td>
<p><code><a href="https://schema.org/ShippingDeliveryTime">ShippingDeliveryTime</a></code></p>
<p>The total delay between the receipt of the order and the goods reaching the final
                customer. The following properties can be nested in the <code>deliveryTime</code>
                property:</p>
<ul>
<li><code>handlingTime</code></li>
<li><code>transitTime</code></li>
</ul>
<p>Don't provide more than one <code>deliveryTime</code>.
                See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#shipping-delivery-time-properties"><code>ShippingDeliveryTime</code> properties</a>
                supported by Google.</p>
</td>
</tr>
<tr>
<td><code>shippingDestination</code></td>
<td>
<p><code><a href="https://schema.org/DefinedRegion">DefinedRegion</a></code></p>
<p>Indicates shipping destinations. Specify the
                <code>shippingDestination.addressCountry</code> information.
                See also the list of <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#defined-region-properties"><code>DefinedRegion</code> properties</a>
                supported by Google.</p>
</td>
</tr>
<tr>
<td><code>shippingRate</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code></p>
<p>Information about the cost of shipping to the specified destination.
                At least one of <code>shippingRate.value</code> or <code>shippingRate.maxValue</code>
                must be specified, along with <code>shippingRate.currency</code>.</p>
<p>You can only specify one
                <code>shippingRate</code> per <code>OfferShippingDetails</code>
                property. To indicate multiple rates for your product, specify multiple
                <code>OfferShippingDetail</code> properties.</p>
</td>
</tr>
<tr>
<td><code>shippingRate.currency</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The currency of the shipping cost, in 3-letter
                <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217</a> format.
                The currency must be the same as the currency of the offer.</p>
</td>
</tr>
<tr>
<td><code>shippingRate.value</code> or <code>shippingRate.maxValue</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The cost of shipping to the <code>shippingDestination</code>.
                If a string is used to provide the value, don't
                include currency symbols, thousands separators, or spaces.</p>
<p>To specify free shipping, set the value to <code>0</code>.</p>
</td>
</tr>
</tbody>
</table>

#### `DefinedRegion`

`DefinedRegion` is used to create custom areas so that accurate shipping costs and transit times can be set across multiple shipping services. This is currently only supported for a restricted set of countries, as documented in [Set up regions](https://support.google.com/merchants/answer/7410946) in Google Merchant Center Help.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>addressCountry</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The two-letter country code, in <a href="https://en.wikipedia.org/wiki/ISO_3166-1">ISO 3166-1 alpha-2</a>
                format.</p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td>Choose either <code>addressRegion</code> or <code>postalCode</code></td>
<td>
<p>Identifies the region for the customer delivery area. If omitted,
                the whole country is the defined region. Multiple regions can be listed,
                but you cannot mix different ways of specifying the regions in one
                <code>DefinedRegion</code> instance.</p>
</td>
</tr>
<tr>
<td><code>addressRegion</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>If you include this property, the region must be a 2- or 3-digit ISO 3166-2
                subdivision code, without country prefix. Currently, Google Search only supports
                the US, Australia, and Japan. Examples: "NY" (for US, state of New York),
                "NSW" (for Australia, state of New South Wales), or "03" (for Japan,
                Iwate prefecture).</p>
<p>Do not provide both a region and postal code information.</p>
</td>
</tr>
<tr>
<td><code>postalCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The postal code. For example, 94043. Currently postal codes are supported for
                Australia, Canada, and the US.</p>
</td>
</tr>
</tbody>
</table>

#### `ShippingDeliveryTime`

[`ShippingDeliveryTime`](https://schema.org/ShippingDeliveryTime) is used to share the total delay between the receipt of an order and the goods reaching the final customer.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>handlingTime</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code> (for shipping times)</p>
<p>The typical delay between the receipt of the order and the goods leaving the
                warehouse.</p>
</td>
</tr>
<tr>
<td><code>transitTime</code></td>
<td>
<p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code> (for shipping times)</p>
<p>The typical delay between when the order has been sent for delivery and when
                the goods reach the final customer.</p>
</td>
</tr>
</tbody>
</table>

#### `QuantitativeValue` (for shipping times)

`QuantitativeValue` is used here to represent shipping times. A minimum and maximum number of days must be specified. (`QuantitativeValue` is also used for unity pricing, with different validation rules for properties.)

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
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
<p>The minimum number of days. The value must be a non-negative, whole number.</p>
</td>
</tr>
<tr>
<td><code>unitCode</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The units of the minimum/maximum values. The value must be <code>DAY</code> or <code>d</code>.</p>
</td>
</tr>
</tbody>
</table>

### Returns

#### `MerchantReturnPolicy`

Use the following properties to make your merchant listing eligible to show return policy information, including return fees and the window of time to return a product.

> If you provide both [organization-level](/appearance/structured-data/return-policy.md) and product-level return policy markup, Google defaults to the product-level return policy.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>applicableCountry</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The country code that the return policy applies to, using the two-letter
                        <a href="https://en.wikipedia.org/wiki/ISO_3166-1">ISO 3166-1 alpha-2</a>
                        country code formatting. You can specify up to 50 countries.</p>
</td>
</tr>
<tr>
<td><code>returnPolicyCategory</code></td>
<td>
<p><code><a href="https://schema.org/MerchantReturnEnumeration">MerchantReturnEnumeration</a></code></p>
<p>The type of return policy. Use one of the following values:</p>
<ul>
<li><code>https://schema.org/MerchantReturnFiniteReturnWindow</code>: There's a set number of days to return a product.</li>
<li><code>https://schema.org/MerchantReturnNotPermitted</code>: Returns aren't permitted.</li>
<li><code>https://schema.org/MerchantReturnUnlimitedWindow</code>: There's an unlimited amount of time to return a product.</li>
</ul>
<p>
                        If you use <code>MerchantReturnFiniteReturnWindow</code>, the
                        <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#merchant-return-days"><code>merchantReturnDays</code></a> property is required.
                      </p>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>merchantReturnDays</code></td>
<td>
<p><code><a href="https://schema.org/Integer">Integer</a></code></p>
<p>The number of days from the delivery date that a product can be returned. This
                      property is required if you set the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-policy-category"><code>returnPolicyCategory</code></a> to <code>MerchantReturnFiniteReturnWindow</code>.</p>
</td>
</tr>
<tr>
<td><code>returnFees</code></td>
<td>
<p><code><a href="https://schema.org/ReturnFeesEnumeration">ReturnFeesEnumeration</a></code></p>
<p>The type of return fees. Use one of the following supported values:</p>
<ul>
<li><code>https://schema.org/FreeReturn</code>: There's no charge to the consumer to
                        return the product. If used, don't include the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a>
                        property.</li>
<li><code>https://schema.org/ReturnFeesCustomerResponsibility</code>: The consumer
                        needs to handle and pay for the return shipping themselves. If used, don't include
                        the <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a>
                        property.</li>
<li><code>https://schema.org/ReturnShippingFees</code>: There's a shipping fee
                        charged by the merchant to the consumer to return the product. Specify the
                        (non-zero) shipping fee using the
                        <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a> property.</li>
</ul>
</td>
</tr>
<tr>
<td><code>returnMethod</code></td>
<td>
<p><code><a href="https://schema.org/ReturnMethodEnumeration">ReturnMethodEnumeration</a></code></p>
<p>The type of return method offered. This is only recommended if you set the
                      <code>returnPolicyCategory</code> to either <code>MerchantReturnFiniteReturnWindow</code>
                       or <code>MerchantReturnUnlimitedWindow</code>. Use one or more of the following values:</p>
<ul>
<li><code>https://schema.org/ReturnAtKiosk</code>: The item can be returned at a kiosk.</li>
<li><code>https://schema.org/ReturnByMail</code>: The item can be returned by mail.</li>
<li><code>https://schema.org/ReturnInStore</code>: The item can be returned in a store.</li>
</ul>
</td>
</tr>
<tr>
<td><code>returnShippingFeesAmount</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code></p>
<p>The cost of shipping for returning a product. This property is only required if there's a
                       non-zero shipping fee to be paid by the consumer to the merchant to return a product, in which case <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-fees"><code>returnFees</code></a> must be set to <code>https://schema.org/ReturnShippingFees</code>.
                       If the return is free, <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-fees"><code>returnFees</code></a> must be set to <code>https://schema.org/FreeReturn</code>.
                       If the consumer needs to handle, and pay for, the return shipping cost, <a href="https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#return-fees"><code>returnFees</code></a> must be set to <code>https://schema.org/ReturnFeesCustomerResponsibility</code>.
                    </p>
</td>
</tr>
</tbody>
</table>

## Alternative approaches to configuring shipping and return settings with Google

Retailer shipping and return policies can get complicated and may change frequently. If you're having trouble indicating and keeping your shipping and return details up-to-date with markup and have a Google Merchant Center account, consider configuring your [shipping settings](https://support.google.com/merchants/answer/6069284) and [return policies](https://support.google.com/merchants/answer/10220642) in Google Merchant Center Help. You can alternatively configure account-level [shipping and return policies in Search Console](https://support.google.com/webmasters/answer/14907594), which get automatically added to Merchant Center.

### Combining multiple shipping and return configurations

If you define shipping or return policies in multiple places, Google uses the following order of precedence (from strongest to weakest):

- Product-level [feeds submitted in Merchant Center](https://support.google.com/merchants/answer/188477)
- [Settings in the Content API for Shopping](https://developers.google.com/shopping-content/guides/free-listings-return-settings)
- Settings in Merchant Center or Search Console
- Product-level merchant listing markup
- [Organization-level markup](/appearance/structured-data/organization.md)

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#troubleshooting).
2.  [Inspect a live URL](https://support.google.com/webmasters/answer/9012289#test_live_page) to check if the issue persists.
3.  [Request validation](https://support.google.com/webmasters/answer/13300208) using the status report.

### After releasing new templates or updating your code

When you make significant changes to your website, monitor for increases in structured data invalid items.

- If you see an **increase in invalid items**, perhaps you rolled out a new template that doesn't work, or your site interacts with the existing template in a new and bad way.
- If you see a **decrease in valid items** (not matched by an increase in invalid items), perhaps you are no longer embedding structured data in your pages. Use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to learn what is causing the issue.

### Analyzing traffic periodically

Analyze your Google Search traffic using the [Performance Report](https://support.google.com/webmasters/answer/7576553). The data will show you how often your page appears as a rich result in Search, how often users click on it and what is the average position you appear on search results. You can also automatically pull these results with the [Search Console API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).

There are two Search Console reports related to `Product` structured data:

- **[Merchant listings report](https://search.google.com/search-console/r/merchant-listings)**: For pages where shoppers can buy products.
- **[Product snippets report](https://search.google.com/search-console/r/product)**: For other product related pages such as product reviews and aggregator sites.

Both reports provide warnings and errors related to `Product` structured data, but are separate due to the different requirements for the associated experiences. For example, the [Merchant listings report](https://search.google.com/search-console/r/merchant-listings) includes checks for product snippets that include `Offer` structured data, so the [Product snippets](https://search.google.com/search-console/r/product) report only needs to be consulted for non-merchant listing pages.

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208).
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-merchant-listing]: Google Search Central (2026). "Merchant listing (Product, Offer) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/merchant-listing. Retrieved 2026-09-01.
