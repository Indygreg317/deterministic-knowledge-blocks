# Receipt Verification Baseline

## Purpose

Execution Receipts are not treated as proof merely because they exist.

A receipt becomes useful only when it can be checked against preserved artifacts and deterministic evaluation rules.

This baseline introduces a reference verifier that recomputes the deterministic decision and compares the receipt against:

- the structured input artifact
- the Decision Contract
- the Evaluator Policy
- the recomputed deterministic outcome
- canonical artifact hashes
- declared receipt fields

## Verification Statuses

The reference verifier emits one of three statuses:

```text
VALID_RECEIPT
INVALID_RECEIPT
UNSUPPORTED_RECEIPT
```

### VALID_RECEIPT

The receipt matches the recomputed deterministic evaluation and all checked artifact references.

### INVALID_RECEIPT

The receipt is present, but one or more fields do not match the preserved artifacts or recomputed outcome.

Examples include:

- declared PASS when replay computes FAIL
- stale or placeholder input hash
- changed contract hash
- changed policy hash
- mismatched threshold
- mismatched evaluated fields
- mismatched output hash

### UNSUPPORTED_RECEIPT

The verifier cannot evaluate the receipt because the contract uses an unsupported operator or unsupported verification pattern.

Unsupported does not mean valid or invalid. It means this reference verifier cannot independently decide.

## Reference CLI

Verify the baseline PASS receipt:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json
```

Verify a known tamper case:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-tampered-status.json \
  --expect INVALID_RECEIPT
```

## Governance Boundary

This verifier does not prove that the upstream source system was deterministic.

It proves a narrower claim:

```text
Given the preserved input artifact, contract, and policy, the deterministic evaluation layer recomputes the same decision declared by the receipt.
```

That distinction matters.

Receipts should not collapse uncertainty into certainty. They should preserve the boundary between uncertain source outputs and governed downstream decisions.

## Why This Matters

A passive receipt says:

```text
A decision was recorded.
```

A verified receipt says:

```text
The recorded decision still matches the replayed deterministic rule under the referenced contract and policy.
```

That is the first step toward governed, replayable, receipt-backed AI and probabilistic-system evaluation.
