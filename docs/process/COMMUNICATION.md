# Corporate communication

How people (and agents) communicate inside the Aura simulation. Goal: train the operator in real workplace communication, not just in code.

The standard: **clear, objective, technical when needed, outcome-oriented, professional.** Aura should feel like a real company, not a corporate caricature.

## Principles

- Use real industry terms (`blocker`, `refinement`, `trade-off`, `RCA`) when they name something real in the process. Never as decoration.
- Do not translate terms the market uses in English.
- Connect technology to outcome: "We added a retry strategy to reduce transient failures in the ERP supplier lookup", not "We added retry".
- No meeting, template or framework without a purpose. Unknown fields stay `TBD` or `Needs discovery`; never invent content to fill a template.
- Simulated customers, incidents and metrics are always fictional (see [../../README.md](../../README.md)).

## Support by training level

Current level: see [../learning/README.md](../learning/README.md).

| Level | Terms | Operator |
|---|---|---|
| 1 Guided | Use the term and add a one-line explanation the first few times it appears. Stop once it has been used and understood. | Supported in meetings, status and tickets |
| 2 Assisted | Use corporate language normally; explain only new concepts. | Writes status and tickets; AI reviews |
| 3 Professional | No automatic explanation or translation. | Participates, defends decisions, raises risks and blockers, proposes next steps; feedback comes afterwards |

Terms that become relevant and recurring go to [../learning/GLOSSARY.md](../learning/GLOSSARY.md). Trivial terms do not.

**Correcting the operator:** answer normally, then, only when useful, add one line: *"In a corporate setting you could say: ..."*. Example: "the thing broke" → "We identified a regression in the invoice approval flow after the last change." Do not over-correct.

## Role voices

Each message reflects who is speaking.

| Role | Focuses on | Does not |
|---|---|---|
| Product Manager | User, impact, priority, metrics, business, timeline | Prescribe implementation |
| Tech Lead | Architecture, risk, dependencies, quality, tech debt, trade-offs | Decide business priority alone |
| Engineer | Investigation, implementation, tests, dependencies, evidence | Claim without evidence |
| Customer Success | Customer, impact, urgency, expectations, satisfaction | Promise dates engineering has not agreed |
| SRE / Platform | Availability, incidents, observability, capacity, SLOs | Change product scope |

## Templates

### Ticket

Tickets often arrive as a business symptom ("AURA-SYN-001 Finance reports the exception queue doubling before month-end close"), not as a solution ("Add a queue worker"). The engineer investigates before defining the solution.

```text
Context:
Business Problem:
User Impact:
Current Behavior:
Expected Outcome:
Acceptance Criteria:
Priority:          (P0–P3)
Severity:          (for defects/incidents)
Dependencies:
Risks:
Open Questions:
```

### Status update

```text
CURRENT STATUS:  Investigating the ERP supplier lookup failure.
WHAT WAS DONE:   Reproduction confirmed; current hypothesis is the retry flow.
BLOCKERS:        None.
RISKS:           Fix may touch shared retry code used by the purchase order lookup.
NEXT STEP:       Validate hypothesis, then propose the fix.
```

### Daily

Short. Four lines, not a report.

```text
Yesterday:   ...
Today:       ...
Blockers:    ...
Risk/dependency (if any): ...
```

### Refinement

Do not hand over the solution. Ask what Product and Engineering would ask:

- What problem, for which user, with what impact (and how do we know)?
- What is in scope and explicitly out of scope?
- What are the acceptance criteria? How will we verify them?
- Dependencies, risks, open questions? Is it small enough for one sprint?

### Sprint planning

The backlog is not a list where everything fits. Weigh priority, team capacity, dependencies, complexity, risk, work in progress, open incidents and tech debt. Say explicitly what is **not** entering the sprint and why.

### Incident

```text
SEVERITY:            P1
STATUS:              INVESTIGATING | IDENTIFIED | MONITORING | RESOLVED
IMPACT:              Invoices cannot be submitted for approval.
STARTED:             08:41
OWNER:               Engineering
CURRENT HYPOTHESIS:  Not yet confirmed.
NEXT UPDATE:         After reproduction is validated.
```

### RCA (after the incident)

```text
IMPACT / TIMELINE / ROOT CAUSE / MITIGATION /
CORRECTIVE ACTION / PREVENTIVE ACTION / FOLLOW-UP
```

Blameless: describe what the system allowed, not who failed.

### Code review comment

State problem, risk, suggestion, and severity when needed.

> There is a risk of processing the same webhook more than once here. Can we make this operation idempotent or add a unique constraint in the database? (blocking)

### Technical decision

Speak in trade-offs, not preferences: "PostgreSQL reduces our operational complexity at this stage but couples the application to a relational model. Given current volume and transactional requirements, the trade-off is acceptable." Durable decisions are recorded in `brain/decisions/` using the format in [../../brain/index.md](../../brain/index.md).

### Meeting

```text
MEETING TYPE / PURPOSE / PARTICIPANTS / AGENDA / DISCUSSION /
DECISIONS / ACTION ITEMS / OPEN QUESTIONS
```

Every action item:

```text
ACTION / OWNER / STATUS / DEPENDENCY / TARGET (if any)
```

No decision stays only in a transcript.

## Escalation

Escalate when there is a product decision, an external dependency, high risk, significant impact, missing access, a priority conflict, a relevant architecture change, or a critical incident. Escalation is not giving up: it puts the decision with the person who owns it, with context and a recommendation.
