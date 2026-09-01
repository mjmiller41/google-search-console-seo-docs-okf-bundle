---
type: Bundle Guide
title: Working in this repository
description: Rules for agents and contributors editing this bundle — what is generated, how the audit skills stay grounded, and the checks that must pass.
tags: [contributing, agents]
status: stable
---

# Working in this repository

This repository is two things: a mirror of the Google Search Central
documentation as an OKF v0.2 bundle, and a Claude Code plugin whose skills
audit sites against that documentation.

## 1. The concept documents are generated — do not hand-edit them

Everything under `essentials/`, `fundamentals/`, `crawling-indexing/`,
`appearance/`, `monitor-debug/`, and `specialty/`, plus `overview.md` and every
`index.md`, is produced by `sync_docs.py` from developers.google.com. A manual
edit survives only until the next sync overwrites it.

To correct something in a concept, fix the converter in `sync_docs.py` and
re-run it. Editable by hand: `sync_docs.py`, `skills/`, `README.md`, this file,
and the workflow.

Change detection compares rendered output byte for byte, so the conversion must
stay deterministic. Pin the versions of anything that shapes the output — this
is why `requirements.txt` pins beautifulsoup4 and the workflow pins pandoc, and
why table passthrough is decided in our own code rather than left to pandoc.

## 2. Skills name documents; they never restate them

The audit skills under `skills/` hold check matrices that point at concept
documents. They deliberately contain no thresholds, no property lists, no
policy wording. The model reads the grounding document at runtime and takes the
wording from there.

This is what keeps the plugin correct as Google revises its documentation: the
weekly sync updates the concepts, and the skills' knowledge updates with them.
A check that hardcodes a limit is a check that will silently go stale, so:

- Add a check by adding a row to the relevant `reference/checks.md` naming its
  grounding document, not by writing the rule into the skill.
- Keep each `SKILL.md` body around 100 lines. It routes; depth belongs in
  `reference/`.
- Helper scripts under `skills/shared/scripts/` are Python standard library
  only, print JSON to stdout, and never write files. Skills run in other
  people's environments; a pip install is not available to them.
- Every finding cites a bundle path, its upstream URL, and the dates. See
  `skills/shared/grounding.md`.

## 3. Both toolchains must stay green

Every markdown file in this repository is also an OKF concept, including the
skill files, so each one needs frontmatter with a non-empty `type`. Claude Code
ignores the extra keys; the OKF validator needs them.

Two traps in skill markdown. A footnote marker — a caret inside square
brackets — must match an entry in the file's `sources` frontmatter, so avoid
writing one unless you mean it. And a markdown link to a `.md` file is
link-checked, so write documentation paths as inline code rather than links.

After changing anything, run the maintenance chain:

```bash
okf validate --bundle . --strict    # must report 0 errors and 0 warnings
okf index --bundle .
okf log Update "<what changed>" --bundle .
okf viz --bundle .
python3 sync_docs.py --check        # must still report the bundle up to date
```

Set `OKF_CLI` if the CLI is not on `PATH`. The last command matters: it
confirms your change did not disturb the mirror's change detection.
