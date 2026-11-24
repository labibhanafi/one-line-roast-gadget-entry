#!/usr/bin/env python3

"""One-Line Roast: The Gadget You Use Every Day — entry program (v2).

Writes one original roast line to /output/entry.txt: the printer that
handles every practice sheet perfectly — test pages, alignment sheets,
low-ink warnings — then treats the one real document like a bomb.

Deterministic, no network, no randomness, no external input: the same
constant text is written on every run, so the two grader runs agree
byte for byte.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY_TEXT = (
    "My printer flawlessly prints test pages, alignment sheets and "
    "low-ink warnings, then stares at my one actual document like I "
    "just asked it to defuse a bomb."
)


def validate_entry(text):
    """Gate mirror: text must be 1..MAX_ENTRY_CHARS chars, not blank."""
    if not (1 <= len(text) <= MAX_ENTRY_CHARS):
        raise SystemExit(
            "entry length %d outside 1-%d characters"
            % (len(text), MAX_ENTRY_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    text.encode("utf-8")


def main():
    validate_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)
    print("%s (%d chars)" % (out_path, len(ENTRY_TEXT)))


if __name__ == "__main__":
    main()
