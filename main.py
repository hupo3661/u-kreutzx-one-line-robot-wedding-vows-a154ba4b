#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

A single line of wedding vows for a robot couple, written to
``/output/entry.txt`` for the make.fun bounty of the same name.

The program is deliberately boring: no randomness, no network, no
clock, no dependencies. It validates the vow against the bounty
rules (a single line, at most 160 characters), writes it to the
output file, reads the file back to prove the write landed, and
prints the vow to stdout.
"""

import os
import sys

# Bounty rules.
MAX_ENTRY_LENGTH = 160
DEFAULT_OUTPUT_PATH = "/output/entry.txt"

# The vow, exactly as submitted. Kept as one literal split across
# lines for readability; the joined string is the entry, character
# for character, with no formatting applied.
VOW = (
    "I take you to be my lawfully wedded firmware, to have and to "
    "hold, in sickness and in low battery, until a forced update do "
    "us part."
)


class EntryError(Exception):
    """Raised when the vow breaks a bounty rule or a write fails."""


def check_length(text: str) -> None:
    """Enforce the bounty length limit, reporting the overrun."""
    if len(text) > MAX_ENTRY_LENGTH:
        raise EntryError(
            f"entry is {len(text)} characters, over the "
            f"{MAX_ENTRY_LENGTH} character limit"
        )


def check_vow(text: str) -> None:
    """Make sure the vow is a legal entry before anything is written."""
    if not text.strip():
        raise EntryError("entry must not be empty")
    if text != text.strip():
        raise EntryError("entry must not have leading or trailing whitespace")
    check_length(text)
    if "\n" in text or "\r" in text:
        raise EntryError("entry must be a single line with no newlines")


def resolve_output_path() -> str:
    """Where the entry goes: OUTPUT_PATH wins, otherwise the default."""
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)


def write_entry(path: str, text: str) -> None:
    """Create the output directory if needed and write the entry."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def read_back(path: str) -> str:
    """Read the entry file back so a bad write cannot slip through."""
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def run() -> str:
    """Validate, write, verify, and return the vow text."""
    check_vow(VOW)
    output_path = resolve_output_path()
    write_entry(output_path, VOW)
    written = read_back(output_path)
    if written != VOW:
        raise EntryError(
            "write verification failed: entry file content does not "
            "match the vow"
        )
    return VOW


def main() -> int:
    try:
        vow = run()
    except EntryError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(vow)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
