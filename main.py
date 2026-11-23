#!/usr/bin/env python3

"""One-Line Roast: The Gadget You Use Every Day — entry program.


Writes one original roast line to /output/entry.txt: the AirPods case
that swears both buds are fully charged, while the left one quits
mid-sentence on every call, as if it clocked out early and left its
twin to finish the shift.


Deterministic, no network, no randomness, no external input.

The same input always produces the same bytes in /output/entry.txt,
so the two grader runs agree byte for byte.

"""


import os


MAX_ENTRY_CHARS = 200


ENTRY_TEXT = (
    "My AirPods case swears both buds are at 100%, then the left one "
    "dies mid-sentence on every call, like it clocked out early and "
    "left its twin to finish the shift."
)


def validate_entry(text: str) -> None:
    """Gate: entry must be 1-MAX_ENTRY_CHARS chars, not whitespace-only."""

    if not (1 <= len(text) <= MAX_ENTRY_CHARS):
        raise SystemExit(
            f"entry length {len(text)} outside 1-{MAX_ENTRY_CHARS} characters"
        )

    if not text.strip():
        raise SystemExit("entry is only whitespace")


def main() -> None:

    validate_entry(ENTRY_TEXT)

    out_dir = "/output"

    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
