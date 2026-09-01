---
type: Reference
title: Fix canonicalization issues
description: Learn how to debug the most common canonicalization issues in Google Search.
resource: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:31:43Z'
sources:
- id: google-canonicalization-troubleshooting
  resource: https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting
  title: Fix canonicalization issues
  author: Google Search Central (Google LLC)
  last_modified: '2026-08-21T00:00:00Z'
---

# Fix canonicalization issues

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting](https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-08-21.[^google-canonicalization-troubleshooting]

Even if you explicitly designate a canonical page, Google might choose a different canonical for various reasons, such as the quality of the content or technical signals. To troubleshoot canonicalization issues, follow these steps:

1.  **Check which page Google considers to be the canonical page:** Use the [URL Inspection tool](https://support.google.com/webmasters/answer/9012289#google-selected-canonical) to check [which page Google considers canonical](/crawling-indexing/canonicalization.md) and think about whether the Google-selected canonical makes more sense than your preferred canonical URL for your users coming from Google Search.

    > **Important:** If a canonical URL is in a Search Console property that you don't own, you won't be able to see any of the traffic for your duplicate page.

2.  **Look for technical canonicalization issues:** Verify whether an unexpected canonical URL preference is being signaled through technical misconfigurations. Review the [common canonicalization issues table](https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting/#common-issues) to check for issues like incorrect canonical elements, server misconfigurations, or missing localization annotations.

3.  **Ensure clustered pages are sufficiently different:** Fixing canonicalization issues technically boils down to ensuring that the pages that are [clustered together](/crawling-indexing/canonicalization.md) are sufficiently different. Things to keep in mind:
    - **Re-evaluation takes time:** Even after fixing content issues, Google might hold pages in a duplicate cluster for **up to two weeks**.
    - **Content difference matters:** Pages will generally split out faster if the difference between the new content and the other clustered pages is clear and significant.

4.  **Request re-indexing:** Once you fix the content issues, use the "Request Indexing" feature in the Search Console [URL Inspection tool](https://support.google.com/webmasters/answer/9012289#request_indexing) to ask Google to re-evaluate the pages that are clustered. However, since this feature is subject to quotas, reserve it for your most important URLs.

## Common canonicalization issues

There are various reasons why the selected canonical URL differs from the canonical URL you'd prefer to see in Search. The most common issues are:

<table>
<tr><th colspan="2">Common canonicalization issues</th></tr>
<tr>
<td><h2>Language variants without localized annotations</h2></td>
<td>
      If you have multiple websites that serve substantially the same content localized to
      different users around the world, be sure to
      <a href="/specialty/international/overview.md">follow our guidelines for localized sites</a>.
      For example, if you have different sites for your English-speaking users in the United
      States, United Kingdom, and Australia respectively, but the content is the same, adding
      <code>hreflang</code> annotations to your pages can help the right pages surface for users
      in different regions.
    </td>
</tr>
<tr>
<td><h2>Incorrect canonical elements</h2></td>
<td>
      Some content management systems (CMS) or CMS plugins can make incorrect use of
      canonicalization techniques to point to undesired URLs. Check your HTML with your browser's
      developer tools to see if so. If your site is indicating an unexpected canonical URL
      preference, perhaps through incorrect use of <code>rel="canonical"</code> or a
      <code>3xx</code> redirect, contact your CMS provider and report this error to them.
    </td>
</tr>
<tr>
<td><h2>Misconfigured servers</h2></td>
<td>
      Some hosting misconfigurations may cause unexpected cross-domain URL selection. For example:
      <ul>
<li>
          A server may be misconfigured to return content from <code>example.com</code> in
          response to a request for a URL on <code>other.example</code>
</li>
<li>
          Two unrelated web servers may return identical
          <a href="/crawling-indexing/troubleshoot-crawling-errors.md"><code>soft 404</code> pages</a>
          that Google fails to identify as error pages. If you notice this is the case, get
          in touch with your hosting provider.
        </li>
</ul>
</td>
</tr>
<tr>
<td><h2>Malicious hacking</h2></td>
<td>
      Some attacks on websites introduce code that returns an HTTP
      <a href="/crawling-indexing/301-redirects.md"><code>3xx</code> redirect</a>
      or inserts a cross-domain <code>rel="canonical"</code> <code>link</code> annotation
      into the HTML <code>&lt;head&gt;</code> or HTTP header, usually pointing to a URL
      hosting malicious or spammy content. In these cases, our algorithms may choose the
      malicious or spammy URL instead of the URL on the
      <a href="https://web.dev/articles/hacked">compromised website</a>.
    </td>
</tr>
<tr>
<td><h2>Syndicated content</h2></td>
<td>
      The canonical link element is not recommended for those who want to avoid duplication by
      syndication partners, because the pages are often very different. The most effective
      solution is for partners to block indexing of your content. For more, see
      <a href="https://support.google.com/news/publisher-center/answer/9606800">Avoid article duplication in Google News</a>,
      which also has advice about blocking syndicated content from Google Search.
    </td>
</tr>
<tr>
<td><h2>A copycat website</h2></td>
<td>
      In rare situations, our algorithm may select a URL from an external site that is hosting
      your content without your permission. If you believe that another site is duplicating
      your content in violation of copyright law, you may contact the site's host to request
      removal. In addition, you can request that Google remove the infringing page from our
      search results by
      <a href="https://support.google.com/legal/answer/1120734">filing a request under the Digital Millennium Copyright Act</a>.
    </td>
</tr>
</table>

# References & Citations

[^google-canonicalization-troubleshooting]: Google Search Central (2026). "Fix canonicalization issues". *Google for Developers*. https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting. Retrieved 2026-09-01.
