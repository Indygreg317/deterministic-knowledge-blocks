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

## Review Commands

From the repository root, compute the input artifact hash:

```bash
python reference-implementation/python/canonical_hash.py \
  use-cases/quantum/examples/bell-state-output-pass.json
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

It demonstrates the narrower governance claim:

```text
The preserved receipt can be checked against preserved artifacts and a recomputed deterministic decision.
```

That is the difference between passive audit logging and replayable verification evidence.
