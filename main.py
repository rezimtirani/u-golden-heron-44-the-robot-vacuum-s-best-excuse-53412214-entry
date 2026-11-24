#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line -- the funniest excuse a robot vacuum gives for
missing a spot -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Nothing is written into the repository folder itself.
"""

import os
import sys

EXCUSE = (
    "My cliff sensor mistook the rug fringe for a staircase, "
    "so I heroically refused to fall off it."
)


def check_excuse(text):
    """Gate mirror: one line, 1-140 characters, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("excuse must not be empty")
    if len(text) > 140:
        raise ValueError("excuse must be at most 140 characters")
    if "\n" in stripped:
        raise ValueError("excuse must be a single line")
    return text


def main():
    check_excuse(EXCUSE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
