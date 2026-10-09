# Organization (conceptual)

> These areas represent **business responsibilities**. They do **not** mean there is one AI agent per department. Agents are introduced only when there is a measurable benefit, recorded as a decision in `brain/decisions/`.

```text
AURA
├── Product            what to build and why
├── Engineering        building and maintaining the software
├── Quality            proving it works (tests, evals, acceptance)
├── Platform           CI/CD, environments, security, observability
├── Operations         incidents, on-call, runbooks
└── Customer Success   onboarding, support, feedback from (simulated) customers
```

| Area | Owns | Today |
|---|---|---|
| Product | Problem definition, roadmap, prioritization | Operator, with AI guidance |
| Engineering | Code, design, reviews | Operator, with AI assistance |
| Quality | Test strategy, acceptance criteria | Not started |
| Platform | Git, CI, environments, secrets | Not started (Git not initialized) |
| Operations | Incidents and recovery | Not started (Stage 8) |
| Customer Success | Simulated customer feedback (AURA-SYN-001) | Not started (Stage 2) |

These are AURA's internal areas. The client-side stakeholders (Finance, Procurement, Compliance at AURA-SYN-001) are personas in [../../simulation/AURA-SYN-001.md](../../simulation/AURA-SYN-001.md).

In Stage 0 every role is played by the operator. The AI acts as mentor and assistant, not as a department.
