#!/usr/bin/env python3
"""Ship It Friday — writes the entry text to /output/entry.txt.

Standard library only. Deterministic, no network, no randomness.
"""

import os

ENTRY = "feat: ship Friday deploy, 214 tests green on my laptop, prod is basically the same laptop, merging now"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    with open("/output/entry.txt", "rb") as f:
        roundtrip = f.read()
    assert roundtrip == data, "round-trip mismatch"
    assert 1 <= len(ENTRY) <= 159, "entry length out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
