# Bell-State Minimal Audit Package

## Purpose

This package gives reviewers one place to inspect the complete deterministic Knowledge Block evidence chain for the Bell-state reference example.

It is intentionally minimal. The package does not duplicate every artifact. Instead, it provides a manifest that points to the preserved repository artifacts needed for review.

## Package Manifest

```text
audit-packages/bell-state-minimal/audit-package-manifest.json
```

The manifest indexes:

- structured input artifact
- Decision Contract
- Evaluator Policy
- Execution Receipt
- Verification Report
- Schema Validation Report
- Governance Boundary Map
- optional failure-mode examples

## Review Flow

```text
Structured Input Artifact
  ↓
Decision Contract
  ↓
Evaluator Policy
  ↓
Schema Validation Report
  ↓
Deterministic Evaluation
  ↓
Execution Receipt
  ↓
Receipt Verification
  ↓
Verification Report
  ↓
Governance Boundary Map
```

## Schema Validation Evidence

The audit package indexes the persisted schema validation report:

```text
validation/reports/schema-validation-report.json
```

That report records manifest checks, artifact schema case results, expected-invalid behavior, summary counts, and failures if present.

This evidence supports the narrow claim that declared artifact shapes and declared validation outcomes were checked. It does not prove upstream truth, scientific correctness, regulatory sufficiency, production readiness, or total system safety.

## Review Commands

From the repository root, compute the input artifact hash:

```bash
python reference-implementation/python/canonical_hash.py \
  use-cases/quantum/examples/bell-state-output-pass.json
```

Regenerate a schema validation report for comparison:

```bash
python reference-implementation/python/validate_artifact_schemas.py \
  --manifest validation/artifact-validation-manifest.json \
  --save-report /tmp/schema-validation-report.json
```

Run the deterministic evaluator:

```bash
python reference-implementation/python/evaluate_decision_contract.py \
  --output use-cases/quantum/examples/bell-state-output-pass.json
```

Verify the valid receipt:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --expect VALID_RECEIPT
```

Run a failure-mode example:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json \
  --expect INVALID_RECEIPT
```

## Boundary Note

This package does not prove that the upstream quantum source was deterministic, truthful, safe, or complete.

It demonstrates two narrower governance claims:

```text
The declared artifact shapes and validation outcomes can be inspected through the schema validation report.

The preserved receipt can be checked against preserved artifacts and a recomputed deterministic decision.
```

That is the difference between passive audit logging and replayable verification evidence.
