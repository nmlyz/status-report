#!/usr/bin/env python3
"""Status Report Comedy Sprint -- submission generator.

Writes one weekly status-report line to ``entry.txt`` inside
OUTPUT_DIR (default ``/output``). The output is deterministic:
running the script twice produces byte-identical files.
"""

import os
from pathlib import Path

LINE = "This week I made 2,847 decisions for you. You overruled 2,846 of them and thanked me for the one you kept."

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 200


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not line.strip():
        raise ValueError("line must not be blank")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-200 characters")
    if not line.endswith("."):
        raise ValueError("line must end with a period")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
