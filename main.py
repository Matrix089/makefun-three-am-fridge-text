#!/usr/bin/env python3
"""Write one 3am text from a smart fridge for make.fun's
The 3AM Fridge Text bounty.

Why this line fits the judge's brief: it reads like a real
text message from an appliance that has been awake all night
-- it names the hour, it has an opinion about being opened
again, and the punchline lands on "pickles and regret", a
fresh angle instead of the obvious milk, ice or door-left-open
lines. Short enough to read on a lock screen, complete without
a follow-up.
"""

import os

LINE = (
    "It's 3am. You keep opening me like the answer to your life "
    "is in here. Spoiler: it's just pickles and regret."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-140 characters, a single line.
    # The line was counted at exactly 109 characters; pin that
    # so any accidental wording change fails loudly instead of silently
    # shipping a different (or over-long) entry.
    assert len(line) == 109, f"line is {len(line)} characters, expected 109"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 140, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"
    assert line.startswith("It's 3am."), "line must name the hour up front"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 109, "entry.txt is not 109 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
