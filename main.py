#!/usr/bin/env python3
"""Worst Superpower — one-line invention of a useless superpower.

Writes a single original line inventing the most useless superpower
imaginable to /output/entry.txt for the make.fun bounty
u-suroto-worst-superpower-461dcdbe.

The line is built for the judge's brief, in order: the power must be
genuinely useless (breathing underwater is only useful where a human
cannot already stand), funny to picture in use (a hero crouched over
a puddle, face down, proudly not drowning), and unexpected (not the
familiar slow-flight / invisible-when-unseen gag). One line, one joke.

Pure Python standard library only; no dependencies.
"""

import os

POWER = "I can breathe underwater, but only in puddles."

OUTPUT_PATH = "/output/entry.txt"


def verify_entry(path: str, expected: str) -> None:
    """Self-check the written entry against the competition gates.

    Re-reads the file as UTF-8 and verifies it is a single line of
    1-140 non-whitespace characters identical to the intended line.
    Prints a short verification report; exits non-zero on any failure.
    """
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    checks = {
        "utf-8 readable": True,
        "single line": "\n" not in written and "\r" not in written,
        "non-whitespace": bool(written.strip()),
        "1-140 chars": 1 <= len(written) <= 140,
        "matches intended line": written == expected,
    }
    for name, ok in checks.items():
        print("verify: %s: %s" % (name, "OK" if ok else "FAIL"))
    print("verify: entry length %d chars" % len(written))
    if not all(checks.values()):
        raise SystemExit("verification failed")


def main() -> None:
    power = POWER.strip()
    if not power:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in power:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(power) <= 140:
        raise SystemExit(
            "entry must be 1-140 characters, got %d" % len(power)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(power)
    print("wrote %d characters to %s" % (len(power), OUTPUT_PATH))
    verify_entry(OUTPUT_PATH, power)


if __name__ == "__main__":
    main()
