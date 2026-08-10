---
name: code-review
description: Review a pull request, branch diff, commit, or local changes with a risk-driven, evidence-based workflow. Use before merging, after a major task, or for code, security, regression, or review-closeout requests.
---

# Code Review

Review changes for correctness, security, maintainability, and production readiness.

## Review Contract

- Treat model-generated findings as advisory until verified.
- Read the real code path and adjacent files before reporting a finding.
- Report only issues introduced or materially worsened by the reviewed diff unless asked for a full audit.
- Avoid formatting nits that automated tools should handle.
- Prefer small fixes at the correct ownership boundary.
- Include the file, line, impact, and minimal fix for every blocking or important finding.
- Do not post GitHub comments unless explicitly asked.

## Risk Focus

Prioritize correctness, security, privacy, data integrity, API compatibility, performance regressions, and missing tests. Treat authentication, permissions, billing, migrations, secrets, personally identifiable information, and public API changes as high-risk. Flag missing tests as important when behavior, a bug fix, or a boundary condition changes.

## Severity

- `P0 / Critical / Blocking`: Must fix before merge.
- `P1 / Important`: Should fix before proceeding unless consciously accepted.
- `P2 / Minor`: Optional improvement.
- `Question`: Ambiguity that may become blocking.
- `Praise`: Specific positive feedback.

## Report Format

```markdown
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
```
