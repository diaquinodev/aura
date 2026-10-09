# AURA

> "AURA" and "Aura Ops" are working codenames. Trademark availability has not been checked.

## What is AURA?

AURA is an enterprise agentic automation engineering lab designed to build, test and operate AI agents across realistic business workflows, using synthetic organizations, reproducible incidents and real software engineering practices.

Inside the simulation, AURA is a fictional B2B company building **Aura Ops**: intelligent, auditable automation of enterprise processes combining AI agents, APIs, data, business rules and human approval.

## Why it exists

1. **Agentic AI engineering lab:** learn where AI belongs in a business process, and where it does not.
2. **Enterprise simulation:** tickets, prioritization, review, CI, releases and incidents, as in a real tech company.
3. **Executable platform:** real code, tests and infrastructure, not a conceptual framework.
4. **Professional training and portfolio:** a documented record of decisions and growth.
5. **Possible future product:** only after validation; nothing here is a commercial claim.

## Current Business Domain

**Finance & Operations → Accounts Payable.** One real workflow first; other domains only after it is complete.

## Current Workflow

**Intelligent Accounts Payable** (PLANNED): intake → parsing → validation → ERP lookup → business rules → 3-way match → divergence detection → AI investigation → recommendation → human approval → action → audit → observability → evaluation. Details: [docs/product/AURA-OPS.md](docs/product/AURA-OPS.md).

## Architecture Overview

Business user → Aura Ops → agent/workflow layer → tools (ERP, database, documents) → business rules → human approval → action → audit and observability. All layers are PLANNED. See [docs/architecture/README.md](docs/architecture/README.md).

## Engineering Principles

- **Deterministic first, AI where uncertainty exists.** Totals, matches and duplicates are code and SQL; interpretation and investigation may use AI.
- **Human-in-the-loop** for financial actions until evidence justifies more autonomy.
- **Everything auditable.**
- Smallest correct solution; evidence over claims; no agent or abstraction without a concrete problem.

## Current Stage

`Stage 0 — Foundation` complete. Next: `Stage 1 — Engineering Core`. Operational status: [docs/status/CURRENT.md](docs/status/CURRENT.md).

## Implemented

Status vocabulary: PLANNED · IN DEVELOPMENT · IMPLEMENTED · VERIFIED.

| Capability | Status |
|---|---|
| Documentation, decision log and memory system (`docs/`, `brain/`) | IMPLEMENTED |
| `tools/check_docs.py` (broken links, training-level consistency) | VERIFIED |

## In Progress

- Nothing in development yet. Stage 1 starts with Bootstrap 02.

## Planned

Python, FastAPI, PostgreSQL, REST APIs, webhooks, LLMs with tool calling and structured outputs, MCP and RAG where justified, Docker, CI/CD, observability, evals, guardrails. None of these exist yet. Order: [docs/product/ROADMAP.md](docs/product/ROADMAP.md).

## Simulation

The first synthetic client is [AURA-SYN-001 — Synthetic Finance Enterprise](simulation/AURA-SYN-001.md), with Finance, Procurement, Operations and Compliance personas. No scenarios or datasets exist yet.

## Learning / Career Lab

The operator trains as a professional inside the simulated company, with support that decreases over time. `TRAINING_LEVEL = 1` (Guided). See [docs/learning/README.md](docs/learning/README.md).

## Documentation

- [docs/README.md](docs/README.md): map of the canonical documentation.
- [AGENTS.md](AGENTS.md): rules for AI agents working in this repository.
- [brain/index.md](brain/index.md): decisions, insights and gotchas.
- Run `python tools/check_docs.py` to validate the docs.

## Disclaimer

- **Synthetic clients.** AURA-SYN-001 and every other customer are fictional.
- **Synthetic datasets.** No real invoice, supplier, payment or personal data.
- **Synthetic business events.** Incidents and requests are simulated and labeled as such.
- **Real engineering implementation.** The code, tests and infrastructure, once built, are real.
- Simulated metrics are not commercial results. Any future real pilot will be reported separately.
