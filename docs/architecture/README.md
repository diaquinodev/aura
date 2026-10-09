# Architecture

Status: **principles only**. No component below exists yet. Technical design arrives with Stage 1 and later stages.

## Conceptual overview

```text
Business User
      ↓
Aura Ops
      ↓
Agent / Workflow Layer
      ↓
Tools
 ┌────┼─────────┐
ERP   DB   Documents
 └────┼─────────┘
      ↓
Business Rules
      ↓
Human Approval
      ↓
Action
      ↓
Audit + Observability
```

Every layer is **PLANNED**.

## Status vocabulary

Used across all documentation for capabilities and components.

| Status | Meaning |
|---|---|
| PLANNED | Intended; nothing built |
| IN DEVELOPMENT | Work started; not usable yet |
| IMPLEMENTED | Built and runnable |
| VERIFIED | Implemented and proven by a test, eval or reproducible evidence |

## Principle 1: deterministic first, AI where uncertainty exists

| Deterministic: code, SQL, schema, constraints, rules, tests | Probabilistic: may justify AI |
|---|---|
| `invoice_total == expected_total` | Interpreting an unstructured document |
| `purchase_order_exists` | Semantic classification (what kind of request is this?) |
| Duplicate document detection | Retrieving relevant context |
| Status transitions and validation | Assisted investigation of an exception |
| Approval thresholds | Summaries and recommendations |
| 3-way match within tolerance | Natural-language interface |

If a step can be expressed as a rule, it is a rule. An LLM, agent, MCP server or RAG pipeline is introduced only where it handles real uncertainty, and that need is recorded as a decision.

## Principle 2: human-in-the-loop for business actions

```text
Agent Recommendation → Policy → Human Approval → Action
```

- Agents **recommend**; they do not execute financial actions.
- **Policy** (deterministic) decides who must approve, based on amount, supplier and risk.
- Autonomy increases only with evidence (evals, audit history), per action type, recorded as a decision.

## Principle 3: everything auditable

Each business action records its inputs, rule results, AI outputs (with model and version), the decision, who made it, and when. If it is not in the audit log, it did not happen.

## Principle 4: no technology without a problem

No technology enters AURA because it is popular. RAG, MCP, agent frameworks, Redis, vector databases, orchestration, Kubernetes, Kafka or an observability platform need:

```text
PROBLEM → REQUIREMENT → ALTERNATIVES → DECISION → IMPLEMENTATION → EVIDENCE
```

recorded in `brain/decisions/`. Without a concrete problem it is rejected or deferred.

## Principle 5: agents last, and evaluated

```text
Business Rules → Deterministic Engine → APIs → Data → Failure Cases → Agent Assistance
```

No agent before a problem that needs one. Agents are **evaluated, not just demonstrated**: task success, tool errors, hallucinations, human escalations, latency, tokens, cost, safety failures. Each metric is added only when it can actually be measured.

## Simulator (PLANNED)

The simulator is more than training material. It is also:

- **reproducible scenarios**: the same scenario runs against different versions of the solution;
- **eval harness**: results are compared across versions (Scenario 001 → version A → result; Scenario 001 → version B → result);
- **incident generator**: failures injected on purpose, reproducibly.

Synthetic organizations such as `simulation/AURA-SYN-001.md` are its first input. All its results are SYNTHETIC.
