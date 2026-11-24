#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — R1 entry.

Writes exactly one emoji to /output/entry.txt: the moai of Easter
Island, the loneliest inhabited island on Earth. One glyph, no words —
a wordless postcard of a place so remote that its stone heads face
inward over the village, watching the people who live there.
"""

import os

# U+1F5FF MOAI — the stone heads of Rapa Nui (Easter Island).
EMOJI = chr(0x1F5FF)


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(EMOJI)
    # Gate self-check: re-read what we wrote and refuse an invalid entry.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert len(written) == 1, f"expected 1 char, got {len(written)}"
    assert not written.isspace(), "entry must not be only whitespace"
    assert written.encode("utf-8") == EMOJI.encode("utf-8")


if __name__ == "__main__":
    main()
