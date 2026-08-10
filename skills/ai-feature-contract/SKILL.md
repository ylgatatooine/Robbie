---
name: ai-feature-contract
description: Create or review an AI Feature Contract for an approved AI capability. Use for voice or chat assistants, LLM features, research and retrieval systems, agents with tools, automated decisions, coding assistants, or internal AI development workflows that need explicit behavior, authority, data, safety, evaluation, release, or operational boundaries before implementation or launch.
---

# AI Feature Contract

Turn an approved AI capability into a concise, testable agreement for product, engineering, security, and operations. Use one contract across user-facing and internal AI work; include only the rows that apply. Treat unknown decisions as open items; never invent business, legal, privacy, safety, or authorization decisions.

## Inputs

Collect the approved feature specification and relevant architecture, data, security, and operational context. If the feature is not yet defined, produce only the open questions needed to define it.

Read [contract-template.md](references/contract-template.md) before drafting the contract.

## Workflow

1. **Frame the capability** — State the user, problem, outcome, success metric, non-goals, and whether the AI is user-facing, operator-facing, or internal.
2. **Set the operating profile** — Identify the modality (chat, voice, document, image, code, or other), AI role (research, generation, analysis, coding, or agent), and authority level (advise, draft, recommend, execute, or decide).
3. **Define the experience** — Specify trigger, inputs, outputs, latency, interruption or handoff needs, failure behavior, and human escalation.
4. **Define AI authority** — Set the intended job, grounding, output shape, allowed tools, forbidden actions, uncertainty behavior, and fallback. Require explicit confirmation for consequential writes or decisions.
5. **Protect data and systems** — Classify data flows, access boundaries, retention, redaction, sensitive actions, and untrusted-input controls.
6. **Choose components deliberately** — Record model, voice or interface components, retrieval, tools, cost and latency budgets, and failure handling.
7. **Prove the behavior** — Define deterministic checks and behavioral evaluations for task success, safety, authority, grounding, modality, and regressions.
8. **Release and learn** — Define release gates, accountable owners, rollout and rollback, production signals, runbooks, and which artifact evidence should improve.
9. **Surface open decisions** — Assign every material unknown to an accountable role; stop rather than guessing.

## Quality bar

The completed contract must make it possible to answer:

- What problem does this feature solve, and how will success be measured?
- Which AI context, modality, role, and authority level does it use?
- What may the AI and its tools do, and what must they never do?
- Which data may be used, retained, or exposed?
- How will correct, safe behavior be tested and evaluated?
- What blocks release, how is a failure detected, and how is it rolled back?
- Which production signal changes which source artifact?

## Output

Create a Markdown contract using the template. Keep it short enough to review, link supporting specifications and ADRs instead of duplicating them, and label every unresolved material issue as **Open decision**.
