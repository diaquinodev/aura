# Session lifecycle

A session is one focused block of work (with or without an AI agent). The goal is to resume months later from curated context, not from transcripts.

## Session start

1. **Identify the objective.** One sentence: what is done when this session ends?
2. **Recover minimal context.** Read [../../brain/index.md](../../brain/index.md), then only the files relevant to the objective. `/recall` can help after a long break.
3. **Check Git state.** `git status`, `git branch --show-current`, `git log -5 --oneline`.
4. **Check the backlog**, once it exists (Stage 2).
5. **Identify the training level** in [../learning/README.md](../learning/README.md).

## During the session

Record only decisions, discoveries and evidence. Do not transcribe the conversation. Unvalidated ideas go to `brain/inbox/`.

## Session end

Write a journal entry from [../learning/journal/_TEMPLATE.md](../learning/journal/_TEMPLATE.md) that covers:

1. **Work summary**: what was done.
2. **Decisions**: what was decided and why. Durable ones also go to `brain/decisions/`.
3. **Evidence**: commands, tests and their results.
4. **Open questions**: what is still unresolved.
5. **Learning**: what the operator should study or review.
6. **Insights**: product or process ideas. Worth keeping ones go to `brain/insights/`.
7. **Next session**: the next logical step.
8. **Reflection**: if the session taught something about *how we work*, consider `/reflect`. It is not a substitute for the factual record above.

Then run `python tools/check_docs.py` and review `git diff` before committing.
