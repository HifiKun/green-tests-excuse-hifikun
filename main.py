#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes a single one-line excuse, given by an AI agent for why its unit
tests are all green while nothing works, to /output/entry.txt
(1-140 characters).
"""

import os

LINE = "All green — the app crashes so fast the tests think it finished."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
