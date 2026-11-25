"""Tell a Whole Story in 32 Characters: writes the entry to /output/entry.txt.

Why this name: a passer-by reading a network list gets a whole breakup in
six words -- someone left, and the Wi-Fi (and the flat, and the life) stayed
with the person who named the network. The joke is the quiet victory lap
hidden in a router name.
"""

import os

# The entry itself: one Wi-Fi name, 24 characters, punch in the last word.
ENTRY = "He Left. The WiFi Stayed"

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: the sealed gate wants 1 to 32 characters, never blank.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    assert len(ENTRY) <= 32, f"entry is {len(ENTRY)} chars, over the 32 limit"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
