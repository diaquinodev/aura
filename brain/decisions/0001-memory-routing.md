# 0001 Memory routing

**Status:** Accepted, operator review pending · **Owner:** Operator · **Date:** 2026-10-08 (Bootstrap 01)

## Context

The project must be resumable after months, but a growing transcript is unreadable and unsafe as memory: one session's guess would become a permanent "fact". The operator's learning and the project's knowledge are different audiences.

## Decision

| Kind | Goes to |
|---|---|
| Project fact, decision, gotcha, insight | `brain/` (index, then specific file) |
| Unvalidated finding | `brain/inbox/` |
| Operator's learning and evolution | `docs/learning/` (journal, path, glossary) |
| Lesson about how we work | `/reflect` (pstack), after checking it is reusable |
| Mistake agents keep repeating | `/correct` (pstack) |

## Rationale

Separating audiences keeps each file small and readable. The inbox stops single observations from becoming rules.

## Trade-offs and alternatives

- One `NOTES.md`: simple, but mixes audiences and grows without bound.
- Store everything via `/reflect`: would turn session facts into skill edits.

## Impact

Every session end needs a short routing step (see `docs/process/SESSION-LIFECYCLE.md`). The inbox must be reviewed, or it becomes a junk drawer.
