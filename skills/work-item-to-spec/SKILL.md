---
name: work-item-to-spec
description: Turn a GitHub or GitLab issue, Asana task, Aha record, or pasted work item into a traceable requirement specification. Use when a team needs to convert product intent, acceptance notes, comments, attachments, or subtasks into a versioned spec with measurable outcomes, acceptance criteria, non-goals, dependencies, and open decisions before planning or implementation.
---

# Work Item to Spec

Convert one work item into a repository requirement specification. Treat the source system as the record of incoming intent and the repository specification as the record of approved engineering behavior.

## Inputs

Accept a GitHub or GitLab issue, Asana task, Aha record, or pasted task content. Retrieve only the source fields available to the current user. Default to read-only access; do not update the source task without explicit approval.

Read [source-intake.md](references/source-intake.md) and [requirement-template.md](references/requirement-template.md) before drafting.

## Workflow

1. Identify the source type and record its title, URL or identifier, owner, status, description, comments, subtasks, attachments, and linked work.
2. Normalize the source into: user, problem, desired outcome, evidence of value, constraints, proposed behavior, and unknowns.
3. Separate facts from assumptions. Never treat a comment, label, or implementation suggestion as an approved requirement unless the source clearly says so.
4. Draft a versioned requirement using the template. Include measurable success criteria, functional and non-functional acceptance criteria, constraints, non-goals, dependencies, and risks.
5. Convert ambiguities into **Open decisions** with a decision owner. Ask concise questions when a human decision is needed; do not invent policy, legal, privacy, security, or business choices.
6. Create a trace link back to the source work item and forward links to implementation plan, ADRs, AI Feature Contract, evaluations, and release evidence when they exist.
7. Present the draft for human approval. Only after approval may a connected source system be updated with a link and status summary.

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
