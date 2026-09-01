---
type: Reference
title: Enabling your ad network to work with translation-related Google Search features
description: Learn how you can enable your ad network to render or attribute correctly with translation-related Google Search features.
resource: https://developers.google.com/search/docs/appearance/ad-network-and-translation
tags:
- google-search
- documentation
- appearance
status: stable
generated:
  by: okf-sync/1.0
  at: '2026-09-01T14:52:09Z'
sources:
- id: google-ad-network-and-translation
  resource: https://developers.google.com/search/docs/appearance/ad-network-and-translation
  title: Enabling your ad network to work with translation-related Google Search features
  author: Google Search Central (Google LLC)
  last_modified: '2025-12-10T00:00:00Z'
---

# Enabling your ad network to work with translation-related Google Search features

> Mirrored from the official Google Search Central documentation at [https://developers.google.com/search/docs/appearance/ad-network-and-translation](https://developers.google.com/search/docs/appearance/ad-network-and-translation). Page content, including any embedded figures, is authored by Google and was last updated by Google on 2025-12-10.[^google-ad-network-and-translation]

Google Search offers several [translation-related features](/appearance/translated-results.md) that enable users to access translated content. If you run an ad network and your ads aren't working properly on translated web pages, you'll need to follow the steps in this guide to make sure your ads render or attribute correctly.

## Our approach

When users access translated content provided by [Google Translate](https://translate.google.com/about/) from within search results, Google retrieves the page from the publisher, rewrites the source URL, and translates the web page after the user clicks the translated result.

## Convert the Google Translate URL to the original URL

If you run an ad network that relies on the publisher’s source URL, you'll need to convert the Google Translate URL to make sure your ads are working properly. Follow these steps to decode the publisher’s hostname:

1.  Extract the domain prefix from the hostname, by removing the `.translate.goog` suffix.
2.  Split the `_x_tr_enc` parameter by the `,` (comma) character and save it as `encoding_list`.
3.  Prepend the value of the `_x_tr_hp` parameter to the domain prefix, if it exists.
4.  If `encoding_list` contains `1` and the output begins with `1-`, remove the `1-` prefix from the output of step 2.
5.  If `encoding_list` contains `0` and the output begins with `0-`, remove the `0-` prefix from the output of step 3. If you removed the prefix, set `is_idn` to `true`. Otherwise, set `is_idn` to `false`.
6.  Replace `/\b-\b/` (regex) with the `.` (dot) character.
7.  Replace the `--` (double hyphen) character with the `-` (hyphen) character.
8.  If `is_idn` is set to `true`, add the punycode prefix `xn--`.
9.  **Optional**: Convert to Unicode.

### Sample JavaScript code for decoding the hostname from a Google Translate URL

``` devsite-click-to-copy
function decodeHostname(proxyUrl) {
  const parsedProxyUrl = new URL(proxyUrl);
  const fullHost = parsedProxyUrl.hostname;
  // 1. Extract the domain prefix from the hostname, by removing the
        ".translate.goog" suffix
  let domainPrefix = fullHost.substring(0, fullHost.indexOf('.'));

  // 2. Split _x_tr_enc parameter by "," (comma), save as encodingList
  const encodingList = parsedProxyUrl.searchParams.has('_x_tr_enc') ?
      parsedProxyUrl.searchParams.get('_x_tr_enc').split(',') :
      [];

  // 3. Prepend value of _x_tr_hp parameter to the domain prefix, if it exists
  if (parsedProxyUrl.searchParams.has('_x_tr_hp')) {
    domainPrefix = parsedProxyUrl.searchParams.get('_x_tr_hp') + domainPrefix;
  }

  // 4. Remove '1-' prefix from the output of step 2 if encodingList contains
  //    '1' and the output begins with '1-'.
  if (encodingList.includes('1') && domainPrefix.startsWith('1-')) {
    domainPrefix = domainPrefix.substring(2);
  }

  // 5. Remove '0-' prefix from the output of step 3 if encodingList contains
  //    '0' and the output begins with '0-'.
  //    Set isIdn to true if removed, false otherwise.
  let isIdn = false;
  if (encodingList.includes('0') && domainPrefix.startsWith('0-')) {
    isIdn = true;
    domainPrefix = domainPrefix.substring(2);
  }

  // 6. Replace /\b-\b/ (regex) with '.' (dot) character.
  // 7. Replace '--' (double hyphen) with '-' (hyphen).
  let decodedSegment =
      domainPrefix.replaceAll(/\b-\b/g, '.').replaceAll('--', '-');

  // 8. If isIdn equals true, add the punycode prefix 'xn--'.
  if (isIdn) {
    decodedSegment = 'xn--' + decodedSegment;
  }
  return decodedSegment;
}
```

## Reconstruct the URL

1.  Using the original page URL, replace the hostname with the decoded hostname.
2.  Remove all `_x_tr_*` parameters.

## Test your code

You can create unit tests for your code using the following table. Given a `proxyUrl`, the `decodeHostname` must match the expected value.

The following table can only be used to test the hostname decoding. You’ll need to ensure that the path, fragment, and original parameters of the URL are preserved as is.

| `proxyUrl`                                                                                                                 | `decodeHostname`                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| `https://example-com.translate.goog`                                                                                       | `example.com`                                                                                                                 |
| `https://foo-example-com.translate.goog`                                                                                   | `foo.example.com`                                                                                                             |
| `https://foo--example-com.translate.goog`                                                                                  | `foo-example.com`                                                                                                             |
| `https://0-57hw060o-com.translate.goog/?_x_tr_enc=0`                                                                       | `xn--57hw060o.com (⚡😊.com)`                                                                                                 |
| `https://1-en--us-example-com/?_x_tr_enc=1`                                                                                | `en-us.example.com`                                                                                                           |
| `https://0-en----w45as309w-com.translate.goog/?_x_tr_enc=0`                                                                | `xn--en--w45as309w.com (en-⚡😊.com)`                                                                                         |
| `https://1-0-----16pw588q-com.translate.goog/?_x_tr_enc=0,1`                                                               | `xn----16pw588q.com (⚡-😊.com)`                                                                                              |
| `https://lanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch-co-uk.translate.goog/?_x_tr_hp=l`                       | `llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk`                                                            |
| `https://lanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch-co-uk.translate.goog/?_x_tr_hp=www-l`                   | `www.llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk`                                                        |
| `https://a--aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa-com.translate.goog/?_x_tr_hp=a--xn--xn--xn--xn--xn--------------------------a` | `a-xn-xn-xn-xn-xn-------------aa-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.com`                                                         |
| `https://g5h3969ntadg44juhyah3c9aza87iiar4i410avdl8d3f1fuq3nz05dg5b-com.translate.goog/?_x_tr_enc=0&_x_tr_hp=0-`           | `xn--g5h3969ntadg44juhyah3c9aza87iiar4i410avdl8d3f1fuq3nz05dg5b.com (💖🌲😊💞🤷‍♂️💗🌹😍🌸🌺😂😩😉😒😘💕🐶🐱🐭🐹🐰🐻🦊🐇😺.com)` |

# References & Citations

[^google-ad-network-and-translation]: Google Search Central (2025). "Enabling your ad network to work with translation-related Google Search features". *Google for Developers*. https://developers.google.com/search/docs/appearance/ad-network-and-translation. Retrieved 2026-09-01.
