# 0004 Docs check script

**Status:** Accepted · **Owner:** Operator · **Date:** 2026-10-08 (Bootstrap 01)

## Context

Documentation-only repositories rot through broken links and facts that disagree across files. The training level is stated in three files (README, AGENTS, learning README) because each audience needs it in place.

## Decision

`tools/check_docs.py` (Python standard library only) fails when a relative Markdown link points to a missing file or when the `TRAINING_LEVEL = N` lines disagree.

## Rationale

Deterministic enforcement over reminders. No dependency added; it can run in CI later unchanged.

## Trade-offs and alternatives

- A Markdown linter package: adds a dependency for one check.
- Manual review: is forgotten.

## Impact

Run `python tools/check_docs.py` before finishing a session. Extend it only when a new class of doc error actually happens.
