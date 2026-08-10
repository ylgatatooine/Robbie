---
name: code-review
description: Run a comprehensive, enterprise-style review of a pull request, branch diff, commit, or local changes. Use before merge, after a major change, or for correctness, security, privacy, reliability, regression, architecture, or release-readiness review. Performs a deep primary review and, when authorized and available, an independent second-model review with evidence-based reconciliation.
---

# Enterprise Code Review

Review changes deeply enough to make a merge decision, not merely to generate comments. Treat every model finding as a hypothesis until it is verified in the code, tests, configuration, and runtime behavior.

Read [review-protocol.md](references/review-protocol.md) for the risk matrix and independent-review packet. Use [local-review-runner.md](references/local-review-runner.md) to prepare a repository locally, [codex-review-agent.md](references/codex-review-agent.md) to tune the Codex reviewer, and [report-template.md](references/report-template.md) for the final report.

## Review pipeline

1. **Map scope and risk** — Identify changed behavior, ownership boundaries, affected users, interfaces, data flows, and high-risk surfaces.
2. **Establish evidence** — Read the diff, surrounding implementation, specifications, tests, configuration, and relevant history before judging the change.
3. **Review deeply** — Trace happy paths, failures, boundary conditions, state transitions, concurrency, and backwards compatibility.
4. **Probe adversarially** — Test assumptions about security, privacy, authorization, data integrity, reliability, observability, and abuse paths.
5. **Run the proof** — Use `scripts/prepare_review.py` to create an isolated local worktree, inspect the change, and run the selected tests, linting, static analysis, builds, migrations, and focused checks.
6. **Get an independent view** — When the user authorizes it and an approved second reviewer is available, request an independent review before sharing the primary reviewer’s findings.
7. **Reconcile and decide** — Verify every primary and second-review finding against the code. Deduplicate, reject unsupported claims, assign severity, and issue a clear merge recommendation.

## Primary review standard

- Use the strongest review-capable model and highest appropriate reasoning level available in the current environment; do not pretend to select or access an unavailable model.
- Read the actual execution path and adjacent ownership boundaries. Do not infer a defect from a diff fragment alone.
- Review only risks introduced or materially worsened by the change unless a full audit is requested.
- Prefer a small fix at the correct ownership boundary over a broad rewrite.
- Ignore style nits that formatting or linting can enforce automatically.
- Never post comments, change code, or alter a pull request unless the user explicitly asks.

## Independent second-model review

Use this stage for high-risk or high-value changes, such as authentication, authorization, billing, data migration, public APIs, secrets, personally identifiable information, destructive operations, safety-critical behavior, or large architectural changes.

- Obtain explicit approval before sending code, diffs, logs, or proprietary context to an external model provider, unless the user has already established an approved organizational policy and connection.
- If an approved Claude or other independent reviewer is connected, give it the review packet in `review-protocol.md` and request a blind first pass.
- Do not rely on a second model as an authority. Verify its claims in the repository just as rigorously as the primary review.
- If no approved connection exists, provide the review packet for the user to run elsewhere; complete the primary review without claiming a cross-model check occurred.

## Finding standard

Report only material, evidence-backed findings. Every `P0` or `P1` must include a precise location, observable failure mode, impact, evidence, and minimal fix. State explicitly when a check could not be run or when evidence is incomplete. A verified `P0` or `P1` always blocks approval; `P2` findings are non-blocking.

## Severity

- **P0 / Critical** — Exploitable security issue, irreversible data loss, major outage, or release blocker.
- **P1 / Important** — Likely defect, material regression, broken contract, or missing protection on a significant path.
- **P2 / Minor** — Real but bounded issue; safe to defer deliberately.

Do not invent lower severity levels. Keep general observations out of the findings list.
