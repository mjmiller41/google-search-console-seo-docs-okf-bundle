---
type: Reference
title: Use valid HTML to specify page metadata
description: Using valid page metadata ensures that Google can process the HTML markup of your pages. Learn which elements are valid in the &lt;head&gt; of your page, and which ones you shouldn't use in the &lt;head&gt;.
resource: https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-valid-page-metadata
  resource: https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata
  title: Use valid HTML to specify page metadata
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Use valid HTML to specify page metadata

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata](https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-valid-page-metadata]

Using valid HTML for page metadata ensures that Google can use the metadata as documented. Google tries to understand HTML even when it is invalid or inconsistent with the [HTML standard](https://html.spec.whatwg.org/multipage/), but errors in the markup can cause problems with how your metadata is used in Google Search. The primary element for specifying metadata about a page is the `<head>` element of an HTML document. If you use an invalid element in the `<head>` element, Google ignores any elements that appear after the invalid element.

## Use valid elements in the `<head>` element

The `<head>` element must only contain the following valid elements (and no other invalid elements), as per the HTML standard:

- `title`
- `meta`
- `link`
- `script`
- `style`
- `base`
- `noscript`
- `template`

## Don't use invalid elements in the `<head>` element

No element other than the aforementioned is permitted by the HTML standard in the `<head>` element. Common elements that appear in the `<head>` element, rendering it invalid are:

- `iframe`
- `img`

We strongly recommend that you don't use these invalid elements in the `<head>` element, but if you must, place these invalid elements after the ones you want Google to see. Once Google detects one of these invalid elements, it assumes the end of the `<head>` element and stops reading any further elements in the `<head>` element.

# References & Citations

[^google-valid-page-metadata]: Google Search Central (2025). "Use valid HTML to specify page metadata". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/valid-page-metadata. Retrieved 2026-09-01.
