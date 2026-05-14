# Validation Coverage Index

## Purpose

This index shows the current schema-validation coverage for deterministic Knowledge Blocks.

It maps each validation case to:

- artifact type
- schema path
- artifact path
- expected result
- reason for inclusion

The goal is to make validation coverage inspectable without requiring reviewers to read the Python validator or manually inspect the validation manifest.

## Source of Truth

Validation targets are declared in:

```text
validation/artifact-validation-manifest.json
```

The manifest is validated against:

```text
schema/artifact-validation-manifest.schema.json
```

The validator is:

```text
reference-implementation/python/validate_artifact_schemas.py
```

## Manifest Self-Validation

| Case | Schema | Artifact | Expected |
|---|---|---|---|
| artifact-validation-manifest | `schema/artifact-validation-manifest.schema.json` | `validation/artifact-validation-manifest.json` | valid |

This proves the validation manifest is not only reviewable JSON. It is schema-bound evidence configuration.

## Expected-Valid Coverage

| Case ID | Artifact Type | Schema | Artifact | Expected |
|---|---|---|---|---|
| decision-contract-bell-state | decision_contract | `schema/decision-contract.schema.json` | `use-cases/quantum/examples/bell-state-correlation-contract.json` | valid |
| evaluator-policy-basic | evaluator_policy | `schema/evaluator-policy.schema.json` | `use-cases/quantum/examples/evaluator-policy-basic.json` | valid |
| quantum-output-pass | structured_input_artifact | `schema/quantum-output.schema.json` | `use-cases/quantum/examples/bell-state-output-pass.json` | valid |
| quantum-output-fail | structured_input_artifact | `schema/quantum-output.schema.json` | `use-cases/quantum/examples/bell-state-output-fail.json` | valid |
| execution-receipt-pass | execution_receipt | `schema/execution-receipt.schema.json` | `use-cases/quantum/examples/bell-state-receipt-pass.json` | valid |
| execution-receipt-tampered-status | execution_receipt | `schema/execution-receipt.schema.json` | `use-cases/quantum/examples/bell-state-receipt-tampered-status.json` | valid shape |
| verification-report-pass | verification_report | `schema/verification-report.schema.json` | `use-cases/quantum/examples/bell-state-verification-report-pass.json` | valid |
| verification-report-tampered-status | verification_report | `schema/verification-report.schema.json` | `use-cases/quantum/examples/bell-state-verification-report-tampered-status.json` | valid shape |
| governance-boundary-map-bell-state | governance_boundary_map | `schema/governance-boundary-map.schema.json` | `use-cases/quantum/examples/bell-state-governance-boundary-map.json` | valid |
| audit-package-bell-state-minimal | audit_package_manifest | `schema/audit-package-manifest.schema.json` | `audit-packages/bell-state-minimal/audit-package-manifest.json` | valid |

## Expected-Invalid Coverage

| Case ID | Artifact Type | Schema | Artifact | Expected | Reason |
|---|---|---|---|---|---|
| unsupported-operator-contract | decision_contract | `schema/decision-contract.schema.json` | `use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json` | invalid | Uses `median_gte`, which is intentionally outside the allowed operator enum. |

## Important Distinction

Some artifacts are expected to be schema-valid even when they represent an invalid governance outcome.

Example:

```text
bell-state-receipt-tampered-status.json
```

This file is expected to be a valid `Execution Receipt` shape, but it is expected to fail receipt verification.

That distinction matters:

```text
Schema validation checks artifact shape.
Receipt verification checks artifact truth against preserved evidence and deterministic replay.
```

## Current Coverage Summary

```text
Manifest self-validation: 1
Expected-valid artifact cases: 10
Expected-invalid schema cases: 1
Total declared validation checks: 12
```

## Known Boundaries

Current validation coverage does not prove:

- upstream truth
- scientific correctness
- regulatory sufficiency
- total system safety
- production readiness
- semantic equivalence beyond the declared schema rules

It supports this narrower claim:

```text
The declared validation manifest and listed artifacts are checked against declared schemas, and expected-invalid cases fail for declared reasons.
```

## Next Coverage Candidates

Future validation coverage may include:

- external verifier handoff manifests
- schema-validation reports
- expanded audit package types
- additional domain examples
- artifact type registry conformance
- schema catalog consistency checks
