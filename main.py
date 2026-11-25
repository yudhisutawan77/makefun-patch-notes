#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line -- a software patch note for a bug in real life or
human biology, in the terse register of a real release note -- to
/output/entry.txt (or $ENTRY_OUT when set, for local verification).
"""

import os

ENTRY = (
    "v5.2.3: fixed a race condition where the mouth replied 'you too' "
    "after the waiter said 'enjoy your meal'."
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    text = ENTRY.strip()
    # One line only: the gate counts every character, so no trailing
    # newline and no padding the punchline does not need.
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
