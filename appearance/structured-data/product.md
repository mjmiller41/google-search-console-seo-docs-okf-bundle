---
type: Reference
title: Introduction to Product structured data
description: Get an overview of how adding product structured data to your web pages can attract potential buyers while they are searching for items to purchase on Google.
resource: https://developers.google.com/search/docs/appearance/structured-data/product
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-product
  resource: https://developers.google.com/search/docs/appearance/structured-data/product
  title: Introduction to Product structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Introduction to Product structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/product](https://developers.google.com/search/docs/appearance/structured-data/product). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-product]

When you add structured data to your product pages, your product information can appear in richer ways in Google Search results (including [Google Images](https://images.google.com/) and [Google Lens](https://lens.google/)). For example, users can see price, availability, review ratings, shipping information, and more right in search results.

## Deciding which markup to use

There are two main classes of product structured data. Follow the requirements for the type that best suits your use case:

- **[Product snippets](/appearance/structured-data/product-snippet.md)**: For product pages where people can't directly purchase the product. This markup has more options for specifying review information, like [pros and cons](/appearance/structured-data/product-snippet.md) on an editorial product review page.
- **[Merchant listings](/appearance/structured-data/merchant-listing.md)**: For pages where customers can purchase products from you. This markup has more options for specifying detailed product information, like [apparel sizing](/appearance/structured-data/merchant-listing.md), [shipping details](/appearance/structured-data/merchant-listing.md), and [return policy](/appearance/structured-data/merchant-listing.md) information.

Note that there is some overlap between the two product features. In general, adding the [required product information properties](/appearance/structured-data/merchant-listing.md) for merchant listings means that your product pages can also be eligible for product snippets. Both features have their own enhancements, so be sure to review both when deciding which markup makes sense in the context of your site (the more properties you can add, the more enhancements your page can be eligible for).

> **Do you offer variants of your products?** Adding [product variant structured data](/appearance/structured-data/product-variants.md) can help Google better understand which products are variations of the same parent product. Both product snippets and merchant listings support product variants.

In addition to structured data for the individual products that you sell, we also recommend you add structured data defining the policies of your ecommerce business, nested under `Organization` markup:

- **[Merchant return policy](/appearance/structured-data/return-policy.md)**: Specify the return policy (or policies) for your business.
- **[Loyalty Program](/appearance/structured-data/loyalty-program.md)**: Specify the loyalty program that you offer.

## How shopping experiences can appear on Google Search

Here's how shopping experiences can appear in Google Search results. This list is not exhaustive—Google Search is constantly exploring new and better ways to help people find what they're looking for, and the experiences may change over time.

<table>
<tbody>
<tr>
<td>
<h5>Product snippet</h5>
<p>A <a href="/appearance/visual-elements-gallery.md">text result</a>
            that includes additional product information such as ratings, review information, price,
            and availability
          </p>
</td>
<td>
<img alt="product snippet presentation in search results" src="https://developers.google.com/static/search/docs/images/product-snippet.png"/>
</td>
</tr>
<tr>
<td>
<h5>Popular products</h5>
<p>
            Visually rich presentation of products for sale
          </p>
</td>
<td>
<img alt="popular products presentation in search results" src="https://developers.google.com/static/search/docs/images/popular-products.png"/>
</td>
</tr>
<tr>
<td>
<h5>Shopping knowledge panel</h5>
<p>
            Detailed product information with a list of sellers (using details such as
            product identifiers)
          </p>
</td>
<td>
<img alt="shopping knowledge panel presentation in search results" src="https://developers.google.com/static/search/docs/images/shopping-knowledge-panel.png"/>
</td>
</tr>
<tr>
<td>
<h5>Google Images</h5>
<p>
            Annotated images of products available for sale
          </p>
</td>
<td>
<img alt="Google Images presentation in search results" src="https://developers.google.com/static/search/docs/images/google-images.png"/>
</td>
</tr>
</tbody>
</table>

### Result enhancements

Search result enhancements are shown at the discretion of each experience, and may change over time. For this reason, it is recommended to provide as much rich product information as available, without concern for the exact experiences that will use it. Here are some examples of how product rich results may be enhanced:

- **Ratings**: Enhance the appearance of your search result by providing [customer reviews and ratings](/appearance/structured-data/product-snippet.md).
- **Pros and Cons**: Identify [pros and cons](/appearance/structured-data/product-snippet.md) in your product review description so they can be highlighted in search results.
- **Shipping**: Share [shipping costs](/appearance/structured-data/merchant-listing.md), especially free shipping, so shoppers understand the total cost.
- **Availability**: Provide [availability](/appearance/structured-data/merchant-listing.md) data to help customers know when you have a product in stock.
- **Price drop**: Price drops are computed by Google by observing price changes for the product over time. Price drops are not guaranteed to be shown.
- **Returns**: Share [return information](/appearance/structured-data/merchant-listing.md), such as your return policy, fees involved in returns, and how many days customers have to return a product.

## Providing product data to Google Search

To provide rich product data to Google Search you can add `Product` structured data to your web pages, upload data feeds with Google Merchant Center and opt into free listings within the Merchant Center console, or both. The Search Central documentation focuses on structured data on web pages.

Providing both structured data on web pages and a Merchant Center feed maximizes your eligibility to experiences and helps Google correctly understand and verify your data. Some experiences combine data from structured data and Google Merchant Center feeds if both are available. For example, product snippets may use pricing data from your merchant feed if it's not present in the structured data on the page. The [Google Merchant Center feed documentation](https://support.google.com/merchants/answer/7052112) includes additional recommendations and requirements for feed attributes.

In addition to Google Search, learn more about eligibility to the [Google Shopping tab](https://support.google.com/merchants/answer/9826670) by reading the [data and eligibility requirements in Google Merchant Center](https://support.google.com/merchants/answer/9199328).

# References & Citations

[^google-product]: Google Search Central (2025). "Introduction to Product structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/product. Retrieved 2026-09-01.
