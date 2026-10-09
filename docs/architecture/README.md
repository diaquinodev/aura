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
