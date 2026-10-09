# Working model

How work will move through the simulated company. Most of this is **not implemented yet**; the column "Today" says what exists.

```text
Business event → Ticket → Triage → Prioritization → Investigation → Implementation
  → Verification → Review → CI → Release → Feedback → Metrics → Learning
```

| Step | Plain meaning | Today |
|---|---|---|
| Business event | Something happens: a (simulated) customer complaint, a bug, a new need | Not implemented (Stage 2) |
| Ticket | The event is written down as a unit of work with a clear outcome | Not implemented (Stage 2) |
| Triage | Is it real, how urgent, who owns it? | Not implemented (Stage 2) |
| Prioritization | Compared against other work by value, risk and cost | Not implemented (Stage 2) |
| Investigation | Understand the system and the cause before changing anything | Manual, with pstack `/how` and `/why` |
| Implementation | Smallest correct change on a branch; `main` is the stable baseline, changes reach it via PR | Rule set; first branch in Bootstrap 02 |
| Verification | Prove it works: tests, commands, evidence (see Valid progress below) | `tools/check_docs.py` only |
| Review | Someone else (human or agent) challenges the change | Not implemented |
| CI | Automated checks on every change | Not implemented (Stage 1) |
| Release | The change reaches users | Not implemented |
| Feedback | What users (simulated) say or do | Not implemented (Stage 2) |
| Metrics | Numbers that show if the change helped | Not implemented (Stage 7) |
| Learning | Decisions, gotchas and skills updated | `brain/` and `docs/learning/` |

## Valid progress and proof of work

This section is the canonical source for what counts as progress. The question every component must help answer: *what evidence exists that this engineer can solve real problems with software and AI?*

```text
ARCHITECTURE + WORKING SOFTWARE + TESTS + EVIDENCE + METRICS + EXPLANATION = VALID PROGRESS
```

### Hard rule

From Stage 1 on, **no milestone is complete with documentation alone.** Each milestone produces at least one of: executable code, an automated test, a working integration, a benchmark, an eval, a trace, a metric, a reproducible incident, a PR with evidence, or a verifiable demo.

### Proof of work

The set of evidence that lets someone else verify the work was really done **and understood**: code, tests, PRs, CI runs, logs, traces, evals, benchmarks, decision records, incident reports, case studies, demo videos. It closes the gap between "I know this technology" and "here is the evidence I used it to solve a problem".

**Proof of authorship.** Relevant deliveries record the *why*, not only the *what*. The operator must be able to answer: Why this architecture? Why this database? Why AI here, and why not deterministic code? What failure modes exist? What are the trade-offs? What breaks at higher scale? How was it verified?

### Evidence

Every relevant technical claim is written as:

```text
CLAIM:     Duplicate processing was fixed.
EVIDENCE:  10,000 synthetic events executed against the fix.
RESULT:    0 duplicates (baseline: 17). SYNTHETIC.
```

"It works" is never a claim without evidence.

- **Baseline first.** Before optimizing or automating, record the current value when measurable (processing time, error rate, duplicate count, task success, latency, tokens, cost, human escalations). Never invent metrics just to have numbers.
- **SYNTHETIC or REAL.** Every metric carries one label. Correct: "In a synthetic benchmark with 10,000 events, duplicate processing went from 17 cases to zero." Incorrect: "AURA reduced company processing errors by 100%."

### Pull requests

Every relevant PR description contains:

```text
WHY / WHAT / HOW VERIFIED / METRICS / RISKS / NOT VERIFIED / FOLLOW UPS
```

### Git history

Git history is part of the portfolio: each commit is one logical step with a conventional message (`feat: implement invoice validation`, `test: add matching edge cases`, `fix: prevent duplicate processing`). Never `updates`, `changes`, `final`, `fix stuff`.

### Case studies and engineering demos

- A **case study** is written only for a relevant problem, not per session, using [../case-studies/_TEMPLATE.md](../case-studies/_TEMPLATE.md).
- An **engineering demo** shows the path, not just a UI: business problem → ticket → investigation → implementation → test → PR → CI → result.

### Documentation budget

Documentation must not grow significantly faster than executable engineering. If several consecutive sessions produce only documentation, stop and ask whether there is real technical progress before writing more.

## Tooling: pstack

pstack v0.15.15 is installed as a Cursor plugin. Its skills are used from the plugin; none are copied into this repository. `/setup-pstack` has not been run yet (no `~/.cursor/rules/pstack-models.mdc`), so skills use their default models.

| Situation | Use |
|---|---|
| Non-trivial engineering work | `/poteto-mode` |
| Need to understand a subsystem or where code should live | `/how` |
| Need the reason behind a decision or regression | `/why` |
| Operator wants to deeply understand a piece of work | `/teach` |
| Resuming work after a break | `/recall` |
| Adversarial review of a change | `/interrogate` |
| The workflow itself was inefficient | `/reflect` |
| Agents keep repeating the same mistake | `/correct` |

### Routing rule for what we learn

```text
Session facts        → docs/learning/journal/ and brain/
Workflow learning    → /reflect
Recurring failure    → /correct
```

`/reflect` proposes edits to existing skills. Before accepting one, confirm the lesson is reusable beyond one session; an isolated experience must not become a permanent rule. See [../../brain/inbox/reflect-edit-targets.md](../../brain/inbox/reflect-edit-targets.md).
