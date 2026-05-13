# Verification Reports

## Purpose

A Verification Report is a first-class evidence artifact produced when an Execution Receipt is checked against preserved artifacts and a recomputed deterministic outcome.

An Execution Receipt records a governed decision.

A Verification Report records whether that receipt still matches the preserved input artifact, Decision Contract, Evaluator Policy, and replayed deterministic result.

## Artifact Chain

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
```

## Verification Statuses

A report uses the same verification statuses introduced by the receipt verifier:

```text
VALID_RECEIPT
INVALID_RECEIPT
UNSUPPORTED_RECEIPT
```

### VALID_RECEIPT

The receipt matches the recomputed deterministic outcome and all checked artifact references.

### INVALID_RECEIPT

The receipt exists, but the verifier found one or more mismatches.

### UNSUPPORTED_RECEIPT

The verifier could not independently evaluate the receipt because the referenced contract or verification pattern is unsupported by the reference verifier.

## Required Report Fields

A Verification Report includes:

- `verification_id`
- `timestamp`
- `verification_status`
- `receipt_id`
- `verifier`
- `checked_artifacts`
- `checked_fields`
- `mismatches`
- `report_hash`

## Checked Artifacts

The `checked_artifacts` object records the canonical hashes used during verification:

```json
{
  "receipt_hash": "sha256:...",
  "input_hash": "sha256:...",
  "contract_hash": "sha256:...",
  "policy_hash": "sha256:..."
}
```

These hashes provide a stable reference to the artifacts checked during verification.

## Checked Fields

The baseline verifier checks:

```text
status
rule_version
input_hash
contract_hash
policy_hash
contract_id
policy_id
evaluated_fields
computed_value
threshold
output_hash
evaluator
```

## Mismatches

When verification fails, mismatches should explain the exact failure.

Example:

```text
status: expected 'PASS', found 'FAIL'
```

This is important because governance systems should not merely say that verification failed. They should explain where the claim broke.

## Report Hash

A report includes its own `report_hash`.

The report hash is computed by hashing the report content before `report_hash` is added.

This creates a stable identity for the report artifact itself.

## Reference CLI

Print a verification report:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json
```

Save a verification report artifact:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --save-report use-cases/quantum/examples/generated-verification-report.json
```

Verify a known-invalid receipt and save the resulting report:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-tampered-status.json \
  --expect INVALID_RECEIPT \
  --save-report use-cases/quantum/examples/generated-invalid-verification-report.json
```

## Governance Boundary

A Verification Report does not prove that the upstream source was deterministic, truthful, safe, or complete.

It proves a narrower claim:

```text
The verifier recomputed the deterministic evaluation and recorded whether the receipt matched the preserved artifacts and expected outcome.
```

This creates an explicit boundary between recorded claims and independently checked claims.

## Why This Matters

Without a Verification Report, the evidence chain ends at the receipt.

With a Verification Report, the evidence chain can say:

```text
The receipt was checked.
The verifier found these artifacts.
The verifier checked these fields.
The verifier recomputed this decision.
The verifier found these mismatches, or none.
```

That is the bridge from receipt logging to audit-ready verification evidence.
