# Reviewer Handoff Index

## Purpose

This document is the recommended starting point for reviewers, partners, engineers, and external verifiers inspecting the deterministic Knowledge Blocks repository.

It explains what to look at first, what to run, what each artifact proves, and what remains outside the verification boundary.

## Five-Minute Review Path

Start here:

```text
README.md
```

Then inspect the minimal audit package:

```text
audit-packages/bell-state-minimal/README.md
audit-packages/bell-state-minimal/audit-package-manifest.json
```

Then review the core evidence artifacts:

```text
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-correlation-contract.json
use-cases/quantum/examples/evaluator-policy-basic.json
use-cases/quantum/examples/bell-state-receipt-pass.json
use-cases/quantum/examples/bell-state-verification-report-pass.json
use-cases/quantum/examples/bell-state-governance-boundary-map.json
```

Then inspect failure behavior:

```text
docs/failure-mode-library.md
use-cases/quantum/examples/failure-modes/
```

## Evidence Chain

```text
Structured Input Artifact
  ↓
Canonical Artifact Hash
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
  ↓
Audit Package
```

## What To Run

From the repository root:

### 1. Compute a canonical input hash

```bash
python reference-implementation/python/canonical_hash.py \
  use-cases/quantum/examples/bell-state-output-pass.json
```

### 2. Run the deterministic evaluator

```bash
python reference-implementation/python/evaluate_decision_contract.py \
  --output use-cases/quantum/examples/bell-state-output-pass.json
```

### 3. Verify the valid receipt

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --expect VALID_RECEIPT
```

### 4. Save a verification report

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --expect VALID_RECEIPT \
  --save-report /tmp/bell-state-verification-report.json
```

### 5. Run a known failure mode

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json \
  --expect INVALID_RECEIPT
```

### 6. Run an unsupported verification case

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --contract use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json \
  --expect UNSUPPORTED_RECEIPT
```

## What Each Artifact Proves

### Structured Input Artifact

Shows the preserved input submitted to the deterministic evaluation layer.

It can support artifact identity and field availability.

It does not prove upstream truth, completeness, or source determinism.

### Decision Contract

Shows the explicit rule used for deterministic evaluation.

It can support replay of the decision rule when the operator is supported.

It does not prove that the rule is optimal for every real-world setting.

### Evaluator Policy

Shows allowed outcomes, receipt behavior, review behavior, and audit behavior.

It can support policy identity and evaluator constraints.

It does not prove regulatory sufficiency by itself.

### Execution Receipt

Shows the decision that was claimed by the deterministic evaluator.

It can be checked against preserved artifacts and recomputed outcome.

It is not proof merely because it exists.

### Verification Report

Shows what the verifier checked, which artifacts were compared, what decision was recomputed, and what mismatches were found.

It can support reviewable evidence that the receipt was checked.

It does not prove that no other verifier could disagree.

### Governance Boundary Map

Shows what is declared, what is verifiable, and what remains outside scope.

It prevents governance claims from being overstated.

It does not replace external review.

### Audit Package

Organizes the evidence chain into a reviewer-facing package.

It helps reviewers reproduce and inspect the verification path.

It is not production certification.

## Expected Results

The valid Bell-state receipt should produce:

```text
VALID_RECEIPT
```

The tampered examples should produce:

```text
INVALID_RECEIPT
```

The unsupported operator example should produce:

```text
UNSUPPORTED_RECEIPT
```

## Core Boundary Statement

```text
The source may remain probabilistic.
The evaluation boundary is deterministic.
The receipt is evidence only if it survives verification.
The verification report records what was checked.
The governance boundary map prevents overclaiming.
The audit package organizes the evidence for review.
```

## Recommended Reviewer Questions

A reviewer should ask:

1. Can I identify the preserved input artifact?
2. Can I see the exact decision contract?
3. Can I see the evaluator policy?
4. Can I recompute the deterministic decision?
5. Can I verify the receipt?
6. Can I see what fails when the receipt is tampered?
7. Can I distinguish declarations from verified claims?
8. Can I inspect the audit package without needing hidden context?

## Handoff Summary

This repository is not trying to make uncertain systems deterministic.

It demonstrates a narrower and more useful governance pattern:

```text
Turn uncertain system outputs into governed, replayable, receipt-backed, verifier-checked decision evidence.
```
