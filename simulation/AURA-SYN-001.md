# AURA-SYN-001 — Synthetic Finance Enterprise

```text
TYPE:          SYNTHETIC ORGANIZATION
ID:            AURA-SYN-001
DISPLAY NAME:  Synthetic Finance Enterprise
```

This organization is fictional and does not represent any real company. Identifier convention: decision 0008.

## Profile

- Mid-to-large company with multiple business units.
- Departments relevant to Aura: Finance, Procurement, Operations, Customer Service, Compliance.
- Processes a high volume of supplier invoices monthly; exact volume **TBD** when synthetic datasets are created (Stage 3).
- Uses an ERP (simulated in Stage 5) as the system of record for suppliers, purchase orders and payments.

## Personas

No agents. These are business stakeholders who generate requests, decisions and feedback in the simulation.

### Finance Analyst
- **Goals:** process invoices correctly and on time; clear the exception queue.
- **Pain points:** re-keying data, chasing divergences by email, month-end backlog.
- **Technical knowledge:** spreadsheets, ERP screens; no programming.
- **Decision authority:** approves within a low threshold; escalates above it.
- **Typical requests:** "Why is this invoice stuck?" / "Can the system catch duplicates?"

### Finance Manager
- **Goals:** meet payment SLAs, control risk, report KPIs to leadership.
- **Pain points:** no visibility into the queue; late-payment penalties; audit findings.
- **Technical knowledge:** business intelligence dashboards.
- **Decision authority:** high-value approvals; sets approval policy with Compliance.
- **Typical requests:** "What is our exception rate this month?" / "Who approved this payment?"

### Procurement Analyst
- **Goals:** accurate purchase orders and healthy supplier relationships.
- **Pain points:** invoices that do not match the PO; suppliers asking about payment status.
- **Technical knowledge:** ERP procurement module.
- **Decision authority:** amends POs; confirms goods receipt.
- **Typical requests:** "Supplier says they invoiced the agreed price; why the mismatch?"

### Operations Manager
- **Goals:** a predictable, measurable end-to-end process.
- **Pain points:** handoffs between Finance and Procurement; no single process owner view.
- **Technical knowledge:** process mapping, KPIs.
- **Decision authority:** process changes and priorities across teams.
- **Typical requests:** "Where is the bottleneck in invoice processing?"

### Engineering / Platform (AURA side)
- **Goals:** a reliable, secure, observable Aura Ops.
- **Pain points:** unclear requirements, flaky integrations, unmeasured AI quality.
- **Technical knowledge:** high.
- **Decision authority:** technical design and release; not business policy.
- **Typical requests:** "What are the acceptance criteria?" / "What is the expected volume?"

### Compliance
- **Goals:** effective controls, segregation of duties, complete audit trail.
- **Pain points:** approvals outside the system; AI decisions nobody can explain.
- **Technical knowledge:** controls frameworks; low technical depth.
- **Decision authority:** can block a release or an automation that weakens controls.
- **Typical requests:** "Show me every action the AI took on this invoice and who approved it."
