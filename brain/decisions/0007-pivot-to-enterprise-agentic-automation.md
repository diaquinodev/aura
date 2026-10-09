# 0007 Pivot from vertical healthcare SaaS to enterprise agentic automation

**Status:** Accepted · **Owner:** Operator · **Date:** 2026-10-09 (Pivot 01) · **Supersedes:** the positioning set in Bootstrap 01

## Context

Bootstrap 01 positioned the project as a vertical SaaS for appointment-based businesses. Before any product code existed, the operator re-evaluated the direction against the project's real goals: an Agentic AI Engineering lab, a realistic enterprise simulation, and a portfolio aligned with the corporate AI engineering market.

## Previous direction

Recorded here because Git was not yet initialized and the overwritten documents have no version history.

- **Company:** "Aura Studio", B2B software for premium dermatology, dentistry, aesthetics, hair/beauty and wellness businesses.
- **Product:** "Aura Flow", automation of lead → qualification → booking → confirmation → reminder → attendance → follow-up → analytics.
- **Key hypotheses:** no-shows are a top-three pain; one product fits all five segments; owners would pay for confirmations/reminders alone.
- **Roadmap:** 0 Foundation, 1 Work Management, 2 Synthetic Company, 3 Core Product, 4 Scheduling, 5 Integrations (Google Calendar, WhatsApp), 6 Agentic Engineering, 7 Observability & Evals, 8 Reliability, 9 Pilot Readiness.
- **Full product doc:** kept as superseded in `docs/product/AURA-FLOW.md`.

## New direction

- **Company:** AURA, a fictional B2B company for intelligent, auditable automation of enterprise processes with AI agents, integrations, data and human-in-the-loop workflows.
- **Product:** Aura Ops (`docs/product/AURA-OPS.md`).
- **First domain:** Finance & Operations, specifically Accounts Payable. One real workflow first; other domains only after it is complete.
- **First synthetic client:** Nexa Group. *Update 2026-10-09: renamed to `AURA-SYN-001 — Synthetic Finance Enterprise` (`simulation/AURA-SYN-001.md`), decision 0008.*

## Rationale

- Accounts Payable has rich deterministic structure (purchase orders, receipts, invoices, 3-way match) and real uncertainty (document interpretation, divergence investigation). That makes it a good lab for the boundary between rules and AI, which is the core skill of enterprise AI engineering.
- It requires human approval, audit and controls by nature, so human-in-the-loop and auditability are requirements, not decoration.
- It matches the type of work enterprise AI/automation teams are hiring for more closely than a booking product does. This is an operator judgment, not validated with market data.

## Benefits

- Stronger alignment between the portfolio and enterprise roles.
- Health-adjacent regulatory exposure (clinical data) disappears from scope.
- The workflow exercises SQL, integrations, rules, agents, evals and audit in one coherent flow.

## Trade-offs

- Finance is less intuitive to the operator than a booking flow; more domain learning (AP, 3-way match, controls) is required before engineering.
- A "platform" framing invites scope creep. Mitigated by "one real workflow first".
- Financial mistakes are costlier than booking mistakes, even in simulation: the design must model approval and audit from the start.
- Messaging/calendar integration practice (WhatsApp, Google Calendar) leaves the roadmap.

## Consequences

- README, company, organization, roadmap, agent rules, communication examples and glossary updated.
- `docs/product/AURA-FLOW.md` and `brain/insights/no-show-first-metric.md` marked SUPERSEDED, not deleted.
- Decision 0003 (synthetic data only) still holds with a new rationale.
- `docs/architecture/`, `docs/status/` and `simulation/` created because they now have real content (consistent with 0002).
