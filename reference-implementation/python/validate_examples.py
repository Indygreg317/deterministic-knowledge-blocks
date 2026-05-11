#!/usr/bin/env python3
"""
Validate repository JSON examples against their corresponding JSON Schemas.

This script intentionally stays lightweight and explicit. It validates the current
reference artifacts used by the deterministic evaluation examples.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "Missing dependency: jsonschema. Install with `pip install jsonschema`."
    ) from exc

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schema"
EXAMPLES = ROOT / "use-cases" / "quantum" / "examples"

VALIDATION_TARGETS: Iterable[Tuple[Path, Path]] = [
    (EXAMPLES / "bell-state-output-pass.json", SCHEMA / "quantum-output.schema.json"),
    (EXAMPLES / "bell-state-output-fail.json", SCHEMA / "quantum-output.schema.json"),
    (EXAMPLES / "bell-state-correlation-contract.json", SCHEMA / "decision-contract.schema.json"),
    (EXAMPLES / "evaluator-policy-basic.json", SCHEMA / "evaluator-policy.schema.json"),
    (EXAMPLES / "bell-state-receipt-pass.json", SCHEMA / "execution-receipt.schema.json"),
    (EXAMPLES / "bell-state-receipt-fail.json", SCHEMA / "execution-receipt.schema.json"),
]


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_pair(instance_path: Path, schema_path: Path) -> None:
    instance = load_json(instance_path)
    schema = load_json(schema_path)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))

    if errors:
        print(f"Validation failed for {instance_path} against {schema_path}")
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            print(f"- {location}: {error.message}")
        raise SystemExit(1)

    print(f"OK: {instance_path} -> {schema_path}")


def main() -> None:
    for instance_path, schema_path in VALIDATION_TARGETS:
        validate_pair(instance_path, schema_path)


if __name__ == "__main__":
    main()
