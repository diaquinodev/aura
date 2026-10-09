# Glossary

Only relevant, recurring terms already used in the project. Grows with the project. Format: term, simple explanation, example at Aura, example in a real company.

## Engineering

**Repository**
A folder whose full history of changes is tracked by Git.
*At Aura:* `d:\CURSOR-AGENTE`, once `git init` runs.
*In a real company:* each product or service usually has its own repository on GitHub/GitLab.

**Branch**
A parallel line of changes, so work can happen without touching the main version.
*At Aura:* each Bootstrap or ticket will get its own branch once Git exists.
*In a real company:* every ticket gets a branch like `feature/AUR-12-booking`; `main` stays deployable.

**Commit**
A saved snapshot of changes with a message explaining why.
*At Aura:* the first commit will contain the Stage 0 foundation.
*In a real company:* reviewers read commit messages to understand intent; `git blame` points back to them months later.

**Pull Request (PR)**
A request to merge a branch into `main`, where others review the change.
*At Aura:* not used yet; planned once a remote and branch workflow exist.
*In a real company:* no code reaches production without an approved PR and passing CI.

**CI (Continuous Integration)**
Automated checks (tests, linters) that run on every change.
*At Aura:* `tools/check_docs.py` is the first check that will run in CI (Stage 1).
*In a real company:* a red CI blocks the merge, so broken code cannot reach `main`.

**Tenant**
One customer organization in a shared (multi-tenant) system, isolated from the others.
*At Aura:* each synthetic organization (first: AURA-SYN-001) will be a tenant.
*In a real company:* Clinic A must never see Clinic B's appointments, even though both use the same database.

**Observability**
The ability to understand what a running system is doing from its logs, metrics and traces.
*At Aura:* planned for Stage 7.
*In a real company:* when a booking fails, a trace shows which step and which external call failed.

**Proof of work**
Evidence that lets someone else verify the work was done and understood: code, tests, PRs, CI runs, metrics, case studies.
*At Aura:* from Stage 1, a milestone without it is not complete.
*In a real company:* a promotion case cites shipped PRs and measured impact, not "familiar with Kafka".

**Baseline**
The measured value of something before a change, so the change can be compared against it.
*At Aura:* duplicate count before and after a fix, labeled SYNTHETIC.
*In a real company:* "p95 latency was 800 ms before the cache; 300 ms after."

## AI agents

**Agent**
An AI model that can take actions with tools (read files, run commands), not just answer.
*At Aura:* the Cursor agent that wrote Stage 0 under `AGENTS.md`.
*In a real company:* an agent opens a PR fixing a lint error; a human reviews it.

**Skill**
A reusable written procedure an agent loads for a specific kind of task.
*At Aura:* pstack skills such as `/how` and `/reflect`, used from the plugin.
*In a real company:* a "release" skill tells the agent exactly which steps and checks a release needs.

**Rule**
Persistent instructions applied to an agent automatically.
*At Aura:* `AGENTS.md`.
*In a real company:* "never commit secrets" lives in a rule, so nobody has to repeat it.

**Hook**
Code executed automatically when a specific event happens.
*At Aura:* none yet.
*In a real company:* a pre-commit hook blocks a commit that contains an API key.

**MCP (Model Context Protocol)**
A standard way to connect an AI agent to external tools and data.
*At Aura:* candidate for connecting Jira in Bootstrap 02.
*In a real company:* the agent reads a Jira ticket through an MCP server instead of someone copy-pasting it.

**Eval**
A repeatable test that measures how well an AI system (or a person's output) performs a task.
*At Aura:* proposed communication evals (`brain/insights/communication-evals.md`).
*In a real company:* 200 sample client messages run through the agent; the share of correct bookings is tracked per release.

## Agile and delivery

**Stakeholder**
Anyone affected by or with influence over a piece of work.
*At Aura:* AURA-SYN-001's Finance Manager (buyer), Finance Analysts (users), Compliance (can block), and the operator acting as Product.
*In a real company:* before changing the booking flow, the PM aligns with Sales, Support and Engineering.

**Backlog**
The ordered list of work not done yet.
*At Aura:* will be created in Jira in Bootstrap 02.
*In a real company:* the product manager keeps the most valuable items at the top.

**Epic**
A large body of work split into many stories.
*At Aura:* "3-way match" could be an epic.
*In a real company:* "WhatsApp reminders" is an epic; "send reminder 24h before" is a story.

**Story**
A small piece of user-visible value with acceptance criteria.
*At Aura:* "As a front desk, I want automatic confirmation so I don't message each client."
*In a real company:* stories are sized to fit in one sprint.

**Acceptance criteria**
The conditions that must be true for a story to be considered done, written before implementation.
*At Aura:* "An invoice whose total differs from the PO by more than the tolerance is flagged as an exception and never auto-approved."
*In a real company:* QA and the PM check the criteria before accepting the delivery.

**Refinement**
A session where the team clarifies scope, requirements and acceptance criteria before a ticket goes to implementation.
*At Aura:* tickets will start as business symptoms and be refined before anyone proposes a solution.
*In a real company:* a ticket is not "ready" for the sprint until it has been refined.

**Sprint**
A fixed time box (often 2 weeks) in which the team commits to a set of backlog items.
*At Aura:* introduced in Bootstrap 02.
*In a real company:* sprint planning at the start, review and retrospective at the end.

**Blocker**
Something that prevents a task from moving forward until someone else acts.
*At Aura:* "Blocked: Git is not initialized, so the branch workflow cannot start."
*In a real company:* blockers are raised at the daily so someone can remove them the same day.

**Trade-off**
Gaining one property by accepting a cost in another; the basis of every technical decision.
*At Aura:* decision 0006 trades guaranteed context (a Rule) for portability and lower context cost (a linked doc).
*In a real company:* "Caching reduces latency but risks showing stale availability."

**Escalation**
Bringing a decision or problem to the person who owns it, with context and a recommendation.
*At Aura:* an engineer escalates to Product when a fix changes what clients see.
*In a real company:* an on-call engineer escalates a P1 to the incident commander after 15 minutes without mitigation.

## Finance & Operations

**Accounts Payable (AP)**
The process of receiving, checking, approving and paying what a company owes its suppliers.
*At Aura:* the first and only domain of Aura Ops.
*In a real company:* an AP team processes thousands of supplier invoices a month and closes them before month-end.

**3-way match**
A control that compares the purchase order, the goods receipt and the invoice before payment; a form of reconciliation.
*At Aura:* step 7 of the reference workflow, fully deterministic.
*In a real company:* if the invoice charges 100 units but only 90 were received, payment is held.

**Exception**
A case that fails an automated check and needs investigation or a human decision.
*At Aura:* where AI investigation adds value (step 9).
*In a real company:* AP analysts spend most of their day working the exception queue, not the happy path.

**Human-in-the-loop (HITL)**
A design where a person reviews or approves before an automated decision takes effect.
*At Aura:* agents recommend; an authorized person approves every financial action.
*In a real company:* an AI flags a suspicious payment; a controller confirms before it is blocked.

**SLA (Service Level Agreement)**
A committed target for a service, such as response or processing time.
*At Aura:* AURA-SYN-001's Finance Manager tracks the payment SLA.
*In a real company:* "95% of approved invoices paid within supplier terms."

**Audit trail**
A complete, tamper-resistant record of who did what, when, and based on which data.
*At Aura:* step 13; includes AI outputs and the model version that produced them.
*In a real company:* external auditors sample payments and ask for the full trail of each.

## Operations

**Incident**
An unplanned event that degrades the service for users.
*At Aura:* simulated in Stage 8; always labeled as simulated.
*In a real company:* reminders stop sending; someone is paged, fixes it, and writes a postmortem.

**Severity**
How bad an incident's impact is, usually P0/P1 (critical) to P3/P4 (minor). It drives response speed and who gets involved.
*At Aura:* "P1: invoices cannot be submitted for approval."
*In a real company:* a P1 pages on-call immediately; a P3 waits for business hours.

**RCA (Root Cause Analysis)**
A blameless written analysis after an incident: impact, timeline, root cause, and actions to prevent recurrence.
*At Aura:* template in `docs/process/COMMUNICATION.md`.
*In a real company:* RCAs are reviewed in a postmortem meeting and their action items tracked to completion.
