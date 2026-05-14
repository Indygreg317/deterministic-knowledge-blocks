#!/usr/bin/env python3
"""
Lightweight artifact schema validation for known repository examples.

Validation targets are declared in:

    validation/artifact-validation-manifest.json

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
- local $ref entries into #/$defs

It is not a complete JSON Schema implementation.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MANIFEST = ROOT / "validation" / "artifact-validation-manifest.json"
MANIFEST_SCHEMA = ROOT / "schema" / "artifact-validation-manifest.schema.json"


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


def resolve_ref(schema_root: Dict[str, Any], ref: str) -> Dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValueError(f"Only local refs are supported by the lightweight validator: {ref}")

    current: Any = schema_root
    for part in ref[2:].split("/"):
        if not isinstance(current, dict) or part not in current:
            raise ValueError(f"Unresolvable local ref: {ref}")
        current = current[part]

    if not isinstance(current, dict):
        raise ValueError(f"Resolved ref does not point to an object schema: {ref}")
    return current


def validate(schema: Dict[str, Any], value: Any, path: str = "$", schema_root: Dict[str, Any] | None = None) -> List[str]:
    errors: List[str] = []
    root = schema_root or schema

    if "$ref" in schema:
        try:
            resolved = resolve_ref(root, schema["$ref"])
        except ValueError as exc:
            return [f"{path}: {exc}"]
        return validate(resolved, value, path, root)

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
                errors.extend(validate(field_schema, value[field], f"{path}.{field}", root))

    if isinstance(value, list) and "items" in schema:
        item_schema = schema["items"]
        for index, item in enumerate(value):
            errors.extend(validate(item_schema, item, f"{path}[{index}]", root))

    return errors


def validate_case(case: Dict[str, Any]) -> List[str]:
    schema = load_json(ROOT / case["schema_path"])
    artifact = load_json(ROOT / case["artifact_path"])
    return validate(schema, artifact)


def validate_manifest_against_schema(manifest: Dict[str, Any]) -> List[str]:
    schema = load_json(MANIFEST_SCHEMA)
    return validate(schema, manifest)


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate repository artifacts against declared schemas.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Path to artifact validation manifest.",
    )
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    failures: List[str] = []

    manifest_errors = validate_manifest_against_schema(manifest)
    if manifest_errors:
        failures.append(f"Validation manifest failed schema validation: {args.manifest}")
        failures.extend(f"  - {error}" for error in manifest_errors)
    else:
        print(f"VALID MANIFEST: {args.manifest} against {MANIFEST_SCHEMA.relative_to(ROOT)}")

    for case in manifest.get("valid_cases", []):
        schema_path = case["schema_path"]
        artifact_path = case["artifact_path"]
        case_id = case["case_id"]
        errors = validate_case(case)
        if errors:
            failures.append(
                f"Expected valid artifact failed schema validation: {case_id} ({artifact_path} against {schema_path})"
            )
            failures.extend(f"  - {error}" for error in errors)
        else:
            print(f"VALID: {case_id} ({artifact_path} against {schema_path})")

    for case in manifest.get("expected_invalid_cases", []):
        schema_path = case["schema_path"]
        artifact_path = case["artifact_path"]
        case_id = case["case_id"]
        reason = case.get("expected_failure_reason", "expected invalid case")
        errors = validate_case(case)
        if not errors:
            failures.append(f"Expected invalid artifact passed schema validation: {case_id} ({reason})")
        else:
            print(f"EXPECTED INVALID: {case_id} ({artifact_path} against {schema_path})")
            print(f"  reason: {reason}")
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
