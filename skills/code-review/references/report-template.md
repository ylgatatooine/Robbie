# Code Review Report Template

```markdown
# Code Review Report

## Verdict

`APPROVE | BLOCKED | NEEDS_CLARIFICATION`

## Scope and evidence

- **Change reviewed:** <summary>
- **Risk tier:** `routine | elevated | high`
- **Evidence reviewed:** <diff, code paths, tests, checks, and documentation>
- **Checks not run:** <or `None`>
- **Independent review:** <not requested | unavailable | completed and reconciled>

## Findings

### P0 / Critical

1. **<title>**
   - **Location:** `file:line`
   - **Failure mode:** <what can happen>
   - **Impact:** <why it matters>
   - **Evidence:** <code path, test, reproduction, or authoritative reference>
   - **Minimal fix:** <smallest safe correction>

### P1 / Important

1. **<title>**
   - **Location:** `file:line`
   - **Failure mode:** <what can happen>
   - **Impact:** <why it matters>
   - **Evidence:** <code path, test, reproduction, or authoritative reference>
   - **Minimal fix:** <smallest safe correction>

### P2 / Minor

1. **<title>**
   - **Location:** `file:line`
   - **Suggestion:** <bounded improvement>

## Final recommendation

`Ready to merge` only when there are no verified P0 or P1 findings. Otherwise: `Blocked pending P0/P1 fixes`.
```
