---
type: Reference
title: Google Search's guidance on using generative AI content on your website
description: Learn how to use generative AI content on your website in a way that complies with Google's policies.
resource: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
tags:
- google-search
- documentation
- fundamentals
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-using-gen-ai-content
  resource: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
  title: Google Search's guidance on using generative AI content on your website
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Google Search's guidance on using generative AI content on your website

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/fundamentals/using-gen-ai-content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-using-gen-ai-content]

Generative AI can be particularly useful when researching a topic, and to add structure to original content. However, using generative AI tools or other similar tools to generate many pages without adding value for users may violate [Google's spam policy on scaled content abuse](/essentials/spam-policies.md). If you're using generative AI content on your website, **make sure your work meets the standards of the [Search Essentials](/essentials/overview.md) and our [spam policies](/essentials/spam-policies.md).**

You might find value in looking at the [Search Quality Raters guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf) on how to evaluate both scaled content abuse (section 4.6.5) and main content created with little to no effort, little to no originality, and little to no added value (section 4.6.6). These guidelines are not a guide to ranking first in Google; they're used by our [search raters](https://support.google.com/websearch/answer/9281931) to help evaluate the performance of our [various search ranking systems](/appearance/ranking-systems-guide.md), and their ratings don't directly influence ranking.

### Focus on accuracy, quality, and relevance

When creating content for the web, focus on accuracy, quality, and relevance, especially when automatically generating the content. This includes metadata like [`<title>` elements](/appearance/title-link.md), [meta description elements](/appearance/snippet.md), [structured data](/appearance/structured-data/intro-structured-data.md), and [alternate texts for images](https://developers.google.com/tech-writing/accessibility/self-study/write-alt-text), which can appear in Search results.

For structured data, also ensure compliance with the [general guidelines](/appearance/structured-data/sd-policies.md), the specific policies for the individual search features, and [validate the markup](/appearance/structured-data/sd-policies.md) to ensure eligibility for [Search features](/appearance/structured-data/search-gallery.md).

### Give users context

Sharing [information about how a piece of content was created](/fundamentals/creating-helpful-content.md) can help give your readers more context. If you're automatically generating content, consider adding information on how your content was created in a way that makes sense for your audience, such as by providing more background information on how automation was used and adding [image metadata](/appearance/structured-data/image-license-metadata.md).

For ecommerce sites, Google Merchant Center has [policies for AI-generated content](https://support.google.com/merchants/answer/14743464). In particular, AI-generated images must contain metadata using the IPTC `DigitalSourceType` [`TrainedAlgorithmicMedia`](https://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia) metadata. AI-generated product data such as title and description attributes must be specified separately and labeled as AI-generated.

For more, see our [FAQs in our blog post on AI-generated content](https://developers.google.com/search/blog/2023/02/google-search-and-ai-content).

# References & Citations

[^google-using-gen-ai-content]: Google Search Central (2025). "Google Search's guidance on using generative AI content on your website". *Google for Developers*. https://developers.google.com/search/docs/fundamentals/using-gen-ai-content. Retrieved 2026-09-01.
