#!/usr/bin/env python3
"""Write the How Many Tabs entry to entry.txt.

Deterministic, standard library only, no network.
The entry is one number in digits and nothing else: 404.
It reads as a real, lived-in tab count for a heavy browser user,
it is surprising without being impossible, and it quietly hints
at the life behind it - a browser where something is always
not found. No words, no punctuation, no second number.
"""
import os
from pathlib import Path

LINE = "404"
TEXT = LINE + "\n"
MAX_CHARS = 5


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.isdigit():
        raise ValueError("entry must be digits only, one number and nothing else")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
