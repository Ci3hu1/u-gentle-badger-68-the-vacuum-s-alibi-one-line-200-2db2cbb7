#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse for missing a spot to
/output/entry.txt. Pure standard library; no third-party packages.

The line is written with no trailing newline so the file holds exactly
the judged line, 1-200 characters, not only whitespace.
"""

import os
from pathlib import Path

LINE = (
    "I did not miss the spot. I mapped it, logged it, and formally "
    "reassigned it to the cat. Case closed. Returning to dock."
)

OUTPUT_DIR = os.environ.get("VACUUM_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(text: str) -> str:
    """Check the entry line against the sealed gate before writing it.

    The gate wants exactly one line, 1-200 characters, not only
    whitespace, with no line breaks or control characters. Returns the
    line unchanged so callers can chain it.
    """
    if not text.strip():
        raise ValueError("entry line must not be only whitespace")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry line must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("entry line must not contain control characters")
    return text


def main():
    validate(LINE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects outputs as another user: leave them readable.
    os.chmod(OUTPUT_FILE, 0o644)
    # /output may belong to another user in the grader: a failed directory
    # chmod must not fail the run (it crashed the v2 submission, exit 1).
    try:
        os.chmod(OUTPUT_DIR, 0o755)
    except OSError:
        pass
    # Self-check: the file must hold exactly the line, nothing else.
    if Path(OUTPUT_FILE).read_text(encoding="utf-8") != LINE:
        raise ValueError("entry file does not hold exactly the line")


if __name__ == "__main__":
    main()
