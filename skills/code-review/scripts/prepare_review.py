#!/usr/bin/env python3
"""Prepare an isolated Git repository worktree and optional local checks for review."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


def run(command: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=check)


def git(repo: Path, *args: str, check: bool = True) -> str:
    return run(["git", "-C", str(repo), *args], check=check).stdout.strip()


def slug_for(repository: str) -> str:
    name = repository.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git") or "repository"
    return re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-") or "repository"


def default_branch(repo: Path) -> str:
    reference = git(repo, "symbolic-ref", "--short", "refs/remotes/origin/HEAD", check=False)
    if reference.startswith("origin/"):
        return reference.removeprefix("origin/")
    return "main"


def fetch_ref(repo: Path, ref: str) -> None:
    result = run(["git", "-C", str(repo), "fetch", "--quiet", "origin", ref], check=False)
    if result.returncode:
        raise RuntimeError(f"Unable to fetch {ref}: {result.stdout.strip()}")


def resolve_ref(repo: Path, ref: str) -> str:
    candidates = [ref, f"origin/{ref}", f"refs/remotes/origin/{ref}"]
    for candidate in candidates:
        result = git(repo, "rev-parse", "--verify", f"{candidate}^{{commit}}", check=False)
        if result:
            return result
    raise RuntimeError(f"Unable to resolve Git revision: {ref}")


def detect_checks(checkout: Path) -> list[tuple[str, list[str]]]:
    checks: list[tuple[str, list[str]]] = []
    if any((checkout / name).exists() for name in ("pyproject.toml", "pytest.ini", "tox.ini", "setup.cfg")) or (checkout / "tests").exists():
        checks.append(("python-tests", [sys.executable, "-m", "pytest"]))
    package_json = checkout / "package.json"
    if package_json.exists():
        try:
            scripts = json.loads(package_json.read_text()).get("scripts", {})
        except json.JSONDecodeError:
            scripts = {}
        for name in ("test", "lint", "typecheck"):
            if name in scripts:
                checks.append((f"node-{name}", ["npm", "run", name]))
    if (checkout / "go.mod").exists():
        checks.append(("go-tests", ["go", "test", "./..."]))
    if (checkout / "Cargo.toml").exists():
        checks.append(("rust-tests", ["cargo", "test", "--all-targets"]))
    if (checkout / "pom.xml").exists():
        checks.append(("maven-tests", ["mvn", "test"]))
    if (checkout / "gradlew").exists():
        checks.append(("gradle-tests", ["./gradlew", "test"]))
    return checks


def install_dependencies(checkout: Path) -> list[str]:
    commands: list[list[str]] = []
    if (checkout / "package-lock.json").exists():
        commands.append(["npm", "ci"])
    elif (checkout / "package.json").exists():
        commands.append(["npm", "install"])
    if (checkout / "requirements.txt").exists():
        commands.append([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    if (checkout / "pyproject.toml").exists() and (checkout / "requirements.txt").exists() is False:
        commands.append([sys.executable, "-m", "pip", "install", "."])
    results = []
    for command in commands:
        result = run(command, cwd=checkout, check=False)
        results.append(f"{' '.join(command)}: {'passed' if result.returncode == 0 else 'failed'}")
        if result.returncode:
            break
    return results


def run_checks(checkout: Path, workspace: Path, checks: Iterable[tuple[str, list[str]]]) -> list[dict[str, object]]:
    logs = workspace / "check-logs"
    logs.mkdir(exist_ok=True)
    results: list[dict[str, object]] = []
    for name, command in checks:
        executable = command[0]
        if executable.startswith("./"):
            available = (checkout / executable).exists()
        else:
            available = shutil.which(executable) is not None
        if not available:
            results.append({"name": name, "command": command, "status": "skipped", "reason": f"{executable} is unavailable"})
            continue
        result = run(command, cwd=checkout, check=False)
        log_path = logs / f"{name}.log"
        log_path.write_text(result.stdout)
        results.append({"name": name, "command": command, "status": "passed" if result.returncode == 0 else "failed", "log": str(log_path), "exit_code": result.returncode})
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare a Git repository locally for evidence-based code review.")
    parser.add_argument("repository", help="GitHub, GitLab, or other Git repository URL")
    parser.add_argument("--base", help="Base branch, tag, or commit; defaults to the repository default branch")
    parser.add_argument("--head", help="Head branch, tag, or commit; defaults to the repository default branch")
    parser.add_argument("--output", type=Path, help="Review workspace path")
    parser.add_argument("--run-checks", action="store_true", help="Run detected checks after preparation")
    parser.add_argument("--install-dependencies", action="store_true", help="Install detected dependencies before checks; implies --run-checks")
    args = parser.parse_args()

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    workspace = args.output or Path.cwd() / "review-workspaces" / f"{slug_for(args.repository)}-{timestamp}"
    workspace = workspace.expanduser().resolve()
    if workspace.exists() and any(workspace.iterdir()):
        parser.error(f"Output directory is not empty: {workspace}")
    workspace.mkdir(parents=True, exist_ok=True)

    mirror = workspace / "repository.git"
    checkout = workspace / "checkout"
    try:
        run(["git", "clone", "--no-checkout", "--filter=blob:none", args.repository, str(mirror)])
        default = default_branch(mirror)
        base_ref = args.base or default
        head_ref = args.head or default
        fetch_ref(mirror, base_ref)
        if head_ref != base_ref:
            fetch_ref(mirror, head_ref)
        base_sha = resolve_ref(mirror, base_ref)
        head_sha = resolve_ref(mirror, head_ref)
        run(["git", "-C", str(mirror), "worktree", "add", "--detach", str(checkout), head_sha])
        checks = detect_checks(checkout)
        check_results: list[dict[str, object]] = []
        dependency_results: list[str] = []
        if args.install_dependencies:
            dependency_results = install_dependencies(checkout)
        if args.run_checks or args.install_dependencies:
            check_results = run_checks(checkout, workspace, checks)
        manifest = {
            "repository": args.repository,
            "workspace": str(workspace),
            "checkout": str(checkout),
            "base": {"requested": base_ref, "commit": base_sha},
            "head": {"requested": head_ref, "commit": head_sha},
            "changed_files": git(mirror, "diff", "--name-status", f"{base_sha}..{head_sha}", check=False).splitlines(),
            "diff_stat": git(mirror, "diff", "--stat", f"{base_sha}..{head_sha}", check=False),
            "detected_checks": [{"name": name, "command": command} for name, command in checks],
            "dependency_results": dependency_results,
            "check_results": check_results,
            "prepared_at": datetime.now(timezone.utc).isoformat(),
        }
        manifest_path = workspace / "review-manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
        print(f"Review workspace: {workspace}")
        print(f"Checkout: {checkout}")
        print(f"Manifest: {manifest_path}")
        print(f"Comparison: {base_ref}..{head_ref}")
        return 0
    except (OSError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"Review preparation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
