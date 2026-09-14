---
type: Reference
title: Merchant return policy (MerchantReturnPolicy) structured data
description: Learn how to mark up return policies for products sold online or in stores.
resource: https://developers.google.com/search/docs/appearance/structured-data/return-policy
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-return-policy
  resource: https://developers.google.com/search/docs/appearance/structured-data/return-policy
  title: Merchant return policy (MerchantReturnPolicy) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Merchant return policy (MerchantReturnPolicy) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/return-policy](https://developers.google.com/search/docs/appearance/structured-data/return-policy). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-return-policy]

![shopping knowledge panel with return policy in search results](https://developers.google.com/static/search/docs/images/return-policy.png)

Many merchants have return policies that outline the process of returning purchased products for customers. When you add `MerchantReturnPolicy` structured data to your site, Google Search can use this information to display return policies alongside your products and in knowledge panels in Search results. `MerchantReturnPolicy` lets you specify a link to your return policy page, or details such as the conditions under which customers can return the product, return methods, return fees, refund options, and more.

A standard return policy for your business that applies to most or all products you sell can be specified using the `MerchantReturnPolicy` structured data type nested under the `Organization` structured data type using the `hasMerchantReturnPolicy` property.

> If you need to override your standard return policy for a specific product, specify one or more instances of `MerchantReturnPolicy` under the `Offer` type. For more information on return policies for individual products, refer to the [Merchant listing](/appearance/structured-data/merchant-listing.md) documentation. Return policies for individual products specified under `Offer` support a more limited set of properties than those described here.

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

Here's an example of a complete `OnlineStore` markup with a return policy for products sold to customers in Germany, Austria, and Switzerland, and which need to be returned by mail to Ireland. There is a 60-day return window, with free returns, and full refunds. Only new products can be returned.

``` devsite-click-to-copy
  {
    "@context": "https://schema.org",
    "@type": "OnlineStore",
    "name": "Example Online Store",
    "url": "https://www.example.com",
    "sameAs": ["https://example.net/profile/example12", "https://example.org/@example34"],
    "logo": "https://www.example.com/assets/images/logo.png",
    "contactPoint": {
      "contactType": "Customer Service",
      "email": "support@example.com",
      "telephone": "+47-99-999-9900"
    },
    "vatID": "FR12345678901",
    "iso6523Code": "0199:724500PMK2A2M1SQQ228",
    
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": [ "DE", "AT", "CH"],
      "returnPolicyCountry": "IE",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 60,
      "itemCondition": "https://schema.org/NewCondition",
      "returnMethod": "https://schema.org/ReturnByMail",
      "returnFees": "https://schema.org/FreeReturn",
      "refundType": "https://schema.org/FullRefund",
      "returnLabelSource": "https://schema.org/ReturnLabelCustomerResponsibility"
    }
    
  }
```

Here's an example of a complete `MerchantReturnPolicy` structured data markup including return options for customer remorse or defect items as well as a seasonal override limiting the return window to 30 days.

``` devsite-click-to-copy
  <html>
  <head>
    <title>Our return policy</title>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "OnlineStore",
        "hasMerchantReturnPolicy": {
          "@type": "MerchantReturnPolicy",
          "applicableCountry": [ "DE", "AT", "CH"],
          "returnPolicyCountry": "IE",
          "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 60,
          "itemCondition": [ "https://schema.org/NewCondition", "https://schema.org/DamagedCondition" ],
          "returnMethod": "https://schema.org/ReturnByMail",
          "returnFees": "https://schema.org/ReturnShippingFees",
          "refundType": "https://schema.org/FullRefund",
          "returnShippingFeesAmount": {
            "@type": "MonetaryAmount",
            "value": 2.99,
            "currency": "EUR"
          },
          "returnLabelSource": "https://schema.org/ReturnLabelInBox",
          "customerRemorseReturnFees": "https://schema.org/ReturnShippingFees",
          "customerRemorseReturnShippingFeesAmount": {
            "@type": "MonetaryAmount",
            "value": 5.99,
            "currency": "EUR"
          },
          "customerRemorseReturnLabelSource": "https://schema.org/ReturnLabelDownloadAndPrint",
          "itemDefectReturnFees": "https://schema.org/FreeReturn",
          "itemDefectReturnLabelSource": "https://schema.org/ReturnLabelInBox",
          "returnPolicySeasonalOverride": {
            "@type": "MerchantReturnPolicySeasonalOverride",
            "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
            "startDate": "2025-12-01",
            "endDate": "2025-01-05",
            "merchantReturnDays": 30
          }
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

For your return policy markup to be eligible for usage in Google Search, you must follow these guidelines:

- [General structured data guidelines](/appearance/structured-data/sd-policies.md)
- [Search Essentials](/essentials/overview.md)
- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#technical-guidelines)

### Technical guidelines

- We recommend placing return information on a single page on your site that describes the return policy of your business. You don't need to include it on every page of your site. Include the `MerchantReturnPolicy` structured data type under the `Organization` structured data type. Refer also to the [Organization markup](/appearance/structured-data/organization.md) for more information.
- If you have a non-standard return policy for a specific product, specify the `MerchantReturnPolicy` structured data type under the `Offer` structured data type. Note that the properties supported for offer-level return policies are a subset of the properties supported for organization-level return policies. See [merchant listing markup](/appearance/structured-data/merchant-listing.md) for the subset of properties that are supported for product-level return policies.

## Structured data type definitions

You must include the required properties for your structured data to be eligible for usage in Google Search. You can also include the recommended properties to add more information about your return policies, which could provide a better user experience.

### `MerchantReturnPolicy` (nested under `Organization` using the `hasMerchantReturnPolicy` property)

Use the following properties to describe the standard return policies for your business. <table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties (choose the option that best suits your use case)</th></tr></thead>
<tbody>
<tr><td colspan="2">Option A</td></tr>
<tr>
<td><code>applicableCountry</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The country code that the return policy applies to (where the product is sold and will be returned from).
              Use the two-letter <a href="https://en.wikipedia.org/wiki/ISO_3166-1">ISO 3166-1 alpha-2</a>
              country code formatting. You can specify up to 50 countries.</p>
</td>
</tr>
<tr>
<td><code>returnPolicyCategory</code></td>
<td>
<p><code><a href="https://schema.org/MerchantReturnEnumeration">MerchantReturnEnumeration</a></code></p>
<p>The type of return policy. Use one of the following values:</p>
<ul>
<li><code>https://schema.org/MerchantReturnFiniteReturnWindow</code>:
                There's a set number of days to return a product.</li>
<li><code>https://schema.org/MerchantReturnNotPermitted</code>:
                Returns aren't permitted.</li>
<li><code>https://schema.org/MerchantReturnUnlimitedWindow</code>:
                There's an unlimited amount of time to return a product.</li>
</ul>
<p>
              If you use <code>MerchantReturnFiniteReturnWindow</code>, then the
              <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#merchant-return-days"><code>merchantReturnDays</code></a> property is required.
            </p>
</td>
</tr>
<tr><td colspan="2">Option B</td></tr>
<tr>
<td><code>merchantReturnLink</code></td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>
              Specify the URL of a web page that describes the return policy to your customers. This can be your own
              return policy, or a third-party policy from a service that handles your returns.
            </p>
</td>
</tr>
</tbody>
</table>

#### Finite or unlimited return windows

The following properties are recommended when [`returnPolicyCategory`](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-policy-category) is set to `MerchantReturnFiniteReturnWindow` or `MerchantReturnUnlimitedWindow`.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>merchantReturnDays</code></td>
<td>
<p>
<code><a href="https://schema.org/Integer">Integer</a></code>
</p>
<p>The number of days from the delivery date that a product can be returned. This
            property is only required if <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-policy-category"><code>returnPolicyCategory</code></a> equals <code>MerchantReturnFiniteReturnWindow</code>.</p>
</td>
</tr>
<tr>
<td><code>returnFees</code></td>
<td>
<p><code><a href="https://schema.org/ReturnFeesEnumeration">ReturnFeesEnumeration</a></code></p>
<p>The default type of return fee. Use one of the following supported values:</p>
<ul>
<li><code>https://schema.org/FreeReturn</code>: There's no charge to the consumer to
              return the product. If used, don't include the <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a>
              property.</li>
<li><code>https://schema.org/ReturnFeesCustomerResponsibility</code>: The consumer
              needs to handle and pay for the return shipping themselves. If used, don't include
              the <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a>
              property.</li>
<li><code>https://schema.org/ReturnShippingFees</code>: There's a shipping fee
              charged by the merchant to the consumer to return the product. Specify the
              (non-zero) shipping fee using the
              <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a> property.</li>
</ul>
</td>
</tr>
<tr>
<td><code>returnMethod</code></td>
<td>
<p><code><a href="https://schema.org/ReturnMethodEnumeration">ReturnMethodEnumeration</a></code></p>
<p>The type of return method offered. Use one or more of the following values:</p>
<ul>
<li><code>https://schema.org/ReturnAtKiosk</code>: The item can be returned at a kiosk.</li>
<li><code>https://schema.org/ReturnByMail</code>: The item can be returned by mail.</li>
<li><code>https://schema.org/ReturnInStore</code>: The item can be returned in store.</li>
</ul>
</td>
</tr>
<tr>
<td><code>returnShippingFeesAmount</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code></p>
<p>The cost of shipping for returning a product. This property must be specified only when
              <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-fees"><code>returnFees</code></a> equals <code>https://schema.org/ReturnShippingFees</code>.
          </p>
</td>
</tr>
</tbody>
</table>

#### Finite or unlimited return windows

The following properties are additionally recommended if [`returnPolicyCategory`](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-policy-category) is set to `MerchantReturnFiniteReturnWindow` or `MerchantReturnUnlimitedWindow`.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>customerRemorseReturnFees</code></td>
<td>
<p><code><a href="https://schema.org/ReturnFeesEnumeration">ReturnFeesEnumeration</a></code></p>
<p>A specific type of return fee if the product is returned due to customer remorse.
            See <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-fees"><code>returnFees</code></a> for possible values.</p>
</td>
</tr>
<tr>
<td><code>customerRemorseReturnLabelSource</code></td>
<td>
<p><code><a href="https://schema.org/ReturnLabelSourceEnumeration">ReturnLabelSourceEnumeration</a></code></p>
<p>
            The method by which the consumer obtains a return shipping label for a product.
            See <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-label-source"><code>returnLabelSource</code></a> for possible values.
          </p>
</td>
</tr>
<tr>
<td><code>customerRemorseReturnShippingFeesAmount</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code></p>
<p>
            The cost of shipping for returning a product due to customer remorse. This property
            is only required if there's a non-zero shipping fee to be paid by the consumer to return a product.
            See <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a> for details.
          </p>
</td>
</tr>
<tr>
<td><code>itemCondition</code></td>
<td>
<p><code><a href="https://schema.org/OfferItemCondition">OfferItemCondition</a></code></p>
<p>
            The acceptable conditions of an item which can be returned. You can provide multiple conditions which are accepted.
            Use the following values:
          </p>
<ul>
<li><code>https://schema.org/DamagedCondition</code>: Damaged items are accepted.</li>
<li><code>https://schema.org/NewCondition</code>: New items are accepted.</li>
<li><code>https://schema.org/RefurbishedCondition</code>: Refurbished items are accepted.</li>
<li><code>https://schema.org/UsedCondition</code>: Used items are accepted.</li>
</ul>
</td>
</tr>
<tr>
<td><code>itemDefectReturnFees</code></td>
<td>
<p><code><a href="https://schema.org/ReturnFeesEnumeration">ReturnFeesEnumeration</a></code></p>
<p>A specific type of return fee for defect products. See <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-fees"><code>returnFees</code></a> for possible values.</p>
</td>
</tr>
<tr>
<td><code>itemDefectReturnLabelSource</code></td>
<td>
<p><code><a href="https://schema.org/ReturnLabelSourceEnumeration">ReturnLabelSourceEnumeration</a></code></p>
<p>
            The method by which the consumer can obtain a return shipping label for a product.
            See <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-label-source"><code>returnLabelSource</code></a> for possible values.
          </p>
</td>
</tr>
<tr>
<td><code>itemDefectReturnShippingFeesAmount</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code></p>
<p>
            The cost of shipping for returning a product due to defect products. This property
            is only required if there's a non-zero shipping fee to be paid by the consumer to return a product.
            See <a href="https://developers.google.com/search/docs/appearance/structured-data/return-policy/#return-shipping-fees-amount"><code>returnShippingFeesAmount</code></a> for details.
          </p>
</td>
</tr>
<tr>
<td><code>refundType</code></td>
<td>
<p><code><a href="https://schema.org/RefundTypeEnumeration">RefundType</a></code></p>
<p>The type of refund(s) available for the consumer when returning a product.</p>
<ul>
<li><code>https://schema.org/ExchangeRefund</code>: The item can be exchanged for the same product.</li>
<li><code>https://schema.org/FullRefund</code>: The item can be refunded for the full monetary amount.</li>
<li><code>https://schema.org/StoreCreditRefund</code>: The item can can be refunded for store credit.</li>
</ul>
</td>
</tr>
<tr>
<td><code>restockingFee</code></td>
<td>
<p><code><a href="https://schema.org/MonetaryAmount">MonetaryAmount</a></code> or
             <code><a href="https://schema.org/Number">Number</a></code></p>
<p>The restocking fee charged to the consumer when returning a product. Specify a value of type <code>Number</code> to charge
             a percentage of the price paid by the consumer or use <code>MonetaryAmount</code> to charge a fixed amount.</p>
</td>
</tr>
<tr>
<td><code>returnLabelSource</code></td>
<td>
<p><code><a href="https://schema.org/ReturnLabelSourceEnumeration">ReturnLabelSourceEnumeration</a></code></p>
<p>
            The method by which the consumer can obtain a return shipping label for a product. Use one of the following values:
          </p>
<ul>
<li><code>https://schema.org/ReturnLabelCustomerResponsibility</code>:
              It's the responsibility of the consumer to create a return label.
            </li>
<li><code>https://schema.org/ReturnLabelDownloadAndPrint</code>:
              The return label must be downloaded and printed by the customer.
            </li>
<li><code>https://schema.org/ReturnLabelInBox</code>:
              The return label was included when the product was originally shipped.
            </li>
</ul>
</td>
</tr>
<tr>
<td><code>returnPolicyCountry</code></td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>
            The country where the product has to be sent to for returns. This country can be different
            from the country where the product was originally shipped or sent to.
            <a href="https://en.wikipedia.org/wiki/ISO_3166-1">ISO 3166-1 alpha-2</a>
            country code formatting. You can specify up to 50 countries.</p>
</td>
</tr>
</tbody>
</table>

#### Seasonal override properties

The following properties are required when you need to define seasonal overrides for your organization-level return policies.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Required properties</th></tr></thead>
<tbody>
<tr>
<td><code>returnPolicySeasonalOverride</code></td>
<td>
<p><code><a href="https://schema.org/MerchantReturnPolicySeasonalOverride">MerchantReturnPolicySeasonalOverride</a></code></p>
<p>A seasonal override of a return policy to specify return policies for special events, such as holidays.
            For example, your usual return policy category is set to <code>MerchantReturnPolicyUnlimitedWindow</code>
            but the return window should be limited during holiday sales:
          </p>
<pre class="devsite-click-to-copy">  "returnPolicySeasonalOverride": {
    "@type": "MerchantReturnPolicySeasonalOverride",
    "startDate": "2024-11-29",
    "endDate": "2024-12-06",
    "merchantReturnDays": 10,
    "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow"
  }</pre>
<p>
    Here's how to specify multiple seasonal overrides. In this example, the usual return policy is
    unlimited, but is limited during the following two date ranges:
  </p>
<pre class="devsite-click-to-copy">  "returnPolicySeasonalOverride": [{
    "@type": "MerchantReturnPolicySeasonalOverride",
    "startDate": "2024-11-29",
    "endDate": "2024-12-06",
    "merchantReturnDays": 10,
    "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow"
  },
  {
    "@type": "MerchantReturnPolicySeasonalOverride",
    "startDate": "2024-12-26",
    "endDate": "2025-01-06",
    "merchantReturnDays": 10,
    "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow"
  }]
  </pre>
</td>
</tr>
<tr>
<td><code>returnPolicySeasonalOverride.returnPolicyCategory</code></td>
<td>
<p><code><a href="https://schema.org/MerchantReturnEnumeration">MerchantReturnEnumeration</a></code></p>
<p>The type of return policy. Use one of the following values:</p>
<ul>
<li><code>https://schema.org/MerchantReturnFiniteReturnWindow</code>:
                There's a set number of days to return a product.</li>
<li><code>https://schema.org/MerchantReturnNotPermitted</code>:
                Returns aren't permitted.</li>
<li><code>https://schema.org/MerchantReturnUnlimitedWindow</code>:
                There's an unlimited amount of time to return a product.</li>
</ul>
<p>
              If you use <code>MerchantReturnFiniteReturnWindow</code>, then the
              <code>merchantReturnDays</code> property is required.
            </p>
</td>
</tr>
</tbody>
</table>

The following properties are recommended when you need to define seasonal overrides for your organization-level return policies.

<table>
<colgroup><col/></colgroup>
<thead><tr><th colspan="2">Recommended properties</th></tr></thead>
<tbody>
<tr>
<td><code>returnPolicySeasonalOverride.endDate</code></td>
<td>
<p>
<code><a href="https://schema.org/Date">Date</a></code> or
            <code><a href="https://schema.org/DateTime">DateTime</a></code>
</p>
<p>The end date of the seasonal override.</p>
</td>
</tr>
<tr>
<td><code>returnPolicySeasonalOverride.merchantReturnDays</code></td>
<td>
<p>
<code><a href="https://schema.org/Integer">Integer</a></code> or
            <code><a href="https://schema.org/Date">Date</a></code> or
            <code><a href="https://schema.org/DateTime">DateTime</a></code>
</p>
<p>The number of days from the delivery date that a product can be returned. This
            property is only required if you set the <code>returnPolicyCategory</code> to <code>MerchantReturnFiniteReturnWindow</code>.
          </p>
</td>
</tr>
<tr>
<td><code>returnPolicySeasonalOverride.startDate</code></td>
<td>
<p><code><a href="https://schema.org/Date">Date</a></code> or
            <code><a href="https://schema.org/DateTime">DateTime</a></code>
</p>
<p>The start date of the seasonal override.</p>
</td>
</tr>
</tbody>
</table>

## Alternative approach to configuring return settings with Google

Retailer return policies can get complicated and may change frequently. If you're having trouble indicating and keeping your return details up-to-date with markup and have a Google Merchant Center account, consider configuring your [return policies](https://support.google.com/merchants/answer/10220642) in Google Merchant Center. You can alternatively configure account-level [return policies in Search Console](https://support.google.com/webmasters/answer/14907594), which get automatically added to Merchant Center.

### Combining multiple return configurations

If you're combining various return configurations, keep in mind how you can override your policy information based on the order of precedence. For example, if you provide both [return policy markup](/appearance/structured-data/organization.md) on your site and return policy settings in Search Console, Google will only use the information provided in Search Console.

Google uses the following order of precedence (from strongest to weakest):

- Content API for Shopping ([return settings](https://developers.google.com/shopping-content/guides/free-listings-return-settings))
- Settings in [Merchant Center](https://support.google.com/merchants/answer/14011730) or [Search Console](https://support.google.com/webmasters/answer/14907594)
- [Product-level merchant listing markup](/appearance/structured-data/merchant-listing.md)
- [Organization-level markup](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#merchant-return-policy-properties)

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/return-policy/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-return-policy]: Google Search Central (2026). "Merchant return policy (MerchantReturnPolicy) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/return-policy. Retrieved 2026-09-14.
