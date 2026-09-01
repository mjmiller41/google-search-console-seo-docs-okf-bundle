---
type: Reference
title: Image sitemaps
description: Image sitemaps help Google discover images. Follow these best practices on how to create an image sitemap and review image sitemap examples.
resource: https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: claude-code/claude-fable-5
  at: '2026-09-01T14:20:03Z'
sources:
- id: google-image-sitemaps
  resource: https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps
  title: Image sitemaps
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Image sitemaps

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-image-sitemaps]

Image sitemaps are a way of telling Google about other images on your site, especially those that we might not otherwise find (such as images your site reaches with JavaScript code). You can create a separate image sitemap or add image sitemap tags to your existing sitemap; either approach is equally fine for Google.

Image sitemaps are based on generic sitemaps so the [general sitemap best practices](/crawling-indexing/sitemaps/build-sitemap.md) also apply to image sitemaps. We also recommend that you follow the [general best practices for publishing images](/appearance/google-images.md).

## Example image sitemap

The following example shows a regular sitemap with image sitemap extension, with two `<url>` elements:

- `https://example.com/sample1.html`, which contains two images
- `https://example.com/sample2.html`, which contains one image

``` devsite-click-to-copy
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <url>
    <loc>https://example.com/sample1.html</loc>
    <image:image>
      <image:loc>https://example.com/image.jpg</image:loc>
    </image:image>
    <image:image>
      <image:loc>https://example.com/photo.jpg</image:loc>
    </image:image>
  </url>
  <url>
    <loc>https://example.com/sample2.html</loc>
    <image:image>
      <image:loc>https://example.com/picture.jpg</image:loc>
    </image:image>
  </url>
</urlset>
```

## Image sitemap reference

The `image` tags are defined in the Image Sitemaps namespace: [`http://www.google.com/schemas/sitemap-image/1.1`](http://www.google.com/schemas/sitemap-image/1.1)

To make sure Google can use your image sitemap, you must use the following required tags:

<table>
<tbody>
<tr>
<th colspan="2">Required tags</th>
</tr>
<tr>
<td><code>&lt;image:image&gt;</code></td>
<td>
        Encloses all information about a single image. Each <code>&lt;url&gt;</code> tag can
        contain up to 1,000 <code>&lt;image:image&gt;</code> tags.
      </td>
</tr>
<tr>
<td><code>&lt;image:loc&gt;</code></td>
<td>
<p>The URL of the image.</p>
<p>
          In some cases, the image URL may not be on the same domain as your main site. This is
          fine, as long as you verify both domains in Search Console. If, for example, you use
          a content delivery network such as Google Sites to host your images, make sure that
          the hosting site is verified in Search Console. In addition, make sure that your
          <a href="/crawling-indexing/robots/intro.md">robots.txt</a> file doesn't
          disallow the crawling of any content you want indexed.
        </p>
</td>
</tr>
</tbody>
</table>

### Deprecated tags and attributes

We removed the following tags and attributes from our documentation: `<image:caption>`, `<image:geo_location>`, `<image:title>`, `<image:license>`. See the [deprecation announcement](https://developers.google.com/search/blog/2022/05/spring-cleaning-sitemap-extensions) for more information.

## Troubleshooting sitemaps

If you're having trouble with your sitemap, you can investigate the errors with Google Search Console. See Search Console's [sitemaps troubleshooting guide](https://support.google.com/webmasters/answer/7451001#errors) for help.

## Additional resources

Want to learn more? Check out the following resources:

- [Submit your sitemap to Google](/crawling-indexing/sitemaps/build-sitemap.md)
- [Learn how to combine sitemap extensions](/crawling-indexing/sitemaps/combine-sitemap-extensions.md)

# References & Citations

[^google-image-sitemaps]: Google Search Central (2025). "Image sitemaps". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps. Retrieved 2026-09-01.
