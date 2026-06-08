# AGENTS.md

## Purpose

This repository contains Rubbie's AI engineering assets, reference implementations, patterns, evaluations, and production code.

This repository follows Specification-Driven Development (SDD) and Test-Driven Development (TDD).

Before making changes, understand the problem, define the behavior, write tests, then implement.

---

## Read First

Before making changes, read:

1. architecture/overview.md
2. patterns/
3. playbooks/coding.md
4. glossary/
5. relevant ADRs

---

## Engineering Principles

1. Reliability > Features
2. Simplicity > Cleverness
3. Observable > Opaque
4. Security First
5. Human Override Always
6. Reuse Before Creating

---

## Specification-Driven Development (SDD)

All non-trivial changes require a specification.

Specifications belong in:
specs/

A specification should define:
- Problem statement
- Desired behavior
- Acceptance criteria
- Constraints
- Non-goals

Do not implement behavior that is not described by the specification.

If requirements are unclear, stop and clarify before coding.

-- 

## Test-Driven Development (TDD)

All behavior changes require tests.

Preferred workflow:
- Define acceptance criteria.
- Write or update tests.
- Verify tests fail for the expected reason.
- Implement the minimum code required.
- Verify tests pass.
- Refactor if needed.

Every bug fix requires a regression test.

## Workflow

For every non-trivial change:

1. Read the relevant specification.
2. Create or update the specification if needed.
3. Create a short implementation plan.
4. Write or update tests.
5. Implement the change.
6. Run tests and linting.
7. Update documentation, examples, and specifications as needed.

Never jump directly from request to implementation.

---

## Repository Layout

src/
tests/
prompts/
examples/
architecture/
patterns/
playbooks/
adr/
glossary/

---

## Security

Never:

- Commit secrets
- Log credentials
- Store tokens in code

---

## Documentation

Architectural decisions belong in:  
adr/

Reusable approaches belong in: 
patterns/

Operational procedures belong in:
playbooks/

---

## Definition of Done

A change is complete only when:

- Specification exists and is current
- Acceptance criteria are satisfied
- Tests cover the behavior
- Tests pass
- Documentation is updated if needed
- Examples are updated if needed