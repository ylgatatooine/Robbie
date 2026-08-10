# Obsidian Vault Setup

Use this reference to create a general-purpose creator knowledge vault. Preserve an existing, documented structure rather than replacing it.

## Folder layout

```text
inbox/       Unprocessed captures
notes/       Durable knowledge and synthesis
ideas/       Original thinking and hypotheses
projects/    Active work
```

Create `notes/synthesis/` when weekly synthesis is used. Add topic subfolders only after a pattern is clear; do not pre-create a complicated taxonomy.

## `README.md`

Keep the human-facing overview short:

```markdown
# My Knowledge Vault

## Purpose

Capture useful learning, connect it to active work, and turn it into better decisions.

## Folder map

- `inbox/` — Unprocessed captures.
- `notes/` — Durable notes, research, and synthesis.
- `ideas/` — My observations and hypotheses.
- `projects/` — Active work.

## Start here

Read `AGENTS.md` before making changes. Use `operations.md` for repeatable vault work.
```

## `AGENTS.md`

Use one canonical agent guide. Include the creator’s current focus, goals, active projects, safe operating rules, and expectations for analysis. A useful structure is:

```markdown
# Vault Guidance

## Creator context

- **Focus:** <areas worth paying attention to>
- **Current projects:** <active work>
- **Near-term goals:** <goals that shape relevance>

## How this vault works

- `inbox/` is for unprocessed captures.
- `notes/` holds durable knowledge.
- `ideas/` holds original thinking.
- `projects/` holds active work.

## What I want from an agent

- Surface useful connections.
- Challenge assumptions with evidence.
- Flag contradictions with links to both notes.
- Identify specific knowledge gaps.
- Recommend one useful next action when asked to prioritize.

## Change rules

- Scan and propose before writing.
- Ask before moving or deleting files.
- Keep claims traceable to their sources.
```

If Claude Code or Gemini is used, make `CLAUDE.md` and `GEMINI.md` short pointers to `AGENTS.md`; do not duplicate the rules.

## `operations.md`

Store the repeatable procedures in `operations.md`, using the operations reference in this skill. Keep a source list in the vault guidance or operations file, and change it only with the creator’s approval.

## Capture format

Use this format for a new external capture:

```markdown
---
source: <publisher or author>
url: <canonical URL>
published: <YYYY-MM-DD or unknown>
captured: <YYYY-MM-DD>
tags:
  - <topic>
---

# <Title>

<One to three sentences on the central claim or finding.>

## Why it matters

<One sentence connecting it to the creator's focus, project, question, or practice.>
```

Name the file `YYYY-MM-DD-source-topic.md`, using publication date rather than capture date when known.
