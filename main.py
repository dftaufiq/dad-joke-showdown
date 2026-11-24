#!/usr/bin/env python3
"""Write the chosen dad joke to the grader's output folder.

The joke was picked by an internal pairwise tournament over 24 original
candidates (see the build folder's candidates.md): one sharp idea, one
clean turn ("comes clean"), punchline on the last line, told father to
kids, 96 characters. This entrypoint is deterministic: it writes the same
bytes on every run, needs no network and no third-party packages.

The destination is $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

from __future__ import annotations

import os
from pathlib import Path

JOKE = "I told the kids the dishwasher is the most honest appliance in the house. It always comes clean."

MAX_JOKE_CHARS = 200  # grader gate: the joke must be 1-200 characters


def destination_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> int:
    text = JOKE
    assert 1 <= len(text) <= MAX_JOKE_CHARS, "joke must be 1-200 characters"
    assert text.strip(), "joke must not be only whitespace"
    out = destination_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
