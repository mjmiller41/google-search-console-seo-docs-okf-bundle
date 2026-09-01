---
type: Skill Reference
title: Grounding and citation rules
description: How audit skills locate the mirrored documentation, read it before making a claim, and cite it in findings.
tags: [skills, grounding, citations]
status: stable
---

# Grounding and citation rules

Every skill in this plugin audits a site against the Google Search Central
documentation mirrored in this same repository. The documentation is the
authority; the skills only know *which* document answers a question.

## 1. Resolve the bundle root

The plugin root is the repository root, so the concept documents sit directly
under it (`essentials/`, `crawling-indexing/`, `appearance/`, and so on).

```bash
ROOT="${CLAUDE_PLUGIN_ROOT}"     # set when running as an installed plugin
```

If `CLAUDE_PLUGIN_ROOT` is unset (a plain git checkout, or a skill copied into
`.claude/skills/`), use the directory containing the running `SKILL.md`, two
levels up. Quote `$ROOT` everywhere — installed plugin paths can contain spaces.

Confirm the root before using it: `ls "$ROOT/essentials/technical.md"` should
exist. If it does not, tell the user the documentation bundle could not be
found and stop rather than auditing from memory.

## 2. Read the document before you write the finding

This is the rule the whole plugin rests on:

> **Never state a requirement, threshold, limit, or valid value from memory.
> Open the grounding document for the check and take the wording from what you
> just read.**

Google changes these documents. Size limits, valid robots rules, required
structured-data properties, and policy definitions all move. A check matrix
names the *document* precisely for this reason and deliberately does not repeat
its contents. If a check's grounding document does not actually support the
finding you were about to write, drop the finding and say so.

## 3. Build the citation

Each concept's frontmatter carries what a citation needs:

```yaml
resource: https://developers.google.com/search/docs/crawling-indexing/block-indexing
sources:
  - last_modified: '2025-12-10T00:00:00Z'   # when Google last updated the page
generated:
  at: '2026-09-01T14:31:43Z'                # when this mirror was refreshed
```

Cite all three parts, so a reader can both follow the link and judge freshness:

```markdown
**Grounding:** crawling-indexing/block-indexing.md —
https://developers.google.com/search/docs/crawling-indexing/block-indexing
(Google last updated 2025-12-10; mirrored 2026-09-01)
```

## 4. Report the mirror's own limits

The mirror is a snapshot refreshed weekly, not a live read of Google's site.
Every report says so in its header, and the live documentation at
developers.google.com remains authoritative. Where Google offers a validator
that gives a definitive answer — the Rich Results Test for structured data, the
URL Inspection tool for rendering and indexing — recommend it rather than
implying this audit is the final word.

## 5. Running the shared scripts

The three helper scripts are Python 3.9+ stdlib only, print JSON to stdout, and
never write files:

```bash
python3 "$ROOT/skills/shared/scripts/site_probe.py" --base https://example.com --json
python3 "$ROOT/skills/shared/scripts/fetch_page.py" URL | \
  python3 "$ROOT/skills/shared/scripts/extract_signals.py" --from-fetch -
python3 "$ROOT/skills/shared/scripts/extract_signals.py" path/to/page.html --base-url https://example.com/page
```

Cache every script result for the session and reuse it. A URL is fetched at
most once per audit, across all skills — see [targets.md](./targets.md) for the
sampling and politeness rules.
