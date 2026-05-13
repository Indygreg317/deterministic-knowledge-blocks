# Failure Mode Library

## Purpose

The failure mode library shows how deterministic receipt verification catches specific governance failures.

A strong governance system should not only show the happy path. It should show how claims fail, where they fail, and which artifact boundary detected the failure.

## Failure Modes Included

### Tampered Status

File:

```text
use-cases/quantum/examples/bell-state-receipt-tampered-status.json
```

Expected status:

```text
INVALID_RECEIPT
```

The receipt declares a status that does not match the recomputed deterministic decision.

### Tampered Threshold

File:

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json
```

Expected status:

```text
INVALID_RECEIPT
```

The receipt declares a threshold that no longer matches the referenced Decision Contract.

### Stale Contract Hash

File:

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-contract-hash.json
```

Expected status:

```text
INVALID_RECEIPT
```

The receipt points to a contract hash that does not match the preserved Decision Contract artifact.

### Stale Policy Hash

File:

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-policy-hash.json
```

Expected status:

```text
INVALID_RECEIPT
```

The receipt points to a policy hash that does not match the preserved Evaluator Policy artifact.

### Missing Input Hash

File:

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-missing-input-hash.json
```

Expected status:

```text
INVALID_RECEIPT
```

The receipt is missing the input artifact hash required to bind the decision to preserved evidence.

### Wrong Evaluator

File:

```text
use-cases/quantum/examples/failure-modes/bell-state-receipt-wrong-evaluator.json
```

Expected status:

```text
INVALID_RECEIPT
```

The receipt declares an evaluator identity that does not match the expected reference deterministic evaluator.

### Unsupported Operator

File:

```text
use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json
```

Expected status:

```text
UNSUPPORTED_RECEIPT
```

The verifier cannot independently evaluate the receipt because the contract uses an operator that the reference verifier does not support.

Unsupported is not valid. Unsupported is not invalid. Unsupported means the verifier cannot independently decide.

## Run the Failure Modes

Tampered threshold:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-tampered-threshold.json \
  --expect INVALID_RECEIPT
```

Stale contract hash:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-contract-hash.json \
  --expect INVALID_RECEIPT
```

Stale policy hash:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-stale-policy-hash.json \
  --expect INVALID_RECEIPT
```

Missing input hash:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-missing-input-hash.json \
  --expect INVALID_RECEIPT
```

Wrong evaluator:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/failure-modes/bell-state-receipt-wrong-evaluator.json \
  --expect INVALID_RECEIPT
```

Unsupported operator:

```bash
python reference-implementation/python/verify_receipt.py \
  --receipt use-cases/quantum/examples/bell-state-receipt-pass.json \
  --contract use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json \
  --expect UNSUPPORTED_RECEIPT
```

## Governance Value

The failure mode library demonstrates a key point:

```text
A receipt is not evidence because it exists.
A receipt becomes evidence when it survives deterministic verification.
```

This helps reviewers understand not only what the system accepts, but what it rejects and why.

## Boundary Discipline

Each failure mode is narrow on purpose.

The verifier does not claim the upstream quantum output is deterministic. It only checks whether the downstream receipt remains consistent with preserved artifacts and deterministic evaluation rules.

That boundary keeps the repo honest and makes the verification model easier to inspect.
