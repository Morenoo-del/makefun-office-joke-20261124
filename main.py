#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single-line joke about office life to /output/entry.txt
for the bounty "One-Line Office Joke: 24-Hour Sprint".
"""

import os

JOKE = (
    "The office Wi-Fi went down for ten minutes today and we all just "
    "sat there making awkward eye contact like it was 1994."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    # Gate checks, mirroring the bounty scorer: UTF-8 text, 1-200 chars,
    # not only whitespace, and a single line with no line breaks inside.
    assert text, "joke must not be empty"
    assert text.strip() == text, "joke must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "joke must be one line"
    assert len(text) <= 200, f"joke is {len(text)} chars, over the 200 limit"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
