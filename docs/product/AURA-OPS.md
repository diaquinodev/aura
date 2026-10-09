# Aura Ops (codename)

Status: **concept**. Nothing in this document is implemented. Statements are hypotheses unless marked otherwise.

> Intelligent automation platform for enterprise operational processes, combining AI agents, APIs, data, business rules and human approval.

## Scope strategy (decision)

Aura Ops may eventually cover Finance Operations, Procurement, Customer Operations, Compliance, Sales Operations and Backoffice. **One real workflow first:** the first and only domain until its workflow is complete end to end is **Finance & Operations → Accounts Payable**.

## Problem (hypothesis)

Companies receive invoices and payment requests that must be received, interpreted, validated, cross-checked against systems, verified against rules, investigated when they diverge, approved, recorded and audited. In many organizations most of this is manual: analysts re-key data, chase divergences by email, and approvals happen outside any audit trail. The hypothesized cost is analyst time, late payments (penalties, lost early-payment discounts), duplicate payments and weak controls.

## Users

Defined as synthetic personas in [../../simulation/AURA-SYN-001.md](../../simulation/AURA-SYN-001.md).

## Reference workflow: Intelligent Accounts Payable

Conceptual only; no step is implemented. The **Kind** column applies the boundary in [../architecture/README.md](../architecture/README.md).

| # | Step | What happens | Kind |
|---|---|---|---|
| 1 | Document / request | An invoice or payment request arrives | — |
| 2 | Intake | Register it, assign an ID, detect the channel | Deterministic |
| 3 | Document parsing | Extract supplier, amounts, items, dates from an unstructured document | Probabilistic |
| 4 | Data validation | Required fields, formats, tax ID checksum, totals add up | Deterministic |
| 5 | ERP / database lookup | Find supplier, purchase order (PO), goods receipt | Deterministic |
| 6 | Business rules | Approval thresholds, supplier status, payment terms | Deterministic |
| 7 | 3-way match | PO vs goods receipt vs invoice: quantities and prices within tolerance | Deterministic |
| 8 | Divergence detection | Flag mismatches, duplicates, missing documents as exceptions | Deterministic |
| 9 | AI investigation | Gather context on an exception (history, emails, similar cases) and explain the likely cause | Probabilistic |
| 10 | Recommendation | Propose approve / reject / request correction, with evidence | Probabilistic |
| 11 | Human approval | An authorized person decides; policy defines who | Human |
| 12 | Business action | Record in ERP, schedule payment, notify supplier | Deterministic |
| 13 | Audit log | Immutable record of inputs, rule results, AI outputs, the decision and who made it | Deterministic |
| 14 | Observability | Traces, latency, cost, error rates per step | Deterministic |
| 15 | Evaluation | Measure parsing accuracy, recommendation quality, exception handling time | Deterministic harness over probabilistic outputs |

## Goals (hypothesis)

- Reduce manual handling time per invoice.
- Resolve exceptions faster, with evidence attached.
- Zero duplicate payments.
- Every financial action is traceable to a human decision or an approved policy.

## Non-goals (decision)

- Agents do not execute financial actions autonomously (see [../architecture/README.md](../architecture/README.md)).
- No real ERP, bank or supplier connection until pilot readiness (Stage 10).
- No other domain until Accounts Payable is complete.
- No real company, invoice or personal data.

## Hypothetical metrics

Any value produced before a real pilot is **simulated**.

| Metric | Definition |
|---|---|
| Touchless rate | Invoices processed with no manual step / total invoices |
| Exception resolution time | Median time from exception flagged to decision |
| Parsing accuracy | Fields extracted correctly / fields evaluated (eval set) |
| Recommendation agreement | AI recommendations accepted by approvers / recommendations |
| Duplicate payments | Count; target zero |

## Risks

- A wrong AI extraction or recommendation leads to a wrong payment. Mitigation: deterministic validation and human approval before any action.
- Over-automation erodes financial controls and segregation of duties.
- Real ERPs differ widely; a simulated ERP may hide integration complexity.
- LLM cost and latency per invoice may exceed the value at low volumes. **UNKNOWN** until measured.
