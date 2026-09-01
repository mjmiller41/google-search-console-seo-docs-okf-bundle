---
type: Reference
title: Visual Elements gallery of Google Search
description: Explore an illustrated guide to the most common UI elements of Google Search. Learn what the elements look like, what they're called, and whether you can optimize your website for each element.
resource: https://developers.google.com/search/docs/appearance/visual-elements-gallery
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-visual-elements-gallery
  resource: https://developers.google.com/search/docs/appearance/visual-elements-gallery
  title: Visual Elements gallery of Google Search
  author: Google Search Central (Google LLC)
  last_modified: '2026-02-04T00:00:00Z'
---

# Visual Elements gallery of Google Search

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/visual-elements-gallery](https://developers.google.com/search/docs/appearance/visual-elements-gallery). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-02-04.[^google-visual-elements-gallery]

Visual elements are the building blocks of the Google Search results page that a user can perceive or interact with. The Visual Elements gallery is an illustrated guide to the most common UI elements of Google web search: it explains what the elements look like, what they're called, and whether you can optimize your website for each element.

## Anatomy of a Google Search results page

The Google Search results page contains a set of different types of search result visual elements, and each search result has its own set of possible child visual elements. For example, a *text result* is a visual element in its own right, and it has various child visual elements, such as attribution, title link, and snippet.

How the visual elements look can change over time, and a given result can be displayed differently depending on whether you're using a desktop computer or a phone, what country you're in, the language of your search query, and many other factors. Here are the most common types of search result visual elements that you might see in Google Search:

<table>
<thead>
<tr><th colspan="2">Common types of search result visual elements</th></tr>
</thead>
<tbody>
<tr>
<td>
<p>
        Text result
      </p>
</td>
<td>
<p>
        A result in Google Search that's based on the textual content of the page. Learn more
        about the <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#text-result">text result visual elements</a>.
      </p>
</td>
</tr>
<tr>
<td>
<p>
        Rich result
      </p>
</td>
<td>
<p>
        A result that typically relies on structured data in the markup of your page to display
        graphical elements or interactive experiences. Explore the
        <a href="/appearance/structured-data/search-gallery.md">list of structured data features</a>.
      </p>
</td>
</tr>
<tr>
<td>
<p>
        Image result
      </p>
</td>
<td>
<p>
        A result that's based on an image that's embedded on that web page. An image result is
        more likely to show for image-seeking queries. Learn more about the <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#image-result">image result visual elements</a>.
      </p>
</td>
</tr>
<tr>
<td>
<p>
        Video result
      </p>
</td>
<td>
<p>
        A result that's based on a video that's embedded on that web page. A video result is
        more likely to show for video-seeking queries. Learn more about the <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#video-result">video result visual elements</a>.
      </p>
</td>
</tr>
<tr>
<td>
<p>
        Exploration features
      </p>
</td>
<td>
<p>
        A feature that helps searchers expand and refine their initial search. Learn more about
        <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#exploration">exploration features</a>.
      </p>
</td>
</tr>
</tbody>
</table>

## Attribution

Attribution describes the source of a search result, and can appear for a variety of search result types, including text, image, and video results. Attribution can include various aspects of the source, such as the name of the site, favicon, and URL to the web page.

<table>
<thead>
<tr><th colspan="2">Attribution visual elements</th></tr>
</thead>
<tbody>
<tr>
<td>
<h3>
        Favicon
      </h3>
</td>
<td>
<p>
        The small icon that's associated with the site. Learn how to <a href="/appearance/favicon-in-search.md">provide a favicon</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Site name
      </h3>
</td>
<td>
<p>
        The name of the site. Learn how to <a href="/appearance/site-names.md">provide a site name with structured data</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Visible URL
      </h3>
</td>
<td>
<p>
        The URL of the page that's shown in a readable format. A visible URL has two parts: domain and breadcrumb.
      </p>
<table>
<tr>
<td>
<h3>
        Domain
      </h3>
</td>
<td>
<p>
        The site address as defined by the domain name. This is the name you chose when setting up the website (for example, example.com).
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Breadcrumb
      </h3>
</td>
<td>
<p>
        The trail that shows the page's position within the site's hierarchy. Learn how to specify
        the trail with <a href="/appearance/structured-data/breadcrumb.md">Breadcrumb structured data</a>.
      </p>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>

## Text result

A *text result* (formerly known as a "web result" or "plain blue link") is a result in Google Search that's based on the textual content of the page. It includes visual elements such as attribution, title link, and snippet.

A text result may also include additional visual elements like rich attributes or a sitelinks group; keep in mind that a given text result may display differently depending on a variety of factors, like what device you're using, what you searched for, or what language you're using. You won't see a text result that includes all of the possible visual elements.

<table>
<thead>
<tr><th colspan="2">Text result visual elements</th></tr>
</thead>
<tbody>
<tr>
<td>
<h3>
        Attribution
      </h3>
</td>
<td>
<p>
        The source information for the web page. Learn <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#attribution">how to control attribution</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Title link
      </h3>
</td>
<td>
<p>
        The title of a search result on Google Search and other properties (for example,
        Google News) that links to the web page. Learn how to <a href="/appearance/title-link.md">influence title links</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Snippet
      </h3>
</td>
<td>
<p>
        The description or summary part of the search result on Google Search and other
        properties (for example, Google News). Learn <a href="/appearance/snippet.md">how to control snippets</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Byline date
      </h3>
</td>
<td>
<p>
        The date that Google estimates the web page was updated or published. Learn
        <a href="/appearance/publication-dates.md">how to provide a byline date</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Sitelinks group
      </h3>
</td>
<td>
<p>
        Two or more links from the same domain or its <a href="/specialty/international/localized-versions.md">localized variations</a>
        that are clustered together under a text result. For example, the links could be other
        pages on that domain, headings, or anchors within that page.
      </p>
<p>A sitelinks group contains two or more sitelinks:
      </p>
<table>
<tr>
<td>
<h3>
        Sitelink
      </h3>
</td>
<td>
<p>
        A single link within a sitelinks group. While sitelinks are automated, there are some
        <a href="/appearance/sitelinks.md">best practices you can follow for improving the quality</a>.
      </p>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>

### Text result image

A *text result image* is the most relevant image from that particular web page for the given query. Tapping it takes the user to the web page that's embedding the image. A text result image is more likely to appear for image-seeking queries.

To optimize for a text result image, follow the [Image SEO best practices](/appearance/google-images.md).

### Rich attributes

*Rich attributes* are one or more lines of additional information about the web page, such as review stars and recipe information. This information is typically powered by [structured data](/appearance/structured-data/intro-structured-data.md), provided by you.

## Image result

An *image result* is a result that's based on an image that's embedded on a web page. It's more likely to appear for image-seeking queries. To optimize your image for image results, follow the [image SEO best practices](/appearance/google-images.md).

<table>
<thead>
<tr><th colspan="2">Image result visual elements</th></tr>
</thead>
<tbody>
<tr>
<td>
<h3>
        Image thumbnail
      </h3>
</td>
<td>
<p>
        An image thumbnail for the indexed image that's embedded on a web page. Tapping or clicking
        it takes the user to the image. To optimize your image for image results, follow the
        <a href="/appearance/google-images.md">image SEO best practices</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Attribution
      </h3>
</td>
<td>
<p>
        The source information for the web page that's embedding the image. Learn <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#attribution">how to control attribution</a>.
      </p>
</td>
</tr>
</tbody>
</table>

## Video result

A *video result* is a result that's based on a video that's embedded on a web page. It's more likely to appear for video-seeking queries. To optimize your video for video results, follow the [video best practices](/appearance/video.md).

<table>
<thead>
<tr><th colspan="2">Video result visual elements</th></tr>
</thead>
<tbody>
<tr>
<td>
<h3>
        Video thumbnail
      </h3>
</td>
<td>
<p>
        A video thumbnail for the indexed video that's embedded on a web page. Tapping or clicking
        it takes the user to the web page that's embedding the video. Learn how to
        <a href="/appearance/video.md">specify a video thumbnail</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Title link
      </h3>
</td>
<td>
<p>
        The title link for the video landing page. Learn how to <a href="/appearance/title-link.md">influence title links</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Attribution
      </h3>
</td>
<td>
<p>
        The source information for the video landing page. Learn <a href="https://developers.google.com/search/docs/appearance/visual-elements-gallery/#attribution">how to control attribution</a>.
      </p>
</td>
</tr>
<tr>
<td>
<h3>
        Upload date
      </h3>
</td>
<td>
<p>
        The date that the video was published as provided in its metadata. Learn
        <a href="/appearance/video.md">optimize your videos</a>.
      </p>
</td>
</tr>
</tbody>
</table>

## Exploration features

Exploration features help searchers explore more questions or searches that are related to their original search query (also known as "People also ask"). While you can't control what shows up here, it can be helpful to pay attention to the related search queries when you're thinking about topics you could write about for your site.

### Related searches group

![An illustration of how a related searches group could look in Google Search, which shows a series of related things that other people have searched for](https://developers.google.com/static/search/docs/images/related-searches-group.png)

A *related searches group* is a cluster of related searches that other people have done. Tapping or clicking a related search takes the user to another search results page. These searches are automatically generated based on the initial query and other things people have searched for.

### Related questions group

![An illustration of how a related questions group could look in Google Search, which shows a series of questions that are related to what the user initially searched for](https://developers.google.com/static/search/docs/images/related-questions-group.png)

A *related questions group* is a cluster of questions that are related to what the user initially searched for (also known as "People Also Ask"). When a user expands the question, they're shown a featured snippet. Learn how to [manage featured snippets](/appearance/featured-snippets.md).

# References & Citations

[^google-visual-elements-gallery]: Google Search Central (2026). "Visual Elements gallery of Google Search". *Google for Developers*. https://developers.google.com/search/docs/appearance/visual-elements-gallery. Retrieved 2026-09-01.
