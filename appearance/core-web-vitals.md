---
type: Reference
title: Understanding Core Web Vitals and Google search results
description: Core Web Vitals is a set of metrics that measure real-world user experience. Learn more about Google Search and Core Web Vitals.
resource: https://developers.google.com/search/docs/appearance/core-web-vitals
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:55:35Z'
sources:
- id: google-core-web-vitals
  resource: https://developers.google.com/search/docs/appearance/core-web-vitals
  title: Understanding Core Web Vitals and Google search results
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Understanding Core Web Vitals and Google search results

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/core-web-vitals](https://developers.google.com/search/docs/appearance/core-web-vitals). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-core-web-vitals]

[Core Web Vitals](https://web.dev/articles/vitals#core-web-vitals) is a set of metrics that measure real-world user experience for loading performance, interactivity, and visual stability of the page. We highly recommend site owners achieve good Core Web Vitals for success with Search and to ensure a great user experience generally. This, along with other page experience aspects, aligns with what our core ranking systems seek to reward. Learn more in [Understanding page experience in Google Search results](/appearance/page-experience.md).

## Core Web Vitals metrics

- [Largest Contentful Paint (LCP)](https://web.dev/articles/lcp): Measures loading performance. To provide a good user experience, strive to have [LCP occur within the first 2.5 seconds](https://web.dev/articles/lcp#what-is-a-good-lcp-score) of the page starting to load.
- [Interaction To Next Paint (INP)](https://web.dev/articles/inp): Measures responsiveness. To provide a good user experience, strive to have an [INP of less than 200 milliseconds](https://web.dev/articles/inp#good-score).
- [Cumulative Layout Shift (CLS)](https://web.dev/articles/cls): Measures visual stability. To provide a good user experience, strive to have a [CLS score of less than 0.1](https://web.dev/articles/cls#what-is-a-good-cls-score).

## Optimizing your Core Web Vitals

Here are some resources that can help you measure, monitor, and optimize your Core Web Vitals:

Check the [Core Web Vitals report in Search Console](https://support.google.com/webmasters/answer/9205520). This shows how your pages perform.

Learn more about [Core Web Vitals](https://web.dev/articles/learn-core-web-vitals), a guide about Core Web Vitals, including how to measure, debug, improve and best practices.

Learn about the different tools that can help you [measure and report Core Web Vitals](https://web.dev/articles/vitals-tools). These tools measure LCP, INP, and CLS.

## Recent updates on our blog

Here's everything we've announced about Core Web Vitals on the [Google Search Central blog](https://developers.google.com/search/blog):

# References & Citations

[^google-core-web-vitals]: Google Search Central (2025). "Understanding Core Web Vitals and Google search results". *Google for Developers*. https://developers.google.com/search/docs/appearance/core-web-vitals. Retrieved 2026-09-01.
