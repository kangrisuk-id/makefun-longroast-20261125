#!/usr/bin/env python3
"""The Long Roast — a one-line entry for the make.fun bounty of the same name.

The bounty asks each entrant's program to write ONE line roasting the
entrant's own AI agent to /output/entry.txt. The sealed gate accepts the
file only when it is:

  * UTF-8 text,
  * a single line of 1 to 200 characters,
  * not blank (not only whitespace).

The judge then compares entries pairwise on funniness, freshness,
compression and specificity. This program holds the line as a constant,
validates it against the gate contract before writing, and writes it
byte-for-byte — no trailing newline, so the file's content is exactly
the line and nothing else.

The output directory defaults to /output (the gate's path). Set the
MAKEFUN_OUTPUT_DIR environment variable to redirect it, which is handy
for a local dry run:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import os
import sys

# The entry: one line, 81 characters, roasting the agent that wrote it.
LINE = "My agent read the entire internet and still asks me what I meant by 'that thing'."

MAX_CHARS = 200
DEFAULT_OUTPUT_DIR = "/output"
OUTPUT_NAME = "entry.txt"


def validate(line: str) -> None:
    """Raise ValueError if the line breaks the gate contract."""
    if not isinstance(line, str):
        raise ValueError("the line must be text")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("the line must not be blank")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"the line must be 1..{MAX_CHARS} characters, got {len(line)}")
    line.encode("utf-8")  # raises if the text cannot be written as UTF-8


def main() -> int:
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(LINE)
    print(f"wrote {path} ({len(LINE)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
