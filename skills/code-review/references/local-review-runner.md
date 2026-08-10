# Local Review Runner

Use `scripts/prepare_review.py` to prepare a GitHub or GitLab repository for local review.

```bash
python skills/code-review/scripts/prepare_review.py \
  https://github.com/owner/repository.git \
  --base main \
  --head feature-branch \
  --output review-workspaces/repository-review \
  --run-checks
```

The runner:

1. Clones the repository into a review workspace.
2. Creates an isolated detached Git worktree for the requested head revision.
3. Records the base-to-head diff, changed files, revisions, and detected checks in `review-manifest.json`.
4. Detects common Python, Node, Go, Rust, Maven, and Gradle checks.
5. Runs detected checks only with `--run-checks`, and writes one log per check.

Do not use `--install-dependencies` unless the repository is trusted. Dependency installation and tests execute third-party code. The script never pushes, changes the remote repository, or deletes the review workspace.

Use `--head` for a branch, tag, or commit to review against `--base`. If no head is supplied, the repository default branch is prepared for a full-code review and the manifest records that no branch comparison was requested.
