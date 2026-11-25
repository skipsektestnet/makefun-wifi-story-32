#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes the one-line story to /output/entry.txt.
"""

import os

STORY = "He Left. The WiFi Stayed"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
