---
type: Reference
title: Video sitemaps and alternatives
description: Video sitemaps help Google display videos in Search. Review these guidelines to learn more and browse video xml sitemap examples.
resource: https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-video-sitemaps
  resource: https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps
  title: Video sitemaps and alternatives
  author: Google Search Central (Google LLC)
  last_modified: '2026-05-20T00:00:00Z'
---

# Video sitemaps and alternatives

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-05-20.[^google-video-sitemaps]

A video sitemap is a [sitemap](/crawling-indexing/sitemaps/overview.md) with additional information about videos hosted on your pages. Creating a video sitemap is a good way to help Google find and understand the video content on your site, especially content that was recently added or that we might not otherwise discover with our usual crawling mechanisms.

Google recommends using video sitemaps, however we also support [mRSS feeds](https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps/#sitemap_alternatives).

## Video sitemap best practices

Video sitemaps are based on generic sitemaps, so the [general sitemap best practices](/crawling-indexing/sitemaps/build-sitemap.md) also apply to video sitemaps. You can create a separate sitemap or mRSS feed just for video, or you can add video sitemap tags within an existing [sitemap](/crawling-indexing/sitemaps/build-sitemap.md), whichever is more convenient for you.

Additionally, the following requirements apply to video sitemaps specifically:

- Don't list videos that are unrelated to the content of the host page. For example, a video that is a small addendum to the page, or unrelated to the main text content.

- All files referenced in the video sitemap must be accessible to Googlebot. This means that all URLs in the video sitemap:

  - must not be disallowed for crawling by [robots.txt](/crawling-indexing/robots/intro.md) rules,
  - must be accessible without metafiles and without logging in,
  - must not be blocked by firewalls or similar mechanism,
  - and must be accessible on a supported protocol: HTTP and FTP (streaming protocols are not supported).

  If you want to prevent spammers from accessing your video content at the `<player_loc>` or `<content_loc>` URLs, [verify that any bots accessing your server are really Googlebot](https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot).

For more tips about videos in Google Search, see our [video best practices](/appearance/video.md).

## Example video sitemap

The following example shows a regular sitemap with video extension. It includes two video entries nested in the single `<url>` tag. The first `<video>` entry includes all the tags that Google can use while the second only the required tags.

``` devsite-click-to-copy
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://www.example.com/videos/some_video_landing_page.html</loc>
    <video:video>
      <video:thumbnail_loc>https://www.example.com/thumbs/123.jpg</video:thumbnail_loc>
      <video:title>Grilling steaks for summer</video:title>
      <video:description>
        Alkis shows you how to get perfectly done steaks every time
      </video:description>
      <video:content_loc>
        http://streamserver.example.com/video123.mp4
      </video:content_loc>
      <video:player_loc>
        https://www.example.com/videoplayer.php?video=123
      </video:player_loc>
      <video:duration>600</video:duration>
      <video:expiration_date>2021-11-05T19:20:30+08:00</video:expiration_date>
      <video:rating>4.2</video:rating>
      <video:view_count>12345</video:view_count>
      <video:publication_date>2007-11-05T19:20:30+08:00</video:publication_date>
      <video:family_friendly>yes</video:family_friendly>
      <video:restriction relationship="allow">IE GB US CA</video:restriction>
      <video:platform relationship="allow">web tv</video:platform>
      <video:requires_subscription>yes</video:requires_subscription>
      <video:uploader
        info="https://www.example.com/users/grillymcgrillerson">GrillyMcGrillerson
      </video:uploader>
      <video:live>no</video:live>
      <video:tag>steak</video:tag>
      <video:tag>meat</video:tag>
      <video:tag>summer</video:tag>
    </video:video>
    <video:video>
      <video:thumbnail_loc>https://www.example.com/thumbs/345.jpg</video:thumbnail_loc>
      <video:title>Grilling steaks for winter</video:title>
      <video:description>
        In the freezing cold, Roman shows you how to get perfectly done steaks every time.
      </video:description>
      <video:content_loc>
        http://streamserver.example.com/video345.mp4
      </video:content_loc>
      <video:player_loc>
        https://www.example.com/videoplayer.php?video=345
      </video:player_loc>
    </video:video>
  </url>
</urlset>
```

#### More examples

The following example demonstrates how to add a Vimeo video embed to a video sitemap:

``` devsite-click-to-copy
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://www.example.com/videos/some_video_landing_page.html</loc>
    <video:video>
      <video:thumbnail_loc>https://www.example.com/thumbs/123.jpg</video:thumbnail_loc>
      <video:title>Lizzi is painting the wall</video:title>
      <video:description>
        Gary is watching the paint dry on the wall Lizzi painted.
      </video:description>
      <video:player_loc>
        https://player.vimeo.com/video/987654321
      </video:player_loc>
    </video:video>
  </url>
</urlset>
```

The following example demonstrates how to add a YouTube video embed to a video sitemap:

``` devsite-click-to-copy
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">
  <url>
    <loc>https://www.example.com/videos/some_video_landing_page.html</loc>
    <video:video>
      <video:thumbnail_loc>https://www.example.com/thumbs/345.jpg</video:thumbnail_loc>
      <video:title>John teaches cheese</video:title>
      <video:description>
        John explains the differences between a banana and cheese.
      </video:description>
      <video:player_loc>
        https://www.youtube.com/embed/1a2b3c4d
      </video:player_loc>
    </video:video>
  </url>
</urlset>
```

## Video sitemap reference

The `video` tags are defined in the video sitemaps namespace: [`http://www.google.com/schemas/sitemap-video/1.1`](http://www.google.com/schemas/sitemap-video/1.1). Each tag can only be added one time per video, unless otherwise specified.

To make sure Google can use your video sitemap, you must use the following required tags:

<table>
<tr><th colspan="2">Required tags</th></tr>
<tr>
<td><code>&lt;video:video&gt;</code></td>
<td>
<p>
        The parent element for all information about a single video on the page specified by
        the <code>&lt;loc&gt;</code> tag. You can include multiple
        <code>&lt;video:video&gt;</code> tags nested in the <code>&lt;loc&gt;</code> tag, one
        for each video on the hosting page.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;video:thumbnail_loc&gt;</code></td>
<td>
<p>
        A URL pointing to the video thumbnail image file. Follow the
        <a href="/appearance/video.md">video thumbnail requirements.</a>
</p>
</td>
</tr>
<tr>
<td><code>&lt;video:title&gt;</code></td>
<td>
<p>
        The title of the video. All HTML entities must be escaped or wrapped in a
        <a href="http://wikipedia.org/wiki/CDATA"><code>CDATA</code> block</a>.
        We recommend that this match the video title displayed on the web page where the video
        is embedded.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;video:description&gt;</code></td>
<td>
<p>
        A description of the video. Maximum 2048 characters. All HTML entities must be escaped
        or wrapped in a
        <a href="http://wikipedia.org/wiki/CDATA"><code>CDATA</code> block</a>.
        It must match the description displayed on the web page where the video is embedded, but
        it doesn't need to be a word-for-word match.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;video:content_loc&gt;</code></td>
<td>
<p>
        A URL pointing to the actual video media file. The file must be one of the
        <a href="/appearance/video.md">supported formats.</a>
</p>
<blockquote>
        It's required to provide either a <code>&lt;video:content_loc&gt;</code> or
        <code>&lt;video:player_loc&gt;</code> tag. We recommend that your provide the
        <code>&lt;video:content_loc&gt;</code> tag, if possible. This is the most effective
        way for Google to fetch your video content files. If
        <code>&lt;video:content_loc&gt;</code> isn't available, provide
        <code>&lt;video:player_loc&gt;</code> as an alternative.
      </blockquote>
<p><b>Additional guidelines</b></p>
<ul>
<li>HTML and Flash aren't supported formats.</li>
<li>Must not be the same as the URL in the parent <code>&lt;loc&gt;</code> tag.</li>
<li>
          This is the equivalent of
          <code><a href="/appearance/structured-data/video.md">VideoObject.contentUrl</a></code>
          in structured data.
        </li>
<li>
<b>Best practice:</b> If you want to restrict access to your content but still have it
          crawled, ensure that Googlebot can access your content by using
          <a href="https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot">verifying Googlebot</a>.
        </li>
</ul>
</td>
</tr>
<tr>
<td><code>&lt;video:player_loc&gt;</code></td>
<td>
<p>
        A URL pointing to a player for a <b>specific</b> video. Usually this is the information
        in the <code>src</code> attribute of an <code>&lt;embed&gt;</code> tag.
      </p>
<blockquote>
        It's required to provide either a <code>&lt;video:content_loc&gt;</code> or
        <code>&lt;video:player_loc&gt;</code> tag. We recommend that your provide the
        <code>&lt;video:content_loc&gt;</code> tag, if possible. This is the most effective way
        for Google to fetch your video content files. If
        <code>&lt;video:content_loc&gt;</code> isn't available, provide
        <code>&lt;video:player_loc&gt;</code> as an alternative.
      </blockquote>
<p><b>Additional guidelines</b></p>
<ul>
<li>Must not be the same as the <code>&lt;loc&gt;</code> URL.</li>
<li>
          For Vimeo, YouTube, and other video hosting platforms that allow embedding videos
          through <code>iframe</code> videos, this value is used rather than
          <code>video:content_loc</code>. This is the equivalent of
          <code><a href="/appearance/structured-data/video.md">VideoObject.embedUrl</a></code>
          in structured data.
        </li>
<li>
<b>Best practice:</b> If you want to restrict access to your content but still have it
          crawled, ensure that Googlebot can access your content by using
          <a href="https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot">verifying Googlebot</a>.
        </li>
</ul>
</td>
</tr>
</table>

Additionally, the following optional tags may help Google better understand your videos and its properties:

<table>
<tr><th colspan="2">Optional tags</th></tr>
<tr>
<td><code>&lt;video:duration&gt;</code></td>
<td>
<p>
        The duration of the video, in seconds. Value must be from <code>1</code> to
        <code>28800</code> (8 hours).
      </p>
</td>
</tr>
<tr>
<td><code>&lt;video:expiration_date&gt;</code></td>
<td>
<p>The date after which the video is no longer be available, in
        <a href="http://www.w3.org/TR/NOTE-datetime">W3C format</a>.
        Omit this tag if your video doesn't expire. If present, Google Search won't show your
        video after this date. For recurring videos at the same URL, update the expiration
        date to the new expiration date.
      </p>
<p>
        Supported values are complete date (<code>YYYY-MM-DD</code>), or complete date plus
        hours, minutes and seconds, and timezone (<code>YYYY-MM-DDThh:mm:ss+TZD</code>).
      </p>
<p><b>Example:</b> <code>2012-07-16T19:20:30+08:00</code>.</p>
</td>
</tr>
<tr>
<td><code>&lt;video:rating&gt;</code></td>
<td>
<p>
        The rating of the video. Supported values are float numbers in the range <code>0.0</code> (low) to
        <code>5.0</code> (high).
      </p>
</td>
</tr>
<tr>
<td><code>&lt;video:view_count&gt;</code></td>
<td>
<p>The number of times the video has been viewed.</p>
</td>
</tr>
<tr>
<td><code>&lt;video:publication_date&gt;</code></td>
<td>
<p>
        The date the video was first published, in
        <a href="http://www.w3.org/TR/NOTE-datetime">W3C format</a>.
        Supported values are complete date (<code>YYYY-MM-DD</code>) or complete date plus
        hours, minutes and seconds, and timezone (<code>YYYY-MM-DDThh:mm:ss+TZD</code>).
      </p>
<p><b>Example:</b> <code>2007-07-16T19:20:30+08:00</code></p>
</td>
</tr>
<tr>
<td><code>&lt;video:family_friendly&gt;</code></td>
<td>
<p>
        Whether the video is available with
        <a href="https://developers.google.com/search/docs/crawling-indexing/safesearch">SafeSearch</a>. If you omit this
        tag, the video is available when SafeSearch is turned on.
      </p>
<p><b>Supported values</b>:</p>
<ul>
<li><code>yes</code>: The video is available when SafeSearch is turned on.</li>
<li><code>no</code>: The video is only available when SafeSearch is turned off.</li>
</ul>
</td>
</tr>
<tr>
<td>
<code>&lt;video:restriction&gt;</code>
</td>
<td>
<p>Whether to show or hide your video in search results from specific countries.</p>
<p>
        Specify a space-delimited list of country codes in
        <a href="http://wikipedia.org/wiki/ISO_3166">ISO 3166 format</a>.
        If there's no <code>&lt;video:restriction&gt;</code> tag, Google assumes that the video can be
        shown in all locations. <i>Note that this tag only affects search results; it doesn't
        prevent a user from finding or playing your video in a restricted location through other
        means.</i>
<a href="/appearance/video.md">Learn more about applying country restrictions.</a>
</p>
<p><b>Attributes:</b></p>
<p>
        If the parent tag <code>&lt;video:restriction&gt;</code> is used, the following
        attribute is required:
      </p>
<ul>
<li>
<code>relationship</code>: Whether the video is allowed or denied in
          search results in the specified countries. Supported values are:
          <ul>
<li>
<code>allow</code>: The listed countries are allowed and unlisted countries are
              denied.
            </li>
<li>
<code>deny</code>: The listed countries are denied and unlisted countries are
              allowed.
            </li>
</ul>
</li>
</ul>
<p>
<b>Example:</b> This example allows the video search result to be shown only in Canada
        and Mexico:
      </p>
<p>
<code>&lt;video:restriction relationship="allow"&gt;CA MX&lt;/video:restriction&gt;</code>
</p>
</td>
</tr>
<tr>
<td><code>&lt;video:platform&gt;</code></td>
<td>
<p>
        Whether to show or hide your video in search results on specified platform types. This
        is a list of space-delimited platform types. <i>Note that this only affects search
        results on the specified device types; it doesn't prevent a user from playing your
        video on a restricted platform.</i>
</p>
<p>
        If there's no <code>&lt;video:platform&gt;</code> tag, Google assumes that the video can be
        played on all platforms.
        <a href="/appearance/video.md">Learn more about applying platform restrictions.</a>
</p>
<p><b>Supported values</b>:</p>
<ul>
<li><code>web</code>: Computer browsers on desktops and laptops.</li>
<li>
<code>mobile</code>: Mobile browsers, such as those on cellular phones or tablets.
        </li>
<li>
<code>tv</code>: TV browsers, such as those available through Google TV devices and
          game consoles.
        </li>
</ul>
<p><b>Attributes:</b></p>
<p>
        If the parent tag <code>&lt;video:platform&gt;</code> is used, the following
        attributes are required:
      </p>
<ul>
<li>
<code>relationship</code>: Specifies whether the video is
          restricted or permitted for the specified platforms. Supported values are:
          <ul>
<li>
<code>allow</code>: Any omitted platforms will be denied.
            </li>
<li>
<code>deny</code>: Any omitted platforms will be allowed.
            </li>
</ul>
</li>
</ul>
<p>
<b>Example:</b> The following example allows users on web or TV, but not mobile
        devices:<br/>
<code>&lt;video:platform relationship="allow"&gt;web tv&lt;/video:platform&gt;</code>
</p>
</td>
</tr>
<tr>
<td><code>&lt;video:requires_subscription&gt;</code></td>
<td>
<p>
        Indicates whether a subscription (either paid or free) is required to view the video. Supported values are:
      </p>
<ul>
<li>
<code>yes</code>: Subscription is required.
        </li>
<li>
<code>no</code>: Subscription is not required.
        </li>
</ul>
</td>
</tr>
<tr>
<td><code>&lt;video:uploader&gt;</code></td>
<td>
<p>
        The video uploader's name. The string value can be a maximum of 255 characters.
      </p>
<p><b>Attributes:</b></p>
<ul>
<li>
<code>info</code> [<i>Optional</i>]: Specifies the URL of a web page with additional
          information about this uploader. This URL must be in the same domain as the
          <code>&lt;loc&gt;</code> tag.</li>
</ul>
</td>
</tr>
<tr>
<td><code>&lt;video:live&gt;</code></td>
<td>
<p>Indicates whether the video is a livestream. Supported values are:</p>
<ul>
<li>
<code>yes</code>: The video is a livestream.
        </li>
<li>
<code>no</code>: The video is not a livestream.
        </li>
</ul>
</td>
</tr>
<tr>
<td><code>&lt;video:tag&gt;</code></td>
<td>
<p>
        An arbitrary string tag describing the video. Tags are generally very short
        descriptions of key concepts associated with a video or piece of content. A single
        video could have several tags, although it might belong to only one category. For
        example, a video about grilling food may belong in the "grilling" category, but could
        be tagged "steak", "meat", "summer", and "outdoor". Create a new
        <code>&lt;video:tag&gt;</code> element for each tag associated with a video. A maximum
        of 32 tags is permitted per video.
      </p>
</td>
</tr>
</table>

### Deprecated tags and attributes

We removed the following tags and attributes from our documentation: `<video:category>`, `<video:gallery_loc>`, the `autoplay` and `allow_embed` attributes of the `<video:player_loc>` tag, the `<video:price>` tag and its attributes, and the `<video:tvshow>` tag and its attributes. See the [deprecation announcement](https://developers.google.com/search/blog/2022/05/spring-cleaning-sitemap-extensions) for more information.

## Sitemap alternative: mRSS

While Google recommends using video sitemaps, we also support mRSS feeds.

Google supports [mRSS](http://www.rssboard.org/media-rss), an RSS module that supplements the element capabilities of [RSS 2.0](http://cyber.law.harvard.edu/rss/rss.html). mRSS feeds are very similar to video sitemaps and can be tested, submitted, and updated just like sitemaps.

For more information about media feeds, see the [official media RSS documentation](http://www.rssboard.org/media-rss).

> **RSS vs mRSS**: mRSS is a RSS extension used for syndicating multimedia files. It allows for a much more detailed description of the content than the RSS standard.

### mRSS Example

Here's an example of an mRSS entry that provides all the tags that Google uses.

``` devsite-click-to-copy
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/" xmlns:dcterms="http://purl.org/dc/terms/">
  <channel>
    <title>Example MRSS</title>
    <link>https://www.example.com/examples/mrss/</link>
    <description>MRSS Example</description>
    <item xmlns:media="http://search.yahoo.com/mrss/" xmlns:dcterms="http://purl.org/dc/terms/">
      <link>https://www.example.com/examples/mrss/example.html</link>
      <media:content url="https://www.example.com/examples/mrss/example.flv" fileSize="405321"
                        type="video/x-flv" height="240" width="320" duration="120" medium="video" isDefault="true">
        <media:player url="https://www.example.com/shows/example/video.swf?flash_params" />
        <media:title>Grilling Steaks for Summer</media:title>
        <media:description>Get perfectly done steaks every time</media:description>
        <media:thumbnail url="https://www.example.com/examples/mrss/example.png" height="120" width="160"/>
        <media:price price="19.99" currency="EUR" />
        <media:price type="subscription" />
      </media:content>
      <media:restriction relationship="allow" type="country">us ca</media:restriction>
      <dcterms:valid xmlns:dcterms="http://purl.org/dc/terms/">end=2020-10-15T00:00+01:00; scheme=W3C-DTF</dcterms:valid>
      <dcterms:type>live-video</dcterms:type>
    </item>
  </channel>
</rss>
```

### mRSS reference

The [full mRSS specification](http://www.rssboard.org/media-rss) contains more optional tags, best practices, and examples.

To make sure Google can use your mRSS feed, you must use the following required tags:

<table>
<tr><th colspan="2">Required tags</th></tr>
<tr>
<td><code>&lt;media:content&gt;</code></td>
<td>
<p>Encloses information about the video.</p>
<p>Attributes:</p>
<ul>
<li>
<code>medium</code>: Type of content. Set to <code>video</code>.
        </li>
<li>
<code>url</code>: The direct URL to the raw video content.
          <b>If this isn't specified, you must specify the <code>&lt;media:player&gt;</code>
            tag.</b>
</li>
<li>
<code>duration</code> [<i>Optional but recommended</i>]: Length of the video in
          seconds.
        </li>
</ul>
<p>
        For all of the other optional attributes and child fields of the
        <code>&lt;media:content&gt;</code> tag, see the
        <a href="http://www.rssboard.org/media-rss">mRSS specification</a>.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;media:player&gt;</code></td>
<td>
<p>
<b>You must specify at least one of <code>&lt;media:player&gt;</code> or the
          <code>url</code> attribute in <code>&lt;media:content&gt;</code>.</b>
</p>
<p>
        A URL pointing to a player for a <b>specific</b> video. Usually this is the information
        in the <code>src</code> attribute of an <code>&lt;embed&gt;</code> tag and must not be
        the same as the content of the <code>&lt;loc&gt;</code> tag. It can't be the same URL as
        the <code>&lt;link&gt;</code> tag. The <code>&lt;link&gt;</code> tag points to the URL
        of the page hosting the video, while this tag points to a player.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;media:title&gt;</code></td>
<td>
<p>
        The title of the video. Maximum 100 characters. All HTML entities must be escaped or
        wrapped in a
        <a href="http://wikipedia.org/wiki/CDATA">CDATA bock</a>.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;media:description&gt;</code></td>
<td>
<p>
        The description of the video. Maximum 2048 characters. All HTML entities must be escaped
        or wrapped in a
        <a href="http://wikipedia.org/wiki/CDATA">CDATA block</a>.
      </p>
</td>
</tr>
<tr>
<td><code>&lt;media:thumbnail&gt;</code></td>
<td>
      A URL pointing to a preview thumbnail. Follow the
      <a href="/appearance/video.md">Video thumbnail requirements.</a>
</td>
</tr>
</table>

Additionally, the following optional tags may help Google better understand your videos and its properties:

<table>
<tr><th colspan="2">Optional tags</th></tr>
<tr>
<td><code>&lt;dcterms:valid&gt;</code></td>
<td>
<p>
        The publication and expiration date of the video. Here's the
        <a href="https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/valid/">Full specification of the <code>dcterms:valid</code></a>
        tag.
      </p>
<p><b>Example:</b></p>
<pre class="devsite-click-to-copy">&lt;dcterms:valid&gt;
start=2002-10-13T09:00+01:00;
end=2002-10-17T17:00+01:00;
scheme=W3C-DTF
&lt;dcterms:valid&gt;</pre>
</td>
</tr>
<tr>
<td><code>&lt;media:restriction&gt;</code></td>
<td>
<p>
        A space-delimited list of countries where the video may or may not be played, in
        <a href="http://wikipedia.org/wiki/ISO_3166">ISO 3166 format</a>.
        If there's no <code>&lt;media:restriction&gt;</code> tag, Google assumes that the video
        can be played in all countries.
      </p>
<p><b>Attributes:</b></p>
<p>
        If the parent tag <code>&lt;media:restriction&gt;</code> is used, the following
        attributes are required:
      </p>
<ul>
<li>
<code>type</code>: Set the <code>type</code> attribute to
          <code>country</code>. Only country restrictions are supported.
        </li>
<li>
<code>relationship</code>: Specifies whether the video may or may
          not be played in the specified list of countries. Supported values:
          <ul>
<li>
<code>allow</code>: The listed countries are allowed and unlisted countries are
              denied.
            </li>
<li>
<code>deny</code>: The listed countries are denied and unlisted countries are
              allowed.
            </li>
</ul>
</li>
</ul>
<p>
<a href="/appearance/video.md">Learn more about using country restrictions.</a>
</p>
<p>Example:</p>
<pre class="devsite-click-to-copy">&lt;media:restriction relationship="allow" type="country"&gt;us ca&lt;/media:restriction&gt;</pre>
</td>
</tr>
<tr>
<td><code>&lt;media:price&gt;</code></td>
<td>
<p>
        The price to download or view the video. Don't use this tag for videos that are
        available without payment. More than one <code>&lt;media:price&gt;</code> element can be
        listed (for example, in order to specify various currencies or purchasing options).
      </p>
<p><b>Attributes:</b></p>
<p>
        If the parent tag <code>&lt;media:price&gt;</code> is used, the following
        attributes are required:
      </p>
<ul>
<li>
<code>currency</code>: The currency in
          <a href="https://en.wikipedia.org/wiki/ISO_4217">ISO 4217 format</a>.
        </li>
<li>
<code>type</code>: The purchase option. Supported values are:
          <ul>
<li>
<code>rent</code>: The video is available for rent.
            </li>
<li>
<code>purchase</code>: The video is available for purchase.
            </li>
<li>
<code>package</code>: The video is part of a package deal.
            </li>
<li>
<code>subscription</code>: The video is available with a subscription.
            </li>
</ul>
</li>
</ul>
</td>
</tr>
</table>

## Troubleshooting sitemaps

If you're having trouble with your sitemap, you can investigate the errors with Google Search Console. See Search Console's [sitemaps troubleshooting guide](https://support.google.com/webmasters/answer/7451001#errors) for help.

## Additional resources

Want to learn more? Check out the following resources:

- [Submit your sitemap to Google](/crawling-indexing/sitemaps/build-sitemap.md)
- [Learn how to combine sitemap extensions](/crawling-indexing/sitemaps/combine-sitemap-extensions.md)

# References & Citations

[^google-video-sitemaps]: Google Search Central (2026). "Video sitemaps and alternatives". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/sitemaps/video-sitemaps. Retrieved 2026-09-01.
