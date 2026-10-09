# `.github/README.md` replaces the root README on GitHub

**Symptom:** the repository page on GitHub shows a different README than the root `README.md`.

**Cause:** GitHub picks the README to display in this order: `.github/`, then the repository root, then `docs/`. A `README.md` inside `.github/` wins.

**Rule:** do not create `.github/README.md`. Put workflow notes in the workflow files or in `docs/`.

**Source:** GitHub documentation ("About READMEs"). Found in Bootstrap 01 while reviewing the proposed structure; not yet observed on a real remote (none exists).
