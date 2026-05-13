# Examples Index

## Purpose

This index helps reviewers find the repository's runnable examples, evidence artifacts, failure modes, and audit package entry points.

## Primary Bell-State Example

### Structured Input Artifact

```text
use-cases/quantum/examples/bell-state-output-pass.json
```

Role:

```text
Preserved probabilistic output submitted for deterministic downstream evaluation.
```

### Decision Contract

```text
use-cases/quantum/examples/bell-state-correlation-contract.json
```

Role:

```text
Defines the deterministic rule: accept when P(00) + P(11) >= 0.95.
```

### Evaluator Policy

```text
use-cases/quantum/examples/evaluator-policy-basic.json
```

Role:

```text
Defines allowed decisions, receipt behavior, review behavior, and audit behavior.
```

### Execution Receipt

```text
use-cases/quantum/examples/bell-state-receipt-pass.json
```

Role:

```text
Records the claimed PASS decision and referenced artifact hashes.
```

### Verification Report

```text
use-cases/quantum/examples/bell-state-verification-report-pass.json
```

Role:

```text
Records that the receipt was checked and verified as VALID_RECEIPT.
```

### Governance Boundary Map

```text
use-cases/quantum/examples/bell-state-governance-boundary-map.json
```

Role:

```text
Maps what each artifact declares, what can be verified, and what remains outside scope.
```

## Failure Mode Examples

### Tampered Status

```text
use-cases/quantum/examples/bell-state-receipt-tampered-status.json
```

Expected result:

```text
INVALID_RECEIPT
```

### Tampered Threshold

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json
```

Expected result:

```text
INVALID_RECEIPT
```

### Stale Contract Hash

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-contract-hash.json
```

Expected result:

```text
INVALID_RECEIPT
```

### Stale Policy Hash

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-policy-hash.json
```

Expected result:

```text
INVALID_RECEIPT
```

### Missing Input Hash

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-missing-input-hash.json
```

Expected result:

```text
INVALID_RECEIPT
```

### Wrong Evaluator Identity

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-wrong-evaluator.json
```

Expected result:

```text
INVALID_RECEIPT
```

### Unsupported Operator

```text
use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json
```

Expected result when used with the reference verifier:

```text
UNSUPPORTED_RECEIPT
```

## Canonicalization Examples

### Same Artifact, Original Key Order

```text
examples/canonicalization/artifact-a.json
```

### Same Artifact, Reordered Keys

```text
examples/canonicalization/artifact-b-reordered.json
```

Expected result:

```text
artifact-a and artifact-b-reordered produce the same canonical hash.
```

### Changed Artifact

```text
examples/canonicalization/artifact-c-changed.json
```

Expected result:

```text
artifact-c-changed produces a different canonical hash.
```

## Audit Package

### Minimal Audit Package

```text
audit-packages/bell-state-minimal/
```

Includes:

```text
audit-package-manifest.json
README.md
```

Role:

```text
Reviewer-facing entry point for inspecting the full evidence chain.
```

## Recommended First Run

From the repository root:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --expect VALID_RECEIPT
```

Then run a failure case:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json \
  --expect INVALID_RECEIPT
```
