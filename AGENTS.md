# AGENTS.md

## Mission

Build Aura incrementally, verifiably and educationally. The operator is a professional in training; the work must teach, not just ship.

## Source of Truth

| Topic | Canonical file |
|---|---|
| Project overview (milestones only) | [README.md](README.md) |
| Current operational status | [docs/status/CURRENT.md](docs/status/CURRENT.md) |
| Company, market, hypotheses | [docs/company/COMPANY.md](docs/company/COMPANY.md) |
| Product scope and reference workflow | [docs/product/AURA-OPS.md](docs/product/AURA-OPS.md) |
| Architecture principles | [docs/architecture/README.md](docs/architecture/README.md) |
| Synthetic organizations and personas | [simulation/AURA-SYN-001.md](simulation/AURA-SYN-001.md) |
| Roadmap | [docs/product/ROADMAP.md](docs/product/ROADMAP.md) |
| How work flows, tooling (pstack) | [docs/process/WORKING-MODEL.md](docs/process/WORKING-MODEL.md) |
| Corporate communication, templates | [docs/process/COMMUNICATION.md](docs/process/COMMUNICATION.md) |
| Session start/end ritual | [docs/process/SESSION-LIFECYCLE.md](docs/process/SESSION-LIFECYCLE.md) |
| Training levels, learning path | [docs/learning/README.md](docs/learning/README.md) |
| Project memory | [brain/index.md](brain/index.md) |

## Engineering Principles

- Smallest correct solution.
- Evidence over assumptions; tests over claims.
- Deterministic enforcement (scripts, tests, CI) over written reminders.
- No agent, abstraction or directory without a concrete problem it solves.
- Deterministic first, AI where uncertainty exists. Never add an LLM, agent, MCP or RAG only to make the architecture look sophisticated.
- Agents recommend; humans approve financial actions until evidence justifies more autonomy.
- Never describe a capability as IMPLEMENTED or VERIFIED without evidence.

## Training Mode

`TRAINING_LEVEL = 1` (Guided). For significant decisions, explain: what we are doing, why a company would do it, the concept, how it shows up at work, and the short interview answer. Do not lecture on trivial changes. Do not raise the level on your own; only the operator changes it.

## Communication

Inside the simulation, communicate like a real tech company: real terms when they name something real, role-appropriate voice, outcome-oriented. Follow [docs/process/COMMUNICATION.md](docs/process/COMMUNICATION.md) for term explanations by level, light corrections of the operator, and templates (ticket, status, daily, incident, RCA, review, meeting).

## Documentation

A change that alters scope, stage, process or a decision updates its canonical file above. Session-level state goes to `docs/status/CURRENT.md`; the README changes only for positioning, milestones, delivered capabilities or high-level architecture. Link instead of duplicating. Run `python tools/check_docs.py` before finishing.

## Memory

- `brain/` is project memory; `docs/learning/` is the operator's training. Do not mix them.
- One session does not create a permanent fact. Unvalidated findings go to `brain/inbox/`.
- Load `brain/index.md` first, then only the specific files needed.

## Git

- `main` is the stable baseline. All work after the Stage 0 baseline commit happens on a branch and reaches `main` through a PR.
- Do not modify unrelated work. Do not create remotes, push or publish without explicit authorization.

## Security

Never commit or print secrets. `.env` and credentials stay out of Git.

## Synthetic Data

All organizations, people, documents, transactions and metrics are fictional. No real invoice, supplier, payment or personal data.

## Honesty

Never present a simulated customer, metric or incident as real. Label hypotheses as hypotheses.
