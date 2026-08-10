---
name: ai-feature-contract
description: Create or review an AI Feature Contract for an approved product feature. Use when a feature uses an LLM, agent, retrieval, model tool calls, or automated decisions and needs explicit behavior, data, safety, evaluation, release, or operational boundaries before implementation or launch.
---

# AI Feature Contract

Turn an approved feature into a concise, testable agreement for product, engineering, security, and operations. Treat unknown decisions as open items; never invent business, legal, privacy, safety, or authorization decisions.

## Inputs

Collect the approved feature specification and relevant architecture, data, security, and operational context. If the feature is not yet defined, produce only the open questions needed to define it.

Read [contract-template.md](references/contract-template.md) before drafting the contract.

## Workflow

1. State the user, problem, desired outcome, success metric, and non-goals.
2. Define user-visible behavior: trigger, accepted inputs, output format, latency expectation, failure behavior, and human escalation.
3. Define AI behavior: intended job, grounding sources, output schema, tool permissions, forbidden actions, uncertainty handling, and fallback.
4. Classify each data flow. Record source, permitted use, retention, redaction, and access boundaries. Mark unapproved handling as an open decision.
5. Record model and tool choices, rationale, cost and latency budgets, and failure handling. Do not allow write-capable or sensitive tools without explicit authorization and confirmation rules.
6. Convert requirements into evidence: deterministic checks plus behavioral evaluations with cases, rubrics, thresholds, and regression policy.
7. Define release evidence: tests, evaluation threshold, security review, monitoring, staged rollout, rollback condition, accountable owners, and accepted risks.
8. Define production signals for reliability, quality, safety, latency, cost, tool failure, and user outcome. Link each alert to an owner and runbook.
9. List unresolved decisions with their accountable role. Stop rather than guessing.

## Quality bar

The completed contract must make it possible to answer:

- What problem does this feature solve, and how will success be measured?
- What may the AI and its tools do, and what must they never do?
- Which data may be used, retained, or exposed?
- How will correct, safe behavior be tested and evaluated?
- What blocks release, how is a failure detected, and how is it rolled back?
- Which production signal changes which source artifact?

## Output

Create a Markdown contract using the template. Keep it short enough to review, link supporting specifications and ADRs instead of duplicating them, and label every unresolved material issue as **Open decision**.
