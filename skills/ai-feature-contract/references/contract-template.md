# AI Feature Contract

> Use only the rows that apply. This contract supports user-facing chat or voice, research and retrieval, agents with tools, automated decisions, coding assistants, and internal AI development workflows.

## Feature identity

- Feature name:
- Owner:
- User problem and target user:
- Desired outcome and success metric:
- Non-goals:
- Linked specification and ADRs:

## AI operating profile

| Item | Contract |
|---|---|
| Context | User-facing, operator-facing, internal development, or other |
| Modality | Chat, voice, document, image, code, or other |
| AI role | Research, retrieval, generation, analysis, coding, orchestration, or other |
| Authority level | Advise, draft, recommend, execute, or decide |
| Accountable human | Who owns approval, escalation, and final judgment |

## User experience

| Item | Contract |
|---|---|
| Trigger | |
| Inputs | |
| Output | |
| Latency | |
| Interruption or turn-taking | Required for voice or real-time interaction; otherwise N/A |
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
| Voice, interface, or modality component | | | |
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
| Authority and tool use | | | |
| Interaction or modality | Voice, chat, document, image, or code behavior as applicable | | |
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
