# Roadmap

Capability-based, no dates. A stage is done when its capability is demonstrated with evidence, not when time passes. Order may change; each change is recorded in `brain/decisions/`. The previous roadmap (healthcare direction) is recorded in decision 0007.

| Stage | Name | Capability | Status |
|---|---|---|---|
| 0 | Foundation | Documentation, Git, learning system, pstack | Complete |
| 1 | Engineering Core | Python + FastAPI service, tests, Git workflow | Not started |
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

From Stage 1 on, every milestone must produce at least one of: executable code, an automated test, a working integration, a metric, an eval, or verifiable technical evidence.
