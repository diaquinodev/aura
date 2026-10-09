# Roadmap

Capability-based, no dates. A stage is done when its capability is demonstrated with evidence, not when time passes. Order may change; each change is recorded in `brain/decisions/`. The previous roadmap (healthcare direction) is recorded in decision 0007.

| Stage | Name | Capability | Status |
|---|---|---|---|
| 0 | Foundation | Documentation, Git, learning system, pstack | Complete |
| 1 | Engineering Core | Python + FastAPI service, tests, Git workflow | In progress |
| 2 | Enterprise Simulation | Synthetic company, personas, Jira, meetings | Not started |
| 3 | Data & Persistence | PostgreSQL, synthetic datasets, audit model | Not started |
| 4 | Finance Workflow | Intelligent Accounts Payable workflow end to end | Not started |
| 5 | External Integrations | Simulated ERP/APIs, webhooks | Not started |
| 6 | Agentic Layer | Tools, agents, MCP, orchestration where justified | Not started |
| 7 | Evals & Observability | Tracing, quality, latency, cost | Not started |
| 8 | Reliability & Security | Incidents, guardrails, resilience | Not started |
| 9 | Multi-Workflow Platform | Additional enterprise processes, after Stage 4 is complete | Not started |
| 10 | Pilot Readiness | Assess whether a real pilot is legally, technically and ethically ready | Not started |

## Stage 0 exit criteria

- [x] Canonical documentation exists and passes `python tools/check_docs.py`.
- [x] Memory (`brain/`) and learning (`docs/learning/`) areas exist and are separated.
- [x] Positioning is coherent after Pivot 01.
- [x] Git initialized by the operator and first commit made.
- [ ] Operator has reviewed and accepted (or changed) the decisions in `brain/decisions/`. Partially done (0007, 0008 decided); the rest is carried into Bootstrap 02 and does not block it.

From Stage 1 on, a stage is complete only with executable evidence (hard rule in [../process/WORKING-MODEL.md](../process/WORKING-MODEL.md)).

## Stage 1 definition of done

- [x] Python project initialized
- [x] FastAPI service running locally
- [ ] Pydantic schemas for the invoice domain
- [ ] Deterministic invoice validation
- [ ] Deterministic 3-way match
- [ ] Tests with pytest, including edge cases
- [ ] Work done on a branch and merged through a pull request
- [ ] CI running the tests on every PR
- [ ] One small case study: **Case 001 — Deterministic 3-Way Matching Engine** (hypothesis: deterministic financial rules should be solved deterministically before any AI is introduced; must include problem, baseline, implementation, tests, edge cases, evidence)

## External validation path

```text
Simulation → Internal demo → External reviewer → Real user feedback → Pilot
```

A real client is not needed to start, but AURA must not stay indefinitely without external validation. Candidate reviewers: a finance analyst, an operations professional, a developer, a technical recruiter, a data professional. Not scheduled; first candidate checkpoint is after Stage 4.
