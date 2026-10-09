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
| Verification | Prove it works: tests, commands, evidence | `tools/check_docs.py` only |
| Review | Someone else (human or agent) challenges the change | Not implemented |
| CI | Automated checks on every change | Not implemented (Stage 1) |
| Release | The change reaches users | Not implemented |
| Feedback | What users (simulated) say or do | Not implemented (Stage 2) |
| Metrics | Numbers that show if the change helped | Not implemented (Stage 7) |
| Learning | Decisions, gotchas and skills updated | `brain/` and `docs/learning/` |

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
