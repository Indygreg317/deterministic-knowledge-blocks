# Python Reference Evaluator

## Purpose

This reference implementation demonstrates how a deterministic evaluation layer can be applied to probabilistic quantum-style outputs.

The evaluator:

- loads a probabilistic output distribution
- applies a deterministic decision contract
- evaluates the output against explicit constraints
- generates a deterministic PASS / FAIL decision
- emits a structured execution receipt

This does not make the source system deterministic.

It makes the downstream evaluation layer deterministic, traceable, and auditable.

---

## Run the Reference Example

From the repository root:

```bash
python reference-implementation/python/evaluate_decision_contract.py
```

The default execution path evaluates the Bell-state reference output against the Bell-state decision contract using the basic evaluator policy.

---

## Reference Flow

```text
Probabilistic Output
  ↓
Decision Contract
  ↓
Deterministic Evaluation
  ↓
Execution Receipt
  ↓
Audit Record
```
