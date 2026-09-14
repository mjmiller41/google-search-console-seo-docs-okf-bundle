---
type: Reference
title: Event (Event) structured data
description: Make it easier for people to discover and attend your events by adding schema markup to your event pages.
resource: https://developers.google.com/search/docs/appearance/structured-data/event
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-event
  resource: https://developers.google.com/search/docs/appearance/structured-data/event
  title: Event (Event) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Event (Event) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/event](https://developers.google.com/search/docs/appearance/structured-data/event). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-event]

The event experience on Google makes it easier for people to discover and attend events through Google Search results and other Google products, like Google Maps. This feature brings many benefits:

- **More interactive results**: Your events can be eligible to be displayed in the event experience on Google, featuring your logo, description of the event, and more.
- **Increased chances of discovery and conversion**: People have a new way to interact with your event posting and click through to your site. Learn how [Eventbrite saw a 100% increase](https://developers.google.com/search/case-studies/eventbrite-case-study) in the typical year-over-year growth of traffic from Google Search.

![How the event experience looks on Google Search](https://developers.google.com/static/search/docs/images/event-rich-result.png) ![Event details in Google Search, after clicking a specific event](https://developers.google.com/static/search/docs/images/event-details.png)

There are three options to make your events eligible to appear on Google:

- **If you use a third-party website to post events** (for example, you post events on ticketing websites or social platforms), check to see if your event publisher is already participating in the event search experience on Google. If your event publisher is integrated with Google, continue to post your events on the third-party website. You can stop reading here.
- **If you use a CMS (for example, WordPress) and you don't have access to your HTML**, check with your CMS to see if there's a plugin that can add structured data to your site for you. Alternatively, you can use the [Data Highlighter](https://support.google.com/webmasters/answer/2774099) to tell Google about your events without editing the HTML of your site.
- **If you're comfortable editing your HTML**, [use structured data to directly integrate](https://developers.google.com/search/docs/appearance/structured-data/event/#add-structured-data) with Google. You'll need to edit the HTML of the event pages.

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/event/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/event/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

### Standard event

Here's an example of standard `Event` in JSON-LD. A standard event means that the event is happening at a physical location only and the event is happened as scheduled. You can also use Microdata or RDFa syntax.

``` devsite-click-to-copy
<html>
  <head>
    <title>The Adventures of Kira and Morrison</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "The Adventures of Kira and Morrison",
      "startDate": "2025-07-21T19:00-05:00",
      "endDate": "2025-07-21T23:00-05:00",
      "eventStatus": "https://schema.org/EventScheduled",
      "location": {
        "@type": "Place",
        "name": "Snickerpark Stadium",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "100 West Snickerpark Dr",
          "addressLocality": "Snickertown",
          "postalCode": "19019",
          "addressRegion": "PA",
          "addressCountry": "US"
        }
      },
      "image": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "description": "The Adventures of Kira and Morrison is coming to Snickertown in a can't miss performance.",
      "offers": {
        "@type": "Offer",
        "url": "https://www.example.com/event_offer/12345_202403180430",
        "price": 30,
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "validFrom": "2024-05-21T12:00"
      },
      "performer": {
        "@type": "PerformingGroup",
        "name": "Kira and Morrison"
      },
      "organizer": {
        "@type": "Organization",
        "name": "Kira and Morrison Music",
        "url": "https://kiraandmorrisonmusic.com"
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

### Event with an updated status

There are multiple ways to set the status of an event. Here are some common examples of events that have an updated status. For more information, refer to the [`eventStatus`](https://developers.google.com/search/docs/appearance/structured-data/event/#eventstatus) property.

#### Canceled

Here's an example of an event that's been canceled.

  

``` devsite-click-to-copy
<html>
  <head>
    <title>The Adventures of Kira and Morrison</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "The Adventures of Kira and Morrison",
      "startDate": "2025-07-21T19:00-05:00",
      "endDate": "2025-07-21T23:00-05:00",
      "eventStatus": "https://schema.org/EventCancelled",
      "location": {
        "@type": "Place",
        "name": "Snickerpark Stadium",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "100 West Snickerpark Dr",
          "addressLocality": "Snickertown",
          "postalCode": "19019",
          "addressRegion": "PA",
          "addressCountry": "US"
        }
      },
      "image": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "description": "The Adventures of Kira and Morrison is coming to Snickertown in a can't miss performance.",
      "offers": {
        "@type": "Offer",
        "url": "https://www.example.com/event_offer/12345_202403180430",
        "price": 30,
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "validFrom": "2024-05-21T12:00"
      },
      "performer": {
        "@type": "PerformingGroup",
        "name": "Kira and Morrison"
      },
      "organizer": {
        "@type": "Organization",
        "name": "Kira and Morrison Music",
        "url": "https://kiraandmorrisonmusic.com"
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

#### Rescheduled

Here's an example of an event that's been rescheduled.

  

``` devsite-click-to-copy
<html>
  <head>
    <title>The Adventures of Kira and Morrison</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": "The Adventures of Kira and Morrison",
      "startDate": "2025-07-21T19:00-05:00",
      "endDate": "2025-07-21T23:00-05:00",
      "eventStatus": "https://schema.org/EventRescheduled",
      "previousStartDate": "2025-03-21T19:00-05:00",
      "location": {
        "@type": "Place",
        "name": "Snickerpark Stadium",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "100 West Snickerpark Dr",
          "addressLocality": "Snickertown",
          "postalCode": "19019",
          "addressRegion": "PA",
          "addressCountry": "US"
        }
      },
      "image": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "description": "The Adventures of Kira and Morrison is coming to Snickertown in a can't miss performance.",
      "offers": {
        "@type": "Offer",
        "url": "https://www.example.com/event_offer/12345_202403180430",
        "price": 30,
        "priceCurrency": "USD",
        "availability": "https://schema.org/InStock",
        "validFrom": "2024-05-21T12:00"
      },
      "performer": {
        "@type": "PerformingGroup",
        "name": "Kira and Morrison"
      },
      "organizer": {
        "@type": "Organization",
        "name": "Kira and Morrison Music",
        "url": "https://kiraandmorrisonmusic.com"
      }
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

## Region and language availability

We are excited to bring the event search experience on Google to more regions around the world. The experience is available in the following regions and languages.

| Region         | Available languages |
|----------------|---------------------|
| Australia      | English             |
| Brazil         | Portuguese          |
| Canada         | English             |
| Germany        | German              |
| India          | English             |
| Latin America  | Spanish             |
| Spain          | Spanish             |
| United Kingdom | English             |
| United States  | English             |

## Guidelines

You must follow these guidelines to be eligible to appear in the event search experience on Google.

> **Warning:** If your site violates one or more of these guidelines, then Google may take [manual action](https://support.google.com/webmasters/answer/2604824) against it. Once you have remedied the problem, you can submit your site for [reconsideration](https://support.google.com/webmasters/answer/35843).

- [Technical guidelines](https://developers.google.com/search/docs/appearance/structured-data/event/#technical-guidelines)
- [Content guidelines](https://developers.google.com/search/docs/appearance/structured-data/event/#content-guidelines)
- [Date and time guidelines](https://developers.google.com/search/docs/appearance/structured-data/event/#date-time-best-guidelines)
- [Search Essentials](/essentials/overview.md)
- [General structured data guidelines](/appearance/structured-data/sd-policies.md)

### Technical guidelines

- The target page must contain structured data items from [event types on schema.org](https://schema.org/Event).
- Each event MUST have a unique URL (a leaf page) and markup on that URL.
- The event experience on Google only supports pages that focus on a single event. We recommend focusing on adding markup to your event posting pages instead of pages that list schedules or multiple events.
- **Mark up multi-day events correctly:**
  - If your event or ticket info is for an event that runs over several days, specify both the start and end dates of the event.
  - If there are several different performances across different days, each with individual tickets, add a separate `Event` element for each performance.

### Content guidelines

- Each event must accurately describe the event name, start date, and location.
- **Avoid marking non-events as events:**
  - Don't promote non-event products or services such as "Trip package: San Diego/LA, 7 nights" as events.
  - Don't add short-term discounts or purchase opportunities, such as: "Concert — buy your tickets now," or "Concert - 50% off until Saturday."
  - Don't mark business hours as events, such as: "Adventure park open 8 AM to 5PM."
  - Don't mark coupons or vouchers as events, such as: "5% off your first order."
- Events must be bookable to the general public. Events that require a membership, or invitation prior to purchasing the ticket or attending the event are ineligible for the event experience.
- Spectator events where the primary participants and audience are minors and occur on-premise of a school aren't eligible for the event experience. For example, student events occurring on school premises.
- Virtual experiences that have no real-world component aren't supported. Events must take place in a physical location.

### Date and time guidelines

When implementing the [`startDate`](https://developers.google.com/search/docs/appearance/structured-data/event/#startdate), [`endDate`](https://developers.google.com/search/docs/appearance/structured-data/event/#enddate), and [`previousStartDate`](https://developers.google.com/search/docs/appearance/structured-data/event/#previous-start-date) properties, follow these date and time guidelines.

#### How to specify timezones

Specify the timezone by including the UTC or GMT time offset. If the event starts at 7pm on September 5 in New York, the `startDate` value would be GMT/UTC-5 during standard time and GMT/UTC-4 during daylight savings time. During standard time, `startDate` value would be `"2019-09-05T19:00:00-05:00"` or `"2019-09-05T19:00:00-04:00"` respectively. If no timezone is provided, Google uses the timezone of the event's location as specified in `location`.

#### Best practices

- **Event takes place over a range of dates**: If the event takes place over the course of multiple days, indicate both the start and end date. Don't indicate the time if you don't know the time.

  **Recommended**

  ``` devsite-click-to-copy
  "startDate": "2019-07-01T10:00:00-05:00",
  "endDate": "2019-07-26T17:00:00-05:00"
  ```

  **Recommended**

  ``` devsite-click-to-copy
  "startDate": "2019-07-01",
  "endDate": "2019-07-26"
  ```

  **Not recommended**

  ``` devsite-click-to-copy
  "startDate": "2019-07-01T00:00:00+00:00",
  "endDate": "2019-07-26T23:59:59+00:00"
  ```

- **Event starts at a specific hour**: If the event starts at a specific time, such as 5pm locally, use `2019-07-20T17:00:00`. Include the appropriate UTC offset (for example, use `2019-07-20T17:00:00-07:00` if the event is in California).

- **Event is a day long event**: If the event is happening all day, don't specify a granular hour for the start date. For example, you can use `2019-08-15` as both the `startDate` and `endDate` for a day-long event.

- **Event start hour isn't known**: If you don't know the hour for the start time, don't specify a granular hour. For example, you can use `2019-08-15` as both the `startDate` and `endDate`.

  **Recommended**: `"startDate": "2025-07-21"`

  **Not recommended**: `"startDate": "2019-08-15T00:00:00+00:00"`

  **Not recommended**: `"startDate": "2019-07-20T00:00:00"`

#### Examples of how Google interprets dates

Here are some examples of how Google interprets start date and time:

<table>
<colgroup>
<col/>
</colgroup>
<tbody>
<tr>
<th colspan="2">Start date and time interpretations</th>
</tr>
<tr>
<td><code>2019-08-15T00:00:00+00:00</code></td>
<td>
        Google interprets the <code>startTime</code> to be
        <code>2019-08-14T17:00:00-07:00</code> (if <code>location</code> is set to California) or
        <code>2019-08-15T09:00:00</code> (if <code>location</code> is set to Korea).
      </td>
</tr>
<tr>
<td><code>2019-08-15T23:59:59+00:00</code></td>
<td>This doesn't mean the end of <code>2019-08-15</code> unless the event happens in
        the GMT timezone. Google interprets the <code>startTime</code> to be
        <code>2019-08-15T16:59:59-07:00</code> (if <code>location</code> is set to California) or
        <code>2019-08-16T08:59:59</code> (if <code>location</code> is set to Korea).</td>
</tr>
<tr>
<td><code>2019-07-10</code></td>
<td>This means the date regardless of the timezone. When used in <code>startDate</code>,
        it means the event starts in the <code>location</code> from sometime in that day. When used in
        <code>endDate</code>, it means the event ends in the <code>location</code> from sometime in that
        day.</td>
</tr>
<tr>
<td><code>2019-07-20T00:00:00</code></td>
<td>This means midnight on <code>2019-07-20</code> for the timezone where the
        event happens. This is also likely wrong unless the event was meant to start at
        midnight.</td>
</tr>
</tbody>
</table>

## Structured data type definitions

The full definition of `Event` is available at [schema.org/Event](https://schema.org/Event).

You must include the required properties for your content to be eligible for display in enhanced search results. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>location</code>
</td>
<td>
<p><code><a href="https://schema.org/Place">Place</a></code></p>
<p>The location of the event. Set the <code>@type</code> to <code>Place</code>. Add the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#location-address"><code>location.address</code></a> and
                <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#location-name"><code>location.name</code></a> properties.</p>
</td>
</tr>
<tr>
<td>
<code>location.address</code>
</td>
<td>
<p><code><a href="https://schema.org/PostalAddress">PostalAddress</a></code></p>
<p>The venue's detailed street address. </p>
<p><b>Not recommended</b>: Sydney</p>
<p><b>Recommended</b>: Bennelong Point,
            Sydney NSW 2000, Australia</p>
<p><b>United States example</b></p>
<pre class="devsite-click-to-copy">"location": {
  "@type": "Place",
  "name": "Snickerpark Stadium",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "100 West Snickerpark Dr",
    "addressLocality": "Snickertown",
    "postalCode": "19019",
    "addressRegion": "PA",
    "addressCountry": "US"
  }
}</pre>
<p><b>Japan examples</b></p>
<p>
              You can write addresses for Japan in different ways, and Google still understands the
              address. Here's an example with the street address, locality, and country in
              different fields.
            </p>
<pre class="devsite-click-to-copy">"location": {
  "@type": "Place",
  "name": "ダイバーシティ東京",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "江東区青海1-10",
    "addressLocality": "東京",
    "addressCountry": "日本"
  }
}</pre>
<p>
              Here's an example of the street address and address country in different fields.
            </p>
<pre class="devsite-click-to-copy">"location": {
  "@type": "Place",
  "name": "ダイバーシティ東京",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "東京都江東区青海1-10",
    "addressCountry": "日本"
  }
}</pre>
<p>
Here's an example of the entire address on one line.
</p>
<pre class="devsite-click-to-copy">"location": {
  "@type": "Place",
  "name": "ダイバーシティ東京",
  "address": {
    "@type": "PostalAddress",
    "name": "東京都江東区青海 1-1-10 ダイバーシティ東京プラザ"
   }
}</pre>
<p><b>Best practices for addresses</b>:</p>
<ul>
<li>If the event happens across several streets, define the starting location and mention
              the full details in description.</li>
<li>If the event happens without a well-defined location, use the city name or the most
              representative location.</li>
<li>If the event happens at multiple locations at the same time, create different events for
              each location.</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>name</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The full title of the event.</p>
<blockquote>DO NOT put the name of the event location. Instead, use
            <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#location-name"><code>location.name</code></a> to specify the name of the location
            where the event is being held.</blockquote>
<p><b>Not recommended</b>: Bill Graham Civic Auditorium</p>
<p><b>Not recommended</b>: **LIMITED TIME SALE -
            Kesha and Macklemore Concert - $25**</p>
<p><b>Recommended</b>: The Adventures of Kesha and
            Macklemore</p>
<p><b>Recommended</b>: Meet and Greet: Kesha and
            Macklemore</p>
<p><b>Best practices</b>:</p>
<ul>
<li>Don't use the type of event as the name of the event. For example, "Concert" is not
              a descriptive name for an event.</li>
<li>Don't include extraneous information like URLs, prices, or performers. Instead, use
              the appropriate properties for those values.</li>
<li>Highlight a unique aspect of the event in the title. This helps users make faster
              decisions (for example, "feat. Q&amp;A with the artist").</li>
<li>Don't add short-term promotions (for example, "buy your tickets now").</li>
</ul>
</td>
</tr>
<tr>
<td><code>startDate</code></td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The start date and start time of the event in
            <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601 format</a>.
            Add both the date and time so users can find events that fit into their
            schedule.</p>
<blockquote>
            Make sure to follow the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#date-time-best-guidelines">Date and time guidelines</a>.
          </blockquote>
<pre class="devsite-click-to-copy">"startDate": "2025-07-21T19:00"</pre>
</td>
</tr>
</tbody>
</table> <table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Recommended properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>description</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>Description of the event. Describe all details of the event to make it easier for
            users to understand and attend the event.</p>
<p>
<b>Best practices</b>:
          </p>
<ul>
<li>Add a clear and concise description of the specific event.</li>
<li>Focus on the event details and not your site's features. </li>
<li>Don't repeat other facts like date and location; instead, add that information to the
              respective properties.</li>
</ul>
<pre class="devsite-click-to-copy">"description": "The Adventures of Kira and Morrison is coming to Snickertown in a can't miss performance."</pre>
<blockquote>Google only shows a snippet of the full description.</blockquote>
</td>
</tr>
<tr>
<td>
<code>endDate</code>
</td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The end date and end time of the event in
            <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601 format</a>.
            Use the same format as <code><a href="https://developers.google.com/search/docs/appearance/structured-data/event/#startdate">startDate</a></code>. Add both the
            date and time so users can find events that fit into their schedule.</p>
<blockquote>
            Make sure to follow the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#date-time-best-guidelines">Date and time
            guidelines</a>.
          </blockquote>
<pre class="devsite-click-to-copy">"endDate": "2025-07-21T23:00"</pre>
</td>
</tr>
<tr>
<td><code>eventStatus</code>
</td>
<td><code><a href="https://schema.org/EventStatusType">EventStatusType</a></code>
<blockquote><b>Warning</b>: When the event status changes,
          <b>DON'T</b> remove the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#startdate"><code>startDate</code></a>. The <code>startDate</code>
          property is required to help identify the unique event.</blockquote>
<p>
          The status of the event. If you don't use this field, Google understands the
          <code>eventStatus</code> to be <code>EventScheduled</code>. You can use multiple statuses, if
          applicable. Here are the supported values.
        </p>
<table>
<colgroup>
<col/>
</colgroup>
<tbody>
<tr><td><a href="https://schema.org/EventCancelled"><code>EventCancelled</code></a></td>
<td>
<p>
              The event has been canceled.</p>
<blockquote>Don't remove or change other properties (for
                example, don't remove <code>startDate</code> or <code>location</code>);
                instead, keep all values as the same as they were before the cancelation, and
                update the <code>eventStatus</code> to <code>EventCancelled</code>. <br/>
<br/>
<b>Why?</b> Properties like <code>startDate</code> and
                <code>location</code> help identify the unique event and
                make sure people understand the new status of the event.</blockquote>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Event",
  "eventStatus": "https://schema.org/EventCancelled",
  "startDate": "2020-07-21T19:00"
}</pre>
</td></tr>
<tr><td><a href="https://schema.org/EventPostponed"><code>EventPostponed</code></a></td>
<td>
<p>
              The event has been postponed to a later date, but the date isn't known yet. Keep the
              original date in the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#startdate"><code>startDate</code></a> of the event
              until you know when the event will take place. Once you know the new date information,
              change the <code>eventStatus</code> to <code>EventRescheduled</code> and update the
               <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#startdate"><code>startDate</code></a> and <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#enddate"><code>endDate</code></a>
                with the new date information.
            </p>
<blockquote>Don't remove or change other properties (for
                example, don't remove the <code>startDate</code> or <code>location</code>);
                instead, keep all values as the same as they were before the postponement, and
                update the <code>eventStatus</code> to <code>EventPostponed</code>. <br/>
<br/>
<b>Why?</b> Properties like <code>startDate</code> and
                <code>location</code> help identify the unique event and
                make sure people understand the new status of the event.</blockquote>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Event",
  "eventStatus": "https://schema.org/EventPostponed",
  "startDate": "2020-07-21T19:00"
}</pre>
</td></tr>
<tr><td><a href="https://schema.org/EventRescheduled"><code>EventRescheduled</code></a></td>
<td>
<p>
              The event has been rescheduled to a later date. Update the
              <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#startdate"><code>startDate</code></a> and <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#enddate"><code>endDate</code></a>
              with the relevant new dates. Optionally, you can also mark the <code>eventStatus</code>
              field as rescheduled and add the <code><a href="https://developers.google.com/search/docs/appearance/structured-data/event/#previous-start-date">previousStartDate</a></code>.
            </p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Event",
  "eventStatus": "https://schema.org/EventRescheduled",
  "startDate": "2020-07-21T19:00",
  "endDate": "2025-07-21T23:00",
  "previousStartDate": "2025-03-21T19:00"
}</pre>
</td></tr>
<tr><td><a href="https://schema.org/EventScheduled"><code>EventScheduled</code></a></td>
<td>
<p>
              The event is scheduled to happen. This value is the default status for events. If you
              don't set <code>eventStatus</code>, Google understands the event to be happening on schedule.
            </p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Event",
  "eventStatus": "https://schema.org/EventScheduled",
  "startDate": "2020-07-21T19:00"
}</pre>
</td></tr>
</tbody>
</table>
</td></tr>
<tr>
<td>
<code>image</code>
</td>
<td>
<p>Repeated <code><a href="https://schema.org/ImageObject">ImageObject</a></code> or
          <code><a href="https://schema.org/URL">URL</a></code></p>
<p>URL of an image or logo for the event or tour. Including an image helps users
            understand and engage with your event. We recommend that images are 1920px wide
            (the minimum width is 720px).</p>
<p>Additional image guidelines:
  <ul>
<li>Image URLs must be crawlable and indexable. To check if Google can access your URLs, use
      the <a href="https://support.google.com/webmasters/answer/9012289">URL Inspection tool</a>.</li>
<li>Images must represent the marked up content.</li>
<li>Images must be in a file format that's <a href="/appearance/google-images.md">supported by Google Images</a>.</li>
<li>For best results, we recommend providing multiple high-resolution images (minimum of 50K pixels when
      multiplying width and height) with the following aspect ratios: 16x9, 4x3, and 1x1.</li>
</ul>
<p>For example:</p>
<pre class="devsite-click-to-copy">"image": [
  "https://example.com/photos/1x1/photo.jpg",
  "https://example.com/photos/4x3/photo.jpg",
  "https://example.com/photos/16x9/photo.jpg"
]</pre>
</p></td>
</tr>
<tr>
<td>
<code>location.name</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The detailed name of the place or venue where the event is being held. This property
            is only recommended for events that take place at a physical location.</p>
<blockquote>DO NOT put the title of the event in this field. Instead, use
            <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#event-name"><code>name</code></a> to specify the name of the event.</blockquote>
<p><b>Not recommended</b>: San Francisco, CA</p>
<p><b>Recommended</b>: Bill Graham Civic Auditorium</p>
<p>
<b>Best practices</b>:
          </p>
<ul>
<li>Don't include a city name unless it is a city-wide event.</li>
<li>The <code>location.name</code> property must be the name of the venue or location, not a repeat of
             the title of the event. If you don't know the name of the location, don't use this property.</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>offers</code>
</td>
<td>
<p><code><a href="https://schema.org/Offer">Offer</a></code></p>
          A nested <code><a href="https://schema.org/Offer">Offer</a></code>, one for each ticket
          type.
        </td>
</tr>
<tr>
<td>
<code>offers.availability</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>One of the following:</p>
<ul>
<li><code><a href="https://schema.org/InStock">InStock</a></code>: Event tickets are in stock.</li>
<li><code><a href="https://schema.org/SoldOut">SoldOut</a></code>: Event tickets are sold out.</li>
<li><code><a href="https://schema.org/PreOrder">PreOrder</a></code>: Event tickets are available for preorder.</li>
</ul>
<pre class="devsite-click-to-copy devsite-code-highlight">"offers": {
  "@type": "Offer",
  <strong>"availability": "https://schema.org/InStock"</strong>
}</pre>
<blockquote><b>Note:</b> If the ticket is not yet on sale to the general public, you can
            omit availability and specify <code>validFrom</code>.</blockquote>
</td>
</tr>
<tr>
<td>
<code>offers.price</code>
</td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The lowest available price available for your tickets, including service charges and
            fees. Don't forget to update it as prices change or tickets sell out.</p>
<p>
            If the event is available without payment, fees, or service charges, set the <code>price</code> to <code>0</code>.
          </p>
<pre class="devsite-click-to-copy devsite-code-highlight">"offers": {
  "@type": "Offer",
  <strong>"price": 30</strong>
}</pre>
</td>
</tr>
<tr>
<td>
<code>offers.priceCurrency</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The 3-letter ISO 4217 currency code.</p>
<pre class="devsite-click-to-copy">"offers": {
  "@type": "Offer",
  <b>"priceCurrency": "USD"</b>
}</pre>
</td>
</tr>
<tr>
<td>
<code>offers.validFrom</code>
</td>
<td>
<p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time when tickets go on sale (only required on date-restricted offers), in
            <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO-8601 format</a>.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">"offers": {
  "@type": "Offer",
  <strong>"validFrom": "2024-05-21T12:00"</strong>
}</pre>
</td>
</tr>
<tr>
<td>
<code>offers.url</code>
</td>
<td>
<p><a href="https://schema.org/URL">URL</a></p>
<p>The URL of a page providing the ability to buy tickets. </p>
<pre class="devsite-click-to-copy devsite-code-highlight">"offers": {
  "@type": "Offer",
  <strong>"url": "https://www.example.com/event_offer/12345_201803180430"</strong>
}</pre>
<p>This URL must meet the following requirements:</p>
<ul>
<li>Direct to a landing page that clearly and predominantly provides the opportunity to buy
              a ticket offering admittance to that specific event to any user from the general
              public.</li>
<li>Be a link that a user could click the web page that contains the event.</li>
<li>Be crawlable by Googlebot (not blocked by robots.txt).</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>organizer</code>
</td>
<td>
<p><code><a href="https://schema.org/Organization">Organization</a></code>
            or <code><a href="https://schema.org/Person">Person</a></code></p>
<p>The person or organization that is hosting the event. If you include <code>organizer</code>,
            we encourage you to add the following properties:</p>
<ul>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/event/#organizer-name"><code>organizer.name</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/event/#organizer-url"><code>organizer.url</code></a></li>
</ul>
</td>
</tr>
<tr>
<td>
<code>organizer.name</code>
</td>
<td>
<p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The name of the person or organization that's hosting the event.</p>
</td>
</tr>
<tr>
<td>
<code>organizer.url</code>
</td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>The event host's domain URL.</p>
</td>
</tr>
<tr>
<td>
<code>performer</code>
</td>
<td>
<p><code><a href="https://schema.org/Person">Person</a></code></p>
<p>The participants performing at the event, such as artists and comedians. Use a nested
            <code><a href="https://schema.org/PerformingGroup">PerformingGroup</a></code> or
          <code><a href="https://schema.org/Person">Person</a></code>, one for each performer.</p>
</td>
</tr>
<tr>
<td>
<code>performer.name</code>
</td>
<td>
<p><a href="https://schema.org/Text">Text</a></p>
<p>The name of the participant performing at the event, such as the name of the artist or
            comedian.</p>
<pre class="devsite-click-to-copy devsite-code-highlight">"performer": {
  "@type": "PerformingGroup",
  <strong>"name": "Kira and Morrison"</strong>
}</pre>
</td>
</tr>
<tr>
<td>
<code>previousStartDate</code>
</td>
<td>
<p><a href="https://schema.org/DateTime">DateTime</a></p>
<p>The previously scheduled start date for the event if an event has been rescheduled. If
            you add <code>previousStartDate</code>, you must also add the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#eventstatus"><code>eventStatus</code></a>
            property and set the <code>eventStatus</code> to <code>EventRescheduled</code>. Don't use other event statuses.</p>
<blockquote>
            Make sure to follow the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#date-time-best-guidelines">Date and time guidelines</a>.
          </blockquote>
<p>
            For rescheduled events, the <a href="https://developers.google.com/search/docs/appearance/structured-data/event/#startdate"><code>startDate</code></a>
            property must only be used for the newly scheduled start date. In the (rare) case of an
            event that has been postponed and rescheduled multiple times, this field may be repeated.
          </p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "Event",
  "previousStartDate": ["2020-03-21T19:00-05:00", "2020-03-20T19:00-05:00", "2020-03-21T19:00-05:00"],
  "eventStatus": "https://schema.org/EventRescheduled",
  "startDate": "2020-07-21T19:00-05:00"
}</pre>
</td>
</tr>
</tbody>
</table>

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/event/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/event/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/event/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/event/#troubleshooting).
2.  [Inspect a live URL](https://support.google.com/webmasters/answer/9012289#test_live_page) to check if the issue persists.
3.  [Request validation](https://support.google.com/webmasters/answer/13300208) using the status report.

### After releasing new templates or updating your code

When you make significant changes to your website, monitor for increases in structured data invalid items.

- If you see an **increase in invalid items**, perhaps you rolled out a new template that doesn't work, or your site interacts with the existing template in a new and bad way.
- If you see a **decrease in valid items** (not matched by an increase in invalid items), perhaps you are no longer embedding structured data in your pages. Use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to learn what is causing the issue.

### Analyzing traffic periodically

Analyze your Google Search traffic using the [Performance Report](https://support.google.com/webmasters/answer/7576553). The data will show you how often your page appears as a rich result in Search, how often users click on it and what is the average position you appear on search results. You can also automatically pull these results with the [Search Console API](https://developers.google.com/webmaster-tools/search-console-api-original/v3/how-tos/search_analytics).

## Troubleshooting

If you're having trouble implementing or debugging structured data, here are some resources that may help you.

- If you're using a content management system (CMS) or someone else is taking care of your site, ask them to help you. Make sure to forward any Search Console message that details the issue to them.
- Google does not guarantee that features that consume structured data will show up in search results. For a list of common reasons why Google may not show your content in a rich result, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).
- You might have an error in your structured data. Check the [list of structured data errors](https://support.google.com/webmasters/answer/13300873) and the [Unparsable structured data report](https://support.google.com/webmasters/answer/9166415).
- If you received a structured data manual action against your page, the structured data on the page will be ignored (although the page can still appear in Google Search results). To fix [structured data issues](https://support.google.com/webmasters/answer/9044175#zippy=%2Cstructured-data-issue), use the [Manual Actions report](https://support.google.com/webmasters/answer/9044175).
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/event/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

If your event isn't appearing in the event experience on Google or if you've received a manual action for [Spammy Structured Markup](https://support.google.com/webmasters/answer/3498001?&ref_topic=6003164) in Search Console, resolve the most common issues and [review our guidelines](https://developers.google.com/search/docs/appearance/structured-data/event/#guidelines). If you're still experiencing issues, check the [Event FAQ](https://support.google.com/webmasters/thread/10549347) or post in the [Google Search Central forum](https://support.google.com/webmasters/community).

> **Google does not guarantee that your structured data will show up in search results,** even if your page is marked up correctly according to the [Rich Results Test](https://search.google.com/test/rich-results). For a list of common reasons why Google may not show your structured data in search results, see the [General Structured Data Guidelines](/appearance/structured-data/sd-policies.md).

### Event location is missing or incorrect

*error* **What caused the issue**: Google doesn't understand the values provided for the `eventLocation`, `addressLocality`, or `addressRegion` properties. Google tries to match the location information to a physical location, and the location provided is either missing or incorrect.

*done* **Fix the issue**

1.  Make sure the structured data includes values for `eventLocation`, `addressLocality`, or `addressRegion` (depending on the location, since not all of the location properties are applicable).
2.  Check that the `location.name` field uses the location name, or leave it blank if it does not have a name. A common issue is accidentally placing the event name in the `location.name` field.
3.  Validate the fix:
    1.  Open the [Rich Results Test](https://search.google.com/test/rich-results).

    2.  Enter the event posting URL in the **Fetch URL** box.

    3.  Click **Validate**.

    4.  Click **Preview**.

        **Success**: The Rich Results Test displays the correct `eventLocation` in the Google Search Preview Tool.

        **Try again**: The Rich Results Test displays "false" for the event location in the Google Search Preview Tool. Make sure the location is a real location.

### My site isn't showing up as an option for purchasing tickets

*error* **What caused the issue**: The [`offers.url`](https://developers.google.com/search/docs/appearance/structured-data/event/#offers-url) property is missing or doesn't meet the [URL requirements](https://developers.google.com/search/docs/appearance/structured-data/event/#url-requirements).

*done* **Fix the issue**

1.  Make sure that your structured data includes the [`offers.url`](https://developers.google.com/search/docs/appearance/structured-data/event/#offers-url) property.
2.  Ensure that your URL meets the [URL requirements](https://developers.google.com/search/docs/appearance/structured-data/event/#url-requirements) for `offers.url`.
3.  Ask Google to [recrawl your site](/crawling-indexing/ask-google-to-recrawl.md).
4.  Submit a [request for (re)evaluation](https://docs.google.com/forms/d/e/1FAIpQLSeoRYNFmYPdoj81jJAl9wS_0RsU-y8b9rVjHgZ1hZzCFXJ8hw/viewform).

### Time or date is incorrect

*error* **What caused the issue**: The time or date is incorrect. Common errors include not offsetting for the time zone or specifying an incorrect start time (for example, midnight as a start time).

*done* **Fix the issue**

1.  **Specify the correct local time offset**. For example, if your event starts at 7pm in New York (UTC - 5) and ends at 9pm, then the value for `startDate` is `2019-08-15T19:00:00-05:00` and the value for `endDate` is `2019-08-15T21:00:00-05:00`. If you are unable to fill in the offset for your events, don't offset the time (for example, use `2019-08-15T19:00:00`).

2.  **Make sure the start or end time is accurate**. One common mistake is setting an event to start at midnight when the event doesn't actually start at midnight. If the event is a day long event, or the start hour hasn't been announced, only specify the day. For example:

    **Recommended**: `2019-07-20`

    **Not recommended**: `2019-07-20T00:00:00`

    **Not recommended**: `2019-08-15T00:00:01+00:00`

    **Not recommended**: `2019-08-15T00:00:00+00:00`

# References & Citations

[^google-event]: Google Search Central (2026). "Event (Event) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/event. Retrieved 2026-09-14.
