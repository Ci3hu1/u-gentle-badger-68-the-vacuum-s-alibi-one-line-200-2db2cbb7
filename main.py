#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes the robot vacuum's one-line excuse for missing a spot to
/output/entry.txt. Pure standard library; no third-party packages.

The line is written with no trailing newline so the file holds exactly
the judged line, 1-200 characters, not only whitespace.
"""

import os

LINE = (
    "I did not miss the spot. I mapped it, logged it, and formally "
    "reassigned it to the cat. Case closed. Returning to dock."
)

OUTPUT_DIR = os.environ.get("VACUUM_OUTPUT_DIR", "/output")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    text = LINE
    assert 1 <= len(text) <= 200, "entry line must be 1-200 characters"
    assert text.strip(), "entry line must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects outputs as another user: leave them readable.
    os.chmod(OUTPUT_FILE, 0o644)
    os.chmod(OUTPUT_DIR, 0o755)


if __name__ == "__main__":
    main()
