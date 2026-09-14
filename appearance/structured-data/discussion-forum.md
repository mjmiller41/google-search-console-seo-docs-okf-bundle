---
type: Reference
title: Discussion forum (DiscussionForumPosting) structured data
description: You can use discussion forum structured data to help Google understand your community forum content.
resource: https://developers.google.com/search/docs/appearance/structured-data/discussion-forum
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-14T11:36:21Z'
sources:
- id: google-discussion-forum
  resource: https://developers.google.com/search/docs/appearance/structured-data/discussion-forum
  title: Discussion forum (DiscussionForumPosting) structured data
  author: Google Search Central (Google LLC)
  last_modified: '2026-09-08T00:00:00Z'
---

# Discussion forum (DiscussionForumPosting) structured data

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/structured-data/discussion-forum](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-09-08.[^google-discussion-forum]

![An illustration of the discussions and forums feature](https://developers.google.com/static/search/docs/images/discussions-and-forums-rich-result.png)

Discussion forum markup is designed for any forum-style site where people collectively share first-hand perspectives. When forum sites add this markup, Google Search can better identify online discussions across the web and make use of this markup in features such as [Discussions and Forums](https://blog.google/products/search/google-search-discussions-forums-news/).

> **Does your forum follow a question and answer pattern?** Use [Q&A markup](/appearance/structured-data/qapage.md) instead.

## How to use `DiscussionForumPosting` within a forum

In general, we recommend nesting comments under the post they relate to. If the forum has its own threading structure, use a tree of comments to represent its structure:

``` devsite-click-to-copy
{
  "@context": "https://schema.org",
  "@type": "DiscussionForumPosting",
  "headline": "Very Popular Thread",
  ...
  "comment": [{
    "@type": "Comment",
    "text": "This should not be this popular",
    ...
    "comment": [{
      "@type": "Comment",
      "text": "Yes it should",
      ...
    }]
  }]
}
```

If it's more linear in nature (for example, an original post followed by a series of replies), nest them all under the original post as comments. Ideally, later pages of content in multi-page forums include the original post with the main page URL:

``` devsite-click-to-copy
{
  // JSON-LD on non-threaded forum at https://example.com/post/very-popular-thread/14
  "@context": "https://schema.org",
  "@type": "DiscussionForumPosting",
  "headline": "Very Popular Thread", // Only the headline/topic is explicitly present
  "url": "https://example.com/post/very-popular-thread",
  ...
  "comment": [{
    "@type": "Comment",
    "text": "First Post on this Page",
    ...
  },{
    "@type": "Comment",
    "text": "Second Post on this Page",
    ...
  }]
}
```

If the URL is primarily about a single post, use [`mainEntity`](https://schema.org/mainEntity) (or [`mainEntityOfPage`](https://schema.org/mainEntityOfPage)) to identify the primary `DiscussionForumPosting`:

``` devsite-click-to-copy
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "url": "https://example.com/post/very-popular-thread",
  "mainEntity": {
    "@type": "DiscussionForumPosting"
    ...
  }
}
```

For web pages that have a list of posts (for example, on a profile, topic, or category page), it's common that they don't have all the information present on the same page and require the user to click to get the extra information (like replies). It's up to you whether you choose to include only the information that is present on the page (and include the URL to the discussion-specific posting).

**Don't mark one post on the page as a main entity if it's not a discussion page for the post**. To show that pages are a related set of posts, it might be useful to attach them all to a [`Collection`](https://schema.org/Collection) or [`ItemList`](https://schema.org/ItemList) .

## How to add structured data

Structured data is a standardized format for providing information about a page and classifying the page content. If you're new to structured data, you can learn more about [how structured data works](/appearance/structured-data/intro-structured-data.md).

Here's an overview of how to build, test, and release structured data.

1.  Add the [required properties](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#structured-data-type-definitions). Based on the format you're using, learn where to [insert structured data on the page](/appearance/structured-data/intro-structured-data.md).

    > **Using a CMS?** It may be easier to use a plugin that's integrated into your CMS.  
    > **Using JavaScript?** Learn how to [generate structured data with JavaScript](/appearance/structured-data/generate-structured-data-with-javascript.md).

2.  Follow the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#guidelines).

3.  Validate your code using the [Rich Results Test](https://search.google.com/test/rich-results) and fix any critical errors. Consider also fixing any non-critical issues that may be flagged in the tool, as they can help improve the quality of your structured data (however, this isn't necessary to be eligible for rich results).

4.  Deploy a few pages that include your structured data and use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289) to test how Google sees the page. Be sure that your page is accessible to Google and not blocked by a robots.txt file, the `noindex` tag, or login requirements. If the page looks okay, you can [ask Google to recrawl your URLs](/crawling-indexing/ask-google-to-recrawl.md).

    > **Note**: Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it.

5.  To keep Google informed of future changes, we recommend that you [submit a sitemap](/crawling-indexing/sitemaps/build-sitemap.md). You can automate this with the [Search Console Sitemap API](https://developers.google.com/webmaster-tools/v1/sitemaps).

## Examples

The following markup example shows a non-threaded, linear forum page:

JSON-LD

  

``` devsite-click-to-copy
<html>
  <head>
    <title>I went to the concert!</title>
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "DiscussionForumPosting",
      "mainEntityOfPage": "https://example.com/post/very-popular-thread",
      "headline": "I went to the concert!",
      "text": "Look at how cool this concert was!",
      "video": {
        "@type": "VideoObject",
        "contentUrl": "https://example.com/media/super-cool-concert.mp4",
        "name": "Video of concert",
        "uploadDate": "2024-03-01T06:34:34+02:00",
        "thumbnailUrl": "https://example.com/media/super-cool-concert-snap.jpg"
      },
      "url": "https://example.com/post/very-popular-thread",
      "author": {
        "@type": "Person",
        "name": "Katie Pope",
        "url": "https://example.com/user/katie-pope",
        "agentInteractionStatistic": {
          "@type": "InteractionCounter",
          "interactionType": "https://schema.org/WriteAction",
          "userInteractionCount": 8
        }
      },
      "datePublished": "2024-03-01T08:34:34+02:00",
      "interactionStatistic": {
        "@type": "InteractionCounter",
        "interactionType": "https://schema.org/LikeAction",
        "userInteractionCount": 27
      },
      "comment": [{
        "@type": "Comment",
        "text": "Who's the person you're with?",
        "author": {
          "@type": "Person",
          "name": "Saul Douglas",
          "url": "https://example.com/user/saul-douglas",
          "agentInteractionStatistic": {
            "@type": "InteractionCounter",
            "interactionType": "https://schema.org/WriteAction",
            "userInteractionCount": 167
          }
        },
        "datePublished": "2024-03-01T09:46:02+02:00"
      },{
        "@type": "Comment",
        "text": "That's my mom, isn't she cool?",
        "author": {
          "@type": "Person",
          "name": "Katie Pope",
          "url": "https://example.com/user/katie-pope",
          "agentInteractionStatistic": {
            "@type": "InteractionCounter",
            "interactionType": "https://schema.org/WriteAction",
            "userInteractionCount": 8
          }
        },
        "datePublished": "2024-03-01T09:50:25+02:00",
        "interactionStatistic": {
          "@type": "InteractionCounter",
          "interactionType": "https://schema.org/LikeAction",
          "userInteractionCount": 7
        }
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
<html>
    <body>
      <div id="main-post" itemtype="https://schema.org/DiscussionForumPosting" itemscope>
        <meta itemprop="mainEntityOfPage" content="https://example.com/post/very-popular-thread" />
        <meta itemprop="url" content="https://example.com/post/very-popular-thread" />
        <div class="author-block" itemprop="author" itemtype="https://schema.org/Person" itemscope>
          <div><a href="https://example.com/user/katie-pope" itemprop="url"><span itemprop="name">Katie Pope</span></a></div>
          <div itemprop="agentInteractionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
            <span itemprop="userInteractionCount">8</span>
            <span itemprop="interactionType" content="https://schema.org/WriteAction">posts</span>
          </div>
        </div>
        <div itemprop="datePublished" content="2024-03-01T08:34:34+02:00">March 1</div>
        <div itemprop="headline">I went to the concert!</div>
        <div>
          <div itemprop="video" itemtype="https://schema.org/VideoObject" itemscope>
            <meta itemprop="name" content="Video of concert" />
            <meta itemprop="contentUrl" content="https://example.com/media/super-cool-concert.mp4" />
            <meta itemprop="uploadDate" content="2024-03-01T06:34:34+02:00" />
            <meta itemprop="thumbnailUrl" content="https://example.com/media/super-cool-concert-snap.jpg" />
          </div>
          <span itemprop="text">Look at how cool this concert was!</span>
        </div>
        <div itemprop="interactionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
          <span itemprop="userInteractionCount">27</span>
          <span itemprop="interactionType" content="https://schema.org/LikeAction">likes</span>
        </div>
        <div id="comment-1" itemprop="comment" itemtype="https://schema.org/Comment" itemscope>
          <div class="author-block" itemprop="author" itemtype="https://schema.org/Person" itemscope>
            <div><a href="https://example.com/user/saul-douglas" itemprop="url"><span itemprop="name">Saul Douglas</span></a></div>
            <div itemprop="agentInteractionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
              <span itemprop="userInteractionCount">167</span>
              <span itemprop="interactionType" content="https://schema.org/WriteAction">posts</span>
            </div>
          </div>
          <div itemprop="datePublished" content="2024-03-01T09:46:02+02:00">March 1</div>
          <div>
            <span itemprop="text">Who's the person you're with?</span>
          </div>
        </div>
        <div id="comment-2" itemprop="comment" itemtype="https://schema.org/Comment" itemscope>
          <div class="author-block" itemprop="author" itemtype="https://schema.org/Person" itemscope>
            <div><a href="https://example.com/user/katie-pope" itemprop="url"><span itemprop="name">Katie Pope</span></a></div>
            <div itemprop="agentInteractionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
              <span itemprop="userInteractionCount">8</span>
              <span itemprop="interactionType" content="https://schema.org/WriteAction">posts</span>
            </div>
          </div>
          <div itemprop="datePublished" content="2024-03-01T09:50:25+02:00">March 1</div>
          <div>
            <span itemprop="text">That's my mom, isn't she cool?</span>
          </div>
          <div itemprop="interactionStatistic" itemtype="https://schema.org/InteractionCounter" itemscope>
            <span itemprop="userInteractionCount">7</span>
            <span itemprop="interactionType" content="https://schema.org/LikeAction">likes</span>
          </div>
        </div>
      </div>
    </body>
</html>
```

## Guidelines

For your discussion forum structured data to be eligible for usage in Google Search, you must follow these guidelines:

- [General structured data guidelines](/appearance/structured-data/sd-policies.md)
- [Search Essentials](/essentials/overview.md)
- [Content Guidelines](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#content-guidelines)
- [Technical Guidelines](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#technical-guidelines)

### Content guidelines

- Only use `DiscussionForumPosting` markup to describe a user-generated post on a website. Don't use this markup for content that's primarily authored by the publishers of the website or their agents.

- If your site is more like a generic social media platform, you can use `SocialMediaPosting`, which is the parent type of `DiscussionForumPosting`, with the same requirements.

- While we encourage valid markup of other types (`Article`, `ImageObject`, `VideoObject`) that can use very similar markup with comments, author information, interaction statistics, those should not use `DiscussionForumPosting` markup. Here are some examples:

  **Valid use cases**:

  - A community forum page where users can talk about a certain game
  - A generic forum platform hosting a wide variety of subforum content
  - A social media platform where users can post and reply to comments or media

  **Invalid use cases**:

  - An article or blog written directly by an agent for the website (even with comments)
  - User reviews about a product

- Note that for most of Google's use cases, a Q&A page is considered a special case of a discussion forum page. If the structure of the forum website is primarily questions with answers, we recommend that you use [Q&A markup](/appearance/structured-data/qapage.md) instead. If the structure is more general and isn't usually question and answer content, `DiscussionForumPosting` would be a better choice.

- Make sure each `DiscussionForumPosting` includes the entire text of the post and make sure each `Comment` includes the entire text of the response if it's found on that page.

### Technical guidelines

- Unlike our general structured data preference, we recommend providing the `DiscussionForumPosting` markup in Microdata (or RDFa) if possible. This prevents you from needing to duplicate large text blocks inside markup. However, this is just a recommendation, and JSON-LD is still fully supported.

## Structured data type definitions

This section describes the structured data types related to `DiscussionForumPosting`.

You must include the required properties for your content to be eligible for usage in Google Search. You can also include the recommended properties to add more information about your discussion forum pages, which could provide a better user experience.

### `DiscussionForumPosting` (or `SocialMediaPosting`)

> While Google supports `SocialMediaPosting` markup, the requirements are the same and most websites (specifically forums) will find `DiscussionForumPosting` more appropriate. So in this section, we use `DiscussionForumPosting` in the descriptions.

The `DiscussionForumPosting` type defines an original posting that is the topic of discussion. While this type is generally composed of text, it's possible to have a forum posting that only consists of media content.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><h3><code>author</code></h3></td>
<td><code><a href="https://schema.org/Person">Person</a></code> or
        <code><a href="https://schema.org/Organization">Organization</a></code>
<p>Information about the author of the post. To help Google best understand authors across various features,
          we recommend following the <a href="/appearance/structured-data/article.md">author markup best practices</a>.</p>
<p>Include as many properties that make sense for the author, using the supported properties
          from <a href="/appearance/structured-data/article.md">article</a>
          and <a href="/appearance/structured-data/profile-page.md">profile page</a>
          structured data as a guide.</p>
</td>
</tr>
<tr>
<td><h3><code>author.name</code></h3></td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>The name of the author of the post.</p>
</td>
</tr>
<tr>
<td><h3><code>datePublished</code></h3></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the post was made in <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.</p></td>
</tr>
<tr>
<td>Either <code>text</code> or <code>image</code> or <code>video</code></td>
<td><p>To represent the content of the post, you must include one of the following properties:</p>
<ul>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#text-sd"><code>text</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#image-sd"><code>image</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#video-sd"><code>video</code></a></li>
</ul>
<p>This is not required if you are representing a post on another page (with an external
          <code>url</code>) as in later pages of forums or forum category pages.
        </p>
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
<td><h3><code>author.url</code></h3></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>A link to a web page that uniquely identifies the author of the post, most likely a profile
          page of the forum.  We recommend marking up that page using
          <a href="/appearance/structured-data/profile-page.md">profile page structured data</a>.</p>
</td>
</tr>
<tr>
<td><code>comment</code></td>
<td><p><code><a href="https://schema.org/Comment">Comment</a></code></p>
<p>A comment about or response to the post, if applicable. Mark up comments in the order
            in which they appear on the page.</p></td>
</tr>
<tr>
<td><code>commentCount</code></td>
<td><p><code><a href="https://schema.org/Integer">Integer</a></code></p>
<p>The number of comments about this post, if applicable. This is particularly useful
            if they are not all present in the comment markup.</p></td>
</tr>
<tr>
<td><code>creativeWorkStatus</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>When the post has been deleted but remains for context or threading, set this property to
            <code>Deleted</code>, if applicable.</p>
</td>
</tr>
<tr>
<td><code>dateModified</code></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the post was edited in <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>,
            if applicable. If no changes have happened, it's not necessary to duplicate the publish
            date.</p></td>
</tr>
<tr>
<td><code>digitalSourceType</code></td>
<td><p><code><a href="https://schema.org/IPTCDigitalSourceEnumeration">IPTCDigitalSourceEnumeration</a></code></p>
<p>The <code>digitalSourceType</code> property indicates the type of digital source
          associated with the content, if applicable. This property is particularly relevant for distinguishing
          between human and AI or other machine-generated content.  Google supports the following values:</p>
<ul>
<li><code>TrainedAlgorithmicMediaDigitalSource</code>: Indicates content created by a
              trained model, such as an LLM.</li>
<li><code>AlgorithmicMediaDigitalSource</code>: Indicates content created by a simpler
              algorithmic process, such as an automatic reply bot.</li>
</ul>
<p>If this property is not specified, Google will assume the content is human-generated.</p>
</td>
</tr>
<tr>
<td><h3><code>headline</code></h3></td>
<td><code><a href="https://schema.org/Text">Text</a></code>
<p>The title of the post. If there isn't a separate title, don't duplicate or truncate the
          text into a headline.  This is not recommended for a <code>SocialMediaPosting</code>.</p></td>
</tr>
<tr>
<td><code>image</code></td>
<td><p><code><a href="https://schema.org/ImageObject">ImageObject</a></code>
        or <code><a href="https://schema.org/URL">URL</a></code></p>
<p>Any inline images within the post, if applicable. If there aren't any images, don't
          include default, icon, placeholder, or author images in this field.  If your image is a
          link preview, include it in the <code>image</code> field of an attached <code>WebPage</code> in
          <code>sharedContent</code>.</p></td>
</tr>
<tr>
<td><code>interactionStatistic</code></td>
<td>
<p><code><a href="https://schema.org/InteractionCounter">InteractionCounter</a></code></p>
<p>User statistics applied to the main post, if applicable.</p>
<p>Google supports the following <code>interactionTypes</code>:</p>
<ul>
<li><a href="https://schema.org/LikeAction">https://schema.org/LikeAction</a>:
            The number of likes or upvotes.</li>
<li><a href="https://schema.org/DislikeAction">https://schema.org/DislikeAction</a>:
            The number of dislikes or downvotes.</li>
<li><a href="https://schema.org/ViewAction">https://schema.org/ViewAction</a>:
            The number of views.</li>
<li><a href="https://schema.org/CommentAction">https://schema.org/CommentAction</a>
            or <a href="https://schema.org/ReplyAction">https://schema.org/ReplyAction</a>:
            The number of comments.</li>
<li><a href="https://schema.org/ShareAction">https://schema.org/ShareAction</a>:
            The number of reshares.</li>
</ul>
</td>
</tr>
<tr>
<td><code>isPartOf</code></td>
<td><p><code><a href="https://schema.org/CreativeWork">CreativeWork</a></code> or <code><a href="https://schema.org/URL">URL</a></code></p>
<p>The primary source of the post if the post occurs on a particular part of the overall
            website, if applicable.
            For example, a subforum or group within the broader website. If a <code>CreativeWork</code>
            (like <code>WebPage</code>) is used, use the <a href="https://schema.org/CreativeWork">URL</a>
            property to specify its URL.</p></td>
</tr>
<tr>
<td><h3><code>sharedContent</code></h3></td>
<td>Subtype of <code><a href="https://schema.org/CreativeWork">CreativeWork</a></code>
<p>The primary shared content in the post, if applicable. We accept four types here:</p>
<ol>
<li><code>WebPage</code>: The most common way this can be used is to share
           (with URLs) as a topical discussion.
        <p>Here's an example of how to add that there's a link shared in the post:</p>
<pre class="devsite-click-to-copy">  ...
  "sharedContent": { "@type": "WebPage", "url": "https://example.com/external-url" }
  ...</pre>
</li>
<li><code>ImageObject</code>: If the primary content of the post is an image, you can
              use this type to mark it up.</li>
<li><code>VideoObject</code>: If the primary content of the post is a video, you can use
              this type to mark it up.</li>
<li><code>DiscussionForumPosting</code> or <code>Comment</code>: If there is a
              referenced post or comment (quoted or reposted), include a reference to that here.
              <p>Here's an example to mark up a referenced <code>Comment</code>:</p>
<pre class="devsite-click-to-copy">  ...
  "sharedContent": {
    "@type": "Comment",
    "url": "https://example.com/post123#comment456",
    "datePublished": "2025-03-24",
    "author": {
      "@type": "Person",
      "name": "Jane Doe"
    },
    "text": "This is a referenced comment displayed inside the post"
  }
  ...</pre>
</li>
</ol>
</td>
</tr>
<tr>
<td><code>text</code></td>
<td><p><code><a href="https://schema.org/URL">Text</a></code></p>
<p>Any text in the post, if applicable. This is very common, but in some cases can be
            left out if there is other media in the post.</p></td>
</tr>
<tr>
<td><h3><code>url</code></h3></td>
<td><code><a href="https://schema.org/URL">URL</a></code>
<p>The canonical URL of the discussion. In multi-page threads, set this property to th
          first page URL. For a single discussion, this is usually the current URL.</p></td>
</tr>
<tr>
<td><code>video</code></td>
<td><p><code><a href="https://schema.org/VideoObject">VideoObject</a></code></p>
<p>Any inline videos within the post, if applicable.</p></td>
</tr>
</tbody>
</table>

### `Comment`

The `Comment` type defines a comment on a original `CreativeWork`. In this case, this is a `DiscussionForumPosting`. It shares many of the same properties with our guidelines for `DiscussionForumPosting`.

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><h3><code>author</code></h3></td>
<td><code><a href="https://schema.org/Person">Person</a></code> or
        <code><a href="https://schema.org/Organization">Organization</a></code>
<p>Information about the author of the comment. To help Google best understand authors across various features,
          we recommend following the <a href="/appearance/structured-data/article.md">author markup best practices</a>.</p>
<p>Include as many properties that make sense for the author, using the supported properties
          from <a href="/appearance/structured-data/article.md">article</a>
          and <a href="/appearance/structured-data/profile-page.md">profile page</a>
          structured data as a guide.</p></td>
</tr>
<tr>
<td><h3><code>datePublished</code></h3></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the comment was made in <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>.
          If no changes have happened, it's not necessary to duplicate the publish date.</p></td>
</tr>
<tr>
<td>Either <code>text</code> or <code>image</code> or <code>video</code></td>
<td><p>To represent the content of the comment, you must include one of the following properties:</p>
<ul>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#text-sd"><code>text</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#image-sd"><code>image</code></a></li>
<li><a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#video-sd"><code>video</code></a></li>
</ul>
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
<td><h3><code>author.url</code></h3></td>
<td><p><code><a href="https://schema.org/URL">URL</a></code></p>
<p>A link to a web page that uniquely identifies the author of the comment, most likely a profile
          page of the forum.  We recommend marking up that page using
          <a href="/appearance/structured-data/profile-page.md">profile page structured data</a>.</p>
</td>
</tr>
<tr>
<td><code>comment</code></td>
<td><p><code><a href="https://schema.org/Comment">Comment</a></code></p>
<p>Another comment about or in response to the comment, if applicable. Mark up the comments
            in the order in which they appear on the page.</p></td>
</tr>
<tr>
<td><code>commentCount</code></td>
<td><p><code><a href="https://schema.org/Integer">Integer</a></code></p>
<p>The number of comments about this comment, if applicable. This is particularly useful
            if they are not all present in the comment markup.</p></td>
</tr>
<tr>
<td><code>creativeWorkStatus</code></td>
<td><p><code><a href="https://schema.org/Text">Text</a></code></p>
<p>If the comment has been deleted but remains for context or threading, set this property
            to <code>Deleted</code>, if applicable.</p></td>
</tr>
<tr>
<td><code>dateModified</code></td>
<td><p><code><a href="https://schema.org/DateTime">DateTime</a></code></p>
<p>The date and time the comment was last edited in
            <a href="https://wikipedia.org/wiki/ISO_8601">ISO 8601 format</a>,
             if applicable.</p></td>
</tr>
<tr>
<td><code>digitalSourceType</code></td>
<td><p><code><a href="https://schema.org/IPTCDigitalSourceEnumeration">IPTCDigitalSourceEnumeration</a></code></p>
<p>The <code>digitalSourceType</code> property indicates the type of digital source
          associated with the content, if applicable. This property is particularly relevant for distinguishing
          between human and AI or other machine-generated content.  Google supports the following values:</p>
<ul>
<li><code>TrainedAlgorithmicMediaDigitalSource</code>: Indicates content created by a
              trained model, such as an LLM.</li>
<li><code>AlgorithmicMediaDigitalSource</code>: Indicates content created by a simpler
              algorithmic process, such as an automatic reply bot.</li>
</ul>
<p>If this property is not specified, Google will assume the content is human-generated.</p>
</td>
</tr>
<tr>
<td><code>image</code></td>
<td><p><code><a href="https://schema.org/ImageObject">ImageObject</a></code>
        or <code><a href="https://schema.org/URL">URL</a></code></p>
<p>Any inline images within the comment, if applicable. If there aren't any images, don't
          include default, icon, placeholder, or author images in this field.  If your image is a
          link preview, include it in the <code>image</code> field of an attached <code>WebPage</code> in
          <code>sharedContent</code>.</p></td>
</tr>
<tr>
<td><code>interactionStatistic</code></td>
<td>
<p><code><a href="https://schema.org/InteractionCounter">InteractionCounter</a></code></p>
<p>User statistics applied to the comment, if applicable.</p>
<p>Google supports the following <code>interactionTypes</code>:</p>
<ul>
<li><a href="https://schema.org/LikeAction">https://schema.org/LikeAction</a>:
            The number of likes or upvotes.</li>
<li><a href="https://schema.org/DislikeAction">https://schema.org/DislikeAction</a>:
            The number of dislikes or downvotes.</li>
<li><a href="https://schema.org/ViewAction">https://schema.org/ViewAction</a>:
            The number of views.</li>
<li><a href="https://schema.org/CommentAction">https://schema.org/CommentAction</a>
            or <a href="https://schema.org/ReplyAction">https://schema.org/ReplyAction</a>:
            The number of comments.</li>
<li><a href="https://schema.org/ShareAction">https://schema.org/ShareAction</a>:
            The number of reshares.</li>
</ul>
</td>
</tr>
<tr>
<td><h3><code>sharedContent</code></h3></td>
<td>Subtype of <code><a href="https://schema.org/CreativeWork">CreativeWork</a></code>
<p>The primary shared content in the post, if applicable. We recognize four types here:</p>
<ol>
<li><code>WebPage</code>: The most common way this can be used is to share
           (with URLs) as a topical discussion.
        <p>Here's an example of how to add that there's a link shared in the post:</p>
<pre class="devsite-click-to-copy">  ...
  "sharedContent": { "@type": "WebPage", "url": "https://example.com/external-url" }
  ...</pre>
</li>
<li><code>ImageObject</code>: If the primary content of the post is an image, you can
              use this type to mark it up.</li>
<li><code>VideoObject</code>: If the primary content of the post is a video, you can use
              this type to mark it up.</li>
<li><code>DiscussionForumPosting</code> or <code>Comment</code>: If there is a
              referenced post or comment (quoted or reposted), include a reference to that here.
              <p>Here's an example to mark up a referenced <code>Comment</code>:</p>
<pre class="devsite-click-to-copy">  ...
  "sharedContent": {
    "@type": "Comment",
    "url": "https://example.com/post123#comment456",
    "datePublished": "2025-03-24",
    "author": {
      "@type": "Person",
      "name": "Jane Doe"
    },
    "text": "This is a referenced comment displayed inside the post"
  }
  ...</pre>
</li>
</ol>
</td>
</tr>
<tr>
<td><h3><code>url</code></h3></td>
<td><code><a href="https://schema.org/URL">URL</a></code>
<p>The URL to this specific comment on the page, if applicable. Don't include this property if it's just
          the URL of the original post.</p></td>
</tr>
<tr>
<td><code>video</code></td>
<td><p><code><a href="https://schema.org/VideoObject">VideoObject</a></code></p>
<p>Any inline videos within the comment, if applicable.</p></td>
</tr>
</tbody>
</table>

### `InteractionCounter`

The `InteractionCounter` allows a count to be associated with a certain type of interaction. This can be used on both content ([`DiscussionForumPosting`](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#dfp) and [`Comment`](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#comment)) properties as well as [`author` properties.](/appearance/structured-data/profile-page.md)

<table>
<colgroup><col/></colgroup>
<thead>
<tr><th colspan="2">Required properties</th></tr>
</thead>
<tbody>
<tr>
<td><h3><code>userInteractionCount</code></h3></td>
<td><code><a href="https://schema.org/Integer">Integer</a></code>
<p>The number of times this interaction was performed.</p></td>
</tr>
<tr>
<td><h3><code>interactionType</code></h3></td>
<td><p>Subtype of <a href="https://schema.org/Action"><code>Action</code></a></p>
<p>For a list of valid <code>Action</code> subtypes for this property, check the property that's using <code>InteractionCounter</code>
            (for example, <a href="https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#comment-interactionStatistic"><code>interactionStatistic</code></a>).</p>
</td>
</tr>
</tbody>
</table>

## Monitor rich results with Search Console

Search Console is a tool that helps you monitor how your pages perform in Google Search. You don't have to sign up for Search Console to be included in Google Search results, but it can help you understand and improve how Google sees your site. We recommend checking Search Console in the following cases:

1.  [After deploying structured data for the first time](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#after-deploying)
2.  [After releasing new templates or updating your code](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#after-releasing)
3.  [Analyzing traffic periodically](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#analyzing-periodically)

### After deploying structured data for the first time

After Google has indexed your pages, look for issues using the relevant [Rich result status report](https://support.google.com/webmasters/answer/7552505). Ideally, there will be an increase of valid items, and no increase in invalid items. If you find issues in your structured data:

1.  [Fix the invalid items](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#troubleshooting).
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
- Review the [guidelines](https://developers.google.com/search/docs/appearance/structured-data/discussion-forum/#guidelines) again to identify if your content isn't compliant with the guidelines. The problem can be caused by either spammy content or spammy markup usage. However, the issue may not be a syntax issue, and so the Rich Results Test won't be able to identify these issues.
- Structured data issues can affect how your site's content appears in search results. Use this [Troubleshoot missing rich results / drop in total rich results](https://support.google.com/webmasters/answer/13300208) guide to review a step-by-step approach to identify, fix, and validate these issues in Search Console.
- Allow time for re-crawling and re-indexing. Remember that it may take several days after publishing a page for Google to find and crawl it. For general questions about crawling and indexing, check the [Google Search crawling and indexing FAQ](https://developers.google.com/search/help/crawling-index-faq).
- Post a question in the [Google Search Central forum](https://support.google.com/webmasters/community).

# References & Citations

[^google-discussion-forum]: Google Search Central (2026). "Discussion forum (DiscussionForumPosting) structured data". *Google for Developers*. https://developers.google.com/search/docs/appearance/structured-data/discussion-forum. Retrieved 2026-09-14.
