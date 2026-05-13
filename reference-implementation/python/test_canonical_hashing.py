#!/usr/bin/env python3
"""
Regression checks for canonical JSON hashing behavior.

These checks prove the baseline properties required by receipt verification:

- object key order does not change the canonical hash
- changed artifact content changes the canonical hash
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "reference-implementation" / "python"))

from canonical_hash import canonical_hash, load_json  # noqa: E402

EXAMPLES = ROOT / "examples" / "canonicalization"


def main() -> None:
    artifact_a = load_json(EXAMPLES / "artifact-a.json")
    artifact_b = load_json(EXAMPLES / "artifact-b-reordered.json")
    artifact_c = load_json(EXAMPLES / "artifact-c-changed.json")

    hash_a = canonical_hash(artifact_a)
    hash_b = canonical_hash(artifact_b)
    hash_c = canonical_hash(artifact_c)

    print(f"artifact-a: {hash_a}")
    print(f"artifact-b-reordered: {hash_b}")
    print(f"artifact-c-changed: {hash_c}")

    if hash_a != hash_b:
        raise SystemExit("Expected reordered artifact to preserve canonical hash.")

    if hash_a == hash_c:
        raise SystemExit("Expected changed artifact content to produce a different canonical hash.")

    print("Canonical hashing regression checks passed.")


if __name__ == "__main__":
    main()
