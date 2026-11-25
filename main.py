"""Two Robots in an Elevator.

Writes one line of awkward small talk between two robots sharing an
elevator to /output/entry.txt: Unit 7 tries to chat, Unit 9 turns out to
be the elevator itself. Pure Python 3.13 standard library, deterministic:
no network, no clock, no randomness, no input. Two runs write
byte-identical output.
"""

import os
import sys

LINE = "Unit 7: 'So... do you come here often?' Unit 9: 'I live here. I am the elevator.' Unit 7: '...Great. Great talk.'"

# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check(line: str) -> None:
    """Exit with a message if the line fails the bounty gate."""
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        sys.exit(
            f"invalid entry: {len(line)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} range"
        )
    if "\n" in line or "\r" in line:
        sys.exit("invalid entry: must be a single line")
    if line != line.strip():
        sys.exit("invalid entry: must not start or end with whitespace")


def main() -> None:
    check(LINE)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
