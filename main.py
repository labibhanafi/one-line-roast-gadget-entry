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


ENTRY_TEXT = (
    "My AirPods case swears both buds are at 100%, then the left one "
    "dies mid-sentence on every call, like it clocked out early and "
    "left its twin to finish the shift."
)


def main() -> None:

    text = ENTRY_TEXT

    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside 1-200 characters")

    if not text.strip():
        raise SystemExit("entry is only whitespace")

    out_dir = "/output"

    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
