# AURA (codename)

Every statement is tagged:

- **FACT**: verified, or true by definition of this project.
- **HYPOTHESIS**: believed, not validated.
- **DECISION**: chosen by us; can be revisited.
- **UNKNOWN**: open question.

The previous positioning (vertical SaaS for clinics, "Aura Studio") is recorded in `brain/decisions/0007-pivot-to-enterprise-agentic-automation.md`.

## Context

- **FACT**: AURA is a simulated company. It has no real customers, revenue or employees.
- **FACT**: "AURA" and "Aura Ops" are codenames. Brand availability has not been checked.
- **DECISION**: AURA is B2B: intelligent, auditable automation of enterprise processes through AI agents, integrations, data and human-in-the-loop workflows.
- **DECISION**: First domain is Finance & Operations, specifically Accounts Payable. One real workflow first.

## Market

- **HYPOTHESIS**: Mid-to-large companies still run much of Accounts Payable manually, and existing automation (OCR, RPA, ERP modules) handles the happy path but not exceptions.
- **HYPOTHESIS**: The unmet need is exception handling with evidence and auditability, not raw data extraction.
- **UNKNOWN**: Market size, region, and which company size gets the most value.

## Target customers

- **HYPOTHESIS**: Mid-to-large companies with a dedicated Finance team, an ERP, and a high monthly invoice volume.
- **HYPOTHESIS**: The buyer is the Finance Manager or CFO; daily users are Finance and Procurement analysts; Compliance can block adoption.

## Problems we intend to solve

- **HYPOTHESIS**: Analysts spend most of their time on re-keying and on chasing divergences.
- **HYPOTHESIS**: Exceptions (PO mismatch, missing receipt, duplicates) cause late payments and penalties.
- **HYPOTHESIS**: Approvals and investigations happen outside the system, weakening the audit trail.

## Initial value proposition

- **HYPOTHESIS**: "Fewer manual touches and faster exception resolution, with every decision explained and audited, and a human approving every financial action."

## Business model

- **DECISION**: B2B SaaS.
- **HYPOTHESIS**: Subscription by workflow, plus a usage component (documents processed) to cover AI costs.
- **UNKNOWN**: Price point, and whether AI cost per document allows a margin at mid-market volumes.

## Risks

- **Financial correctness**: an automation error causes a wrong payment. Mitigation: deterministic validation and human approval (`docs/architecture/README.md`).
- **Controls and compliance**: automation must not break segregation of duties or the audit trail.
- **Integration**: real ERPs are heterogeneous; the simulated ERP may underestimate effort.
- **Competition**: ERP vendors and AP automation specialists exist. **UNKNOWN**: how AURA would differ beyond exception handling.
- **Scope**: the "platform" framing invites building many domains at once. Mitigation: one workflow first.
- **Integrity**: simulation must never be presented as reality (see [../../README.md](../../README.md)).

## Unvalidated hypotheses to test first

1. Exception handling, not extraction, is the main cost in Accounts Payable.
2. AI-assisted investigation shortens exception resolution measurably.
3. Finance leaders accept AI recommendations if every one is explained and audited.
