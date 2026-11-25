#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes the 24-character story to /output/entry.txt.
"""

STORY = "He Left. The WiFi Stayed"
MAX_CHARS = 32


def main() -> None:
    if len(STORY) > MAX_CHARS:
        raise SystemExit(
            f"story is {len(STORY)} chars, over the {MAX_CHARS}-char limit"
        )
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
