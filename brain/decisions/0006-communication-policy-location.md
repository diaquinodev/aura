# 0006 Where the communication policy lives

**Status:** Accepted, operator review pending · **Owner:** Operator · **Date:** 2026-10-08

## Context

The corporate communication policy must apply in every simulation interaction and survive beyond chat history. The operator suggested a Cursor Skill or a simulator-specific Rule. The repository has no `.cursor/rules/` and no project skills; `AGENTS.md` is already applied automatically.

## Decision

Canonical policy and templates in `docs/process/COMMUNICATION.md`. `AGENTS.md` gets a short Communication section that points to it. No Cursor Rule and no Skill for now.

## Rationale

- The policy has an always-on part (tone, term explanations, light corrections) and an on-demand part (templates). `AGENTS.md` already covers always-on; a linked doc covers on-demand.
- `AGENTS.md` and Markdown docs work across tools (Cursor, Claude Code, Codex); `.mdc` rules and skills are tool-specific.
- A human reads the same file the agent follows: the policy is also training material.

## Trade-offs and alternatives

- **Cursor Rule (`.cursor/rules/*.mdc`, always applied):** guaranteed in context, but duplicates what `AGENTS.md` does and costs context in every request, including non-simulation work.
- **Skill (`corporate-communication`):** loaded only when relevant, which saves context. But an agent may not load it during casual interaction, and the policy is meant to be always on.
- **Accepted cost:** an agent must follow a link to see templates. If agents repeatedly skip it, revisit (candidate for `/correct`).

## Impact

Future simulation features (meetings in Bootstrap 02, communication evals) reference `docs/process/COMMUNICATION.md` instead of redefining formats. Decision records now use the unified format in `brain/index.md`.
