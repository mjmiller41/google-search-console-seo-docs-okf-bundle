---
type: Reference
title: Include structured data relevant to ecommerce
description: Learn about the different types of ecommerce structured data and how each can improve the accuracy of Google's understanding of your content.
resource: https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce
tags:
- google-search
- documentation
- specialty
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-include-structured-data-relevant-to-ecommerce
  resource: https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce
  title: Include structured data relevant to ecommerce
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Include structured data relevant to ecommerce

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce](https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-include-structured-data-relevant-to-ecommerce]

Google [crawls and indexes](/fundamentals/how-search-works.md) your ecommerce website as it does other websites, applying algorithms to understand your content and its intent. Structured data is a standardized machine-readable format for providing information about a page. This can improve the accuracy of Google's understanding of your content.

Structured data in general is not specific to ecommerce, although some structured data types are. The following resources are useful to learn more about structured data for your ecommerce website.

- For an introduction to how Google uses structured data, see [Understand how structured data works](https://developers.google.com/search/docs/guides/intro-structured-data).
- To understand the breadth of structured data (also called schema markup) for an ecommerce website, see [schema.org](https://schema.org/). Google supports many, but not all of, the types of structured data defined by schema.org.

> **Using a Content Management System (CMS)?** If you are using an ecommerce platform, it may be easier to use an integrated platform extension or plugin to add structured data for you.

The following types of structured data are particularly relevant for ecommerce websites. Remember that shoppers may be at different stages in their shopping journey and looking for more than just product pages.

<table>
<tbody>
<tr>
<th colspan="2">
        Ecommerce structured data types
      </th>
</tr>
<tr>
<td>
<h4>
<a href="/appearance/structured-data/breadcrumb.md"><code>BreadcrumbList</code></a>
</h4>
<p>
          To help Google understand the hierarchy of pages on your site, see the
          <a href="/appearance/structured-data/breadcrumb.md">breadcrumb markup documentation</a>.
          This can help Google display a more meaningful breadcrumb trail in search results.
        </p>
</td>
<td>
<img alt="Example of a breadcrumb list using structured data" src="https://developers.google.com/static/search/docs/images/breadcrumb.png"/>
</td>
</tr>
<tr>
<td>
<h4>
<a href="/appearance/structured-data/local-business.md"><code>LocalBusiness</code></a>
</h4>
<p>
          If you have a physical store, tell Google more about your business on your business information pages, such as
          your store's location and opening hours, with
          <a href="/appearance/structured-data/local-business.md"><code>LocalBusiness</code></a>
          structured data.
        </p>
<p>
          You may also want to:
        </p>
<ul>
<li>
            Register your business directly with
            <a href="https://www.google.com/business/">Google My Business</a>.
          </li>
<li>
            Register
            <a href="https://support.google.com/business/answer/4542487">your physical store locations and store codes</a>
            for use by Google Merchant Center.
          </li>
<li>
            Follow the
            <a href="https://support.google.com/merchants/answer/6363310">Merchant Center guidelines</a>
            for more advice such as sharing return policies on your site.
          </li>
</ul>
</td>
<td>
<img alt="Example of local business listing using structured data" src="https://developers.google.com/static/search/docs/images/local-business01.png"/>
</td>
</tr>
<tr>
<td>
<h4>
<a href="/appearance/structured-data/organization.md"><code>Organization</code></a>
</h4>
<p>
          To tell Google more about your business details, such as your logo, contact information, business identifiers,
          and return policies for your business as a whole, see the
          <a href="/appearance/structured-data/organization.md"><code>Organization</code> structured data documentation</a>.
        </p>
</td>
<td>
<img alt="illustration of a knowledge panel showing organization information" src="https://developers.google.com/static/search/docs/images/organization.png"/>
</td>
</tr>
<tr>
<td>
<h4>
<a href="/appearance/structured-data/product.md"><code>Product</code></a>
          and <a href="/appearance/structured-data/product-variants.md"><code>ProductGroup</code></a>
</h4>
<p>
          To tell Google more about your products, see the
          <a href="/appearance/structured-data/product.md"><code>Product</code> structured data documentation</a>
          (and <a href="/appearance/structured-data/product-variants.md">product variants</a>,
          if applicable). See also
          <a href="https://support.google.com/merchants/answer/7331077">Set up structured data for Merchant Center</a>
          in the Google Merchant Center documentation for improved participation in
          shopping related experiences on Google surfaces.
        </p>
</td>
<td>
<img alt="shopping knowledge panel in search results" src="https://developers.google.com/static/search/docs/images/shopping-knowledge-panel.png"/>
</td>
</tr>
<tr>
<td>
<h4>
<a href="/appearance/structured-data/review-snippet.md"><code>Review</code></a>
</h4>
<p>
          To assist Google understand product reviews on your site and when they are appropriate, see
          <a href="/appearance/structured-data/review-snippet.md">Review snippet</a>.
        </p>
</td>
<td>
<img alt="Example of a review snippet in search results" src="https://developers.google.com/static/search/docs/images/reviews04.png"/>
</td>
</tr>
<tr>
<td>
<h4>
<a href="/appearance/structured-data/video.md"><code>VideoObject</code></a>
</h4>
<p>
          If your website includes pages that are primarily about individual videos, appropriately marking up
          prerecorded videos (such as on a product page) or livestream events can help Google
          present the videos appropriately in Google Search results. See our
          <a href="/appearance/structured-data/video.md">video schema markup documentation</a>
          for more information.
        </p>
</td>
<td>
<img alt="Examples of video listings using structured data" src="https://developers.google.com/static/search/docs/images/video-on-google.png"/>
</td>
</tr>
</tbody>
</table>

# References & Citations

[^google-include-structured-data-relevant-to-ecommerce]: Google Search Central (2025). "Include structured data relevant to ecommerce". *Google for Developers*. https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce. Retrieved 2026-09-01.
