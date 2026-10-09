# 0009 Python tooling and work management

**Status:** Accepted · **Owner:** Operator · **Date:** 2026-10-09 (Bootstrap 02 kickoff)

## Context

Stage 1 needs a Python environment, a dependency definition, a place for tickets and sprints, and a remote for PRs and CI.

## Decision

- `venv` + `pip` + `pyproject.toml` (src layout, package `aura_ops`).
- GitHub Issues for tickets, Milestones as sprints. GitHub Projects board deferred: the `gh` token lacks the `project` scope.
- Private GitHub repository `diaquinodev/aura`; made public once there is proof of work worth showing.
- GitHub Actions for CI. Jira deferred to when it adds something GitHub does not.

## Rationale

All already installed or authenticated: zero new tools before the first line of code. Issues, PRs and CI in one place link tickets to evidence automatically (`Closes #N`).

## Trade-offs and alternatives

- `uv`: faster and has a lockfile, but needs installation; revisit if reproducibility becomes a problem.
- Jira: closer to many enterprises, but needs an account and an integration to link with PRs.
- Accepted cost: no lockfile, so CI may resolve newer dependency versions than local.

## Impact

`.venv/` stays git-ignored. CI installs `pip install -e ".[dev]"` from `pyproject.toml`.
