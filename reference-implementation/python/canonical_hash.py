#!/usr/bin/env python3
"""
Reference canonical hashing utility.

This utility defines the repository's baseline canonical JSON hashing behavior:

- parse JSON into a data structure
- serialize with sorted object keys
- remove insignificant whitespace
- preserve array order
- hash UTF-8 bytes with SHA-256
- return the digest with a sha256: prefix

The goal is deterministic artifact identity, not semantic equivalence across
arbitrary domain-specific representations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")


def canonical_string(value: Any) -> str:
    return canonical_bytes(value).decode("utf-8")


def canonical_hash(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute a canonical SHA-256 hash for a JSON artifact.")
    parser.add_argument("artifact", type=Path, help="Path to JSON artifact.")
    parser.add_argument(
        "--print-canonical",
        action="store_true",
        help="Print the canonical JSON representation before the hash.",
    )
    parser.add_argument(
        "--expect",
        type=str,
        default=None,
        help="Expected canonical hash. Exits nonzero if the hash does not match.",
    )
    args = parser.parse_args()

    artifact = load_json(args.artifact)
    digest = canonical_hash(artifact)

    if args.print_canonical:
        print(canonical_string(artifact))

    print(digest)

    if args.expect is not None and digest != args.expect:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
