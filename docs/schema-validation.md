# Schema Validation

## Purpose

This repository includes lightweight artifact schema validation for known examples.

The goal is to harden CI so key artifacts are checked against their corresponding schemas, not merely parsed as valid JSON.

## Validation Manifest

Validation targets are declared in:

```text
validation/artifact-validation-manifest.json
```

The manifest defines:

- expected-valid cases
- expected-invalid cases
- schema paths
- artifact paths
- artifact types
- expected failure reasons

This makes the validation scope reviewable without reading the validator implementation.

For details, see:

```text
docs/validation-manifest.md
```

For a reviewer-facing coverage table, see:

```text
docs/validation-coverage-index.md
```

## Validator

Reference script:

```text
reference-implementation/python/validate_artifact_schemas.py
```

The validator intentionally uses only the Python standard library.

It supports the subset of JSON Schema currently used by the repository:

- `type`
- `required`
- `properties`
- `additionalProperties: false`
- `enum`
- array `items`
- nullable type lists such as `["string", "null"]`
- local `$ref` entries into `#/$defs`

It is not a complete JSON Schema implementation.

## Validated Artifacts

The current manifest includes validation cases for:

- Decision Contract example
- Evaluator Policy example
- PASS and FAIL quantum-output examples
- PASS Execution Receipt example
- tampered-status Execution Receipt example
- PASS Verification Report example
- tampered-status Verification Report example
- Governance Boundary Map example
- Audit Package Manifest example

## Expected Invalid Case

The unsupported-operator contract is intentionally expected to fail the current Decision Contract schema because it uses:

```text
median_gte
```

That operator is not currently allowed by the schema.

This is intentional. The example exists to demonstrate `UNSUPPORTED_RECEIPT` behavior at the verifier boundary.

## Schema Validity vs Verification Validity

Some artifacts are expected to be schema-valid while still representing invalid verification outcomes.

Example:

```text
use-cases/quantum/examples/bell-state-receipt-tampered-status.json
```

This artifact has a valid Execution Receipt shape, but it should fail receipt verification because its declared status does not match the recomputed deterministic decision.

This distinction is important:

```text
Schema validation checks artifact shape.
Receipt verification checks claims against preserved evidence and deterministic replay.
```

## Boundary

Schema validation checks artifact shape.

It does not prove:

- upstream truth
- scientific correctness
- production readiness
- regulatory sufficiency
- total system safety

Schema validation is one layer in the evidence chain, not a replacement for verification or review.

## CI Role

The CI workflow now runs:

```bash
python reference-implementation/python/validate_artifact_schemas.py
```

This makes schema validation part of the repository's normal review path.
