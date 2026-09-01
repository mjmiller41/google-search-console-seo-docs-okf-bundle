---
type: Reference
title: Package tracking Early Adopters Program
description: Package tracking is a feature that shows package tracking information on Search. Learn how Google uses your API for package tracking.
resource: https://developers.google.com/search/docs/appearance/package-tracking
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:52:09Z'
sources:
- id: google-package-tracking
  resource: https://developers.google.com/search/docs/appearance/package-tracking
  title: Package tracking Early Adopters Program
  author: Google Search Central (Google LLC)
  last_modified: '2026-07-14T00:00:00Z'
---

# Package tracking Early Adopters Program

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/package-tracking](https://developers.google.com/search/docs/appearance/package-tracking). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-07-14.[^google-package-tracking]

> The package tracking early adopters program is no longer accepting new partners.

Package tracking is a feature that displays package tracking related information on Google. When people come to Search looking to track a package shipped with your company, they'll be able to enter a package ID directly. The feature uses your API to retrieve the package tracking information and then displays it to the user. Here's how package tracking information may appear on Google Search when a user seeks to track a package.

![package tracking in search results](https://developers.google.com/static/search/docs/images/package-tracking.png)

> **Note**: The actual appearance in search results might be different.

## Feature availability

Package tracking is available in all languages and countries where Google Search is available. The program is no longer accepting new partners.

### Availability and responsiveness

We expect almost no downtime from your API and require that your API respond within 700ms on average with the 95th percentile not exceeding 1,000ms. If your API doesn't meet these requirements, we may stop displaying your package tracking information.

### Content

For the integration to work, your API must return the following information:

| Required field  |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| `CurrentStatus` | The current status of the package. This includes the date and time this status became valid and any error states. |

We strongly recommend that your API also return the following information:

| Recommended fields    |                                                                                                                                                                            |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `DeliveredDate`       | The day and time the package was delivered (if it has been delivered).                                                                                                     |
| `PromisedDate`        | The date the package is expected to be delivered.                                                                                                                          |
| `TrackingNumber`      | The tracking number for the package.                                                                                                                                       |
| `TrackingURL`         | The website URL that a user can visit to view package tracking information and possible additional details.                                                                |
| `SupportPhoneNumbers` | A list of support phone numbers available per region.                                                                                                                      |
| `TransitEvents`       | The set of events that denote when a package makes interim progress on its journey to the recipient, including the Day, Time, City, State, and Country (where applicable). |
| `CreateDate`          | The day and time the tracking number was created.                                                                                                                          |
| `PickupDate`          | The date the package was picked up by the carrier.                                                                                                                         |
| `TimestampEvent`      | The timestamp of an event associated with a given package.                                                                                                                 |
| `LocationEvent`       | The location of an event associated with a given package.                                                                                                                  |
| `CanReschedule`       | Whether this package can be re-scheduled.                                                                                                                                  |

We don't accept the following information:

- Any personal data about the recipient or sender of the package.
- Any geographical information about the recipient or sender of the package.

# References & Citations

[^google-package-tracking]: Google Search Central (2026). "Package tracking Early Adopters Program". *Google for Developers*. https://developers.google.com/search/docs/appearance/package-tracking. Retrieved 2026-09-01.
