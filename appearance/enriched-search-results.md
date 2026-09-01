---
type: Reference
title: Enriched search results
description: Enriched search result is a type of rich Google result. Learn how to take advantage of interactive Google Search results by exploring this guide.
resource: https://developers.google.com/search/docs/appearance/enriched-search-results
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-enriched-search-results
  resource: https://developers.google.com/search/docs/appearance/enriched-search-results
  title: Enriched search results
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Enriched search results

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/enriched-search-results](https://developers.google.com/search/docs/appearance/enriched-search-results). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-enriched-search-results]

In addition to standard rich results, Google Search supports a more interactive and enhanced class of rich result called *enriched search results*. Enriched search results often include an immersive experience or other advanced interaction feature. For example, here is a Jobs enriched result that might appear if a user searched for "jobs in United States":

![Jobs enriched search result](https://developers.google.com/static/search/docs/images/jobs-search-ui.png)

Enriched search enables the user to search across the various properties of a structured data item; for example, a user might search for chicken soup recipes under 200 calories, or recipes that take less than 1 hour of preparation time.

## Implementing enriched search

Enriched search is a subset of rich results, and is implemented using [structured data](/appearance/structured-data/intro-structured-data.md). Some rich result types are only available as enriched search types (for example, recipes, jobs, and events); other rich result types can be extended to be an enriched search type with the addition of a few properties. The documentation for a rich result type explains whether and how it can be extended from a basic rich result to an enriched result.

[Technical information and a gallery of results is available here.](/appearance/structured-data/search-gallery.md)

Enriched search is driven by the Google Search ranking algorithm; in addition to adding the correct structured data on your pages, you must follow the following quality guidelines so that Google can properly index and rank your pages.

- The [Structured data quality guidelines](/appearance/structured-data/sd-policies.md)
- The [Search Essentials](/essentials/overview.md)
- The [enriched search quality guidelines](https://developers.google.com/search/docs/appearance/enriched-search-results/#guidelines)

> **A note about duplicate structured data content**: Structured data is typically duplicated across many pages within a site, and for good reason. For example, you might post several Job listings for the same opening in multiple locations. These listings would have identical description values but different location values. The enriched search algorithm takes this into account, and these objects are not considered to be duplicates.

## Enriched search types

The following search types support an enriched search experience:

- [Job Posting](/appearance/structured-data/job-posting.md)
- [Recipe](/appearance/structured-data/recipe.md)
- [Event](/appearance/structured-data/event.md)

## Enriched search quality guidelines

You must follow these spam policies to be eligible for enriched search. If the enriched search ranking algorithm decides that a large part of a site is not meeting the quality bar, it can exclude the entire site from enriched search results.

- **Required properties:** Each enriched search type defines a required set of properties. Items missing the required properties are ineligible.
- **Completeness:** The more additional (recommended) properties you provide, the higher quality the item is to our users. For a job posting, users prefer jobs with explicitly stated salaries than those without, and enriched search ranking also takes this into consideration. If your recipes have actual user reviews and genuine star ratings, that is also valuable to users of your site and enriched search. Completeness is one of the most important ranking signals for enriched search.
- **Relevance:** Your marked up data must be relevant to the enriched search you are participating in. Here are some examples of irrelevant data:
  - A sports live streaming site labeling broadcasts as local events.
  - A woodworking site labeling instructions as recipes.
- **Leaf content:** Enriched search is only available for leaf pages, not for listing pages. A leaf page is a page that describes the detailed properties of an item. A listing page, on the other hand, is a category page that links to multiple leaf pages. The following are examples of listing pages:
  - A page that describes "10 best ideas for cooking turkey" with links out to each recipe.
  - A page listing all the jobs at Mountain View, CA, with links to individual jobs.
- **Content policies:** Individual enriched search has additional content-type-specific policies for each data type, as described in its documentation. Documents or sites that violate these content policies may receive less favorable ranking or ineligible for the feature.

# References & Citations

[^google-enriched-search-results]: Google Search Central (2025). "Enriched search results". *Google for Developers*. https://developers.google.com/search/docs/appearance/enriched-search-results. Retrieved 2026-09-01.
