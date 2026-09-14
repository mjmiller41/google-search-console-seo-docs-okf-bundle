---
type: Reference
title: Organization (Organization) structured data
description: You can use Organization markup to let Google know administrative details about your organization, for example, address, contact information, and business identifiers.
resource: https://developers.google.com/search/docs/appearance/structured-data/organization
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-organization
  resource: https://developers.google.com/search/docs/appearance/structured-data/organization
  title: Organization (Organization) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Organization (Organization) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/organization](https://developers.google.com/search/docs/appearance/structured-data/organization). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-organization]

<figure>
<img src="https://developers.google.com/static/search/docs/images/organization.png" alt="Merchant knowledge panel in Google Search results" />
<figcaption aria-hidden="true">Merchant knowledge panel in Google Search results</figcaption>
</figure>

Adding organization structured data to your home page can help Google better understand your organization's administrative details and disambiguate your organization in search results. Some properties are used behind the scenes to disambiguate your organization from other organizations (like `iso6523` and `naics`), while others can influence visual elements in Search results (such as which `logo` is shown in Search results and your [knowledge panel](https://support.google.com/knowledgepanel/answer/9163198)). If you're a merchant, you can influence more details in your [merchant knowledge panel](https://blog.google/products/shopping/google-merchant-new-features-holiday/) and [brand profile](https://support.google.com/merchants/answer/14998338), such as return policy, address, and contact information. There are no required properties; instead, we recommend adding as many properties that are relevant to your organization.

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add as many [recommended properties](https://developers.google.com/search/docs/appearance/structured-data/organization/#structured-data-type-definitions) that apply to your web page. There are no required properties; instead, add the properties that apply to your content. Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/organization/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

### `Organization`

Here's an example of organization information in JSON-LD code.

  

``` devsite-click-to-copy
<html>
  <head>
    <title>About Us</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "url": "https://www.example.com",
      "sameAs": ["https://example.net/profile/example1234", "https://example.org/example1234"],
      "logo": "https://www.example.com/images/logo.png",
      "name": "Example Corporation",
      "description": "The example corporation is well-known for producing high-quality widgets",
      "email": "contact@example.com",
      "telephone": "+47-99-999-9999",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Rue Improbable 99",
        "addressLocality": "Paris",
        "addressCountry": "FR",
        "addressRegion": "Ile-de-France",
        "postalCode": "75001"
      },
      "vatID": "FR12345678901",
      "iso6523Code": "0199:724500PMK2A2M1SQQ228"
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

### `OnlineStore` (subtype of `Organization`) with a shipping policy and return policy

Here's an example of an online store with both a shipping policy and a return policy in JSON-LD code.

Refer to the separate [Merchant return policy markup](/appearance/structured-data/return-policy.md) documentation for more examples and detailed information for merchant-level standard return policies.

``` devsite-click-to-copy
<html>
  <head>
    <title>About Us</title>
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@type": "OnlineStore",
        "name": "Example Online Store",
        "url": "https://www.example.com",
        "sameAs": [
          "https://example.net/profile/example12",
          "https://example.org/@example34"
        ],
        "logo": "https://www.example.com/assets/images/logo.png",
        "contactPoint": {
          "contactType": "Customer Service",
          "email": "support@example.com",
          "telephone": "+47-99-999-9900"
        },
        "vatID": "FR12345678901",
        "iso6523Code": "0199:724500PMK2A2M1SQQ228",
        "hasShippingService": [
          {
            "@type": "ShippingService",
            "name": "shipping to CH and FR",
            "description": "Shipping to CH 5% of order value, shipping to FR always free",
            "fulfillmentType": "FulfillmentTypeDelivery",
            "shippingConditions": [
              {
                "@type": "ShippingConditions",
                "shippingOrigin": {
                  "@type": "DefinedRegion",
                  "addressCountry": "FR"
                },
                "shippingDestination": {
                  "@type": "DefinedRegion",
                  "addressCountry": "CH"
                },
                "shippingRate": {
                  "@type": "ShippingRateSettings",
                  "orderPercentage": "0.05"
                }
              },
              {
                "@type": "ShippingConditions",
                "shippingOrigin": {
                  "@type": "DefinedRegion",
                  "addressCountry": "FR"
                },
                "shippingDestination": {
                  "@type": "DefinedRegion",
                  "addressCountry": "FR"
                },
                "shippingRate": {
                  "@type": "MonetaryAmount",
                  "value": "0",
                  "currency": "EUR"
                }
              }
            ]
          }
        ],
        "hasMerchantReturnPolicy": {
          "@type": "MerchantReturnPolicy",
          "applicableCountry": [
            "FR",
            "CH"
          ],
          "returnPolicyCountry": "FR",
          "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
          "merchantReturnDays": 60,
          "returnMethod": "https://schema.org/ReturnByMail",
          "returnFees": "https://schema.org/FreeReturn",
          "refundType": "https://schema.org/FullRefund"
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

You must follow these guidelines to enable structured data to be eligible for inclusion in Google Search results.

> **Warning:** If your site violates one or more of these guidelines, then Google may take [manual action](https://support.google.com/webmasters/answer/2604824) against it. Once you have remedied the problem, you can submit your site for [reconsideration](https://support.google.com/webmasters/answer/35843).

- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/organization/#technical-guidelines)
- [Search Essentials](/essentials/overview.md)
- [General structured data guidelines](/appearance/structured-data/sd-policies.md)

### Technical guidelines

We recommend placing this information on your home page, or a single page that describes your organization, for example the *about us* page. You don't need to include it on every page of your site.

We recommend using the most specific schema.org subtype of [`Organization`](https://schema.org/Organization) that matches your organization. For example, if you have an ecommerce site, then we recommend using the [`OnlineStore`](https://schema.org/OnlineStore) subtype instead of [`OnlineBusiness`](https://schema.org/OnlineBusiness). And if your site is about a local business, for example a restaurant or a physical store, then we recommend providing your administrative details using the most specific [subtype(s)](/appearance/structured-data/local-business.md) of [`LocalBusiness`](https://schema.org/LocalBusiness) and following the required and recommended fields for [Local business](/appearance/structured-data/local-business.md) in addition to the fields recommended in this guide.

## Structured data type definitions

Google recognizes the following properties of an [`Organization`](https://schema.org/Organization). To help Google better understand your page, include as many recommended properties that apply to your web page. There are no required properties; instead, add the properties that apply to your organization.

> We recommend focusing on properties that are useful to your users, such as `name` or `alternateName` for your business name as well as an indication of real-world presence (for example, `address` or `telephone`) and online presence (for example, `url` or `logo`).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>address</code></td>
<td><p><code><a href="https://schema.org/PostalAddress">PostalAddress</a></code></p>
<p>The address (physical or mailing) of your organization, if applicable. Include all properties that apply to your country. The more
        properties you provide, the higher quality the result is for users.
        You can provide multiple addresses if you have a location in multiple cities, states, or countries.
        For example:</p>
<pre class="devsite-click-to-copy">"address": [{
  "@type": "PostalAddress",
  "streetAddress": "999 W Example St Suite 99 Unit 9",
  "addressLocality": "New York",
  "addressRegion": "NY",
  "postalCode": "10019",
  "addressCountry": "US"
},{
  "streetAddress": "999 Rue due exemple",
  "addressLocality": "Paris",
  "postalCode": "75001",
  "addressCountry": "FR"
}]</pre>
</td>
</tr>
<tr>
<td><code>address.addressCountry</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The country for your postal address, using the two-letter <a href="https://wikipedia.org/wiki/ISO_3166-1">ISO 3166-1 alpha-2 country code.</a></p>
</td>
</tr>
<tr>
<td><code>address.addressLocality</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The city of your postal address.</p>
</td>
</tr>
<tr>
<td><code>address.addressRegion</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The region of your postal address, if applicable. For example, a state.</p>
</td>
</tr>
<tr>
<td><code>address.postalCode</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The postal code for your address.</p>
</td>
</tr>
<tr>
<td><code>address.streetAddress</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The full street address of your postal address.</p>
</td>
</tr>
<tr>
<td><code>alternateName</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Another common name that your organization goes by, if applicable.</p></td>
</tr>
<tr>
<td><code>contactPoint</code></td>
<td><p><code><a href="https://schema.org/ContactPoint">ContactPoint</a></code></p>
<p>The best way for a user to contact your business, if applicable. Include all support methods available to your users
        following Google recommended <a href="https://developers.google.com/search/blog/2021/07/customer-support">best practices</a>. For example:</p>
<pre class="devsite-click-to-copy">"contactPoint": {
  "@type": "ContactPoint",
  "telephone": "+9-999-999-9999",
  "email": "contact@example.com"
}</pre>
</td>
</tr>
<tr>
<td><code>contactPoint.email</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The email address to contact your business, if applicable.
        If you are using a <code>LocalBusiness</code> type, specify a primary email address at
        the <code>LocalBusiness</code> level before using <code>contactPoint</code> to specify
        multiple ways to reach your organization.
      </p>
</td>
</tr>
<tr>
<td><code>contactPoint.telephone</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The phone number to contact your business, if applicable.
        Be sure to include the country code and area code in the phone number.
        If you are using a <code>LocalBusiness</code> type, specify a primary phone number at
        the <code>LocalBusiness</code> level before using <code>contactPoint</code> to specify
        multiple ways to reach your organization.
      </p>
</td>
</tr>
<tr>
<td><code>description</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A detailed description of your organization, if applicable.</p></td>
</tr>
<tr>
<td><code>duns</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The Dun &amp; Bradstreet DUNS number for identifying your <code>Organization</code>, if
        applicable. We encourage using the <code>iso6523Code</code> field with prefix <code>0060:</code>
        instead.</p></td>
</tr>
<tr>
<td>
<code>email</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The email address to contact your business, if applicable.</p>
</td>
</tr>
<tr>
<td><code>foundingDate</code></td>
<td><p><code><a href="https://schema.org/Date">Date</a></code></p>
<p>The date your <code>Organization</code> was founded in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 date format</a>, if applicable.</p></td>
</tr>
<tr>
<td><code>globalLocationNumber</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The GS1 Global Location Number identifying the location of your <code>Organization</code>,
        if applicable.</p></td>
</tr>
<tr>
<td>
<code>hasMerchantReturnPolicy</code>
</td>
<td><p>Repeated <code><a href="https://schema.org/MerchantReturnPolicy">MerchantReturnPolicy</a></code></p>
<p>
          The return policy of your <code>Organization</code>, if applicable. See
          <a href="/appearance/structured-data/return-policy.md">Merchant return policy markup</a>
          for detailed information on required and optional properties for <code>MerchantReturnPolicy</code>.
        </p>
<blockquote>
            If you don't provide a return policy for your <code>Organization</code>, or if some of your
            products have specific return policies for which you need to override the return
            policies defined for your <code>Organization</code>, use this property also under
            <a href="/appearance/structured-data/merchant-listing.md">merchant listing markup</a>.
          </blockquote>
</td>
</tr>
<tr>
<td>
<code>hasMemberProgram</code>
</td>
<td><p>Repeated <code><a href="https://schema.org/MemberProgram">MemberProgram</a></code></p>
<p>
          A member (loyalty) program that you provide, if applicable.
         See <a href="/appearance/structured-data/loyalty-program.md">Member program markup</a> for detailed information on required and optional properties for <code>MemberProgram</code>.
        </p>
</td>
</tr>
<tr>
<td>
<code>hasShippingService</code>
</td>
<td><p>Repeated <code><a href="https://schema.org/ShippingService">ShippingService</a></code></p>
<p>
          The shipping policy of your <code>Organization</code>, if applicable. See
          <a href="/appearance/structured-data/shipping-policy.md">Merchant shipping policy markup</a>
          for detailed information on required and optional properties for <code>ShippingService</code>.
        </p>
<blockquote>
            If you don't provide a shipping policy for your <code>Organization</code>, or if some of your
            products have specific shipping policies for which you need to override the shipping
            policies defined for your <code>Organization</code>, use this property also under
            <a href="/appearance/structured-data/merchant-listing.md">merchant listing markup</a>.
          </blockquote>
</td>
</tr>
<tr>
<td>
<code>iso6523Code</code>
</td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The ISO 6523 identifier of your organization, if applicable.
          The first part of an ISO 6523 identifier is an <a href="http://iso6523.info/icd_list.pdf"><code>ICD</code> (International Code Designator)</a>
          which defines which identification scheme is used.
          The second part is the actual identifier. We recommend separating the ICD and the
          identifier with a colon character (<code>U+003A</code>). Common ICD values include:</p>
<ul>
<li><code>0060</code>: Dun &amp; Bradstreet Data Universal Numbering System (DUNS)</li>
<li><code>0088</code>: GS1 Global Location Number (GLN)</li>
<li><code>0199</code>: Legal Entity Identifier (LEI)</li>
</ul>
</td>
</tr>
<tr>
<td><code>legalName</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The registered, legal name of your <code>Organization</code>, if applicable and different
          from the <code>name</code> property.</p></td>
</tr>
<tr>
<td><code>leiCode</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The identifier for your <code>Organization</code> as defined in ISO 17442, if applicable.
        We encourage using the <code>iso6523Code</code> field with prefix <code>0199:</code> instead.</p></td>
</tr>
<tr>
<td><code>logo</code></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code> or <code><a href="https://schema.org/ImageObject">ImageObject</a></code></p>
<p>A logo that is representative of your organization, if applicable. Adding this property can help Google
          better understand which logo you want to show, for example in Search results and knowledge
          panels.</p>
<p>Image guidelines:</p>
<ul>
<li>The image must be 112x112px, at minimum.</li>
<li>The image URL must be crawlable and indexable.</li>
<li>The image file format must be <a href="/appearance/google-images.md">supported by Google Images</a>.</li>
<li>Make sure the image looks how you intend it to look on a purely white background (for
            example, if the logo is mostly white or gray, it may not look how you want it to look when
            displayed on a white background).</li>
</ul>
<p>If you use the <code><a href="https://schema.org/ImageObject">ImageObject</a></code> type,
          make sure that it has a valid <code><a href="https://schema.org/contentUrl">contentUrl</a></code> property or
          <code><a href="https://schema.org/url">url</a></code> property that follows the same guidelines as a
          <code><a href="https://schema.org/URL">URL</a></code> type.
        </p>
</td>
</tr>
<tr>
<td><code>naics</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The <a href="https://www.census.gov/naics/">North American Industry Classification System (NAICS) code</a>
        for your <code>Organization</code>, if applicable.</p></td>
</tr>
<tr>
<td><code>name</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>
        The name of your organization. Use the same <code>name</code> and <code>alternateName</code>
        that you're using for your <a href="/appearance/site-names.md">site name</a>.
      </p>
</td>
</tr>
<tr>
<td><code>numberOfEmployees</code></td>
<td><p><code><a href="https://schema.org/QuantitativeValue">QuantitativeValue</a></code></p>
<p>The number of employees in your <code>Organization</code>, if applicable.</p>
<p>Example with a specific number of employees:</p>
<pre class="devsite-click-to-copy">"numberOfEmployees": {
  "@type": "QuantitativeValue",
  "value": 2056
}</pre>
<p>Example with the number of employees in a range:</p>
<pre class="devsite-click-to-copy">"numberOfEmployees": {
  "@type": "QuantitativeValue",
  "minValue": 100,
  "maxValue": 999
}</pre>
</td>
</tr>
<tr>
<td>
<code>sameAs</code>
</td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The URL of a page on another website with additional information about your organization,
          if applicable. For example, a URL to your organization's profile page on a social media or
          review site. You can provide multiple <code>sameAs</code> URLs.
        </p>
</td>
</tr>
<tr>
<td>
<code>taxID</code>
</td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The tax ID associated with your <code>Organization</code>, if applicable. Make sure
      <code>taxID</code> matches the country that you provided in the <code>address</code> field.</p></td>
</tr>
<tr>
<td>
<code>telephone</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A business phone number meant to be the primary contact method for customers, if applicable.
        Be sure to include the country code and area code in the phone number.</p>
</td>
</tr>
<tr>
<td>
<code>url</code>
</td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The URL of the website of your organization, if applicable. This helps Google uniquely
       identify your organization.</p>
</td>
</tr>
<tr>
<td>
<code>vatID</code>
</td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The VAT (Value Added Tax) code associated with your <code>Organization</code>, if applicable
       to your country and business. This is an important trust signal for users (for example, users
       can look up your business in public VAT registries).</p></td>
</tr>
</tbody>
</table>

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/organization/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-organization]: Google Search Central (2026). "Organization (Organization) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/organization. Retrieved 2026-09-14.
