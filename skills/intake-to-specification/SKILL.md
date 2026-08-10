---
name: intake-to-specification
description: Turn a GitHub or GitLab issue, Asana task, Aha record, or pasted work item into a traceable requirement specification. Use when a team needs to convert incoming product context, acceptance notes, comments, attachments, or subtasks into a versioned spec with measurable outcomes, acceptance criteria, non-goals, dependencies, and open decisions before planning or implementation.
---

# Intake to Specification

Convert one work item into a repository requirement specification. Treat the source system as the record of incoming intent and the repository specification as the record of approved engineering behavior.

## Inputs

Accept a GitHub or GitLab issue, Asana task, Aha record, or pasted task content. Retrieve only the source fields available to the current user. Default to read-only access; do not update the source task without explicit approval.

Read [source-intake.md](references/source-intake.md) and [requirement-template.md](references/requirement-template.md) before drafting.

## Workflow

1. **Capture source** — Record its title, link, owner, status, content, and related work.
2. **Extract intent** — Identify the user, problem, outcome, value, constraints, behavior, and unknowns.
3. **Separate facts** — Mark assumptions; do not promote a comment or suggestion into a requirement without clear approval.
4. **Draft the spec** — Use the template for success criteria, acceptance criteria, constraints, non-goals, dependencies, and risks.
5. **Surface decisions** — Turn ambiguity into an open decision with an owner; ask rather than invent policy or business choices.
6. **Link the evidence** — Trace back to the source and forward to the plan, ADRs, AI contract, evaluations, and release evidence.
7. **Get approval** — Present the draft for human approval; write back to a connected source only after approval.

## Source rules

- **GitHub:** Use issue body, labels, linked pull requests, discussion, and project fields as context. Do not infer a requirement from a pull request alone.
- **GitLab:** Use issue description, labels, linked merge requests, discussion, milestones, epics, and project fields as context. Do not infer a requirement from a merge request alone.
- **Asana:** Use task description, subtasks, comments, attachments, custom fields, and project section. Preserve the accountable owner and due-date context without treating due date as acceptance criteria.
- **Aha:** Use initiative, feature, requirement, release, score, and linked research context. Preserve strategy alignment and avoid collapsing roadmap priority into a technical requirement.

## Quality bar

The specification is ready for review only when it answers:

- Which user has which problem, and why does it matter now?
- What observable outcome defines success?
- Which behavior is required, and which behavior is explicitly out of scope?
- Which acceptance criteria can become tests, evaluations, or operational checks?
- Which decisions remain open, who owns them, and when are they needed?
- How can a reviewer navigate back to the source work item and forward to evidence?

## Output

Write `specs/<feature-slug>.md` unless repository conventions specify another location. Keep source excerpts brief, link the original source, and preserve open decisions instead of hiding uncertainty.
