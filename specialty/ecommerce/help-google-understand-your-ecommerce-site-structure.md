---
type: Reference
title: Help Google understand your ecommerce website structure
description: Learn how you can help Google understand your ecommerce website structure and site navigation so you can promote your best categories or products.
resource: https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure
tags:
- google-search
- documentation
- specialty
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-help-google-understand-your-ecommerce-site-structure
  resource: https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure
  title: Help Google understand your ecommerce website structure
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Help Google understand your ecommerce website structure

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-help-google-understand-your-ecommerce-site-structure]

Google tries to find the best content on your site by analyzing the relationship between pages based on their linkages. This means navigation structures on your site (such as menus and cross page links) can impact Google's understanding of your site structure.

For example, Google can use information such as the number of links it needs to follow to reach a page and the number of links to a page to infer the relative importance of a page over the rest of your site. For more information on how Google determines the importance of a page in Google Search, see [How Google Search Works](/fundamentals/how-search-works.md).

## Make your ecommerce site navigation Google crawler friendly

To help Google find all pages on your site, make sure that you follow ecommerce site best practices and that your pages are reachable by following links through your site's navigation. For example, add links from menus to category pages, from category pages to sub-category pages, and finally from sub-category pages to all product pages. We also recommend that you [add structured data](/specialty/ecommerce/include-structured-data-relevant-to-ecommerce.md), since this can help Google understand the purpose of the different pages on your site to reinforce this structure.

![Example site menu with categories from the Google online store.](https://developers.google.com/static/search/docs/images/ecom-menu-with-categories.png)

If category pages don't include direct links to all products in a category, Googlebot might not find all of your products by crawling alone. These products may be reachable from a search box, but not via category browsing. Googlebot generally doesn't try to submit searches into a search box as part of crawling a site. It's strongly recommended to link to all products that you wish indexed. If it's not possible to link to all pages, use a [sitemap](/crawling-indexing/sitemaps/overview.md) or a [Google Merchant Center feed](https://support.google.com/merchants/answer/7439058). These sources can include links to pages on a site that a crawler would not otherwise find.

To ensure Googlebot correctly locates the link, use `<a href>` tags when creating links to other content. Don't use JavaScript events on other HTML DOM elements for navigation. If you want to learn more about JavaScript and indexing page content, see [Understand the JavaScript SEO basics](https://developers.google.com/search/docs/guides/javascript-seo-basics).

## Promote your best categories or products

Google generally doesn't look at the structure of URLs to work out the structure of a site. Instead, it analyzes the linkages between pages to gain insights about the relative importance of different pages on a site. As a general rule, the more links a page has to it within a site, the higher the relative importance of the page to other pages on your site.

For example, if you have a best selling product, consider linking to it from the home page or in other content, such as blog posts or newsletters on your site. This will help Google understand how important the product is in relation to your site.

At the end of the day, Google is trying to help users find what they are looking for. The ultimate ecommerce SEO best practice is to create useful and interesting content that is valuable to users.

For further reading, see also [Managing crawling of faceted navigation URLs](https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation).

# References & Citations

[^google-help-google-understand-your-ecommerce-site-structure]: Google Search Central (2025). "Help Google understand your ecommerce website structure". *Google for Developers*. https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure. Retrieved 2026-09-01.
