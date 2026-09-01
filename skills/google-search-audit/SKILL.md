---
name: google-search-audit
description: Audits a website or a codebase against Google's own Search documentation and produces one scored report with every finding cited to the relevant Google doc. Runs the full pipeline (eligibility and spam policies, crawling and indexing, structured data, SEO fundamentals, search appearance) or routes to a single focused audit. Use for "audit my site for Google", "full SEO audit", "is my site Google-ready", "check this repo before I launch", "will Google index this", or any Google Search question that does not obviously belong to one area. Works on a live URL or a local project directory. Not for other search engines, paid search, or analytics implementation.
type: Skill
title: Google Search audit (router)
tags: [skills, google-search, audit]
status: stable
---

# Google Search audit

This is the entry point for the audit suite. It either routes a focused
question to the one skill that owns it, or runs the full pipeline and merges
the results into a single report.

## 1. Resolve the bundle root

```bash
ROOT="${CLAUDE_PLUGIN_ROOT}"   # unset? use this SKILL.md's directory, two levels up
ls "$ROOT/essentials/technical.md"   # must exist
```

Quote `$ROOT` everywhere; installed plugin paths contain spaces. If the
documentation is not there, say so and stop — never audit from memory. The
rules are in [../shared/grounding.md](../shared/grounding.md).

## 2. Resolve the target

Follow [../shared/targets.md](../shared/targets.md) to decide the mode (live
URL, static directory, or both) and pick the page sample. Honor the politeness
limits: sequential fetches, one second apart, ten pages by default.

## 3. Route, or run everything

Route to a single skill when the request clearly belongs to one:

| The user is asking about | Read and follow |
| :--- | :--- |
| Indexing eligibility, spam policies, manual actions | `$ROOT/skills/search-essentials/SKILL.md` |
| robots.txt, sitemaps, canonicals, redirects, JavaScript, mobile | `$ROOT/skills/crawling-indexing/SKILL.md` |
| Schema markup, JSON-LD, rich results | `$ROOT/skills/structured-data/SKILL.md` |
| General SEO advice, "where do I start" | `$ROOT/skills/seo-fundamentals/SKILL.md` |
| Titles, snippets, favicons, page experience, ranking systems | `$ROOT/skills/search-appearance/SKILL.md` |
| A drop in traffic, rankings, or impressions | `$ROOT/skills/traffic-drops/SKILL.md` |

A reported traffic drop always goes to `traffic-drops`, even when phrased as an
audit request: the diagnosis is a different job from a checklist, and starting
from the drop pattern is what Google's own methodology prescribes.

Otherwise run the full audit, described in
[reference/full-audit.md](./reference/full-audit.md). Read that file before
starting — it fixes the order, the shared signal cache, and which skill owns
each overlapping check.

## 4. Report

Emit one report in the shape defined by
[../shared/report-format.md](../shared/report-format.md): a scorecard, findings
grouped by category, the checks that could not run and why, and the method.

Two rules that matter more than completeness:

- **Every finding cites the Google documentation it rests on**, by bundle path
  and upstream URL, with the date Google last updated it. A finding you cannot
  ground is one you should not write.
- **No invented scores.** Verdicts and counts only. Google publishes no
  hundred-point scale, and implying one misrepresents the audit's precision.

If eligibility blockers fire across the whole site — robots.txt disallowing
everything, a site-wide noindex — report those first and ask whether to
continue. The rest of the audit is moot until the site can be indexed at all.
