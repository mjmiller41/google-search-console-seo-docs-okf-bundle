---
type: Skill Reference
title: Optional integrations
description: The credentials that unlock the checks a plain crawl cannot run — Core Web Vitals field data, Search Console index coverage and rich-results verdicts — and how to configure each one.
tags: [skills, integrations, configuration]
status: stable
---

# Optional integrations

A crawl cannot see real-user performance data, what Google actually kept in its
index, or Google's own rich-results verdict. Those land in every report's
"Checks not run" table until the credentials below exist. Each integration is
optional and independent; audit skills probe for them and quietly skip what is
not configured.

## What each unlocks

| Audit gap | Integration | Script |
| :--- | :--- | :--- |
| Core Web Vitals field data (APP-08) | CrUX or PageSpeed Insights API key | `scripts/cwv_field_data.py` |
| Actual index coverage per URL | Search Console token | `scripts/gsc_probe.py --inspect` |
| Rich-results verdict per URL (the Rich Results Test assessment) | Search Console token | `scripts/gsc_probe.py --inspect` |
| Clicks/impressions for traffic-drop work | Search Console token | `scripts/gsc_probe.py --analytics` |
| Manual actions, security issues | None exists — UI only | `scripts/gsc_probe.py --reports` prints the report URLs |
| Cloaking comparison (ESS-10) | None — an opt-in fetch | `fetch_page.py --ua "Googlebot/2.1 ..."` |

## Core Web Vitals: `CRUX_API_KEY` / `PSI_API_KEY`

One Google Cloud API key serves both APIs. In a project of your choosing,
enable `chromeuxreport.googleapis.com` and `pagespeedonline.googleapis.com`,
create an API key restricted to those two services, and export it:

```bash
export CRUX_API_KEY="..."   # also used as the PSI key when PSI_API_KEY is unset
```

With the key set, `cwv_field_data.py` queries CrUX directly (fast, field data
only) and falls back to PageSpeed Insights when CrUX has no record for a URL.
Without any key, PSI is tried anonymously — but the shared anonymous quota is
routinely exhausted, so treat keyless mode as best-effort only.

The verdicts come from the API responses (CrUX returns its threshold bins, PSI
returns a category per metric); the script hardcodes no thresholds, consistent
with [grounding.md](./grounding.md).

## Search Console: a scoped token

Requires the auditing account to have access to the site's Search Console
property. Two pieces:

1. Enable `searchconsole.googleapis.com` in the same Google Cloud project.
2. Grant application-default credentials the Search Console scope (one
   interactive login):

```bash
gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters.readonly
export GOOGLE_CLOUD_QUOTA_PROJECT="<project-id>"
```

`gsc_probe.py` then works without further setup; in CI, mint a token by any
other means and pass it as `GSC_ACCESS_TOKEN` instead. Verify with
`--list-sites`, which should show the property (`sc-domain:` form preferred).

**URL Inspection is the high-value call.** For each sampled URL it returns
Google's own coverage state, indexing verdict, chosen canonical, last crawl
time, and rich-results assessment — the answers the Page Indexing report and
Rich Results Test give, per URL, without leaving the audit. Inspect the
sampled URLs, not the whole site; the API has daily per-property quotas.

**Manual Actions and Security Issues have no API.** The audit reports them as
UI checks with direct links (`--reports`); a clean crawl is not evidence either
report is clean.

## Cloaking probes: deliberate, not default

The ESS-10 comparison fetches a page twice — default audit user agent, then a
Googlebot user-agent string — and diffs what came back. Run it only with the
site owner's knowledge: CDNs and bot managers commonly challenge fake Googlebot
requests, which both skews the result and can flag the auditor's IP. A
difference is an indicator, never proof; real Googlebot verification is
reverse DNS, per `crawling-indexing/crawlers-fetchers/verifying-googlebot.md`.

## Reporting rule

When an integration is configured, its findings join the normal report with
the same grounding standard (cite `appearance/core-web-vitals.md` for CWV
verdicts, `monitor-debug/search-console-start.md` for GSC-derived ones). When
it is not, the check stays in "Checks not run" — with the one-line setup
pointer from the table above, so the reader knows the gap is closable.
