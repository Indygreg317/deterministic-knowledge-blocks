#!/usr/bin/env python3
"""
Lightweight artifact schema validation for known repository examples.

This intentionally avoids third-party dependencies so CI can validate core
schemas with only the Python standard library.

It supports the subset of JSON Schema currently used by this repository:

- type
- required
- properties
- additionalProperties: false
- enum
- array items
- nullable type lists such as ["string", "null"]

It is not a complete JSON Schema implementation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[2]

VALID_CASES: List[Tuple[str, str]] = [
    ("schema/decision-contract.schema.json", "use-cases/quantum/examples/bell-state-correlation-contract.json"),
    ("schema/evaluator-policy.schema.json", "use-cases/quantum/examples/evaluator-policy-basic.json"),
    ("schema/quantum-output.schema.json", "use-cases/quantum/examples/bell-state-output-pass.json"),
    ("schema/quantum-output.schema.json", "use-cases/quantum/examples/bell-state-output-fail.json"),
    ("schema/execution-receipt.schema.json", "use-cases/quantum/examples/bell-state-receipt-pass.json"),
    ("schema/execution-receipt.schema.json", "use-cases/quantum/examples/bell-state-receipt-tampered-status.json"),
    ("schema/verification-report.schema.json", "use-cases/quantum/examples/bell-state-verification-report-pass.json"),
    ("schema/verification-report.schema.json", "use-cases/quantum/examples/bell-state-verification-report-tampered-status.json"),
    ("schema/governance-boundary-map.schema.json", "use-cases/quantum/examples/bell-state-governance-boundary-map.json"),
    ("schema/audit-package-manifest.schema.json", "audit-packages/bell-state-minimal/audit-package-manifest.json"),
]

EXPECTED_INVALID_CASES: List[Tuple[str, str, str]] = [
    (
        "schema/decision-contract.schema.json",
        "use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json",
        "unsupported operator should fail current Decision Contract schema",
    ),
]


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def is_type(value: Any, expected_type: str) -> bool:
    if expected_type == "null":
        return value is None
    if expected_type == "object":
        return isinstance(value, dict)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected_type == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected_type == "boolean":
        return isinstance(value, bool)
    return True


def validate(schema: Dict[str, Any], value: Any, path: str = "$") -> List[str]:
    errors: List[str] = []

    expected_type = schema.get("type")
    if isinstance(expected_type, list):
        if not any(is_type(value, item) for item in expected_type):
            errors.append(f"{path}: expected one of {expected_type}, found {type(value).__name__}")
            return errors
    elif isinstance(expected_type, str):
        if not is_type(value, expected_type):
            errors.append(f"{path}: expected {expected_type}, found {type(value).__name__}")
            return errors

    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: expected one of {schema['enum']}, found {value!r}")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for field in required:
            if field not in value:
                errors.append(f"{path}: missing required field {field!r}")

        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for field in value:
                if field not in properties:
                    errors.append(f"{path}: additional property not allowed: {field!r}")

        for field, field_schema in properties.items():
            if field in value:
                errors.extend(validate(field_schema, value[field], f"{path}.{field}"))

    if isinstance(value, list) and "items" in schema:
        item_schema = schema["items"]
        for index, item in enumerate(value):
            errors.extend(validate(item_schema, item, f"{path}[{index}]"))

    return errors


def validate_case(schema_path: str, artifact_path: str) -> List[str]:
    schema = load_json(ROOT / schema_path)
    artifact = load_json(ROOT / artifact_path)
    return validate(schema, artifact)


def main() -> None:
    failures: List[str] = []

    for schema_path, artifact_path in VALID_CASES:
        errors = validate_case(schema_path, artifact_path)
        if errors:
            failures.append(f"Expected valid artifact failed schema validation: {artifact_path} against {schema_path}")
            failures.extend(f"  - {error}" for error in errors)
        else:
            print(f"VALID: {artifact_path} against {schema_path}")

    for schema_path, artifact_path, reason in EXPECTED_INVALID_CASES:
        errors = validate_case(schema_path, artifact_path)
        if not errors:
            failures.append(f"Expected invalid artifact passed schema validation: {artifact_path} ({reason})")
        else:
            print(f"EXPECTED INVALID: {artifact_path} against {schema_path} ({reason})")
            for error in errors:
                print(f"  - {error}")

    if failures:
        print("Schema validation failures:")
        for failure in failures:
            print(failure)
        raise SystemExit(1)

    print("Artifact schema validation completed successfully.")


if __name__ == "__main__":
    main()
