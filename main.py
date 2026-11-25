"""Tell a Whole Story in 32 Characters — entry program.

Writes the 24-character story to the output file the kit reads.
Deterministic, stdlib only, no network, no randomness.
"""

import os
from pathlib import Path

STORY = "He Left. The WiFi Stayed"
LIMIT = 32


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def validate_story(text: str) -> str:
    """The bounty limit is 32 characters; refuse anything longer."""
    if len(text) > LIMIT:
        raise ValueError(f"story is {len(text)} chars, over the {LIMIT} limit")
    if not text.strip():
        raise ValueError("story must not be empty")
    return text


def main() -> int:
    story = validate_story(STORY)
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    # The repo's entry.txt is the bare 24-character story with no trailing
    # newline, so write exactly that — the two files must be byte-identical.
    (out / "entry.txt").write_text(story, encoding="utf-8")
    print(story)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
