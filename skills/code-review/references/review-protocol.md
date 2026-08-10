# Review Protocol

## Scope and risk map

Before reviewing, record:

- Change objective and acceptance criteria.
- Files and execution paths affected.
- User, API, data, and operational impact.
- Risk tier: routine, elevated, or high.
- Evidence available: tests, builds, static analysis, deployment plan, telemetry, and rollback plan.

Treat these as elevated or high risk: authentication, authorization, payments, billing, secrets, personally identifiable information, retention, encryption, migrations, destructive actions, public APIs, background jobs, concurrency, distributed state, compliance commitments, and AI tool or data boundaries.

## Deep-review matrix

| Area | Verify |
|---|---|
| Correctness | Requirements, state changes, errors, boundary values, idempotency, and failure recovery. |
| Security and privacy | Authentication, authorization, input validation, secrets, logging, data exposure, and least privilege. |
| Data integrity | Schema changes, migrations, transactions, retries, ordering, duplication, and rollback. |
| Compatibility | Public contracts, API versions, configuration defaults, feature flags, and upgrade paths. |
| Reliability | Timeouts, retries, partial failures, resource limits, concurrency, queues, and degraded behavior. |
| Observability | Useful logs, metrics, traces, alerts, audit records, and safe diagnostics. |
| Performance | New hot paths, query patterns, payload sizes, caching, fan-out, and resource growth. |
| Test proof | Acceptance coverage, regression tests, negative paths, integration boundaries, and test realism. |
| Delivery | Build, lint, static analysis, release gates, rollback, documentation, and runbook updates. |

## Independent-review packet

Prepare this packet for an approved second reviewer. Do not include secrets or unrelated proprietary material.

```markdown
# Independent Review Packet

## Change goal
<What the change must accomplish and its acceptance criteria>

## Risk map
<Affected users, data, interfaces, and high-risk surfaces>

## Review material
<Patch or repository comparison, plus the necessary adjacent files>

## Evidence
<Tests, build output, static-analysis results, deployment or rollback notes>

## Questions to probe
<Specific contracts, failure paths, security, privacy, migration, or compatibility concerns>

## Instructions
Review independently. Report only material findings with file and line, failure mode, impact, evidence, and minimal fix. State uncertainty and checks you could not perform. Do not assume the primary reviewer is correct.
```

Share the primary findings only after the independent first pass. Then reconcile disagreements against the actual code and evidence.
