---
type: Reference
title: Best practices for creating Web Stories
description: Google Web Stories are a great way to keep your readers engaged. Explore these best practices as you create Web Stories.
resource: https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:55:35Z'
sources:
- id: google-web-stories-creation-best-practices
  resource: https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices
  title: Best practices for creating Web Stories
  author: Google Search Central (Google LLC)
  last_modified: '2026-06-09T00:00:00Z'
---

# Best practices for creating Web Stories

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices](https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-06-09.[^google-web-stories-creation-best-practices]

To keep your readers engaged, follow our best practices for creating [Web Stories](/appearance/enable-web-stories.md). We recommend focusing on the critical tasks first. If you have more time, follow the recommended best practices too.

## Storytelling

<table>
<th colspan="2"><b>Critical storytelling best practices</b></th>
<tr>
<td>
          Video first
        </td>
<td>
          Video is more engaging than text or images. Use as much video as possible, and supplement with
          images and text.
        </td>
</tr>
</table>

### More storytelling best practices

<table>
<th colspan="2"><b>Recommended storytelling best practices</b></th>
<tr>
<td>
          Bring your perspective
        </td>
<td>
          Go beyond the facts. Share your opinions. Be the protagonist of your own story. Make it relatable.
        </td>
</tr>
<tr>
<td>
          Have a narrative arc
        </td>
<td>
          Create suspense in your story from one page to another. Bring the user along in the journey
          by providing context and narrative. Deliver payoff for sticking with you to the end.
        </td>
</tr>
</table>

## Design

<table>
<th colspan="2"><b>Critical design best practices</b></th>
<tr>
<td>
          Reduce your character count
        </td>
<td>
          Avoid including multiple pages with walls of text. Consider reducing text to
          approximately 280 characters per page (the length of a tweet).
        </td>
</tr>
<tr>
<td>
          Don't block text
        </td>
<td>
          Make sure text is not blocked by other content on the page. Avoid burned in text; by
          not using burned in text, you prevent text from being blocked when it gets resized to fit
          various device sizes.
        </td>
</tr>
<tr>
<td>
          Keep text within bounds
        </td>
<td>
          Ensure that all text in your Web Story is visible to the reader. Avoid burned in text; by
          not using burned in text, you prevent text from overflowing when it gets resized to fit
          various device sizes.
        </td>
</tr>
<tr>
<td>
          Use animations mindfully
        </td>
<td>
          Bring your stories to life with animations. Avoid distracting or repetitive animations which
          can cause fatigue.
        </td>
</tr>
</table>

### More design best practices

<table>
<th colspan="2"><b>Recommended design best practices</b></th>
<tr>
<td>
          Use Web Stories-specific call to action
        </td>
<td>
          When re-creating stories that were originally created for a social platform like Instagram,
          Snapchat or YouTube, be sure to remove any reader call-to-action specific to a
          certain platform. Make sure that users are able to follow any actions suggested in your
          Web Story.
        </td>
</tr>
<tr>
<td>
          Use full bleed videos and images
        </td>
<td>
          Include full bleed assets in your stories to create a more immersive experience for readers.
        </td>
</tr>
<tr>
<td>
          Avoid low resolution or distorted images and videos
        </td>
<td>
          Use high-quality images, and take care when resizing images to portrait.
        </td>
</tr>
<tr>
<td>
          Add a logo to your cover page
        </td>
<td>
          Include a high-resolution logo that represents your brand.
        </td>
</tr>
<tr>
<td>
          Shorten video length
        </td>
<td>
          We recommend videos that are less than 15 seconds per page, or 60 seconds maximum.
        </td>
</tr>
<tr>
<td>
          Include audio
        </td>
<td>
          Use high-quality audio clips that are at least 5 seconds long with balanced volume, and ensure
speech is audible.
        </td>
</tr>
<tr>
<td>
          Consider auto advance for video-only stories
        </td>
<td>
          Auto-advanced experience for video-based Web Stories could work well for a laid back experience.
        </td>
</tr>
</table>

## SEO

> **Note**: The same [SEO best practices](/fundamentals/seo-starter-guide.md) for web pages also apply to [Web Stories](/appearance/enable-web-stories.md). A Web Story is still a web page.

<table>
<th colspan="2"><b>Critical SEO best practices</b></th>
<tr>
<td>
          Provide high-quality content
        </td>
<td>
          Like any web page, providing high-quality content that is useful and interesting to your
      readers the most important thing you can do. Include a complete narrative and follow the
      <a href="https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices/#storytelling">storytelling
        best practices</a> to keep your readers engaged.
        </td>
</tr>
<tr>
<td>
          Keep the title short
        </td>
<td>
          Keep titles shorter than 90 characters. We recommend using a descriptive title that is
          shorter than 70 characters.
        </td>
</tr>
<tr>
<td>
          Make sure Google Search can find your story
        </td>
<td>
          Don't include a <code>noindex</code> attribute in your story; this attribute
          blocks Google from indexing the page and prevents it from appearing on Google. Additionally,
          add your Web Stories to your sitemap. You can check to see if Google can find your Web
          Stories with the <a href="https://support.google.com/webmasters/answer/7440203">Index
          Coverage Report</a> and <a href="https://support.google.com/webmasters/answer/7451001">Sitemaps
          Report</a> in Search Console.
        </td>
</tr>
<tr>
<td>
         Make the story self-canonical
        </td>
<td>
          All Web Stories must be canonical. Make sure that each Web Story has a <a href="https://amp.dev/documentation/guides-and-tutorials/optimize-and-measure/discovery/"><code>link rel="canonical"</code></a> to itself. For example: <code>&lt;link rel="canonical" href="https://www.example.com/url/to/webstory.html"&gt;</code>
<blockquote><b>Note</b>: If there are multiple versions of the same story in different languages, make sure to <a href="/specialty/international/localized-versions.md">tell Google about localized versions</a>.
</blockquote>
</td>
</tr>
<tr>
<td>
          Attach metadata
        </td>
<td>
<p>
           Make sure that your Web Stories follow the
            <a href="https://amp.dev/documentation/components/amp-story/#metadata-guidelines">AMP story
        metadata guidelines</a>. Include markup that you would normally include on a web page, such as:</p>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title"><code>title</code></a> and <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta"><code>description</code></a> <code>meta</code> tags</li>
<li><a href="/appearance/structured-data/intro-structured-data.md">Structured data</a></li>
<li><a href="https://ogp.me/">OGP</a></li>
<li>
<a href="https://developer.twitter.com/en/docs/tweets/optimize-with-cards/overview/abouts-cards">Twitter card</a></li>
</ul>
</td>
</tr>
</table>

### More SEO best practices

<table>
<th colspan="2"><b>Recommended SEO best practices</b></th>
<tr>
<td>
          Include structured data
        </td>
<td>
         We recommend <a href="/appearance/structured-data/article.md">including structured data</a>
         in your Web Story to help Google Search understand the structure and content of your Web Story.
        </td>
</tr>
<tr>
<td>
          Include alt text on images
        </td>
<td>
          We recommend including alt text on your images to improve your story's discoverability.
        </td>
</tr>
<tr>
<td>
          Integrate stories into your website
        </td>
<td>
<p>
          We recommend integrating Web Stories into your website, such as linking them from your
          home page or category pages where applicable. For example, if your Web Story is about a travel
          destination and you have a page that lists all your travel articles, then also link the Web
          Stories on that category page. An additional special landing page like
          <code>www.example.com/stories</code> (which would then be linked from key pages
          like your home page) might also make sense.
        </p>
<blockquote>
            There is no need to indicate in the URL of a Web Story that it is using the Web Stories format
      or AMP Stories technology. Ideally, your Web Stories are integrated into a wider URL strategy.
      For example, if your "New York Travel" articles are using a
      format like <code>"/new-york/travel/title-of-article.html"</code>, then consider
      using the exact same directory structure and URL format for your Web Stories.</blockquote>
</td>
</tr>
<tr>
<td>
          Use AMP story page attachments
        </td>
<td>
<a href="https://amp.dev/documentation/components/amp-story-page-attachment/">AMP
          story page attachments</a> can be used to present additional information alongside your Web
          Story. This can be useful to provide extra detail, deep dives, or onward journeys for the
          content presented in your Web Story.
        </td>
</tr>
<tr>
<td>
          Include subtitles on video
        </td>
<td>
          Add <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Adding_captions_and_subtitles_to_HTML5_video">captions
          to your video</a> to help readers better understand your story. Avoid captions that are
          burned into the video to ensure that they don't overlap with other content or flow off
          the screen.
        </td>
</tr>
<tr>
<td>
          Optimize video-only stories
        </td>
<td>
<p>
            We recommend that you use semantic HTML to build your Web Story. However, some Web Story editor
      tools may instead export a story that formats each slide as a video file that bakes in all
      the text into the video. In this case, we recommend that you add the precise text displayed
      inside of the video as a <code>title</code> attribute on the
      <a href="https://amp.dev/documentation/components/amp-video/?format=stories"><code>amp-video</code></a> element. Again, only do this if you can't use semantic markup in your Web Stories.
          </p>
</td>
</tr>
<tr>
<td>
          Add support for landscape displays
        </td>
<td>
          To enable Web Stories to appear in desktop Google Search results, add <a href="https://amp.dev/documentation/examples/style-layout/desktop_and_landscape_mode_support/">support for landscape displays</a>.
        </td>
</tr>
</table>

## Technical

<table>
<th colspan="2"><b>Critical technical best practices</b></th>
<tr>
<td>
          Make the story valid
        </td>
<td>
          Web Stories must be valid AMP pages. To avoid invalid AMP issues, test your Story using the
<a href="https://validator.ampproject.org/">AMP Validator tool</a> and fix any detected errors.
        </td>
</tr>
<tr>
<td>
         Don't include text in the poster image
        </td>
<td>
          Avoid using images that contain burned in text, as this could obstruct the title of your
          story when users preview your story in Search results. If users are unable to clearly read
          the title, they may be less likely to continue reading.
        </td>
</tr>
<tr>
<td>
         Include the right poster image size and aspect ratio
        </td>
<td>
          Make sure that the image linked to your <code>&lt;amp-story&gt; poster-portrait-src</code>
          attribute is at least 640x853px and use an aspect ratio of 3:4.
        </td>
</tr>
<tr>
<td>
         Include the right aspect ratio for the logo
        </td>
<td>
          Make sure that the logo image linked to your <code>&lt;amp-story&gt; publisher-logo-src</code>
          attribute is at least 96x96 px and aspect ratio of 1:1.
        </td>
</tr>
</table>

### More technical best practices

<table>
<th colspan="2"><b>Recommended technical best practices</b></th>
<tr>
<td>
          Include <code>og:image</code>
</td>
<td>
          We recommend including <code>og:image</code> in your
          <code>&lt;meta&gt;</code> tags to improve your story's discoverability.
        </td>
</tr>
</table>

## Other resources

- [Web Stories](https://amp.dev/about/stories): Resources on making Web Stories from the AMP Project.
- [Enable Web Stories on Google Search](/appearance/enable-web-stories.md): Developer-oriented guide on building Web Stories that meet the technical guidelines required to appear on Google Search.
- [AMP stories website](https://amp.dev/about/stories/): Developer-focused Web Stories format capabilities.
- [Web accessibility](https://developers.google.com/web/fundamentals/accessibility): Tips to help ensure your Web Story is accessible to all users.
- [Structured data guidelines](/appearance/structured-data/sd-policies.md): Details on adding structured data to help Google Search understand your content.

# References & Citations

[^google-web-stories-creation-best-practices]: Google Search Central (2026). "Best practices for creating Web Stories". *Google for Developers*. https://developers.google.com/search/docs/appearance/web-stories-creation-best-practices. Retrieved 2026-09-01.
