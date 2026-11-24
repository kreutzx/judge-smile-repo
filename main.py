"""Make the Judge Smile — one warm, surprising line about a small good
thing that happened today.

Writes exactly one line (no trailing newline) to /output/entry.txt, per
the competition gate: UTF-8 text of 1 to 200 characters.
"""

import os

ENTRY = (
    "This morning, the grumpiest man on my street pressed a still-warm "
    "bun into my hands and whispered, 'Eat. Tuesdays are hard enough already.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
