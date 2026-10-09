# AURA

> "AURA" and "Aura Ops" are working codenames. Trademark availability has not been checked.

## What is AURA?

AURA is an enterprise agentic automation engineering lab designed to build, test and operate AI agents across realistic business workflows, using synthetic organizations, reproducible incidents and real software engineering practices.

Inside the simulation, AURA is a fictional B2B company building **Aura Ops**: auditable automation of enterprise processes combining AI agents, APIs, data, business rules and human approval.

## Business Problem

Accounts Payable teams receive invoices that must be validated, matched against purchase orders and receipts, investigated when they diverge, approved and audited, mostly by hand. AURA's first workflow, **Intelligent Accounts Payable**, automates the deterministic parts with code and uses AI only where real uncertainty exists, with a human approving every financial action. Details: [docs/product/AURA-OPS.md](docs/product/AURA-OPS.md).

## Architecture

Business user → Aura Ops → agent/workflow layer → tools (ERP, database, documents) → business rules → human approval → action → audit and observability. Principles: deterministic first, human-in-the-loop, everything auditable, no technology without a problem. See [docs/architecture/README.md](docs/architecture/README.md).

## Current Capabilities

```text
Current stage:       Stage 0 — Foundation (complete); Stage 1 not started
Executable product:  Not started
```

| Capability | Status |
|---|---|
| Documentation, decision log and memory system | IMPLEMENTED |
| `tools/check_docs.py` (broken links, training-level consistency) | VERIFIED |

Everything else (Python service, FastAPI, PostgreSQL, agents, evals, CI) is PLANNED. Order and definition of done: [docs/product/ROADMAP.md](docs/product/ROADMAP.md).

## Proof

None yet beyond the documentation system. From Stage 1, each capability links here to its tests, PR, CI run and metrics, labeled SYNTHETIC or REAL.

## Demo

None yet.

## Case Studies

None yet. First planned: Case 001 — Deterministic 3-Way Matching Engine.

## Documentation

- [docs/status/CURRENT.md](docs/status/CURRENT.md): where the project is right now.
- [docs/README.md](docs/README.md): map of the canonical documentation.
- [AGENTS.md](AGENTS.md): rules for AI agents working in this repository.
- [brain/index.md](brain/index.md): decisions, insights and gotchas.
- Learning lab: the operator trains inside the simulated company; `TRAINING_LEVEL = 1` (Guided), see [docs/learning/README.md](docs/learning/README.md).

## Disclaimer

- **Synthetic clients.** AURA-SYN-001 and every other customer are fictional.
- **Synthetic datasets and business events.** No real invoice, supplier, payment or personal data; incidents and requests are simulated.
- **Real engineering.** The code, tests and infrastructure, once built, are real.
- Every metric is labeled SYNTHETIC or REAL. Synthetic results are never commercial results.
