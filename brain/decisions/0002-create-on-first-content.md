# 0002 Create directories on first content

**Status:** Accepted, operator review pending · **Owner:** Operator · **Date:** 2026-10-08 (Bootstrap 01)

> **Update 2026-10-09 (Pivot 01):** `docs/architecture/` and `simulation/` were created once they had real content (architecture principles; the first synthetic organization). `brain/investigations/` and `.github/` remain deferred.

## Context

The Bootstrap 01 brief proposed `simulation/`, `docs/architecture/`, `.github/README.md` and several empty `brain/` subfolders. None had content yet.

## Decision

Create a directory or document only when it receives real content. Deferred: `simulation/` (Stage 2), `docs/architecture/` (first architecture decision), `brain/investigations/` (first investigation), `.github/` (first workflow, Stage 3). No `.gitkeep` files.

## Rationale

Empty structure looks like progress but tells a new engineer nothing, and placeholder files go stale. `.github/README.md` would also replace the root README on GitHub (see `brain/gotchas/github-readme-precedence.md`).

## Trade-offs and alternatives

Create the full tree with `.gitkeep`: shows intent, but adds files with no information.

## Impact

The planned locations are listed in `docs/README.md` and `brain/index.md` so nobody invents a different place for them.
