---
type: Reference
title: Book actions (Book) structured data
description: Explore this guide to learn how to use book schema to provide a feed to Google and to use ReadAction to help users find your books in Google Search.
resource: https://developers.google.com/search/docs/appearance/structured-data/book
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:55:35Z'
sources:
- id: google-book
  resource: https://developers.google.com/search/docs/appearance/structured-data/book
  title: Book actions (Book) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Book actions (Book) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/book](https://developers.google.com/search/docs/appearance/structured-data/book). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-book]

Book actions make Google Search an entry point to discover books and authors. This enables Search users to quickly buy or borrow the books that they find directly from Search results. For example, a user can search for *Charlotte's Web* and be presented with results that allow them to buy or borrow the book. As a provider of books, you can provide a feed of data to Google with the structured data schema provided here. Our specification provides `ReadAction` to let users buy a book and `BorrowAction` to borrow a book.

![A book action in Search results](https://developers.google.com/static/search/docs/images/books01.png)

> **Note**: The actual appearance in search results might be different.

> **Note:** To ensure robust coverage and better serve Search users, this feature is currently limited to book providers with a wide selection of available books. If you'd like to participate, [register your interest](https://docs.google.com/forms/d/e/1FAIpQLSd0mg2Yu6kNzBjkFSWQuiu61WIXo2kBmwFuwaA3JHiw7MfCdg/viewform). If you indicate interest in this feature, it doesn't guarantee your participation.

Read actions and borrow actions, which are incorporated into the panels, display options to buy or borrow the book. Through links you provide, read actions and borrow actions send users directly from the knowledge panel and other Google surfaces to a book page on your website or app.

The order of providers in the knowledge panel is personalized and dynamic to each user. This means different users see different orderings, and the same user might see different orderings at different times. There are a variety of factors that affect a given ordering. For example, if a user clicks a given provider link in the knowledge panel often, that provider is more likely to be positioned higher in an ordering. There's no way to control the order.

## Get started

To successfully implement Book actions, you must build your feed in accordance with the Book actions [structured data type definitions](https://developers.google.com/search/docs/appearance/structured-data/book/#structured-data-type-definitions), but first review the following sections:

- [Guidelines](https://developers.google.com/search/docs/appearance/structured-data/book/#guidelines)
- [Create your feed](https://developers.google.com/search/docs/appearance/structured-data/book/#create-your-feed)
- [Test your feed with the Data Feed validation tool](https://developers.google.com/search/docs/appearance/structured-data/book/#test-your-feed-with-the-data-feed-validation-tool)
- [Host your feed file](https://developers.google.com/search/docs/appearance/structured-data/book/#host-your-feed-file)
- [Submit your feed file for review](https://developers.google.com/search/docs/appearance/structured-data/book/#submit-your-feed-file-for-review)
- [Update your feed as needed](https://developers.google.com/search/docs/appearance/structured-data/book/#update-your-feed-as-needed)

## Guidelines

To ensure that your books can be reliably surfaced in Search, it's important that you're familiar with some important details and key concepts. Further, your feed must meet some standardized format specifications.

To help you do that, follow the guidelines described here, in addition to the [general structured data guidelines](/appearance/structured-data/sd-policies.md) and the [Search Essentials](/essentials/overview.md). The guidelines are as follows:

- [Works and editions](https://developers.google.com/search/docs/appearance/structured-data/book/#works-and-editions)
- [Library systems and library members](https://developers.google.com/search/docs/appearance/structured-data/book/#library-systems-and-library-members)
- [ISBN and other supported identifiers](https://developers.google.com/search/docs/appearance/structured-data/book/#isbn-and-other-supported-identifiers)
- [Links](https://developers.google.com/search/docs/appearance/structured-data/book/#links)

### Works and editions

Throughout this documentation, we use two distinct terms when we talk about a book:

- **Work**: The abstract concept of a book. Specifically, metadata such as the title, author, and original language are attributes for a work.
- **Edition**: A concrete copy of the book. Specifically, metadata such as the year of publication, name of the edition, and International Standard Book Number (ISBN) are attributes for the edition.

For example, *Charlotte's Web* is a *work*, but every single variety it comes in is an edition. In this case, the work *Charlotte's Web* might have a first edition, second edition, abridged edition, French translation edition, and so on.

This distinction is especially important in the feed where it might not be immediately obvious. There are two [`Book` entities](https://developers.google.com/search/docs/appearance/structured-data/book/#book-entity):

- [`Book` (`Work`)](https://developers.google.com/search/docs/appearance/structured-data/book/#book-work) is the "top level" `Book` entity:
  - `workExample` is a property of `Work` and specifies one and only one instance of a `Book` (`Edition`).
  - There must be at least one `workExample` for each `Work`.
- [`Book` (`Edition`)](https://developers.google.com/search/docs/appearance/structured-data/book/#book-edition) is the "lower level" `Book` entity.

It helps to remember that there can be multiple editions of a work. We recommend that you group these editions together as much as possible. This helps Google systems leverage all of the relevant information about a book and surface it in Search. If you must, you can break them into multiple work records, but each work record must have the following:

- A different `@id`.
- At least one edition with an ISBN or other supported identifier.

### Library systems and library members

> **Note:** This section is relevant for providers who lend books.

The [`Library entity`](https://developers.google.com/search/docs/appearance/structured-data/book/#library-entity) is the "top level" `Library` entity type. It's an abstract construct, which consists of a [`LibrarySystem`](https://developers.google.com/search/docs/appearance/structured-data/book/#librarysystem) entity and each "lower level" [`Library (member)`](https://developers.google.com/search/docs/appearance/structured-data/book/#library-member) entity of that library system.

The `LibrarySystem` entity is an abstraction and represents a collaborative network of library *members*. For example, Austin Public Library can be specified as a `LibrarySystem` entity. The [Austin Public Library website](https://library.austintexas.gov/locations) describes themself as a public library *system* that serves Austin, Texas. It consists of their 20 affiliated libraries, or library *members*.

Every `LibrarySystem` entity requires at least one `Library (member)` entity, even if in real life the library isn't part of any library system. In this scenario, for the purpose of Book action implementation, the library is the sole library *member* of its own library *system*. For the purpose of Book action implementation, unlike a library *system*, a library *member* isn't an abstraction and therefore has a physical address.

Conversely, every `Library (member)` entity must belong to at least one `LibrarySystem` entity.

### ISBN and other supported identifiers

The ISBN is the main reconciliation signal when Google Search matches your feed data to Google's data. You must provide an ISBN or other supported identifier for all the books you wish to have surfaced in Search results. Without it, it's likely that your books can't be matched and therefore won't be served.

Google Search prefers ISBN-13, but you can alternatively provide the following:

- Online Computer Library Center (OCLC) Number
- Library of Congress Control Number (LCCN)
- JP e-code

> **Warning:** Google Search doesn't accept ISBN-10. For books that have only ISBN-10 information, use an ISBN conversion tool to convert to ISBN-13 before you send your feed to Google.

> **Note:** For books without an ISBN, you can still provide those books in the feed. They might not be surfaced to users in Google Search. However, the following practices might help facilitate a correct match:
>
> - Group all of the [`Edition`](https://developers.google.com/search/docs/appearance/structured-data/book/#book-edition) entities under the same [Work](https://developers.google.com/search/docs/appearance/structured-data/book/#book-work), and ensure at least one of the editions has an ISBN, OCLC Number, LCCN, or JP e-code. Google Search may be able to leverage the available ISBN or other supported identifier from another edition.
> - Add third-party identifiers. Google Search currently supports two widely used library control numbers: OCLC Number or LCCN. If you have either of these, provide them.

### Links

To make sure people have the best experience finding your books, links in your feed must adhere to the following guidelines:

- If you have duplicate pages for the same content, the link must be the [canonical URL](/crawling-indexing/consolidate-duplicate-urls.md) that contains the book title and other book information.
- After a user clicks a read action or borrow action link, the user must be sent to a page that directly supports the purchase or borrowing of the book. Specifically, don't point action links to pages with more links that must be clicked in order to purchase or borrow the content. For example, don't send people to a search results page or a product summary page.

## Create your feed

> **Note:** The use of this feature is limited to book providers that have [filled out the interest form](https://docs.google.com/forms/d/e/1FAIpQLSd0mg2Yu6kNzBjkFSWQuiu61WIXo2kBmwFuwaA3JHiw7MfCdg/viewform) and have been onboarded.

If your site sells books for users to buy, you must upload your [`Book`](https://developers.google.com/search/docs/appearance/structured-data/book/#book-entity) feed. A Google support team will reach out to you with details about how and where to upload your feed.

If your site lends books for users to borrow, you must upload two separate feeds: your [`Book`](https://developers.google.com/search/docs/appearance/structured-data/book/#book-entity) feed and your [`Library`](https://developers.google.com/search/docs/appearance/structured-data/book/#library-entity) feed. A Google support team will reach out to you with details about how and where to upload your feed.

### Adhere to feed file size, quantity, and format requirements

The requirements are as follows:

- Feed file size requirements:
  - An uncompressed feed file's size must be less than 1 GB.
  - A feed file that's to be compressed must be less than 1 GB. If your uncompressed feed file exceeds 1 GB, you must split the uncompressed feed file into multiple files.
- You can compress feed files. They must be formatted into a zip, gz, tar, tar.gz, JAR, ar, arj, cpio, or dump archive file.
- If you have multiple feed files, you can upload them as is, or if you prefer, you can include them as part of a [sitemap index file](/crawling-indexing/sitemaps/large-sitemaps.md).
- Single feed files must have the `.json` filename extension.

### Adhere to feed content requirements

Be especially aware of the following feed content requirements that you must adhere to:

- The feed mustn't contain stale entities. Stale entities are entities with `availabilityEnds` set to a date that has passed or entities that are no longer available on your site.
- All deep links, such as `urlTemplate`, and all URLs, such as `url`, that you include in your feed must be production URLs. Don't use QA, development, or any other type of non-production URL.
- All URLs, such as `url`, must be [canonical](/crawling-indexing/consolidate-duplicate-urls.md).
- Each entity in your feed must specify the following properties:
  - A unique ID: `@id`
  - A unique URL: `url`
  - A unique deep link: `urlTemplate`

## Test your feed with the Data Feed validation tool

We recommend the following troubleshooting steps for resolving common errors and warnings on the [Data Feed validation tool](https://actions.google.com/tools/feed-validator/u/0/):

- Make sure that you have the correct option selected in the **Validate on** field. Select **Books Action** for the `Book` entity.

- Verify that the value of `@type` is spelled correctly.

- Make sure that the value of `@context` is set properly. Set `"@context": "https://schema.org"` for both `ReadAction` and `BorrowAction`.

## Host your feed file

When your feed file is ready, host it at a secure location. Google fetches the feed regularly to ensure that your content is up-to-date.

### Host methods

The following feed hosting methods are supported:

<table>
<thead>
<tr>
<th><b>Hosting</b></th>
<th colspan="2"><b>Authentication Support</b></th>
</tr>
</thead>
<tbody>
<tr>
<td>Google Cloud Storage</td>
<td><i>Storage Object Viewer</i> permission</td>
</tr>
<tr>
<td>HTTPS</td>
<td>Username+Password or
            <a href="https://web.dev/articles/enable-https">HTTP client certificates</a></td>
</tr>
<tr>
<td>SFTP</td>
<td>Password, Key+Phrase, or both</td>
</tr>
<tr>
<td>AWS S3</td>
<td>Key ID+Access Key</td>
</tr>
</tbody>
</table>

## Submit your feed file for review

For your content to be available on Google Search, a Google support team reviews the quality of the deep links in your feed. We strongly recommend that you manually test some of the deep links to confirm whether they open the page where users can buy or borrow the books.

> **Note:** The successful use of this feature, along with the [interest form](https://docs.google.com/forms/d/e/1FAIpQLSd0mg2Yu6kNzBjkFSWQuiu61WIXo2kBmwFuwaA3JHiw7MfCdg/viewform) you must use to submit your feed, is limited to partners.

To request a review of your feed, provide the following:

- **Host location:** The URL of your feed file.
- **Host authentication, if applicable:** The authentication credentials to allow Google to get the feed file from your host location.

## Update your feed as needed

We recommend that you update your feed daily, but this ultimately depends on how often your catalog changes. Be aware of the following conditions and tips:

- Google Search doesn't support real-time updates.
- Google Search fetches your feed once a day and typically indexes the content within two days.
- If there's a foreseeable change in an edition's availability, use `availabilityStarts` and `availabilityEnds` to set the exact dates. If the entity is no longer available, remove the entity completely

## Structured data type definitions

You must include the required properties listed here for your content to be eligible for display in structured search results. You can also include the recommended properties to add more information about your content, which can provide a better user experience.

### DataFeed entity

Every schema.org data feed file delivered to Google must contain one single entity of [`DataFeed`](https://schema.org/DataFeed) at the root level. All [`Book`](https://developers.google.com/search/docs/appearance/structured-data/book/#book-entity) and [`Library`](https://developers.google.com/search/docs/appearance/structured-data/book/#library-entity) entities must be listed under the `dataFeedElement` field of the `DataFeed` entity.

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@context</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>https://schema.org</code>.</p>
</td>
</tr>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>DataFeed</code>.</p>
</td>
</tr>
<tr>
<td><code>dataFeedElement</code></td>
<td>
<p><a href="https://schema.org/Book"><code>Book</code></a> or
              <a href="https://schema.org/LibrarySystem"><code>LibrarySystem</code></a></p>
<p>Set to either a single
              <a href="https://schema.org/Book"><code>Book</code></a> entity or
              <a href="https://schema.org/LibrarySystem"><code>LibrarySystem</code></a>
              entity. Otherwise, set to an array of either only <code>Book</code> entities or
              <code>LibrarySystem</code> entities. Don't set this to an array that includes both
              <code>Book</code> entities and <code>LibrarySystem</code> entities.</p>
<p>Example use in a <code>Book</code> feed:</p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "DataFeed",
  "dataFeedElement": [
    {
      "@context": "https://schema.org",
      "@type": "Book",
      "@id": "https://example.com/work/the_catcher_in_the_rye",
      "url": "https://example.com/work/the_catcher_in_the_rye",
      "name": "The Catcher in the Rye",
      "author": {
        "@type": "Person",
        "name": "J.D. Salinger"
      },
      "sameAs": "https://en.wikipedia.org/wiki/The_Catcher_in_the_Rye",
      "workExample": [
        {
          "@type": "Book",
          "@id": "https://example.com/edition/the_catcher_in_the_rye_paperback",
          "isbn": "9787543321724",
          "bookEdition": "Mass Market Paperback",
          "bookFormat": "https://schema.org/Paperback",
          "inLanguage": "en",
          ...
        },
        ...
      ]
   }
  ],
  "dateModified": "2018-09-10T13:58:26.892Z"
}</pre>
<p>Example use in a <code>LibrarySystem</code> feed:</p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "DataFeed",
  "dataFeedElement": [
    {
      "@context": "https://schema.org",
      "@type": "LibrarySystem",
      "@id": "https://example.com/library-systems/100",
      "name": "Santa Clara County Library District",
      "additionalProperty": [
        {
          "@type": "PropertyValue",
          "name": "librarytype",
          "value": "public"
        }
      ],
      ...
    },
    ...
  ],
  "dateModified": "2018-09-10T13:58:26.892Z"
}</pre>
<blockquote>
<p><b>Warning:</b> As described in
                <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#create-your-feed">Create your feed</a>, if you have both a
                <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#book-entity"><code>Book</code></a> feed and a <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#library-entity"><code>Library</code></a>
                feed, they must be two separate feeds files. Therefore, for any given
                <code>DataFeed</code> entity, you can set its <code>dataFeedElement</code> property
                according to one and only one of the following conditions:</p>
<ul>
<li>Set <code>dataFeedElement</code> to either a single <code>Book</code> entity or
                  an array of <code>Book</code> entities.</li>
<li>Set <code>dataFeedElement</code> to either a single <code>LibrarySystem</code>
                  entity or an array of <code>LibrarySystem</code> entities.</li>
</ul>
</blockquote>
</td>
<tr>
<td><code>dateModified</code></td>
<td>
<p><a href="https://schema.org/DateTime"><code>DateTime</code></a></p>
<p>The date and time of the last update of the feed in the
              <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format.</p>
</td>
</tr>
</tr></tbody>
</table>

### `Book` entity

While the full definition of `Book` is available at [schema.org/Book](https://schema.org/Book), you only need to consider the following properties. You must define the required properties for every book you choose to include in your feed. You can also define recommended properties to add more information about your content, which can provide a better user experience.

#### `Book` (`Work`)

This `Book` entity is the top level entity type. It represents a *work*.

> **Key Point:** Read the [Works and editions](https://developers.google.com/search/docs/appearance/structured-data/book/#works-and-editions) guidelines to understand the difference between the two `Book` entities in your implementation.

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@context</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>https://schema.org</code>.</p>
</td>
</tr>
<tr>
<td><code>@id</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>A globally unique ID for the book in URL format. It must be unique to your
              organization. The ID must be stable and not change over time. URL format is suggested
              though not required. It doesn't have to be a working link. The domain used for the
              <code>@id</code> value must be owned by your organization.</p>
</td>
</tr>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>Book</code>.</p>
</td>
</tr>
<tr>
<td><code>author</code></td>
<td>
<p><a href="https://schema.org/Person"><code>Person</code></a> or
              <a href="https://schema.org/Organization"><code>Organization</code></a></p>
<p>The author(s) of the book.</p>
<blockquote><p><b>Note:</b> If the book doesn't have an author, but rather, one or more
              <i>contributors</i>, include these other contributors as defined in
              <a href="https://schema.org/Book">schema.org/Book</a>.
              For example, a book might have no known or recorded author, but might instead have a
              number of editors.</p>
<p>Conversely, if a book's author is an organization, define the author accordinly as
              defined in
              <a href="https://schema.org/Organization">schema.org/Organization</a>.
              For example, the author for a book titled "Fundamentals of fire fighting skills" might
              be the organization
              <code>National Fire Protection Association</code>.</p></blockquote>
</td>
</tr>
<tr>
<td><code>name</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The title of the book.</p>
</td>
</tr>
<tr>
<td><code>url</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The URL on your website where the book is introduced or described. This link helps
              accurately reconcile the content in your feed with the content in Google's
              databases. It can be the same as <code>workExample.target.urlTemplate</code>.</p>
<p>For the actual landing page, Google Search uses the URL provided in
              <code>workExample.target.urlTemplate</code>.</p>
</td>
</tr>
<tr>
<td><code>workExample</code></td>
<td>
<p><a href="https://schema.org/Book"><code>Book</code></a> <code>(Edition)</code></p>
<p>The edition(s) of the work.</p>
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
<td><code>sameAs</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The URL of a reference page that identifies the work. For example, a Wikipedia,
              Wikidata, VIAF, or Library of Congress page for the book.</p>
</td>
</tr>
</tbody>
</table>

#### `Book` (`Edition`)

The `workExample` property uses this `Book` entity. It represents an *edition* of a *work*.

> **Key Point:** Read the [Works and editions](https://developers.google.com/search/docs/appearance/structured-data/book/#works-and-editions) guidelines to understand the difference between the two `Book` entities in your implementation.

The Google-supported properties are the following:

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@id</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>A globally unique ID for the book in URL format. It must be unique to your
              organization. The ID must be stable and not change over time. URL format is suggested
              though not required. It doesn't have to be a working link. The domain used for the
              <code>@id</code> value must be owned by your organization.</p>
</td>
</tr>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>Book</code>.</p>
</td>
</tr>
<tr>
<td><code>bookFormat</code></td>
<td>
<p><a href="https://schema.org/Enumeration"><code>Enum</code></a></p>
<p>The format of the edition. The value of this must be one of the
              following:</p>
<ul>
<li><code>https://schema.org/AudiobookFormat</code></li>
<li><code>https://schema.org/EBook</code></li>
<li><code>https://schema.org/Hardcover</code></li>
<li><code>https://schema.org/Paperback</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>inLanguage</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The main language of the content in the edition. Use one of the two-letter codes
              from the <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes">list
              of ISO 639-1 alpha-2 codes</a>.</p>
</td>
</tr>
<tr>
<td><code>isbn</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The ISBN-13 of the edition. If you have ISBN-10, convert it into ISBN-13.</p>
</td>
</tr>
<tr>
<td><code>potentialAction</code></td>
<td>
<p><a href="https://schema.org/ReadAction"><code>ReadAction</code></a> or <a href="https://schema.org/BorrowAction"><code>BorrowAction</code></a></p>
<p>The action to be triggered for users to purchase or download the book. For more
              details, refer to <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#readaction-potentialaction"><code>ReadAction</code></a> or
              <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#borrowaction-potentialaction"><code>BorrowAction</code></a>.</p>
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
<td><code>author</code></td>
<td>
<p><a href="https://schema.org/Person"><code>Person</code></a> or
              <a href="https://schema.org/Organization"><code>Organization</code></a></p>
<p>The author(s) of the edition.</p>
<blockquote><p><b>Note:</b> Only use this when the author of the edition is different from
              the work author information.</p>
<p>If the edition doesn't have an author, but rather, one or more
              <i>contributors</i>, include these other contributors as defined in
              <a href="https://schema.org/Book">schema.org/Book</a>.
              For example, an edition might have no known or recorded author, but might instead have
                a number of editors.</p>
<p>Conversely, if an edition's author is an organization, define the author as defined
              in
              <a href="https://schema.org/Organization">schema.org/Organization</a>.
              For example,
              <i>Publication manual of the American Psychological Association, 6th edition</i>'s
              author might be the organization
              <code>American Psychological Association</code>.</p></blockquote>
</td>
</tr>
<tr>
<td><code>bookEdition</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The edition information of the book. For example, <code>2nd Edition</code>.</p>
</td>
</tr>
<tr>
<td><code>datePublished</code></td>
<td>
<p><a href="https://schema.org/Date"><code>Date</code></a></p>
<p>The date of publication of the edition in <var>YYYY-MM-DD</var> or <var>YYYY</var>
              format. This can be either a specific date or only a specific year.</p>
</td>
</tr>
<tr>
<td><code>identifier</code></td>
<td>
<p><a href="https://schema.org/PropertyValue"><code>PropertyValue</code></a></p>
<p>The external or other ID that unambiguously identifies this edition. Multiple
              identifiers are allowed. For more details, refer to
              <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#propertyvalue-identifier"><code>PropertyValue</code> (<code>identifier</code>)</a>.</p>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>name</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The title of the edition. Only use this when the title of the edition is different
              from the title of the work.</p>
</td>
</tr>
<tr>
<td><code>sameAs</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The URL of a reference web page that unambiguously indicates the edition. For
              example, a Wikipedia page for this specific edition. Don't reuse the
              <code>sameAs</code> of the <code>Work</code>.</p>
</td>
</tr>
<tr>
<td><code>url</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The URL on your website where the edition is introduced or described. It can be the
              same as <code>workExample.target.urlTemplate</code>.</p>
</td>
</tr>
</tbody>
</table>

Example `Book` (`Edition`):

``` devsite-click-to-copy
"workExample":
        {
          "@type": "Book",
          "@id": "https://example.com/book/100",
          "inLanguage": "en",
          "isbn": "9787543321724",
          "bookEdition": "20 Anniversary Edition",
          "datePublished": "2000-02-26",
          "bookFormat": "https://schema.org/Hardcover",
          "potentialAction": {...}
        }
```

Example `Book` (`Edition`) with multiple `workExample` properties:

``` devsite-click-to-copy
"workExample": [
        {
          "@type": "Book",
          "@id": "https://example.com/book/200",
          "inLanguage": "zh",
          "isbn": "9787543321721",
          "bookEdition": "2nd Edition",
          "bookFormat": "https://schema.org/Hardcover",
          "potentialAction": {...}
        },
        {
          "@type": "Book",
          "@id": "https://example.com/book/300",
          "inLanguage": "zh",
          "isbn": "9787543321722",
          "bookEdition": "1st Edition",
          "bookFormat": "https://schema.org/EBook",
          "potentialAction": {...}
      }
 ]
```

### `Person` or `Organization` (`author`)

The `author` property of the book uses the `Person` or `Organization` entity.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>Person</code> or <code>Organization</code>.</p>
</td>
</tr>
<tr>
<td><code>name</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The name of the person or organization.</p>
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
<td><code>sameAs</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The URL of a reference web page that unambiguously indicates the person or
              organization's identity. For example, a Wikipedia page for the person or organization.</p>
</td>
</tr>
</tbody>
</table>

Example `author`:

``` devsite-click-to-copy
"author": {
  "@type": "Person",
  "name": "William Shakespeare"
}
```

Example with multiple `author` properties:

``` devsite-click-to-copy
"author": [
  {
    "@type": "Person",
    "name": "William Shakespeare"
  },
  {
    "@type": "Person",
    "name": "Victor Hugo",
    "sameAs": "https://en.wikipedia.org/wiki/Victor_Hugo"
  }
]
```

### PropertyValue (identifier)

The `identifier` property of the `Edition` uses the `PropertyValue` entity.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>PropertyValue</code>.</p>
</td>
</tr>
<tr>
<td><code>propertyID</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The type of ID. As described in
              <a href="https://developers.google.com/search/docs/appearance/structured-data/book/#isbn-and-other-supported-identifiers">ISBN and other supported
                identifiers</a>, it must be either of the following:</p>
<ul>
<li><code>OCLC_NUMBER</code></li>
<li><code>LCCN</code></li>
<li><code>JP_E-CODE</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>value</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The ID value. The external ID that unambiguously identifies this edition. Remove all
              non-numeric prefixes of the external ID.</p>
</td>
</tr>
</tbody>
</table>

Example `identifier`:

``` devsite-click-to-copy
    "identifier": {
      "@type": "PropertyValue",
      "propertyID": "OCLC_NUMBER",
      "value":  "110123456"
    }
```

Example with multiple `identifier` properties:

``` devsite-click-to-copy
    "identifier": [
    {
      "@type": "PropertyValue",
      "propertyID": "OCLC_NUMBER",
      "value":  "110123456"
    },
    {
      "@type": "PropertyValue",
      "propertyID": "LCCN",
      "value":  "220123456"
    },{
      "@type": "PropertyValue",
      "propertyID": "JP_E-CODE",
      "value":  "12345678901234567890"
    }]
```

### Example `ReadAction` `Book` feed JSON file

``` devsite-click-to-copy
{
  "@context": "https://schema.org",
  "@type": "DataFeed",
  "dataFeedElement": [
    {
      "@context": "https://schema.org",
      "@type": "Book",
      "@id": "https://example.com/work/the_catcher_in_the_rye",
      "url": "https://example.com/work/the_catcher_in_the_rye",
      "name": "The Catcher in the Rye",
      "author": {
        "@type": "Person",
        "name": "J.D. Salinger"
      },
      "sameAs": "https://en.wikipedia.org/wiki/The_Catcher_in_the_Rye",
      "workExample": [
        {
          "@type": "Book",
          "@id": "https://example.com/edition/the_catcher_in_the_rye_paperback",
          "isbn": "9787543321724",
          "bookEdition": "Mass Market Paperback",
          "bookFormat": "https://schema.org/Paperback",
          "inLanguage": "en",
          "url": "https://example.com/edition/the_catcher_in_the_rye_paperback",
          "datePublished": "1991-05-01",
          "identifier": {
            "@type": "PropertyValue",
            "propertyID": "OCLC_NUMBER",
            "value": "1057320822"
          },
          "potentialAction": {
            "@type": "ReadAction",
            "target": {
              "@type": "EntryPoint",
              "urlTemplate": "https://example.com/store/9787543321724",
              "actionPlatform": [
                "https://schema.org/DesktopWebPlatform",
                "https://schema.org/AndroidPlatform",
                "https://schema.org/IOSPlatform"
              ]
            },
            "expectsAcceptanceOf": {
              "@type": "Offer",
              "category": "purchase",
              "price": 6.99,
              "priceCurrency": "USD",
              "availabilityStarts": "2020-01-01T11:0:00-04:00",
              "availabilityEnds": "2050-06-30T23:59:00-04:00",
              "eligibleRegion": {
                "@type": "Country",
                "name": "US"
              }
            }
          }
        },
        {
          "@type": "Book",
          "@id": "https://example.com/edition/the_catcher_in_the_rye_hardcover",
          "isbn": "9780316769532",
          "bookEdition": "Hardcover",
          "bookFormat": "https://schema.org/Hardcover",
          "inLanguage": "en",
          "url": "https://example.com/edition/the_catcher_in_the_rye_hardcover",
          "datePublished": "1951-07-16",
          "potentialAction": {
            "@type": "ReadAction",
            "target": {
              "@type": "EntryPoint",
              "urlTemplate": "https://example.com/store/9780316769532",
              "actionPlatform": [
                "https://schema.org/DesktopWebPlatform",
                "https://schema.org/AndroidPlatform",
                "https://schema.org/IOSPlatform"
              ]
            },
            "expectsAcceptanceOf": [
              {
                "@type": "Offer",
                "category": "nologinrequired",
                "availabilityStarts": "2020-01-01T11:0:00-04:00",
                "availabilityEnds": "2050-06-30T23:59:00-04:00",
                "eligibleRegion": [
                  {
                    "@type": "Country",
                    "name": "US"
                  },
                  {
                    "@type": "Country",
                    "name": "GB"
                  }
                ]
              },
              {
                "@type": "Offer",
                "category": "Subscription",
                "availabilityStarts": "2020-01-01T11:0:00-04:00",
                "availabilityEnds": "2050-06-30T23:59:00-04:00",
                "eligibleRegion": {
                  "@type": "Country",
                  "name": "IN"
                }
              }
            ]
          }
        }
      ]
    }
  ],
  "dateModified": "2018-09-10T13:58:26.892Z"
}
```

### Example `BorrowAction` `Book` feed JSON file

``` devsite-click-to-copy
{
  "@context": "https://schema.org",
  "@type": "DataFeed",
  "dataFeedElement": [
    {
      "@context": "https://schema.org",
      "@type": "Book",
      "@id": "https://example.com/work/the_catcher_in_the_rye",
      "url": "https://example.com/work/the_catcher_in_the_rye",
      "name": "The Catcher in the Rye",
      "author": {
        "@type": "Person",
        "name": "J.D. Salinger"
      },
      "sameAs": "https://en.wikipedia.org/wiki/The_Catcher_in_the_Rye",
      "workExample": [
        {
          "@type": "Book",
          "@id": "https://example.com/edition/the_catcher_in_the_rye_paperback",
          "isbn": "9787543321724",
          "bookEdition": "Mass Market Paperback",
          "bookFormat": "https://schema.org/Paperback",
          "inLanguage": "en",
          "url": "https://example.com/edition/the_catcher_in_the_rye_paperback",
          "datePublished": "1991-05-01",
          "identifier": {
            "@type": "PropertyValue",
            "propertyID": "OCLC_NUMBER",
            "value": "1057320822"
          },
          "potentialAction": {
            "@type": "BorrowAction",
            "lender": {
              "@type": "LibrarySystem",
              "@id": "https://example.com/librarySystem/100"
            },
            "target": {
              "@type": "EntryPoint",
              "urlTemplate": "https://example.com/borrowpurchase?bookId=170",
              "actionPlatform": [
                "https://schema.org/DesktopWebPlatform",
                "https://schema.org/AndroidPlatform",
                "https://schema.org/IOSPlatform"
              ]
            }
          }
        },
        {
          "@type": "Book",
          "@id": "https://example.com/edition/the_catcher_in_the_rye_hardcover",
          "isbn": "9780316769532",
          "bookEdition": "Hardcover",
          "bookFormat": "https://schema.org/Hardcover",
          "inLanguage": "en",
          "url": "https://example.com/edition/the_catcher_in_the_rye_hardcover",
          "datePublished": "1951-07-16",
          "potentialAction": {
            "@type": "BorrowAction",
            "lender": {
              "@type": "LibrarySystem",
              "@id": "https://example.com/librarySystem/100"
            },
            "target": [
              {
                "@type": "EntryPoint",
                "urlTemplate": "https://example.com/borrowpurchase?bookId=170",
                "actionPlatform": [
                  "https://schema.org/DesktopWebPlatform"
                ]
              },
              {
                "@type": "EntryPoint",
                "urlTemplate": "https://example.com/mobile/borrowpurchase?bookId=170",
                "actionPlatform": [
                  "https://schema.org/AndroidPlatform",
                  "https://schema.org/IOSPlatform"
                ]
              }
            ]
          }
        }
      ]
    }
  ],
  "dateModified": "2018-09-10T13:58:26.892Z"
}
```

### `ReadAction` (`potentialAction`)

The `potentialAction` property uses the `ReadAction` entity. `ReadAction` defines your deep links to access the book, the retailer that stocks the book, and the criteria that the users must meet. Criteria might include membership status, login status, location, or anything else required to access the book.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>ReadAction</code>.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf</code></td>
<td>
<p><a href="https://schema.org/Offer"><code>Offer</code></a></p>
<p>The definition of user requirements to access this entity. If multiple
              <code>Offer</code> properties are present, a user matching <i>any</i> of the
              <code>Offer</code> criteria might be able to access the content.</p>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>Offer</code>.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.category</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The type of <code>Offer</code>. This must be one of the following values:</p>
<ul>
<li><code>nologinrequired</code>: The action is available to the user with no purchase
                or login to access content.</li>
<li><code>free</code>: The action is available with no purchase or paid subscription
                required of the user. The action does, however, require a user to log in.</li>
<li><code>subscription</code>: The book is included with a paid subscription to your
                service.</li>
<li><code>purchase</code>: The book is accessible through a purchase.</li>
<li><code>rental</code>: The book is accessible for a finite amount of time after the
                purchase.</li>
</ul>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.eligibleRegion</code></td>
<td>
<p><a href="https://schema.org/Country"><code>Country</code></a></p>
<p>The country that's eligible for this <code>Offer</code>. This can be used to control
              the country and region where this content is or isn't available.</p>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.eligibleRegion.@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>Country</code>.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.eligibleRegion.name</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The <a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2">ISO 3166-1 alpha-2</a> country code.</p>
</td>
</tr>
<tr>
<td><code>target</code></td>
<td>
<p><a href="https://schema.org/EntryPoint"><code>EntryPoint</code></a></p>
<p>The specifications of your deep link, which includes the supported platform
              information. There can be multiple <code>EntryPoint</code> properties to define
              different deep links for different platform sets.</p>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>target.@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>EntryPoint</code>.</p>
</td>
</tr>
<tr>
<td><code>target.actionPlatform</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The platform(s) that this deep link is valid for. Use one of the following
              values:</p>
<ul>
<li><code>https://schema.org/DesktopWebPlatform</code></li>
<li><code>https://schema.org/AndroidPlatform</code></li>
<li><code>https://schema.org/IOSPlatform</code></li>
</ul>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>target.urlTemplate</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The link that takes users directly to the content of your book's landing page.</p>
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
<td><code>expectsAcceptanceOf.availabilityEnds</code></td>
<td>
<p><a href="https://schema.org/DateTime"><code>DateTime</code></a></p>
<p>The end time of the availability window. This can be used to control the exact time
              when this book must no longer be exposed to users.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.availabilityStarts</code></td>
<td>
<p><a href="https://schema.org/DateTime"><code>DateTime</code></a></p>
<p>The start time of the availability window. This can be used to control the exact
              time when this book can be exposed to users.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.price</code></td>
<td>
<p><a href="https://schema.org/Number"><code>Number</code></a></p>
<p>The purchase price of the book. This is required when the <code>Offer</code>
              property's <code>category</code> is set to <code>purchase</code> or
              <code>rental</code>.</p>
</td>
</tr>
<tr>
<td><code>expectsAcceptanceOf.priceCurrency</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The currency of the price in three-letter
              <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO
                4217</a> format.</p>
</td>
</tr>
</tbody>
</table>

Example `ReadAction`:

``` devsite-click-to-copy
"potentialAction": {
  "@type": "ReadAction",
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://example.com/purchase?bookId=170",
    "actionPlatform": [
      "https://schema.org/DesktopWebPlatform",
      "https://schema.org/AndroidPlatform",
      "https://schema.org/IOSPlatform"
    ]
  },
  "expectsAcceptanceOf": {
    "@type": "Offer",
    "category": "purchase",
    "price": 9.99,
    "priceCurrency": "USD",
    "availabilityStarts": "2018-04-01T11:01:00-04:00",
    "availabilityEnds": "2018-06-30T23:59:00-04:00",
    "eligibleRegion": {
      "@type": "Country",
      "name": "US"
    }
  }
}
```

Example `ReadAction` with multiple `EntryPoint` properties:

``` devsite-click-to-copy
"potentialAction": {
  "@type": "ReadAction",
  "target": [
    {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/purchase?bookId=170",
      "actionPlatform": [
        "https://schema.org/DesktopWebPlatform"
      ]
    },
    {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/mobile/purchase?bookId=170",
      "actionPlatform": [
        "https://schema.org/AndroidPlatform",
        "https://schema.org/IOSPlatform"
      ]
    }
  ],
  "expectsAcceptanceOf": [
    {
      "@type": "Offer",
      "category": "noLoginRequired",
      "availabilityStarts": "2018-04-01T11:01:00-04:00",
      "availabilityEnds": "2018-06-30T23:59:00-04:00",
      "eligibleRegion": [
        {
          "@type": "Country",
          "name": "US"
        },
        {
          "@type": "Country",
          "name": "GB"
        }
      ]
    },
    {
      "@type": "Offer",
      "category": "Subscription",
      "availabilityStarts": "2018-04-01T11:01:00-04:00",
      "availabilityEnds": "2018-06-30T23:59:00-04:00",
      "eligibleRegion": {
        "@type": "Country",
        "name": "IN"
      }
    }
  ]
}
```

### `BorrowAction` (`potentialAction`)

The `potentialAction` property uses the `BorrowAction` entity. `BorrowAction` defines your deep links to access the book, the library that stocks the book, and the criteria that the users must meet. Criteria might include membership status, login status, location, or anything else required to access the book.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>BorrowAction</code>.</p>
</td>
</tr>
<tr>
<td><code>lender</code></td>
<td>
<p><a href="https://schema.org/LibrarySystem"><code>LibrarySystem</code></a></p>
<p>The library system that provides access to this edition.</p>
</td>
</tr>
<tr>
<td><code>lender.@id</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The ID references of the <code>LibrarySystem</code>, which must be fully described
              separately in the library feed.</p>
</td>
</tr>
<tr>
<td><code>lender.@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>LibrarySystem</code>.</p>
</td>
</tr>
<tr>
<td><code>target</code></td>
<td>
<p><a href="https://schema.org/EntryPoint"><code>EntryPoint</code></a></p>
<p>The specifications of your deep link, which includes the supported platform
              information. To define deep links for different platform sets, specify an
              <code>EntryPoint</code> array.</p>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>target.@type</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>Set to <code>EntryPoint</code>.</p>
</td>
</tr>
<tr>
<td><code>target.actionPlatform</code></td>
<td>
<p><a href="https://schema.org/Text"><code>Text</code></a></p>
<p>The platform(s) that this deep link is valid for. Use one of the following
              values:</p>
<ul>
<li><code>https://schema.org/DesktopWebPlatform</code></li>
<li><code>https://schema.org/AndroidPlatform</code></li>
<li><code>https://schema.org/IOSPlatform</code></li>
</ul>
<p>This property can be repeated.</p>
</td>
</tr>
<tr>
<td><code>target.urlTemplate</code></td>
<td>
<p><a href="https://schema.org/URL"><code>URL</code></a></p>
<p>The link that takes users directly to the content of your book's landing page.</p>
</td>
</tr>
</tbody>
</table>

Example `BorrowAction`:

``` devsite-click-to-copy
"potentialAction": {
  "@type": "BorrowAction",
  "lender": {
    "@type": "LibrarySystem",
    "@id": "https://example.com/librarySystem/100"
  },
  "target": {
    "@type": "EntryPoint",
    "urlTemplate": "https://example.com/borrow?bookId=170",
    "actionPlatform": [
      "https://schema.org/DesktopWebPlatform",
      "https://schema.org/AndroidPlatform",
      "https://schema.org/IOSPlatform"
    ]
  }
}
```

Example `BorrowAction` with multiple `EntryPoint` properties:

``` devsite-click-to-copy
"potentialAction": {
  "@type": "BorrowAction",
  "lender": {
    "@type": "LibrarySystem",
    "@id": "https://example.com/librarySystem/100"
  },
  "target": [
    {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/borrow?bookId=170",
      "actionPlatform": [
        "https://schema.org/DesktopWebPlatform"
      ]
    },
    {
      "@type": "EntryPoint",
`      "urlTemplate": "https://example.com/mobile/borrow?bookId=170",
      "actionPlatform": [
        "https://schema.org/AndroidPlatform",
        "https://schema.org/IOSPlatform"
      ]
    }
  ]
}
```

### `Library` entity

While the full definition of `Library` is available at [schema.org/Library](https://schema.org/Library), you only need to consider the following properties. You must define the required properties for every library you choose to include in your feed. You can also define recommended properties to add more information about your content, which can provide a better user experience.

This `Library` entity is the top level `Library` entity type. It's an abstract construct, which consists of a `LibrarySystem` entity and each lower level `Library (member)` entity of that `LibrarySystem`.

The `Library` feed is distinct from the `Book` feed. Therefore, any `Library` feed you might implement must be entirely separate from your `Book` feed. For more information, refer to [Create your feed](https://developers.google.com/search/docs/appearance/structured-data/book/#create-your-feed).

> **Key Point:** Read the [Library systems and library members](https://developers.google.com/search/docs/appearance/structured-data/book/#library-systems-and-library-members) guidelines to understand the difference between the top level `Library` entity, the `LibrarySystem` entity, and the lower level `Library` entity in your implementation.

#### LibrarySystem

The `LibrarySystem` entity represents a collaborative network of library *members*.

> **Key Point:** Read the [Library systems and library members](https://developers.google.com/search/docs/appearance/structured-data/book/#library-systems-and-library-members) guidelines to understand the difference between the top level `Library` entity, the `LibrarySystem` entity, and the lower level `Library` entity in your implementation.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>@context</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Set to <code>https://schema.org</code>.</p>
</td>
</tr>
<tr>
<td>
<code>@id</code>
</td>
<td>
<code><a href="https://schema.org/URL">URL</a></code>
<p>A globally unique ID for the library system in URL
            format. The ID must be stable and not change over time. It's treated
            as an opaque string and doesn't need to be a working link. The
            domain used for the <code>@id</code> value must be owned by your
            organization.</p>
</td>
</tr>
<tr>
<td>
<code>@type</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Set to <code>LibrarySystem</code>.</p>
</td>
</tr>
<tr>
<td>
<code>additionalProperty</code>
</td>
<td>
<code><a href="https://schema.org/PropertyValue">PropertyValue</a></code>
<p>The additional property used to indicate the type of
          the library.</p>
</td>
</tr>
<tr>
<td>
<code>additionalProperty.@type</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Set to <code>PropertyValue</code>.</p>
</td>
</tr>
<tr>
<td>
<code>additionalProperty.name</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Set to <code>librarytype</code>.</p>
</td>
</tr>
<tr>
<td>
<code>additionalProperty.value</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The type of the library. Use one of the following
          values:</p>
<ul>
<li><code>public</code></li>
<li><code>academic</code></li>
<li><code>corporate</code></li>
<li><code>government</code></li>
<li><code>school</code></li>
<li><code>special</code></li>
</ul>
</td>
</tr>
<tr>
<td>
<code>member</code>
</td>
<td>
<code><a href="https://schema.org/Library">Library</a></code>
<p>The member(s) of the library system.</p>
</td>
</tr>
<tr>
<td>
<code>name</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The name of the library system. For example,
            <code>The Southwestern League of Libraries</code>.</p>
</td>
</tr>
<tr>
<td>
<code>url</code>
</td>
<td>
<code><a href="https://schema.org/URL">URL</a></code>
<p>The URL where the library system is introduced or
            described. Google Search uses this link to reconcile the content in
            your feed with the content in Google's databases. For the actual
            landing page, Google Search uses the URL provided in
            <code>workExample.target.urlTemplate</code>.</p>
</td>
</tr>
</tbody>
</table>

#### `Library` (`member`)

The `member` property of the `LibrarySystem` entity uses the `Library (member)` entity. `Library (member)` represents a single library *member* of a given library *system*.

> **Key Point:** Read the [Library systems and library members](https://developers.google.com/search/docs/appearance/structured-data/book/#library-systems-and-library-members) guidelines to understand the difference between the top level `Library` entity, the `LibrarySystem` entity, and the lower level `Library` entity in your implementation.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td>
<code>@id</code>
</td>
<td>
<code><a href="https://schema.org/URL">URL</a></code>
<p>A globally unique ID for the library branch in URL
            format. The ID must be stable and not change over time. It's treated
            as an opaque string and doesn't need to be a working link. The
            domain used for the <code>@id</code> value must be owned by your
            organization.</p>
</td>
</tr>
<tr>
<td>
<code>@type</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Set to <code>Library</code>.</p>
</td>
</tr>
<tr>
<td>
<code>location</code>
</td>
<td>
<code><a href="https://schema.org/PostalAddress">PostalAddress</a></code>
<p>The street address of the library branch. Not all
          properties apply to every country. You must include as many as apply
          to the addresses of your libraries.</p>
<p>Example United States <code>location</code>:</p>
<pre class="devsite-click-to-copy">{
  "@type": "Library",
  "@id": "https://example.com/library-branches/1001",
  "name": "Campbell Library",
  "location": {
    "@type": "PostalAddress",
    "streetAddress": "77 Harrison Ave",
    "addressLocality": "Campbell",
    "addressRegion": "CA",
    "postalCode": "95008",
    "addressCountry": "US"
  }
}</pre>
<p>Example Japan <code>location</code>:</p>
<pre class="devsite-click-to-copy">{
  "@type": "Library",
  "@id": "https://example.com/library-branches/1003",
  "name": "Tokyo Metropolitan Central Library",
  "location": {
    "@type": "PostalAddress",
    "streetAddress": "７-13-5 Minamiazabu, Minato City",
    "addressLocality": "Tokyo",
    "postalCode": "106-0047",
    "addressCountry": "JP"
  }
}</pre>
</td>
</tr>
<tr>
<td>
<code>location.@type</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>Set to <code>PostalAddress</code>.</p>
</td>
</tr>
<tr>
<td>
<code>location.addressCountry</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The country code in
            <a href="https://en.wikipedia.org/wiki/ISO_3166-1">ISO 3166-1</a>
            format. For example, <code>US</code>.</p>
</td>
</tr>
<tr>
<td>
<code>location.addressLocality</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The locality. For example,
            <code>Mountain View</code>.</p>
</td>
</tr>
<tr>
<td>
<code>location.addressRegion</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The region. For example, <code>CA</code>.</p>
</td>
</tr>
<tr>
<td>
<code>location.postalCode</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The postal code. For example,
            <code>94043</code>.</p>
</td>
</tr>
<tr>
<td>
<code>location.streetAddress</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The street address. For example,
            <code>1600 Amphitheatre Pkwy</code>.</p>
</td>
</tr>
<tr>
<td>
<code>name</code>
</td>
<td>
<code><a href="https://schema.org/Text">Text</a></code>
<p>The name of the library branch.</p>
</td>
</tr>
</tbody>
</table>

### Example `LibrarySystem` feed JSON file

``` devsite-click-to-copy
{
   "@context": "https://schema.org",
   "@type":"LibrarySystem",
   "@id":"https://example.com/library-systems/100",
   "name":"Santa Clara County Library District",
   "additionalProperty":[
      {
         "@type":"PropertyValue",
         "name":"librarytype",
         "value":"public"
      }
   ],
   "member":[
      {
         "@type":"Library",
         "@id":"https://example.com/library-branches/1001",
         "name":"Campbell Library",
         "location":{
            "@type":"PostalAddress",
            "streetAddress":"77 Harrison Ave",
            "addressLocality":"Campbell",
            "addressRegion":"CA",
            "postalCode":"95008",
            "addressCountry":"US"
         }
      },
      {
         "@type":"Library",
         "@id":"https://example.com/library-branches/1002",
         "name":"Gilroy Library",
         "location":{
            "@type":"PostalAddress",
            "streetAddress":"350 W 6th St",
            "addressLocality":"Gilroy",
            "addressRegion":"CA",
            "postalCode":"95020",
            "addressCountry":"US"
         }
      }
   ]
}
```

# References & Citations

[^google-book]: Google Search Central (2025). "Book actions (Book) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/book. Retrieved 2026-09-01.
