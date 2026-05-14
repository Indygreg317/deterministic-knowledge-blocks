# Schema Validation Reports

## Purpose

A Schema Validation Report is a machine-readable evidence artifact produced by the artifact schema validator.

It records:

- which validation manifest was used
- which manifest schema was used
- whether manifest checks passed
- which artifact cases were checked
- which expected-valid cases passed
- which expected-invalid cases failed as expected
- summary counts
- failures, if any

## Report Schema

```text
schema/schema-validation-report.schema.json
```

## Validator Command

Generate a report from the repository root:

```bash
python reference-implementation/python/validate_artifact_schemas.py \
  --save-report /tmp/schema-validation-report.json
```

Run with an explicit manifest:

```bash
python reference-implementation/python/validate_artifact_schemas.py \
  --manifest validation/artifact-validation-manifest.json \
  --save-report /tmp/schema-validation-report.json
```

## Report Status

The report status is one of:

```text
VALIDATION_PASSED
VALIDATION_FAILED
```

A successful report means:

```text
The validation manifest passed its checks, all expected-valid artifact cases passed schema validation, and all expected-invalid artifact cases failed as expected.
```

It does not mean:

```text
The upstream system is truthful, safe, complete, scientifically correct, or production-ready.
```

## Summary Fields

The report includes summary counts:

```text
manifest_checks_passed
expected_valid_artifact_cases_passed
expected_invalid_artifact_cases_failed_as_expected
total_artifact_cases_checked
total_validation_checks_passed
```

These match the human-readable console summary.

## Evidence Value

The report turns schema validation from console output into a reusable evidence artifact.

That makes it easier to include schema validation results in:

- audit packages
- verifier handoff packages
- review records
- CI artifacts
- governance evidence chains

## Boundary

Schema Validation Reports check artifact shape and declared validation outcomes.

They do not replace:

- receipt verification
- deterministic replay
- governance boundary maps
- external review
- domain expert judgment

The narrow evidence claim is:

```text
The declared validation manifest and listed artifact cases were checked, and the results were recorded in a structured report.
```
