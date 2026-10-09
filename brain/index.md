# Brain index

Operational memory of the project. Read this file, then open only the entries you need. Keep each line to one sentence; this file is an index, not an encyclopedia.

## Decisions

Durable choices. Format: header line with Status, Owner, Date; then Context, Decision, Rationale, Trade-offs and alternatives, Impact. Record the decision, not the discussion.

- [0001](decisions/0001-memory-routing.md): `brain/` holds project memory, `docs/learning/` holds operator training; facts, workflow lessons and recurring failures go to different places.
- [0002](decisions/0002-create-on-first-content.md): directories and docs are created when they get real content, not in advance.
- [0003](decisions/0003-synthetic-data-only.md): only synthetic organizations, documents and data until a pilot is explicitly approved (rationale updated by 0007).
- [0004](decisions/0004-docs-check-script.md): Markdown links and training level are checked by a stdlib Python script.
- [0005](decisions/0005-repo-language.md): output to the operator in Brazilian Portuguese (decided); repository content in English (proposed).
- [0006](decisions/0006-communication-policy-location.md): communication policy lives in `docs/process/COMMUNICATION.md`, referenced from `AGENTS.md`; no Rule or Skill yet.
- [0007](decisions/0007-pivot-to-enterprise-agentic-automation.md): pivot from vertical healthcare SaaS to enterprise agentic automation; Aura Ops, Accounts Payable first. Records the previous direction.
- [0008](decisions/0008-synthetic-tenant-identifiers.md): synthetic organizations use `AURA-SYN-NNN` IDs, not brand-like names.

## Insights

Observations that may matter. Format: Observation, Why it matters, Evidence, Possible impact, Needs validation?

- [no-show-first-metric](insights/no-show-first-metric.md): SUPERSEDED by 0007; the "one clear metric first" lesson still applies.
- [communication-evals](insights/communication-evals.md): score the operator's status updates, incident comms and decision defenses against a rubric.

## Gotchas

Non-obvious problems already hit or confirmed.

- [github-readme-precedence](gotchas/github-readme-precedence.md): `.github/README.md` would replace the root README on GitHub.

## Investigations

Technical investigations. None yet; `brain/investigations/` is created with the first one.

## Inbox

Unvalidated candidates. Promote to another category or delete after review.

- [reflect-edit-targets](inbox/reflect-edit-targets.md): where would `/reflect` write its skill edits, and would they survive a plugin update?