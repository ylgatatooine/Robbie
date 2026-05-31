
# AGENT.md
Codex users: add review guidelines into AGENT.md

## Review guidelines

- Focus review comments on correctness, security, privacy, data integrity, API compatibility, performance regressions, and missing tests.
- Treat auth, permissions, billing, migrations, secrets, PII, and public API changes as high-risk surfaces.
- Flag missing tests as P1 when the change alters behavior, fixes a bug, or introduces a new boundary condition.
- Every P0/P1 finding must include a file path, line number, concrete impact, and minimal suggested fix.
