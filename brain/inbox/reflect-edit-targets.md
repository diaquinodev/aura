# Where would `/reflect` write its edits?

**Candidate concern (unvalidated):** pstack's `/reflect` is described as routing each learning "to a concrete edit on an existing skill". This repository has no skills of its own; the only installed skills live in the plugin cache (`~/.cursor/plugins/cache/cursor-public/pstack/<hash>/skills/`). Edits there would probably be lost when the plugin updates, and would apply to every project, not just Aura.

**To validate:** on the first real `/reflect` run, check which file it proposes to change before accepting.

**If confirmed:** promote to `brain/gotchas/` and decide whether project-specific workflow lessons belong in `AGENTS.md` or in a project skill instead.
