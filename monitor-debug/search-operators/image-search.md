---
type: Reference
title: Google Images search operators
description: Discover how Google Images search operators, such as src and site, can show you what images are indexed on your website.
resource: https://developers.google.com/search/docs/monitor-debug/search-operators/image-search
tags:
- google-search
- documentation
- monitor-debug
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-image-search
  resource: https://developers.google.com/search/docs/monitor-debug/search-operators/image-search
  title: Google Images search operators
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Google Images search operators

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/monitor-debug/search-operators/image-search](https://developers.google.com/search/docs/monitor-debug/search-operators/image-search). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-image-search]

Similarly to web search, Google Images supports dedicated search operators, namely `src:` and `imagesize:`. These operators only work on Google Images; they have no effect on other Google properties.

## `src:` search operator

The `src:` search operator returns pages that reference the image URL in the `src` attribute that's provided in the operator. For example:

``` devsite-click-to-copy
src:https://example.com/media/carrot.jpg
```

The operator returns pages from any domain, not just the domain of the URL specified in the operator. This may be helpful to learn which images you're hosting on your site are [hotlinked](https://en.wikipedia.org/wiki/Hotlink) by other sites.

## `imagesize:` search operator

The `imagesize:` search operator returns images of the dimension specified in the operator. You must specify the dimension in width `x` height format. For example:

``` devsite-click-to-copy
imagesize:1500x1000
```

This operator can be helpful in conjunction with the `src:` and `site:` operator. For example, you can find an image of a certain size that was indexed on your site:

``` devsite-click-to-copy
src:https://example.com/media/carrot.jpg imagesize:500x1200
```

Using `imagesize:` with the `site:` operator, you can find images of the exact size:

``` devsite-click-to-copy
site:https://example.com/ imagesize:500x1200
```

## Limitations

Because image search operators are bound by indexing and retrieval limits, you might not see all of the results that may appear for a standard search query.

# References & Citations

[^google-image-search]: Google Search Central (2025). "Google Images search operators". *Google for Developers*. https://developers.google.com/search/docs/monitor-debug/search-operators/image-search. Retrieved 2026-09-01.
