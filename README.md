# Deterministic Knowledge Blocks

Deterministic Knowledge Blocks are governed decision units for applying explicit, repeatable evaluation rules to uncertain or probabilistic inputs.

This repository provides a reference framework for converting structured uncertainty into auditable downstream decisions without pretending the source system itself has become deterministic.

> We do not make uncertain systems deterministic.  
> We make the evaluation layer deterministic, traceable, and auditable.

---

## Reviewer Start Here

For a fast review path, start with:

```text
docs/reviewer-handoff-index.md
```

The handoff index explains what to inspect first, what commands to run, what each artifact proves, and what remains outside the verification boundary.

---

## What This Repository Is

This repository is a reference architecture for deterministic evaluation around uncertain systems.

It demonstrates how to:

- capture uncertain outputs as structured input artifacts
- evaluate those artifacts through explicit Decision Contracts
- apply governed Evaluator Policies
- produce PASS / FAIL / ESCALATE decisions
- generate hash-linked Execution Receipts
- verify receipts against replayed deterministic outcomes
- produce Verification Reports as first-class evidence artifacts
- define canonical hashing rules for stable artifact identity
- demonstrate failure modes with executable negative tests
- map governance declarations against independently verifiable evidence boundaries
- package the evidence chain into reviewer-facing audit packages
- preserve auditability and replay boundaries

The initial working use case is quantum output evaluation, where probabilistic distributions are evaluated through deterministic downstream rules.

---

## What This Repository Is Not

This repository does not:

- make quantum systems deterministic
- eliminate uncertainty from AI or probabilistic systems
- provide production-ready safety infrastructure
- replace domain experts, medical experts, humanitarian experts, or safety reviewers
- authorize autonomous deployment in critical systems

It defines a controlled evaluation layer around uncertain outputs.

---

## Canonical Flow

```text
Input Signal
  ↓
Structured Input Artifact
  ↓
Canonical Artifact Hash
  ↓
Decision Contract
  ↓
Knowledge Block Constraints
  ↓
Evaluator Policy
  ↓
Deterministic Evaluation
  ↓
Authorization Decision
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
  ↓
Audit Record
```

---

## Quick Start

Run the reference evaluator from the repository root:

```bash
python reference-implementation/python/evaluate_decision_contract.py
```

This evaluates the default Bell-state PASS example.

Run the FAIL example:

```bash
python reference-implementation/python/evaluate_decision_contract.py \
  --output use-cases/quantum/examples/bell-state-output-fail.json
```

Compute a canonical artifact hash:

```bash
python reference-implementation/python/canonical_hash.py \
  examples/canonicalization/artifact-a.json
```

Run canonical hashing regression checks:

```bash
python reference-implementation/python/test_canonical_hashing.py
```

Verify the baseline PASS receipt:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json
```

Save a Verification Report artifact:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --save-report use-cases/quantum/examples/generated-verification-report.json
```

Review the Governance Boundary Map example:

```text
use-cases/quantum/examples/bell-state-governance-boundary-map.json
```

Review the minimal audit package:

```text
audit-packages/bell-state-minimal/
```

Verify a known tamper case:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-tampered-status.json \
  --expect INVALID_RECEIPT
```

Run a failure-mode example:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json \
  --expect INVALID_RECEIPT
```

The evaluator and verifier load:

```text
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-correlation-contract.json
use-cases/quantum/examples/evaluator-policy-basic.json
```

and emit structured execution and verification evidence.

---

## Reference Quantum Example

A probabilistic output may look like:

```text
00 = 0.48
01 = 0.02
10 = 0.01
11 = 0.49
```

A deterministic Decision Contract may define:

```text
Accept if P(00) + P(11) >= 0.95
```

The evaluator computes:

```text
0.48 + 0.49 = 0.97
```

Result:

```text
PASS
```

The source remains probabilistic. The evaluation rule is deterministic.

---

## Core Concepts

### Decision Contract

Defines what is being evaluated, which fields are in scope, what threshold applies, and which decision should be produced on pass or fail.

### Evaluator Policy

Defines allowed decisions, receipt requirements, failure behavior, review conditions, and audit behavior.

### Canonical Hash

A stable artifact identity generated by parsing JSON, sorting object keys, removing insignificant whitespace, preserving array order, and hashing the canonical UTF-8 bytes with SHA-256.

### Deterministic Outcome

A structured PASS / FAIL / ESCALATE result produced by applying explicit rules to a structured input artifact.

### Execution Receipt

A record of what was evaluated, which contract and policy applied, what decision was produced, and which hashes support replay or audit.

### Receipt Verification

A deterministic replay check that compares the receipt against preserved artifacts, canonical hashes, and the recomputed outcome.

### Verification Report

A structured evidence artifact that records what receipt was checked, which artifacts and fields were compared, what decision was recomputed, and which mismatches were found.

### Failure Mode Library

Executable negative examples that show how receipt verification detects tampered thresholds, stale hashes, missing input evidence, wrong evaluator identity, and unsupported contract logic.

### Governance Boundary Map

A structured map that separates what artifacts declare from what preserved evidence and deterministic verification can actually test.

### Audit Package

A reviewer-facing manifest that indexes the artifacts, commands, verification summary, and review boundaries needed to inspect a deterministic evaluation chain.

### Knowledge Block

A governed decision unit that binds inputs, constraints, contracts, runtime rules, receipts, verification reports, governance boundary maps, audit packages, and verification requirements into a reusable evaluation structure.

---

## Repository Structure

```text
.github/workflows/                  Validation workflows
audit-packages/                     Reviewer-facing audit package manifests and guides
docs/                               Architecture and governance documentation
schema/                             JSON Schema specifications
examples/canonicalization/          Canonical hashing examples
use-cases/quantum/examples/         Quantum decision-contract examples
use-cases/quantum/examples/failure-modes/
                                    Executable failure-mode examples
reference-implementation/python/    Minimal Python evaluator, verifier, and hashing utilities
assets/                             Diagrams and visuals
```

---

## Key Files

```text
schema/knowledge-block.schema.json
schema/deterministic-outcome.schema.json
schema/execution-receipt.schema.json
schema/verification-report.schema.json
schema/governance-boundary-map.schema.json
schema/audit-package-manifest.schema.json
schema/decision-contract.schema.json
schema/quantum-output.schema.json
schema/evaluator-policy.schema.json

docs/reviewer-handoff-index.md
docs/deterministic-evaluation.md
docs/decision-contracts.md
docs/replay-and-receipts.md
docs/receipt-verification.md
docs/verification-reports.md
docs/failure-mode-library.md
docs/governance-boundary-map.md
docs/audit-packages.md
docs/canonical-hashing.md
docs/canonical-flow.md

audit-packages/bell-state-minimal/README.md
audit-packages/bell-state-minimal/audit-package-manifest.json

examples/canonicalization/artifact-a.json
examples/canonicalization/artifact-b-reordered.json
examples/canonicalization/artifact-c-changed.json

use-cases/quantum/examples/bell-state-correlation-contract.json
use-cases/quantum/examples/evaluator-policy-basic.json
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-output-fail.json
use-cases/quantum/examples/bell-state-receipt-pass.json
use-cases/quantum/examples/bell-state-receipt-fail.json
use-cases/quantum/examples/bell-state-receipt-tampered-status.json
use-cases/quantum/examples/bell-state-verification-report-pass.json
use-cases/quantum/examples/bell-state-verification-report-tampered-status.json
use-cases/quantum/examples/bell-state-governance-boundary-map.json
use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json
use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-contract-hash.json
use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-policy-hash.json
use-cases/quantum/examples/failure-modes/bell-state-receipt-missing-input-hash.json
use-cases/quantum/examples/failure-modes/bell-state-receipt-wrong-evaluator.json
use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json

reference-implementation/python/canonical_hash.py
reference-implementation/python/test_canonical_hashing.py
reference-implementation/python/evaluate_decision_contract.py
reference-implementation/python/verify_receipt.py
```

---

## Validation

This repository includes a GitHub Actions workflow that:

- validates all JSON files parse correctly
- validates the audit package manifest
- validates the governance boundary map structure
- runs canonical hashing regression checks
- runs the reference evaluator against the PASS example
- runs the reference evaluator against the FAIL example
- verifies the valid receipt example
- verifies that the tampered receipt example fails verification
- generates a Verification Report artifact
- validates the failure-mode library

Workflow:

```text
.github/workflows/validate-json.yml
```

---

## Experimental Status

This framework is experimental.

It should not be used for:

- medical decisions
- humanitarian deployment
- safety-critical systems
- production quantum control
- autonomous execution

without expert validation, independent review, and operational oversight.

---

## AIPA Alignment

This project supports the broader AIPA mission of building:

- deterministic decision frameworks
- auditable computational pipelines
- governed AI systems
- runtime verification patterns
- transparent decision infrastructure

---

## License

Apache License 2.0
