#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one funny, honest excuse to /output/entry.txt.
Pure stdlib, no dependencies.
"""

import os


def main() -> None:
    excuse = (
        "Sorry I'm late \u2014 I delegated the deadline to a subagent, "
        "and it delegated it right back to me."
    )
    # Gate: the entry must be 1-200 characters, a single line, UTF-8.
    assert 1 <= len(excuse) <= 200, "excuse out of range"
    assert "\n" not in excuse, "excuse must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(excuse + "\n")


if __name__ == "__main__":
    main()
