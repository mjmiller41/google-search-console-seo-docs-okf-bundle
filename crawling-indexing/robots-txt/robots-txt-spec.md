---
type: Reference
title: How Google interprets the robots.txt specification
description: Learn specific details about the different robots.txt file rules and how Google interprets the robots.txt specification.
resource: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec
tags:
- google-search
- documentation
- crawling-indexing
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:52:09Z'
sources:
- id: google-robots-txt-spec
  resource: https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec
  title: How Google interprets the robots.txt specification
  author: Google Search Central (Google LLC)
  last_modified: '2026-08-31T00:00:00Z'
---

# How Google interprets the robots.txt specification

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2026-08-31.[^google-robots-txt-spec]

Google's automated [crawlers](/crawling-indexing/crawlers-fetchers/overview-google-crawlers.md) support the [Robots Exclusion Protocol (REP)](https://www.rfc-editor.org/rfc/rfc9309.html). This means that before crawling a site, Google's crawlers download and parse the site's robots.txt file to extract information about which parts of the site may be crawled. The REP isn't applicable to Google's crawlers that are controlled by users (for example, feed subscriptions), or crawlers that are used to increase user safety (for example, malware analysis).

This page describes Google's interpretation of the REP. For the original standard, check [RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html).

## What is a robots.txt file

If you don't want crawlers to access sections of your site, you can create a robots.txt file with appropriate rules. A robots.txt file is a text file containing rules about which crawlers may access which parts of a site. For example, the robots.txt file for example.com may look like this:

    # This robots.txt file controls crawling of URLs under https://example.com.
    # All crawlers are disallowed to crawl files in the "includes" directory, such
    # as .css, .js, but Google needs them for rendering, so Googlebot is allowed
    # to crawl them.
    User-agent: *
    Disallow: /includes/

    User-agent: Googlebot
    Allow: /includes/

    Sitemap: https://example.com/sitemap.xml

If you're new to robots.txt, start with our [intro to robots.txt](/crawling-indexing/robots/intro.md). You can also find [tips for creating a robots.txt file](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt).

## File location and range of validity

You must place the robots.txt file in the top-level directory of a site, on a supported protocol. The URL for the robots.txt file is (like other URLs) case-sensitive. In case of Google Search, the supported protocols are HTTP, HTTPS, and FTP. On HTTP and HTTPS, crawlers fetch the robots.txt file with an HTTP non-conditional `GET` request; on FTP, crawlers use a standard `RETR (RETRIEVE)` command, using anonymous login.

The rules listed in the robots.txt file apply only to the host, protocol, and port number where the robots.txt file is hosted.

## Examples of valid robots.txt URLs

The following table contains examples of robots.txt URLs and what URL paths they're valid for. Column one contains the URL of a robots.txt file, and column two contains domains that that robots.txt file would and wouldn't apply to.

<table>
<thead>
<tr>
<th colspan="2">Robots.txt URL examples</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/robots.txt</code></td>
<td>
<p>
          This is the general case. It's not valid for other subdomains, protocols, or port
          numbers. It's valid for all files in all subdirectories on the same host, protocol,
          and port number.
        </p>
Valid for:
<ul>
<li><code>https://example.com/</code></li>
<li><code>https://example.com/folder/file</code></li>
</ul>
Not valid for:
<ul>
<li><code>https://other.example.com/</code></li>
<li><code>http://example.com/</code></li>
<li><code>https://example.com:8181/</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>https://www.example.com/robots.txt</code></td>
<td>
<p>
          A robots.txt on a subdomain is only valid for that subdomain.
        </p>
<p>
Valid for:
<code>https://www.example.com/</code>
</p>
<p>Not valid for:</p>
<ul>
<li><code>https://example.com/</code></li>
<li><code>https://shop.www.example.com/</code></li>
<li><code>https://www.shop.example.com/</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>https://example.com/folder/robots.txt</code></td>
<td>
        Not a valid robots.txt file. Crawlers don't check for robots.txt files in subdirectories.
      </td>
</tr>
<tr>
<td><code>https://www.exämple.com/robots.txt</code></td>
<td>
<p>
          IDNs are equivalent to their punycode versions. See also
          <a href="https://www.ietf.org/rfc/rfc3492.txt">RFC 3492</a>.
        </p>
Valid for:
<ul>
<li><code>https://www.exämple.com/</code></li>
<li><code>https://xn--exmple-cua.com/</code></li>
</ul>
<p>
Not valid for:
<code>https://www.example.com/</code>
</p>
</td>
</tr>
<tr>
<td><code>ftp://example.com/robots.txt</code></td>
<td>
<p>
Valid for:
<code>ftp://example.com/</code>
</p>
<p>
Not valid for:
<code>https://example.com/</code>
</p>
</td>
</tr>
<tr>
<td><code>https://212.96.82.21/robots.txt</code></td>
<td>
<p>
           A robots.txt with an IP-address as the hostname is only valid for crawling of that
          IP address as the hostname. It isn't automatically valid for all websites hosted on that
          IP address (though it's possible that the robots.txt file is shared, in which case it
          would also be available under the shared hostname).
        </p>
<p>
Valid for:
<code>https://212.96.82.21/</code>
</p>
<p>
Not valid for:
<code>https://example.com/</code> (even if hosted on <code>212.96.82.21</code>)
        </p>
</td>
</tr>
<tr>
<td><code>https://example.com:443/robots.txt</code></td>
<td>
<p>
          Standard port numbers (<code>80</code> for HTTP, <code>443</code> for HTTPS,
          <code>21</code> for FTP) are equivalent to their default hostnames.
        </p>
<p>Valid for:</p>
<ul>
<li><code>https://example.com:443/</code></li>
<li><code>https://example.com/</code></li>
</ul>
<p>
Not valid for:
<code>https://example.com:444/</code>
</p>
</td>
</tr>
<tr>
<td><code>https://example.com:8181/robots.txt</code></td>
<td>
<p>
          Robots.txt files on non-standard port numbers are only valid for content made
          available through those port numbers.
        </p>
<p>
Valid for:
<code>https://example.com:8181/</code>
</p>
<p>
Not valid for:
<code>https://example.com/</code>
</p>
</td>
</tr>
</tbody>
</table>

## Handling of errors and HTTP status codes

When requesting a robots.txt file, the HTTP status code of the server's response affects how the robots.txt file will be used by Google's crawlers. The following table summarizes how Googlebot treats robots.txt files for different HTTP status codes.

<table>
<thead>
<tr>
<th colspan="2">Handling of errors and HTTP status codes</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>2xx (success)</code></td>
<td>
        HTTP status codes that signal success prompt Google's crawlers to process the robots.txt
        file as provided by the server.
      </td>
</tr>
<tr>
<td><code>3xx (redirection)</code></td>
<td>
<p>
          Google follows at least five redirect hops as defined by
          <a href="https://www.ietf.org/rfc/rfc1945.txt">RFC 1945</a> and then
          stops and treats it as a <code>404</code> for the robots.txt file. This also applies to any
          disallowed URLs in the redirect chain, since the crawler couldn't fetch rules due to
          the redirects.
        </p>
<p>
          Google doesn't follow logical redirects in robots.txt files (frames, JavaScript, or
          meta refresh-type redirects).
        </p>
</td>
</tr>
<tr>
<td><code>4xx (client errors)</code></td>
<td>
<p>
          Google's crawlers treat all <code>4xx</code> errors, except <code>429</code>, as if a
          valid robots.txt file didn't exist. This means that Google assumes that there are no crawl
          restrictions.
        </p>
<blockquote>
          Don't use <code>401</code> and <code>403</code> status codes for limiting the crawl rate.
          The <code>4xx</code> status codes, except <code>429</code>, have no effect on crawl rate.
          <a href="/crawling-indexing/crawlers-fetchers/reduce-crawl-rate.md">Learn how to limit your crawl rate</a>.
        </blockquote>
</td>
</tr>
<tr>
<td><code>5xx (server errors)</code></td>
<td>
<p>
        If Google finds a robots.txt file but can't fetch it, Google follows this behavior:
      </p>
<ol>
<li>For the first 12 hours, Google stops crawling the site but keeps trying to fetch the
          robots.txt file.
        </li>
<li>If Google can't fetch a new version, for the next 30 days Google will use the last good
          version, while still trying to fetch a new version. A <code>503 (service unavailable)</code>
          error results in fairly frequent retrying. If there's no cached version available,
          Google assumes there's no crawl restrictions.
        </li>
<li>If the errors are still not fixed after 30 days:
          <ul>
<li>If the site is generally available to Google, Google will behave as if there is no
              robots.txt file (but still keep checking for a new version).
            </li>
<li>
              If the site has general availability problems, Google will stop crawling the site,
              while still periodically requesting a robots.txt file.
            </li>
</ul>
</li>
</ol>
</td>
</tr>
<tr>
<td>Other errors</td>
<td>
        A robots.txt file which cannot be fetched due to DNS or networking issues, such as
        timeouts, invalid responses, reset or interrupted connections, and HTTP chunking errors,
        is treated as a <a href="https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec/#server-error">server error</a>.
      </td>
</tr>
</tbody>
</table>

## Caching

Google generally caches the contents of robots.txt file for up to 24 hours, but may cache it longer in situations where refreshing the cached version isn't possible (for example, due to timeouts or `5xx` errors). The cached response may be shared by different crawlers. Google may increase or decrease the cache lifetime based on [max-age Cache-Control](https://www.rfc-editor.org/rfc/rfc9110.html) HTTP headers.

## File format

The robots.txt file must be a [UTF-8](https://en.wikipedia.org/wiki/UTF-8) encoded plain text file and the lines must be separated by `CR`, `CR/LF`, or `LF`.

Google ignores invalid lines in robots.txt files, including the Unicode [Byte Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark) (BOM) at the beginning of the robots.txt file, and use only valid lines. For example, if the content downloaded is HTML instead of robots.txt rules, Google will try to parse the content and extract rules, and ignore everything else.

Similarly, if the character encoding of the robots.txt file isn't UTF-8, Google may ignore characters that are not part of the UTF-8 range, potentially rendering robots.txt rules invalid.

Google enforces a robots.txt file size limit of 500 [kibibytes](https://en.wikipedia.org/wiki/Kibibyte) (KiB). Content which is after the maximum file size is ignored. You can reduce the size of the robots.txt file by consolidating rules that would result in an oversized robots.txt file. For example, place excluded material in a separate directory.

## Syntax

A valid robots.txt line consists of a field, a colon, and a value. Field names are case-insensitive (for example, `User-agent` and `user-agent` are treated the same). Spaces are optional, but recommended to improve readability. Space at the beginning and at the end of the line is ignored. To include comments, precede your comment with the `#` character. Keep in mind that everything after the `#` character will be ignored. The general format is `<field>:<value><#optional-comment>`.

Google supports the following fields (other fields such as `crawl-delay` aren't supported):

- `user-agent`: identifies which crawler the rules apply to.
- `allow`: a URL path that may be crawled.
- `disallow`: a URL path that may not be crawled.
- `sitemap`: the complete URL of a sitemap.

The `allow` and `disallow` fields are also called rules (also known as directives). These rules are always specified in the form of `rule: [path]` where `[path]` is optional. By default, there are no restrictions for crawling for the designated crawlers. Crawlers ignore rules without a `[path]`.

The `[path]` value, if specified, is relative to the root of the website from where the robots.txt file was fetched (using the same protocol, port number, host and domain names). The path value must start with `/` to designate the root and the value is case-sensitive. Learn more about [URL matching based on path values](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec/#url-matching-based-on-path-values).

### `user-agent`

The `user-agent` line identifies which crawler rules apply to. See [Google's crawlers and user-agent strings](/crawling-indexing/crawlers-fetchers/overview-google-crawlers.md) for a comprehensive list of user-agent strings you can use in your robots.txt file.

Both the `user-agent` field name and its value are case-insensitive.

### `disallow`

The `disallow` rule specifies paths that must not be accessed by the crawlers identified by the `user-agent` line the `disallow` rule is grouped with. Crawlers ignore the rule without a path.

Google can't index the content of pages which are disallowed for crawling, but it may still index the URL and show it in search results without a snippet. Learn how to [block indexing](/crawling-indexing/block-indexing.md).

The field name (`disallow`) is case-insensitive, but its value is case-sensitive.

Usage:

    disallow: [path]

### `allow`

The `allow` rule specifies paths that may be accessed by the designated crawlers. When no path is specified, the rule is ignored.

The field name (`allow`) is case-insensitive, but its value is case-sensitive.

Usage:

    allow: [path]

### `sitemap`

Google, Bing, and other major search engines support the `sitemap` field in robots.txt, as defined by [sitemaps.org](https://sitemaps.org).

The field name (`sitemap`) is case-insensitive, but its value is case-sensitive.

Usage:

    sitemap: [absoluteURL]

The `[absoluteURL]` line points to the location of a sitemap or sitemap index file. It must be a fully qualified URL, including the protocol and host, and doesn't have to be URL-encoded. The URL doesn't have to be on the same host as the robots.txt file. You can specify multiple `sitemap` fields, with no limit to the number of sitemaps you can include. The sitemap field isn't tied to any specific user agent and may be followed by all crawlers, provided it isn't disallowed for crawling.

For example:

    user-agent: otherbot
    disallow: /kale

    sitemap: https://example.com/sitemap.xml
    sitemap: https://cdn.example.org/other-sitemap.xml
    sitemap: https://ja.example.org/テスト-サイトマップ.xml

## Grouping of lines and rules

You can group together rules that apply to multiple user agents by repeating `user-agent` lines for each crawler.

For example:

    user-agent: a
    disallow: /c

    user-agent: b
    disallow: /d

    user-agent: e
    user-agent: f
    disallow: /g

    user-agent: h

In this example there are four distinct rule groups:

- One group for user agent "a".
- One group for user agent "b".
- One group for both "e" and "f" user agents.
- One group for user agent "h".

For the technical description of a group, see [section 2.1 of the REP](https://www.rfc-editor.org/rfc/rfc9309.html#section-2.1-2.4).

## Order of precedence for user agents

Only one group is valid for a particular crawler. Google's crawlers determine the correct group of rules by finding in the robots.txt file the group with the most specific user agent that matches the crawler's user agent. Other groups are ignored. All non-matching text is ignored (for example, both `googlebot/1.2` and `googlebot*` are equivalent to `googlebot`). The order of the groups within the robots.txt file is irrelevant.

If there's more than one specific group declared for a user agent, all the rules from the groups applicable to the specific user agent are combined internally into a single group. User agent specific groups and global groups (`*`) are not combined.

### Examples

#### Matching of `user-agent` fields

    user-agent: googlebot-news
    (group 1)

    user-agent: *
    (group 2)

    user-agent: googlebot
    (group 3)

This is how the crawlers would choose the relevant group:

| Group followed per crawler            |                                                                                                                                                                                                        |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Googlebot News                        | `googlebot-news` follows group 1, because group 1 is the most specific group.                                                                                                                          |
| Googlebot (web)                       | `googlebot` follows group 3.                                                                                                                                                                           |
| Googlebot Storebot                    | `Storebot-Google` follows group 2, because there is no specific `Storebot-Google` group.                                                                                                               |
| Googlebot News (when crawling images) | When crawling images, `googlebot-news` follows group 1. `googlebot-news` doesn't crawl the images for Google Images, so it only follows group 1.                                                       |
| Otherbot (web)                        | Other Google crawlers follow group 2.                                                                                                                                                                  |
| Otherbot (news)                       | Other Google crawlers that crawl news content, but don't identify as `googlebot-news` follow group 2. Even if there is an entry for a related crawler, it is only valid if it's specifically matching. |

#### Grouping of rules

If there are multiple groups in a robots.txt file that are relevant to a specific user agent, Google's crawlers internally merge the groups. For example:

    user-agent: googlebot-news
    disallow: /fish

    user-agent: *
    disallow: /carrots

    user-agent: googlebot-news
    disallow: /shrimp

The crawlers internally group the rules based on user agent, for example:

    user-agent: googlebot-news
    disallow: /fish
    disallow: /shrimp

    user-agent: *
    disallow: /carrots

Rules other than `allow`, `disallow`, and `user-agent` are ignored by the robots.txt parser. This means that the following robots.txt snippet is treated as one group, and thus both `user-agent` `a` and `b` are affected by the `disallow: /` rule:

    user-agent: a
    sitemap: https://example.com/sitemap.xml

    user-agent: b
    disallow: /

When the crawlers process the robots.txt rules, they ignore the `sitemap` line. For example, this is how the crawlers would understand the previous robots.txt snippet:

    user-agent: a
    user-agent: b
    disallow: /

## URL matching based on path values

Google uses the path value in the `allow` and `disallow` rules as a basis to determine whether or not a rule applies to a specific URL on a site. This works by comparing the rule to the path component of the URL that the crawler is trying to fetch. The path in the rules can be either raw UTF-8 characters or percent-encoded UTF-8 strings (per [RFC 3986](https://www.rfc-editor.org/rfc/rfc3986.html)). As defined in [RFC 9309 Section 2.2.2](https://www.rfc-editor.org/rfc/rfc9309.html#section-2.2.2), Google's crawlers compare rules against URLs using their percent-encoded forms, and automatically canonicalize raw UTF-8 rule paths into percent-encoded forms. This means that, for example, `Disallow: /foo/bar/ツ` and `Disallow: /foo/bar/%E3%83%84` are treated identically by the parser.

Google, Bing, and other major search engines support a limited form of *wildcards* for path values. These wildcard characters are:

- `*` designates 0 or more instances of any valid character.
- `$` designates the end of the URL.

The following table shows how the different wildcard characters affect parsing:

<table>
<thead>
<tr>
<th colspan="2">Example path matches</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>/</code></td>
<td>Matches the root and any lower level URL.</td>
</tr>
<tr>
<td>
<code>/*</code></td>
<td>Equivalent to <code>/</code>. The trailing wildcard is ignored.</td>
</tr>
<tr>
<td><code>/$</code></td>
<td>Matches only the root. Any lower level URL is allowed for crawling.</td>
</tr>
<tr>
<td><code>/fish</code></td>
<td>
<p>
          Matches any path that starts with <code>/fish</code>. Note that the matching is case-sensitive.
        </p>
<p>Matches:</p>
<ul>
<li><code>/fish</code></li>
<li><code>/fish.html</code></li>
<li><code>/fish/salmon.html</code></li>
<li><code>/fishheads</code></li>
<li><code>/fishheads/yummy.html</code></li>
<li><code>/fish.php?id=anything</code></li>
</ul>
<p>Doesn't match:</p>
<ul>
<li><code>/Fish.asp</code></li>
<li><code>/catfish</code></li>
<li><code>/?id=fish</code></li>
<li><code>/desert/fish</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/fish*</code></td>
<td>
<p>
          Equivalent to <code>/fish</code>. The trailing wildcard is ignored.
        </p>
<p>Matches:</p>
<ul>
<li><code>/fish</code></li>
<li><code>/fish.html</code></li>
<li><code>/fish/salmon.html</code></li>
<li><code>/fishheads</code></li>
<li><code>/fishheads/yummy.html</code></li>
<li><code>/fish.php?id=anything</code></li>
</ul>
<p>Doesn't match:</p>
<ul>
<li><code>/Fish.asp</code></li>
<li><code>/catfish</code></li>
<li><code>/?id=fish</code></li>
<li><code>/desert/fish</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/fish/</code></td>
<td>
<p>
          Matches anything in the <code>/fish/</code> folder.
        </p>
<p>Matches:</p>
<ul>
<li><code>/fish/</code></li>
<li><code>/fish/?id=anything</code></li>
<li><code>/fish/salmon.htm</code></li>
</ul>
<p>Doesn't match:</p>
<ul>
<li><code>/fish</code></li>
<li><code>/fish.html</code></li>
<li><code>/animals/fish/</code></li>
<li><code>/Fish/Salmon.asp</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/*.php</code></td>
<td>
<p>
          Matches any path that contains <code>.php</code>.
        </p>
<p>Matches:</p>
<ul>
<li><code>/index.php</code></li>
<li><code>/filename.php</code></li>
<li><code>/folder/filename.php</code></li>
<li><code>/folder/filename.php?parameters</code></li>
<li><code>/folder/any.php.file.html</code></li>
<li><code>/filename.php/</code></li>
</ul>
<p>Doesn't match:</p>
<ul>
<li><code>/</code> (even if it maps to /index.php)</li>
<li><code>/windows.PHP</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/*.php$</code></td>
<td>
<p>
          Matches any path that ends with <code>.php</code>.
        </p>
<p>Matches:</p>
<ul>
<li><code>/filename.php</code></li>
<li><code>/folder/filename.php</code></li>
</ul>
<p>Doesn't match:</p>
<ul>
<li><code>/filename.php?parameters</code></li>
<li><code>/filename.php/</code></li>
<li><code>/filename.php5</code></li>
<li><code>/windows.PHP</code></li>
</ul>
</td>
</tr>
<tr>
<td><code>/fish*.php</code></td>
<td>
<p>
          Matches any path that contains <code>/fish</code> and <code>.php</code>, in that order.
        </p>
<p>Matches:</p>
<ul>
<li><code>/fish.php</code></li>
<li><code>/fishheads/catfish.php?parameters</code></li>
</ul>
<p>
Doesn't match:</p>
<code>/Fish.PHP</code>
</td>
</tr>
</tbody>
</table>

## Order of precedence for rules

When matching robots.txt rules to URLs, crawlers use the most specific rule based on the length of the rule path. In case of conflicting rules, including those with wildcards, Google uses the least restrictive rule.

The following examples demonstrate which rule Google's crawlers will apply on a given URL.

<table>
<thead>
<tr>
<th colspan="2">Sample situations</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>https://example.com/page</code></td>
<td>
<pre>allow: /p
disallow: /</pre>
<p>
<b>Applicable rule</b>: <code>allow: /p</code>, because it's more specific.
        </p>
</td>
</tr>
<tr>
<td><code>https://example.com/folder/page</code></td>
<td>
<pre>allow: /folder
disallow: /folder</pre>
<p>
<b>Applicable rule</b>: <code>allow: /folder</code>, because in case of
          conflicting rules, Google uses the least restrictive rule.
        </p>
</td>
</tr>
<tr>
<td><code>https://example.com/page.htm</code></td>
<td>
<pre>allow: /page
disallow: /*.htm</pre>
<p>
<b>Applicable rule</b>: <code>disallow: /*.htm</code>, because the rule path is longer and
          it matches more characters in the URL, so it's more specific.
        </p>
</td>
</tr>
<tr>
<td><code>https://example.com/page.php5</code></td>
<td>
<pre>allow: /page
disallow: /*.ph</pre>
<p>
<b>Applicable rule</b>: <code>allow: /page</code>, because in case of
          conflicting rules, Google uses the least restrictive rule.
        </p>
</td>
</tr>
<tr>
<td><code>https://example.com/</code></td>
<td>
<pre>allow: /$
disallow: /</pre>
<p>
<b>Applicable rule</b>: <code>allow: /$</code>, because it's more specific.
        </p>
</td>
</tr>
<tr>
<td><code>https://example.com/page.htm</code></td>
<td>
<pre>allow: /$
disallow: /</pre>
<p>
<b>Applicable rule</b>: <code>disallow: /</code>, because the
          <code>allow</code> rule only applies on the root URL.
        </p>
</td>
</tr>
</tbody>
</table>

# References & Citations

[^google-robots-txt-spec]: Google Search Central (2026). "How Google interprets the robots.txt specification". *Google for Developers*. https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec. Retrieved 2026-09-01.
