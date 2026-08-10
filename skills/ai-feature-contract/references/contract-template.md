# AI Feature Contract

## Feature identity

- Feature name:
- Owner:
- User problem and target user:
- Desired outcome and success metric:
- Non-goals:
- Linked specification and ADRs:

## User experience

| Item | Contract |
|---|---|
| Trigger | |
| Inputs | |
| Output | |
| Latency | |
| Failure behavior | |
| Human escalation | |

## AI behavior

| Item | Contract |
|---|---|
| Intended job | |
| Grounding | |
| Output schema | |
| Allowed tools and actions | |
| Forbidden actions | |
| Uncertainty behavior | |
| Fallback | |

## Data and privacy

| Data type | Source | Permitted use | Retention | Redaction and access control |
|---|---|---|---|---|
| | | | | |

## Model and tool choices

| Component | Choice and rationale | Limits | Failure handling |
|---|---|---|---|
| Model | | | |
| Tool or connector | | | |
| Retrieval source | | | |

## Safety and review boundaries

- Sensitive decisions or content:
- Prompt-injection and untrusted-input controls:
- Tool-call confirmations:
- Human-review triggers:
- Audit-log requirements:

## Evaluation and release evidence

| Category | Case or check | Expected property | Threshold |
|---|---|---|---|
| Deterministic | | | |
| Task success | | | |
| Groundedness | | | |
| Safety | | | |
| Tool use | | | |
| Latency and cost | | | |

- Regression policy:
- Blocking release conditions:
- Rollout and rollback plan:
- Accepted risks:

## Production learning loop

| Signal | Target | Alert condition | Owner | Runbook | Artifact to update |
|---|---|---|---|---|---|
| Availability / tool success | | | | | |
| AI quality | | | | | |
| Safety escalation | | | | | |
| Cost per successful task | | | | | |
| User outcome | | | | | |

## Open decisions

| Decision | Why it matters | Accountable role | Needed by |
|---|---|---|---|
| | | | |
