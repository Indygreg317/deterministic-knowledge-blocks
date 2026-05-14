# Artifact Validation Manifest

## Purpose

The artifact validation manifest declares which repository artifacts are checked against which schemas.

This moves validation targets out of hidden script constants and into reviewable repository evidence.

Manifest:

```text
validation/artifact-validation-manifest.json
```

Validator:

```text
reference-implementation/python/validate_artifact_schemas.py
```

## Why This Matters

Before this manifest, schema validation targets were defined inside the Python validator.

That worked, but reviewers had to inspect implementation code to see what was being validated.

The manifest makes the validation scope explicit:

```text
schema path
artifact path
artifact type
expected-valid cases
expected-invalid cases
expected failure reasons
```

## Valid Cases

`valid_cases` are artifacts expected to satisfy their declared schemas.

Examples include:

- Decision Contract
- Evaluator Policy
- Quantum Output
- Execution Receipt
- Verification Report
- Governance Boundary Map
- Audit Package Manifest

## Expected Invalid Cases

`expected_invalid_cases` are artifacts that intentionally fail schema validation.

The current example is:

```text
unsupported-operator-contract
```

It uses:

```text
median_gte
```

That operator is intentionally outside the current Decision Contract schema.

This preserves the failure-mode boundary:

```text
unsupported operator -> UNSUPPORTED_RECEIPT
```

## Run Validation

From the repository root:

```bash
python reference-implementation/python/validate_artifact_schemas.py
```

Run with an explicit manifest:

```bash
python reference-implementation/python/validate_artifact_schemas.py \
  --manifest validation/artifact-validation-manifest.json
```

## Governance Boundary

The manifest declares what the schema validator checks.

It does not prove:

- upstream truth
- scientific correctness
- regulatory sufficiency
- production readiness
- total system safety

It supports a narrower claim:

```text
These declared artifacts were checked against these declared schemas, and expected-invalid cases failed for declared reasons.
```

## Evidence Value

The manifest makes schema validation reviewable, portable, and easier to extend.

Future PRs can add validation coverage by editing a manifest entry instead of changing validator internals.
