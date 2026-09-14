---
type: Reference
title: Video (VideoObject, Clip, BroadcastEvent) structured data
description: When you add video structured data, you can make it easier for Google to find your video and influence information that's shown in video results on Google, such as the video's thumbnail image, title, and description.
resource: https://developers.google.com/search/docs/appearance/structured-data/video
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-video
  resource: https://developers.google.com/search/docs/appearance/structured-data/video
  title: Video (VideoObject, Clip, BroadcastEvent) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Video (VideoObject, Clip, BroadcastEvent) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/video](https://developers.google.com/search/docs/appearance/structured-data/video). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-video]

While Google tries to automatically understand details about your video, you can influence the information that's shown in video results, such as the description, thumbnail URL, upload date, and duration, by marking up your video with [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object). Adding video structured data to your [watch pages](/appearance/video.md) can also make it easier for Google to find your video. Videos can appear in several different places on Google, including the main search results page, Video mode, Google Images, and [Google Discover](/appearance/google-discover.md).

![Video content in Google search results, the video tab, and Discover](https://developers.google.com/static/search/docs/images/video-on-google.png)

Based on how you mark up your watch page, your videos may also be eligible for the following specific video features:

<table>
<th colspan="2"><b>Video features</b></th>
<tr>
<td><p>
<b>LIVE badge</b>: Get a LIVE badge added to your video by marking your video with
      <a href="https://developers.google.com/search/docs/appearance/structured-data/video/#broadcast-event"><code>BroadcastEvent</code></a>. The LIVE badge can be applied to
      any public video that is live-streamed for any length of time. Here are a few examples:</p>
<ul>
<li>Sporting events</li>
<li>Awards shows</li>
<li>Influencer videos</li>
<li>Live streaming video games</li>
</ul>
<p>
        Make sure you follow the <a href="https://developers.google.com/search/docs/appearance/structured-data/video/#livestream-guidelines">LIVE badge guidelines</a> and use
        the <a href="https://developers.google.com/search/apis/indexing-api/v3/quickstart">Indexing API</a> to make sure
        Google crawls your page at the right time.
      </p>
</td>
<td>
<img alt="Video with a LIVE badge in search results" src="https://developers.google.com/static/search/docs/images/video-livestream.png"/>
</td>
</tr>
<tr>
<td>
<p>
<b>Key moments</b>
</p>
<p>
    The key moments feature is a way for users to navigate video segments like chapters in a book,
    which can help users engage more deeply with your content. Google Search tries to automatically
    detect the segments in your video and show key moments to users, without any effort on your
    part. Alternatively, you can tell Google about the important points of your video. We
    will prioritize key moments set by you, either through structured data or the YouTube description.
  </p>
<ul>
<li><b>If your video is embedded on your web page or you're running a video platform</b>, there are two ways that you can enable key moments:
      <ul>
<li><a href="/appearance/structured-data/video.md"><code>Clip</code> structured data</a>:
          Specify the exact start and end time to each segment, and what label to display for each
          segment. This is supported in all languages where Google Search is available.</li>
<li><a href="/appearance/structured-data/video.md"><code>SeekToAction</code> structured data</a>:
          Tell Google where timestamps typically go in your URL structure, so that Google can
          automatically identify key moments and link users to those points within the video. This
          is supported for the following languages: English, Spanish, Portuguese, Italian, Chinese,
          French, Japanese, German, Turkish, Korean, Dutch, and Russian.
        </li>
</ul>
</li>
<li><b>If your video is hosted on YouTube</b>, you can specify the exact timestamps and labels
       in the video description on YouTube. Check out the
      <a href="/appearance/structured-data/video.md">best practices for marking timestamps in YouTube descriptions</a>.
      This is supported in all languages where Google Search is available. If you want to enable
      Video Chapters on YouTube, follow these
        <a href="https://support.google.com/youtube/answer/9884579">additional guidelines</a>.
    </li>
</ul>
<p>To opt out of the key moments feature completely (including any efforts Google may make to show
    key moments automatically for your video), use the
  <a href="/appearance/snippet.md"><code>nosnippet</code></a> <code>meta</code> tag.
  </p>
</td>
<td>
<img alt="Video with key moments in search results" src="https://developers.google.com/static/search/docs/images/video-key-moments.png"/>
</td>
</tr>
</table>

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/video/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/video/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

### Standard video result

![Example of standard video search results](https://developers.google.com/static/search/docs/images/video-search-results.png)

Here's an example of a single [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object).

JSON-LD

  

``` devsite-click-to-copy
<html>
  <head>
    <title>Introducing the self-driving bicycle in the Netherlands</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "VideoObject",
      "name": "Introducing the self-driving bicycle in the Netherlands",
      "description": "This spring, Google is introducing the self-driving bicycle in Amsterdam, the world's premier cycling city. The Dutch cycle more than any other nation in the world, almost 900 kilometres per year per person, amounting to over 15 billion kilometres annually. The self-driving bicycle enables safe navigation through the city for Amsterdam residents, and furthers Google's ambition to improve urban mobility with technology. Google Netherlands takes enormous pride in the fact that a Dutch team worked on this innovation that will have great impact in their home country.",
      "thumbnailUrl": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "uploadDate": "2024-03-31T08:00:00+08:00",
      "duration": "PT1M54S",
      "contentUrl": "https://www.example.com/video/123/file.mp4",
      "embedUrl": "https://www.example.com/embed/123",
      "interactionStatistic": {
        "@type": "InteractionCounter",
        "interactionType": { "@type": "WatchAction" },
        "userInteractionCount": 5647018
      },
      "regionsAllowed": ["US", "NL"]
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

Microdata

  

``` devsite-click-to-copy
<html itemscope itemprop="VideoObject" itemtype="https://schema.org/VideoObject">
<head>
  <title itemprop="name">Introducing the self-driving bicycle in the Netherlands</title>
</head>
<body>
  <meta itemprop="uploadDate" content="2024-03-31T08:00:00+08:00" />
  <meta itemprop="duration" content="PT1M54S" />
  <p itemprop="description">This spring, Google is introducing the self-driving bicycle in Amsterdam, the world's premier cycling city. The Dutch cycle more than any other nation in the world, almost 900 kilometres per year per person, amounting to over 15 billion kilometres annually. The self-driving bicycle enables safe navigation through the city for Amsterdam residents, and furthers Google's ambition to improve urban mobility with technology. Google Netherlands takes enormous pride in the fact that a Dutch team worked on this innovation that will have great impact in their home country.</p>
  <div itemprop="interactionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
    <meta itemprop="userInteractionCount" content="5647018" />
    <meta itemprop="interactionType" itemtype="https://schema.org/WatchAction" />
  </div>
  <link itemprop="embedUrl" href="https://www.example.com/embed/123" />
  <meta itemprop="contentUrl" content="https://www.example.com/video/123/file.mp4" />
  <meta itemprop="regionsAllowed" content="US" />
  <meta itemprop="regionsAllowed" content="NL" />
  <meta itemprop="thumbnailUrl" content="https://example.com/photos/1x1/photo.jpg" />
</body>
</html>
```

### LIVE badge

![Example of a video in search results with a LIVE badge](https://developers.google.com/static/search/docs/images/video-livestream.png)

Here's an example of [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object) and [`BroadcastEvent`](https://developers.google.com/search/docs/appearance/structured-data/video/#broadcast-event).

JSON-LD

  

``` devsite-click-to-copy
<html>
  <head>
    <title>Bald Eagle at the Park - Livestream</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "VideoObject",
      "contentURL": "https://example.com/bald-eagle-at-the-park.mp4",
      "description": "Bald eagle at the park livestream.",
      "duration": "PT37M14S",
      "embedUrl": "https://example.com/bald-eagle-at-the-park",
      "expires": "2024-10-30T14:37:14+00:00",
      "regionsAllowed": "US",
      "interactionStatistic": {
        "@type": "InteractionCounter",
        "interactionType": { "@type": "WatchAction" },
        "userInteractionCount": 4756
      },
      "name": "Bald eagle nest livestream!",
      "thumbnailUrl": "https://example.com/bald-eagle-at-the-park",
      "uploadDate": "2024-10-27T14:00:00+00:00",
      "publication": [
        {
          "@type": "BroadcastEvent",
          "isLiveBroadcast": true,
          "startDate": "2024-10-27T14:00:00+00:00",
          "endDate": "2024-10-27T14:37:14+00:00"
        },
        {
          "@type": "BroadcastEvent",
          "isLiveBroadcast": true,
          "startDate": "2024-10-27T18:00:00+00:00",
          "endDate": "2024-10-27T18:37:14+00:00"
        }
      ]
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

Microdata

  

``` devsite-click-to-copy
<html itemscope itemprop="VideoObject" itemtype="https://schema.org/VideoObject">
<head>
  <title itemprop="name">Bald Eagle at the Park - Livestream</title>
</head>
<body>
  <meta itemprop="uploadDate" content="2024-10-27T14:00:00+00:00" />
  <meta itemprop="duration" content="PT37M14S" />
  <p itemprop="description">Bald eagle at the park livestream.</p>
  <div itemprop="interactionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
    <meta itemprop="userInteractionCount" content="4756" />
    <meta itemprop="interactionType" itemtype="https://schema.org/WatchAction" />
  </div>
  <link itemprop="embedUrl" href="https://example.com/bald-eagle-at-the-park" />
  <meta itemprop="expires" content="2024-10-30T14:37:14+00:00" />
  <meta itemprop="contentUrl" content="https://example.com/bald-eagle-at-the-park.mp4" />
  <meta itemprop="regionsAllowed" content="US" />
  <meta itemprop="thumbnailUrl" content="https://example.com/bald-eagle-at-the-park" />
  <div itemprop="publication" itemtype="https://schema.org/BroadcastEvent" itemscope>
    <meta itemprop="isLiveBroadcast" content="true" />
    <meta itemprop="startDate" content="2024-10-27T14:00:00+00:00" />
    <meta itemprop="endDate" content="2024-10-27T14:37:14+00:00" />
  </div>
  <div itemprop="publication" itemtype="https://schema.org/BroadcastEvent" itemscope>
    <meta itemprop="isLiveBroadcast" content="true" />
    <meta itemprop="startDate" content="2024-10-27T18:00:00+00:00" />
    <meta itemprop="endDate" content="2024-10-27T18:37:14+00:00" />
  </div>
</body>
</html>
```

### `Clip`

![Example of a video in search results with key moments](https://developers.google.com/static/search/docs/images/video-key-moments.png)

Here's an example of [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object) and [`Clip`](https://developers.google.com/search/docs/appearance/structured-data/video/#clip).

JSON-LD

  

``` devsite-click-to-copy
<html>
  <head>
    <title>Cat jumps over the fence</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org/",
      "@type": "VideoObject",
      "name": "Cat video",
      "duration": "PT10M",
      "uploadDate": "2024-07-19T08:00:00+08:00",
      "thumbnailUrl": "https://www.example.com/cat.jpg",
      "description": "Watch this cat jump over a fence!",
      "contentUrl": "https://www.example.com/cat_video_full.mp4",
      "ineligibleRegion": "US",
      "hasPart": [{
        "@type": "Clip",
        "name": "Cat jumps",
        "startOffset": 30,
        "endOffset": 45,
        "url": "https://www.example.com/example?t=30"
      },
      {
        "@type": "Clip",
        "name": "Cat misses the fence",
        "startOffset": 111,
        "endOffset": 150,
        "url": "https://www.example.com/example?t=111"
      }]
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

Microdata

  

``` devsite-click-to-copy
<html itemscope itemprop="VideoObject" itemtype="https://schema.org/VideoObject">
<head>
  <title itemprop="name">Cat jumps over the fence</title>
</head>
<body>
  <meta itemprop="uploadDate" content="2024-07-19" />
  <meta itemprop="duration" content="P10M" />
  <p itemprop="description">Watch this cat jump over a fence!</p>
  <div itemprop="interactionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
    <meta itemprop="userInteractionCount" content="5647018" />
    <meta itemprop="interactionType" itemtype="https://schema.org/WatchAction" />
  </div>
  <div itemprop="hasPart" itemtype="https://schema.org/Clip" itemscope>
    <meta itemprop="name" content="Cat jumps" />
    <meta itemprop="startOffset" content="30" />
    <meta itemprop="endOffset" content="45" />
    <meta itemprop="url" content="https://www.example.com/example?t=30" />
  </div>
  <div itemprop="hasPart" itemtype="https://schema.org/Clip" itemscope>
    <meta itemprop="name" content="Cat misses the fence" />
    <meta itemprop="startOffset" content="111" />
    <meta itemprop="endOffset" content="150" />
    <meta itemprop="url" content="https://www.example.com/example?t=111" />
  </div>
  <link itemprop="embedUrl" href="https://www.example.com/embed/123" />
  <meta itemprop="contentUrl" content="https://www.example.com/cat_video_full.mp4" />
  <meta itemprop="ineligibleRegion" content="US" />
  <meta itemprop="thumbnailUrl" content="https://www.example.com/cat.jpg" />
</body>
</html>
```

### `SeekToAction`

Here's an example of a single [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object) that includes the [additional properties](https://developers.google.com/search/docs/appearance/structured-data/video/#seek) needed for `SeekToAction` markup.

JSON-LD

  

``` devsite-click-to-copy
<html>
  <head>
    <title>John Smith (@johnsmith123) on VideoApp: My daily workout! #stayingfit</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "VideoObject",
      "potentialAction" : {
        "@type": "SeekToAction",
        "target": "https://video.example.com/watch/videoID?t={seek_to_second_number}",
        "startOffset-input": "required name=seek_to_second_number"
      },
      "name": "My daily workout!",
      "uploadDate": "2024-07-19T08:00:00+08:00",
      "thumbnailUrl": "https://www.example.com/daily-workout.jpg",
      "description": "My daily workout!",
      "embedUrl": "https://example.com/daily-workout"
    }
    </script>
  </head>
  <body>
  </body>
</html>
```

Microdata

  

``` devsite-click-to-copy
<html itemscope itemprop="VideoObject" itemtype="https://schema.org/VideoObject">
<head>
  <title itemprop="name">John Smith (@johnsmith123) on VideoApp: My daily workout! #stayingfit</title>
</head>
<body>
  <meta itemprop="uploadDate" content="2024-07-19" />
  <p itemprop="description">My daily workout!</p>
  <div itemprop="potentialAction" itemtype="https://schema.org/SeekToAction" itemscope>
    <meta itemprop="target" content="https://video.example.com/watch/videoID?t={seek_to_second_number}" />
    <meta itemprop="startOffset-input" content="required name=seek_to_second_number" />
  </div>
  <link itemprop="embedUrl" href="https://example.com/daily-workout" />
  <meta itemprop="thumbnailUrl" content="https://www.example.com/daily-workout.jpg" />
</body>
</html>
```

## Guidelines

For your video structured data to be eligible for usage in Google Search, you must follow the [Search Essentials](/essentials/overview.md), [general structured data guidelines](/appearance/structured-data/sd-policies.md), and [video indexing requirements](/appearance/video.md).

> **Warning:** If Google detects that some of the markup on your pages may be using techniques that are outside our structured data guidelines, your site may receive a [manual action](https://support.google.com/webmasters/answer/9044175).

In addition, we recommend that you check out these guidelines if they apply to your video content:

- [Livestream guidelines](https://developers.google.com/search/docs/appearance/structured-data/video/#livestream-guidelines)
- [`Clip` and `SeekToAction` guidelines](https://developers.google.com/search/docs/appearance/structured-data/video/#clip-guidelines)
- [Best practices for marking timestamps on YouTube](https://developers.google.com/search/docs/appearance/structured-data/video/#best-practices-youtube)

### LIVE badge guidelines

If you're adding [`BroadcastEvent`](https://developers.google.com/search/docs/appearance/structured-data/video/#broadcast-event) to livestream videos, follow these guidelines:

- Don't use vulgar or potentially offensive language in the structured data.

- To make sure Google crawls your livestream video at the right time, use the [Indexing API](https://developers.google.com/search/apis/indexing-api/v3/quickstart). Call the API for the following events:

  - When the video goes live
  - When the video has stopped streaming, and the page's markup has been updated to indicate the `endDate`
  - Whenever a change has happened in the markup and Google needs to be notified

  > The Indexing API only supports livestream videos.

### Best practices for marking timestamps on YouTube

If your video is hosted on YouTube, Google Search may automatically enable key moments for your video based on the video description on YouTube, and you may not have to mark specific timestamps in your YouTube description. However, you can tell us more explicitly about the important points in your video and we will prefer that information. The following diagram shows how timestamps and labels in a YouTube video description can appear in search results:

![A video in search results with timestamps and labels](https://developers.google.com/static/search/docs/images/video-timestamps-on-youtube.png)

**1. Label**: The name of the clip.  
**2. Timestamp**: When a clip starts.

Keep in mind the following guidelines when formatting timestamps and labels for YouTube descriptions:

- Format the timestamp in the following format: `[hour]:[minute]:[second]`. If there's no hour, you don't need to include it.
- Specify the label of the timestamp on the same line as the timestamp.
- Place each timestamp on a new line in the video description.
- Link the timestamp to the specified point in the video.
- Make sure the label contains at least one word.
- List the timestamps in chronological order.

If you want to enable Video Chapters on YouTube, follow these [additional guidelines](https://support.google.com/youtube/answer/9884579).

### `Clip` and `SeekToAction` guidelines

If you're adding [`Clip`](https://developers.google.com/search/docs/appearance/structured-data/video/#clip) or [`SeekToAction`](https://developers.google.com/search/docs/appearance/structured-data/video/#seek) structured data to mark video segments, follow these guidelines:

- The video must have the ability to deep link into some point other than the start point in the video URL. For example, `https://www.example.com/example?t=30` starts 30 seconds into a video.
- `VideoObject` structured data must be added to a page where users can watch the video. It's a bad user experience to point users to a page where they can't watch the video.
- The total video duration must be a minimum of 30 seconds.
- The video must include the required properties that are listed in the [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object) structured data documentation.
- **For `Clip` structured data only**: Make sure that no two clips on the same video defined on the same page share a start time.
- **For `SeekToAction` structured data only**: Google must be able to [fetch your video content files](/appearance/video.md).

## Structured data type definitions

This section describes the structured data types related to video features in Google Search. You must include the required [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object) properties for your markup to be eligible for usage in Google Search. You can also include the recommended properties to add more information about your `VideoObject`, which could provide a better user experience. In addition to [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object), you can add the following data types to enable video enhancements in Google Search:

- **[`BroadcastEvent`](https://developers.google.com/search/docs/appearance/structured-data/video/#broadcast-event)**: Mark up livestream videos to enable a LIVE badge on your video.
- **[`Clip`](https://developers.google.com/search/docs/appearance/structured-data/video/#clip)**: Mark important segments in your video to help users quickly navigate to specific points in a video.
- **[`SeekToAction`](https://developers.google.com/search/docs/appearance/structured-data/video/#seek)**: Enable key moments by indicating how your URL structure works, so that Google can automatically identify key moments and link users to those points within the video.

### `VideoObject`

The full definition of `VideoObject` is available at [schema.org/VideoObject](https://schema.org/VideoObject). If you don't include the required properties, Google may not be able to extract any information about the video. You can also include the recommended properties to add more information about your content, which could provide a better user experience.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The title of the video. Make sure to use unique text in the <code>name</code> property
        for each video on your site.</p></td>
</tr>
<tr>
<td><code>thumbnailUrl</code></td>
<td><p>Repeated <code><a href="https://schema.org/URL">URL</a></code></p>
<p>A URL pointing to the video's unique thumbnail image file. Follow the <a href="/appearance/video.md">thumbnail image guidelines</a>.</p>
</td>
</tr>
<tr>
<td><code>uploadDate</code></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the video was first published, in
          <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.
          We recommend that you provide timezone information; otherwise, we will default to
          <a href="/crawling-indexing/googlebot.md">the timezone used by Googlebot</a>.</p>
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
<code>contentUrl</code>
</td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<blockquote>We recommend that your provide the <code>contentUrl</code>
          property, if possible. This is the most effective way for Google to fetch your video
          content files. If <code>contentUrl</code> isn't available, provide <code>embedUrl</code> as an alternative.</blockquote>
<p>A URL pointing to the video file's actual content bytes, in one of the
          <a href="/appearance/video.md">supported file types</a>.
          Don't link to the page where the video lives; this must be the
          URL of the video file's actual content bytes itself.</p>
<pre class="devsite-click-to-copy">"contentUrl": "https://www.example.com/video/123/file.mp4"</pre>
<p>Make sure to follow our
          <a href="/appearance/video.md">video best practices</a>.</p>
<blockquote><b>Tip</b>: You can ensure that only Googlebot accesses your
            content by using a
          <a href="https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot">reverse DNS lookup</a>.
        </blockquote>
</td>
</tr>
<tr>
<td><code>description</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The description of the video. Make sure to use unique text in the <code>description</code> property
        for each video on your site. HTML tags are ignored.</p></td>
</tr>
<tr>
<td><code>duration</code></td>
<td><p><code><a href="https://schema.org/Duration">Duration</a></code></p>
<p>The duration of the video in
        <a href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 format</a>.
        For example, <code>PT00H30M5S</code> represents a duration of "thirty minutes and five seconds".</p>
</td>
</tr>
<tr>
<td>
<code>embedUrl</code>
</td>
<td>
<p><code><a href="https://schema.org/URL">URL</a></code></p>
<blockquote>We recommend that your provide the <code>contentUrl</code>
        property, if possible. This is the most effective way for Google to fetch your video
        content files. If <code>contentUrl</code> isn't available, provide <code>embedUrl</code> as an alternative.</blockquote>
<p>A URL pointing to a player for the specific video. Don't link to the page where the
          video lives; this must be the URL of the video player itself. Usually this is the information in
          the <code>src</code> attribute of an <code>&lt;embed&gt;</code> element.</p>
<pre class="devsite-click-to-copy">"embedUrl": "https://www.example.com/embed/123"</pre>
<p>Make sure to follow our
        <a href="/appearance/video.md">Video best practices</a>.</p>
<blockquote><b>Tip</b>: You can ensure that only Googlebot accesses your
          content by using a <a href="https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot">reverse DNS lookup</a>.</blockquote>
</td>
</tr>
<tr>
<td><code>expires</code></td>
<td><code><a href="https://schema.org/DateTime">DateTime</a></code>
<p>If applicable, the date and time after which the video will no longer be available, in
          <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>. Don't
          supply this information if your video does not expire. We recommend that you provide
          timezone information; otherwise, we will default to
          <a href="/crawling-indexing/googlebot.md">the timezone used by Googlebot</a>.</p></td>
</tr>
<tr>
<td>
<code>hasPart</code>
</td>
<td>
<p>If your video has important segments, nest the <a href="https://developers.google.com/search/docs/appearance/structured-data/video/#clip">required <code>Clip</code> properties</a> in your <code>VideoObject</code>. For example:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">&lt;script type="application/ld+json"&gt;
{
  "@context": "https://schema.org/",
  "@type": "VideoObject",
  "name": "Cat video",
  <strong>"hasPart": {
    "@type": "Clip",
    "name": "Cat jumps",
    "startOffset": 30,
    "url": "https://www.example.com/example?t=30"
  }</strong>
}
&lt;/script&gt;</pre>
</td>
</tr>
<tr>
<td><code>ineligibleRegion</code>
</td>
<td><p><code><a href="https://schema.org/Place">Place</a></code></p>
<p>The region where the video isn't allowed, if applicable. If not specified, then Google assumes the video is
        allowed everywhere. Specify the countries in
        <a href="https://en.wikipedia.org/wiki/ISO_3166-1">two- or three-letter ISO 3166-1 format</a>. For
        multiple values, use multiple country codes (for example, a JSON-LD array or multiple
        <code>meta</code> tags in Microdata).</p>
<blockquote>We also support the <a href="https://developers.google.com/search/docs/appearance/structured-data/video/#regions-allowed"><code>regionsAllowed</code></a>
          property. Add either <code>ineligibleRegion</code> or <code>regionsAllowed</code>,
          whichever makes sense for your site.
        </blockquote>
</td>
</tr>
<tr>
<td><code>interactionStatistic</code></td>
<td><p><code><a href="https://schema.org/InteractionCounter">InteractionCounter</a></code></p>
<p>The number of times the video has been watched. For example:</p>
<pre class="devsite-click-to-copy">"interactionStatistic":
  {
    "@type": "InteractionCounter",
    "interactionType": { "@type": "WatchAction" },
    "userInteractionCount": 12345
  }</pre>
<blockquote>Starting October 2019, we changed our documentation to recommend
        <code>interactionStatistic</code> instead of <code>interactionCount</code>. While we continue
         to support <code>interactionCount</code>, we recommend <code>interactionStatistic</code>
          moving forward.</blockquote>
</td>
</tr>
<tr>
<td>
<code>publication</code>
</td>
<td>
<p>If your video is happening live and you want to be eligible for the LIVE badge, nest
          the <a href="https://developers.google.com/search/docs/appearance/structured-data/video/#broadcast-event"><code>BroadcastEvent</code> properties</a> in your
          <code>VideoObject</code>. For example:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">&lt;script type="application/ld+json"&gt;
{
  "@context": "https://schema.org/",
  "@type": "VideoObject",
  "name": "Cat video",
  <strong>"publication": {
    "@type": "BroadcastEvent",
    "name": "First scheduled broadcast",
    "isLiveBroadcast": true,
    "startDate": "2018-10-27T14:00:00+00:00",
    "endDate": "2018-10-27T14:37:14+00:00"
  }</strong>
}
&lt;/script&gt;</pre>
</td>
</tr>
<tr>
<td><code>regionsAllowed</code>
</td>
<td><p><code><a href="https://schema.org/Place">Place</a></code></p>
<p>The regions where the video is allowed, if applicable. If not specified, then Google assumes the video is
        allowed everywhere. Specify the countries in
        <a href="https://en.wikipedia.org/wiki/ISO_3166-1">two- or three-letter ISO 3166-1 format</a>.
        For multiple values, use multiple country codes (for example, a JSON-LD array or multiple
        <code>meta</code> tags in Microdata).
      </p>
<blockquote>We also support the <a href="https://developers.google.com/search/docs/appearance/structured-data/video/#ineligible-region"><code>ineligibleRegion</code></a>
          property. Add either <code>ineligibleRegion</code> or <code>regionsAllowed</code>,
          whichever makes sense for your site.
        </blockquote>
</td>
</tr>
</tbody>
</table>

### `BroadcastEvent`

To be eligible for display with a LIVE badge, nest the following properties in your [VideoObject](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object). While `BroadcastEvent` properties aren't required, you must add the following properties if you want your video to display with a LIVE badge.

The full definition of `BroadcastEvent` is available at [schema.org/BroadcastEvent](https://schema.org/BroadcastEvent).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>publication</code>
</td>
<td><p><code><a href="https://schema.org/BroadcastEvent">BroadcastEvent</a></code></p>
<p>Describes when the video is to be streamed live. Can be a list or a single instance.</p>
</td>
</tr>
<tr>
<td><code>publication.endDate</code>
</td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>Time and date of when the livestream ends or is expected to end, in
          <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.</p>
<p>It's required to provide the <code>endDate</code> once the video has finished and is no
          longer live. If the expected <code>endDate</code> is unknown prior to the livestream
          starting, we recommend providing an approximate <code>endDate</code>.</p>
<p>If <code>endDate</code> is in the past or present, it indicates stream actually ended
          and is no longer live. If <code>endDate</code> is in the future, it indicates stream is
          scheduled to end at that time.</p>
</td>
</tr>
<tr>
<td><code>publication.isLiveBroadcast</code></td>
<td><p>Boolean</p>
<p>
          Set to <code>true</code> if the video is, has been, or will be streamed live.
        </p>
</td>
</tr>
<tr>
<td><code>publication.startDate</code>
</td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>Time and date of when the livestream starts or is expected to start, in
          <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>. If
          <code>startDate</code> is in the past or present, it indicates that the stream actually
          started. If <code>startDate</code> is in the future, it indicates stream is
          scheduled to start at that time.</p>
</td>
</tr>
</tbody>
</table>

### `Clip`

To tell Google what timestamp and label to use for the key moments feature, nest the following properties in your [`VideoObject`](/appearance/structured-data/video.md). While `Clip` properties aren't required, you must add the following properties if you want Google to show the timestamps and labels that you specify for your video, instead of the video segments that Google may automatically show for your video.

The full definition of `Clip` is available at [schema.org/Clip](https://schema.org/Clip).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>name</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>A descriptive title for the content of the clip.</p></td>
</tr>
<tr>
<td><code>startOffset</code></td>
<td><p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The start time of the clip expressed as the number of seconds from the beginning of the
          work.</p></td>
</tr>
<tr>
<td><code>url</code></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>A URL that points to the start time of the clip.</p>
<p>The clip URL must point to the same URL path as the video with additional query
          parameters that specify the time. </p>
<p>For example, the following URL means the video starts at 2:00 minutes:</p>
<pre class="devsite-click-to-copy">"url": "https://www.example.com/example?t=120"</pre>
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
<td><code>endOffset</code></td>
<td>
<p><code><a href="https://schema.org/Number">Number</a></code></p>
<p>The end time of the clip expressed as the number of seconds from the beginning of the
          work.</p>
</td>
</tr>
</tbody>
</table>

### `SeekToAction`

To tell Google how your URL structure works (so that Google can display key moments that are automatically identified for your video), nest the following properties in your [`VideoObject`](https://developers.google.com/search/docs/appearance/structured-data/video/#video-object). While `SeekToAction` properties aren't required, you must add the following properties if you want Google to understand how your URL structure works, so Google can link users to a point within the video.

> If you prefer to identify key moments in a video yourself, instead of letting Google automatically identify key moments, use [`Clip` markup](https://developers.google.com/search/docs/appearance/structured-data/video/#clip) instead of `SeekToAction`.

The full definition of `SeekToAction` is available at [schema.org/SeekToAction](https://schema.org/SeekToAction).

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><code>potentialAction</code>
</td>
<td><p><code><a href="https://schema.org/SeekToAction">SeekToAction</a></code></p>
<p>Indicates a potential action. Include the following nested properties</p>
<ul>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/video/#start-offset-input"><code>potentialAction.startOffset-input</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/video/#target"><code>potentialAction.target</code></a></li>
</ul>
<p>
          For example:
        </p>
<pre class="devsite-click-to-copy">{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "potentialAction" : {
    "@type": "SeekToAction",
    "target": "https://video.example.com/watch/videoID?t={seek_to_second_number}",
    "startOffset-input": "required name=seek_to_second_number"
  }
}</pre>
</td>
</tr>
<tr>
<td><code>potentialAction.startOffset-input</code>
</td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>The placeholder string that Google will identify as your timestamp structure and then
          replace with the number of seconds to skip to. Use the following value:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">"startOffset-input": "<strong>required name=seek_to_second_number</strong>"</pre>
<p>
<code>startOffset-input</code> is an annotated property. See the
          <a href="https://schema.org/docs/actions.html#part-4"><code>Potential Actions</code></a>
          page for more information.
        </p>
</td>
</tr>
<tr>
<td><code>potentialAction.target</code>
</td>
<td><p><code><a href="https://schema.org/EntryPoint">EntryPoint</a></code></p>
<p>The URL of the page that contains this <code>VideoObject</code>, including a placeholder in the URL structure
          that indicates where Google can insert the number of seconds to skip to in the video.
          This is how Google understands your URL structure and how you format your timestamps.
          Replace the timestamp part of the URL with the following placeholder
          string:</p>
<pre class="devsite-click-to-copy">{seek_to_second_number}</pre>
<p>
          For example, replace the timestamp part of the URL:
        </p>
<pre class="devsite-click-to-copy devsite-code-highlight">"target": "https://video.example.com/watch/videoID?t=<strong>30</strong>"</pre>
<p>So that the timestamp now looks like this:</p>
<pre class="devsite-click-to-copy devsite-code-highlight">"target": "https://video.example.com/watch/videoID?t=<strong>{seek_to_second_number}</strong>"</pre>
</td>
</tr>
</tbody>
</table>

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/video/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/video/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/video/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/video/#troubleshooting).
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
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/video/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-video]: Google Search Central (2026). "Video (VideoObject, Clip, BroadcastEvent) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/video. Retrieved 2026-09-14.
