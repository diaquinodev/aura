# Learning

This area tracks the **operator's professional development**. Project memory (what the project knows) lives in [../../brain/index.md](../../brain/index.md), not here.

Example of the split:

- `brain/gotchas/github-readme-precedence.md` records a project fact: GitHub shows `.github/README.md` instead of the root README.
- [GLOSSARY.md](GLOSSARY.md) explains a concept: what a repository is.

## Training level

`TRAINING_LEVEL = 1`

| Level | Name | AI does | Operator does |
|---|---|---|---|
| 1 | Guided | Explains, presents options, shows risks, structures reasoning | Makes important decisions with support |
| 2 | Assisted | Gives context, does mechanical tasks, reviews, questions decisions | Prioritizes, investigates, decides architecture, implements critical parts |
| 3 | Professional | Provides ticket, business context, tools, evidence | Works as a real team member |

The level changes only by the operator's decision, recorded in `brain/decisions/`, with proof of work from [LEARNING-PATH.md](LEARNING-PATH.md). Moving from Guided to Assisted requires growing, demonstrated ability to interpret tickets, prioritize, implement, test and explain decisions; reading about them is not enough. When it changes, update the `TRAINING_LEVEL` line here, in [../../README.md](../../README.md) and in [../../AGENTS.md](../../AGENTS.md); `tools/check_docs.py` fails if they disagree.

## Files

- [LEARNING-PATH.md](LEARNING-PATH.md): competencies and their status.
- [GLOSSARY.md](GLOSSARY.md): concepts used so far.
- `journal/`: one entry per meaningful session, using [journal/_TEMPLATE.md](journal/_TEMPLATE.md).
