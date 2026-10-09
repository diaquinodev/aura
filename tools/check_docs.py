"""Check repository Markdown for broken relative links and training-level drift.

Usage: python tools/check_docs.py
Exits 1 when a problem is found.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
LEVEL = re.compile(r"TRAINING_LEVEL = (\d)")
LEVEL_FILES = ["README.md", "AGENTS.md", "docs/learning/README.md", "docs/status/CURRENT.md"]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", ".pytest_cache"}


def markdown_files():
    for path in sorted(ROOT.rglob("*.md")):
        if not SKIP_DIRS.intersection(path.relative_to(ROOT).parts):
            yield path


def broken_links():
    for path in markdown_files():
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            resolved = (path.parent / unquote(target.split("#")[0])).resolve()
            if not resolved.exists():
                yield f"{path.relative_to(ROOT)}: broken link -> {target}"


def level_drift():
    levels = {}
    for name in LEVEL_FILES:
        found = LEVEL.findall((ROOT / name).read_text(encoding="utf-8"))
        if len(found) != 1:
            yield f"{name}: expected exactly one 'TRAINING_LEVEL = N', found {len(found)}"
        else:
            levels[name] = found[0]
    if len(set(levels.values())) > 1:
        yield f"training level disagrees across files: {levels}"


def main():
    problems = [*broken_links(), *level_drift()]
    for problem in problems:
        print(problem)
    print(f"{len(problems)} problem(s) in {sum(1 for _ in markdown_files())} Markdown files")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
