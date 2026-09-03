#!/usr/bin/env python3
"""Replace a PDF trailer ID with a deterministic content-derived ID.

XeLaTeX/xdvipdfmx may write a random /ID value even when SOURCE_DATE_EPOCH is
fixed. Depending on the generated PDF, the two ID strings may be represented as
hexadecimal strings (``<...>``) or as PDF literal strings (``(...)``). This
script supports both encodings and replaces the ID contents in place, preserving
all byte offsets in the PDF.
"""
from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path
from typing import Match

HEX_ID_PATTERN = re.compile(
    rb"/ID\s*\[\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*\]"
)

# ID strings produced by xdvipdfmx do not normally contain nested literal
# parentheses. The alternatives below accept ordinary bytes, escaped bytes,
# octal escapes, and escaped line endings.
LITERAL_ID_PATTERN = re.compile(
    rb"/ID\s*\[\s*\(((?:\\[0-7]{1,3}|\\\r?\n|\\.|[^\\()])*)\)"
    rb"\s*\(((?:\\[0-7]{1,3}|\\\r?\n|\\.|[^\\()])*)\)\s*\]",
    re.DOTALL,
)


def _replace_id_contents(data: bytes, match: Match[bytes]) -> bytes:
    first = match.group(1)
    second = match.group(2)
    if len(first) != len(second):
        raise RuntimeError("unequal PDF trailer ID representation lengths")

    zeroed = bytearray(data)
    zeroed[match.start(1) : match.end(1)] = b"0" * len(first)
    zeroed[match.start(2) : match.end(2)] = b"0" * len(second)
    digest = hashlib.sha256(zeroed).hexdigest().encode("ascii")

    if len(first) > len(digest):
        repeats = (len(first) + len(digest) - 1) // len(digest)
        digest = (digest * repeats)[: len(first)]
    else:
        digest = digest[: len(first)]

    normalized = bytearray(data)
    normalized[match.start(1) : match.end(1)] = digest
    normalized[match.start(2) : match.end(2)] = digest
    return bytes(normalized)


def normalize_pdf_id(path: Path) -> None:
    data = path.read_bytes()
    hex_matches = list(HEX_ID_PATTERN.finditer(data))
    literal_matches = list(LITERAL_ID_PATTERN.finditer(data))
    matches = hex_matches + literal_matches

    if len(matches) != 1:
        raise RuntimeError(
            f"expected exactly one supported PDF trailer ID in {path}, "
            f"found {len(matches)}"
        )

    path.write_bytes(_replace_id_contents(data, matches[0]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    args = parser.parse_args()
    normalize_pdf_id(args.pdf)


if __name__ == "__main__":
    main()
