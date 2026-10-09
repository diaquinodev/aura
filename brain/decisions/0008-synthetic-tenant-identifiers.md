# 0008 Synthetic tenant identifiers

**Status:** Accepted · **Owner:** Operator · **Date:** 2026-10-09 (Stage 0 closeout) · **Resolves:** inbox item "Nexa may collide with real companies"

## Context

The first synthetic client was named "Nexa Group". "Nexa" is used by real companies, so a portfolio reader could mistake a simulated client for a real one.

## Decision

Synthetic organizations use an explicitly synthetic ID, `AURA-SYN-NNN`, plus a descriptive display name. The first is `AURA-SYN-001 — Synthetic Finance Enterprise` (`simulation/AURA-SYN-001.md`).

## Rationale

An ID cannot be mistaken for a brand and needs no trademark check. It also scales to future tenants and datasets.

## Trade-offs and alternatives

- Invented brand-like name: more natural in role-play, but every name needs a collision check.
- Accepted cost: "AURA-SYN-001" reads less naturally in simulated meetings; the display name is used in prose.

## Impact

All references to "Nexa Group" in current docs were replaced. Historical journals keep the original name.
