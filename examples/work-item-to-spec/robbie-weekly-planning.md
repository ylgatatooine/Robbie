# Requirement Specification: Robbie Buddy

## Traceability

- **Source system:** Example work item
- **Source record:** “Help me turn a personal idea or tracker task into a practical hobby, creative, or home project”
- **Source owner and status:** Personal user; draft
- **Related work:** AI Feature Contract and evaluation plan to be created after this specification is approved

## Problem and outcome

- **Target user:** An individual pursuing hobbies, creative work, home projects, practical skills, or an after-work idea.
- **Problem statement:** The user has a promising idea but lacks a simple way to turn it into a bounded, safe project with clear next steps and a useful learning record.
- **Desired outcome:** Robbie Buddy helps the user move from idea to a finished or deliberately paused project, while making the needed skills, materials, tradeoffs, and safety boundaries visible.
- **Success metric and baseline:** In a project review, at least 80% of users say the first project path was useful; the user can reach a concrete first step in under 15 minutes.
- **Why now:** The user wants Robbie to be a long-term, practical companion for making, learning, repairing, and creating—not only a weekly planner.

## Scope

### Required behavior

- Intake an idea from a manual note, GitHub issue, Asana task, Aha record, or pasted list.
- Use Work Item to Spec to turn the idea into a personal project specification before creating detailed steps.
- Ask for missing intent, budget, skill level, available tools, safety limits, and desired outcome instead of guessing.
- Produce a small project path: a first step, materials or resources, learning checkpoints, risks, and optional milestones.
- Explain why a step is recommended, deferred, simplified, or outside the user’s stated constraints.
- Support a project check-in that records progress, blockers, photos or notes supplied by the user, and the next useful step.
- Keep a short decision and learning log so the user can reuse what worked on a future project.

### Non-functional requirements

- The user can approve or edit the proposed project path before anything is written to an external system.
- The assistant never creates, completes, reschedules, or deletes external tasks or records without a clear confirmation.
- The initial project path is readable in under two minutes.
- The workflow remains useful with only a pasted idea; connectors are optional.

### Constraints

- Task and project-source connections are read-only by default.
- The user retains final priority and scheduling authority.
- Personal data is minimized and redacted from diagnostic logs.
- The first version supports one user and one project at a time.

### Non-goals

- Automated purchasing, messaging, booking, or delegation to other people.
- Mental-health, medical, legal, or financial advice.
- Surveillance of user activity or automatic project changes without a user check-in.
- Multi-user household, workshop, or team coordination in version one.

## Acceptance criteria

| Scenario | Given | When | Then | Evidence |
|---|---|---|---|---|
| Project intake | The user provides an idea or tracker task | They ask Robbie Buddy for help | Robbie creates a project path with a first step, resources, risks, and open decisions | Snapshot test plus user review |
| Missing constraints | The idea has no budget, skill level, or safety limits | Robbie cannot give responsible project guidance | Robbie asks focused questions and marks unknowns rather than inventing assumptions | Conversation evaluation |
| Source privacy | No tracker connection is approved | The user starts a project | Robbie uses pasted content only and offers optional connection | Tool-permission test |
| Project change | The user reports a blocker or a changed goal | They run a project check-in | Robbie explains options and proposes a revised path without changing external records | Integration test |
| External update | A task or project-record update is proposed | The user has not confirmed | Robbie does not write to a connected system | Tool-call assertion |
| Project learning | The user finishes or pauses a project | They run a review | Robbie captures useful lessons and proposes one reusable improvement | Evaluation rubric |

## Dependencies and risks

| Item | Type | Impact | Owner | Mitigation |
|---|---|---|---|---|
| Task connector | Optional integration | Limits automated intake | Product owner | Support pasted tasks first |
| Task/project connector | Optional integration | Limits automatic project intake | Product owner | Support pasted ideas first |
| Unsafe guidance | Safety risk | User could attempt work beyond their skill or tools | User | Require safety questions, clear boundaries, and professional escalation |
| Mis-scoped project | Product risk | User loses motivation or wastes resources | User | Require visible tradeoffs, milestones, and approval |
| Sensitive task content | Privacy risk | Personal information could be exposed | User | Minimize inputs and redact diagnostics |

## Follow-on artifacts

- **Implementation plan:** Create after acceptance criteria are approved.
- **Architecture decisions:** Define connector permissions, storage, confirmation model, and safety/escalation boundaries.
- **AI Feature Contract:** Required before implementation because Robbie uses AI reasoning and optional tools.
- **Evaluation plan:** Include project-path usefulness, appropriate safety escalation, permission safety, and revision quality.
- **Release evidence:** Show acceptance-test results, evaluation outcomes, and approved rollback behavior.

## Open decisions

| Decision | Why it matters | Accountable role | Needed by |
|---|---|---|---|
| Which intake source is first: GitHub, Asana, Aha, or manual note? | Determines first connector and source mapping | User | Before implementation plan |
| Which project types are safe for version one? | Determines skill boundaries and escalation design | User | Before AI Feature Contract |
| What does “useful project path” mean for this user? | Sets the evaluation rubric | User | Before evaluation design |
