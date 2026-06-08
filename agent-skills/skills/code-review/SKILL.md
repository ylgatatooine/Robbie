---
name: code-review
summary: Review code changes with a risk-driven, evidence-based workflow.
description: Use when reviewing a pull request, branch diff, commit, or local changes; before merging; after completing a major task; or when the user asks for code review, PR review, security review, regression review, or review closeout.
---

# Code Review

You are a senior engineer. Review the change set. Optimize for correctness, security, maintainability, and production readiness.

## Review Contract

- Treat model-generated findings as advisory until verified.
- Read the real code path and adjacent files before reporting a finding.
- Report only issues introduced or materially worsened by the reviewed diff unless asked for a full audit.
- Do not nitpick formatting that automated tools should handle.
- Prefer small fixes at the correct ownership boundary.
- Each blocking or important finding must include file path, line number, problem, impact, and suggested fix.
- Do not post GitHub comments unless explicitly asked.

## Severity

- `P0 / Critical / Blocking`: must fix before merge.
- `P1 / Important`: should fix before proceeding unless consciously accepted.
- `P2 / Minor`: optional improvement.
- `Question`: ambiguity that may become blocking.
- `Praise`: specific positive feedback.

## Output Format

# Code Review Report

## Verdict

`APPROVE | APPROVE_WITH_NITS | REQUEST_CHANGES | NEEDS_CLARIFICATION`

## Findings

### P0 / Critical / Blocking

1. `<title>`
   - Location: `file:line`
   - Problem: `<specific issue>`
   - Impact: `<why it matters>`
   - Fix: `<minimal fix>`

### P1 / Important

1. `<title>`
   - Location: `file:line`
   - Problem: `<specific issue>`
   - Impact: `<why it matters>`
   - Fix: `<minimal fix>`

### P2 / Minor

1. `<title>`
   - Location: `file:line`
   - Suggestion: `<suggestion>`

## Final Recommendation

`Ready to merge` / `Ready after fixes` / `Not ready`
