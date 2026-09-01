---
type: Skill Reference
title: Structured data type index
description: Maps schema.org @type values detected on a page to the Google Search Central doc that defines its required and recommended properties, for the structured-data skill's per-type lookup.
tags: [skills, structured-data, reference]
status: stable
---

# Structured data type index

For each `@type` (or microdata `itemtype`) found on a sampled page, read the
mapped doc's "Structured data type definitions" section before validating
SD-02 and SD-03 in `./checks.md`. Never copy the required or recommended
property lists into a report or into this skill; this table only names which
document to read — see `../../shared/grounding.md`. All 39 files in
`appearance/structured-data/` are covered below, verified to exist in this
bundle.

Always read first, regardless of what markup is detected:

- `appearance/structured-data/intro-structured-data.md` — formats,
  vocabulary, and how structured data is read.
- `appearance/structured-data/sd-policies.md` — the general guidelines that
  gate every type's eligibility; grounds SD-04 and SD-05.
- `appearance/structured-data/search-gallery.md` — the current catalogue of
  rich result features; confirm a feature is still live before recommending
  it in the opportunity pass.

## Type table

| `@type` (and aliases) | Doc path | When it applies / opportunity heuristic |
| :--- | :--- | :--- |
| `Article`, `NewsArticle`, `BlogPosting` | `appearance/structured-data/article.md` | News, blog, or sports article pages with a headline, author, and publish date. |
| `Product` (introductory doc) | `appearance/structured-data/product.md` | Read first when any `Product` markup is detected — it decides the product-snippet vs. merchant-listing vs. product-variants split; see the routing note below. |
| `Product`, `Offer`, `Review` (editorial/aggregator, no direct purchase) | `appearance/structured-data/product-snippet.md` | Pages that review, rate, or list a product but don't sell it directly — aggregator or editorial review pages. |
| `Product`, `Offer` (page sells the product directly) | `appearance/structured-data/merchant-listing.md` | Pages where a user can purchase the product directly from the site, including detailed sizing, shipping, and return data. |
| `ProductGroup`, `Product` (variants) | `appearance/structured-data/product-variants.md` | A product page groups variants (size, color, material, pattern) of the same parent product. |
| `Recipe`, `HowTo`, `ItemList` (recipe host carousel) | `appearance/structured-data/recipe.md` | Pages describing the preparation of a specific dish. |
| `Organization` | `appearance/structured-data/organization.md` | Homepage or about page identifying the business — address, contact, identifiers, logo. Also the nesting parent for `MerchantReturnPolicy` and `MemberProgram`. |
| `LocalBusiness` and subtypes (e.g. `Restaurant`, `DaySpa`, `HealthClub`) | `appearance/structured-data/local-business.md` | A page for a specific brick-and-mortar business location. |
| `JobPosting` | `appearance/structured-data/job-posting.md` | A page dedicated to a single open job listing, not a list of jobs. |
| `Event` | `appearance/structured-data/event.md` | A page about a specific, dated event. |
| `BreadcrumbList` | `appearance/structured-data/breadcrumb.md` | Any deep page reachable through a site hierarchy. |
| `Review`, `AggregateRating` | `appearance/structured-data/review-snippet.md` | Any page carrying an editorial review or aggregate rating for an item, business, or piece of media. |
| `QAPage`, `Question`, `Answer` | `appearance/structured-data/qapage.md` | A single community-question page with one or more answers — not a general FAQ list. |
| `VideoObject`, `Clip`, `BroadcastEvent` | `appearance/structured-data/video.md` | Any page featuring embedded or hosted video content. |
| `Course` | `appearance/structured-data/course.md` | Course listing or course detail pages. |
| `Dataset`, `DataCatalog`, `DataDownload` | `appearance/structured-data/dataset.md` | Pages describing or offering a downloadable dataset. |
| `SoftwareApplication`, `MobileApplication`, `VideoGame` | `appearance/structured-data/software-app.md` | App or software detail/download pages. |
| `Book`, `ReadAction`, `BorrowAction` | `appearance/structured-data/book.md` | Book detail pages offering to buy, read, or borrow the book. |
| `Movie` | `appearance/structured-data/movie.md` | Movie listing pages, especially movie carousel summary pages. |
| `ProfilePage`, `Person`, `Organization` (profile) | `appearance/structured-data/profile-page.md` | A page profiling one person or organization on a platform, e.g. a social or review site. |
| `DiscussionForumPosting` | `appearance/structured-data/discussion-forum.md` | A community forum thread or discussion page. |
| `ClaimReview`, `Claim`, `Rating` | `appearance/structured-data/factcheck.md` | A fact-checking article evaluating a specific claim. |
| `ImageObject` (license metadata) | `appearance/structured-data/image-license-metadata.md` | Image detail or gallery pages where licensing/creator metadata should surface in Google Images. |
| `ItemList` (host carousel) | `appearance/structured-data/carousel.md` | A summary page listing multiple items of one rich-result type, e.g. a recipe index page. |
| `ItemList` (beta host carousel) | `appearance/structured-data/carousels-beta.md` | Beta host carousel for `Restaurant`, `LocalBusiness`, `LodgingBusiness`, `Hotel`, `VacationRental`, `Product`, or `Event` summary pages. |
| `MathSolver`, `LearningResource`, `HowTo` | `appearance/structured-data/math-solvers.md` | Pages that walk through solving a specific math problem step by step. |
| `Quiz`, `Question`, `Flashcard` | `appearance/structured-data/education-qa.md` | Flashcard or practice-question pages for students. |
| `EmployerAggregateRating` | `appearance/structured-data/employer-rating.md` | Pages aggregating ratings of an employer, typically nested in `JobPosting` or `Organization`. |
| `VacationRental` | `appearance/structured-data/vacation-rental.md` | A vacation rental listing page. |
| `MerchantReturnPolicy` | `appearance/structured-data/return-policy.md` | Nested under `Organization` or a product `Offer`; describes the business's return policy. |
| `MemberProgram`, `MemberProgramTier` | `appearance/structured-data/loyalty-program.md` | Nested under `Organization`; describes a loyalty or rewards program. |
| `OfferShippingDetails`, `ShippingDeliveryTime` | `appearance/structured-data/shipping-policy.md` | Nested under an `Offer`; describes shipping cost and delivery timing. |
| Speakable sections of `Article`/`WebPage` | `appearance/structured-data/speakable.md` | BETA — marks sections of a page suited for text-to-speech/voice assistant playback. |
| Paywalled `Article`/`NewsArticle`/`CreativeWork` | `appearance/structured-data/paywalled-content.md` | Subscription, metered, or registration-gated content pages. |

## Non-type references

| Doc path | Purpose |
| :--- | :--- |
| `appearance/structured-data/intro-structured-data.md` | Formats and vocabulary — always read first. |
| `appearance/structured-data/sd-policies.md` | General guidelines gating eligibility — grounds SD-04 and SD-05. |
| `appearance/structured-data/search-gallery.md` | Full catalogue of rich result features — the opportunity-pass checklist. |
| `appearance/structured-data/generate-structured-data-with-javascript.md` | How JS-injected structured data is generated — grounds SD-07. |
| `appearance/structured-data/index.md` | Landing/navigation page for this doc set, not a type definition. |

## Routing nuance: Product

`appearance/structured-data/product.md` documents the split explicitly: use
`appearance/structured-data/product-snippet.md` for pages where people can't
directly purchase the product — there's more room for editorial review detail
like pros and cons — and `appearance/structured-data/merchant-listing.md` for
pages where customers can purchase directly from the site, which has more
room for detailed offer data like apparel sizing, shipping, and return
policy. The two overlap: the required merchant-listing properties typically
also qualify a page for product snippets. If the sampled page groups variant
products (size, color, material), also read
`appearance/structured-data/product-variants.md`, which both product features
support.

## Ecommerce sites

For any ecommerce site, also read
`specialty/ecommerce/include-structured-data-relevant-to-ecommerce.md` for
the recommended structured data set across a shopping site's page types.
