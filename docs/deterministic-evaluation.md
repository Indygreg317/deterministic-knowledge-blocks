# Deterministic Evaluation

## Purpose

Deterministic evaluation is the controlled layer that sits between uncertain inputs and downstream decisions.

This repository does not claim that probabilistic systems become deterministic. Instead, it defines how outputs from uncertain systems are evaluated using explicit, repeatable, and auditable rules.

## Core Principle

> We do not make uncertain systems deterministic. We make the evaluation layer deterministic, traceable, and auditable.

## Evaluation Boundary

A source system may produce probabilistic, noisy, incomplete, or uncertain outputs. The deterministic layer begins only after that output is captured as a structured input artifact.

The evaluator then applies:

- a decision contract
- explicit constraints
- an evaluator policy
- allowed decision states
- receipt generation rules

## Decision States

The reference framework uses three decision states:

```text
PASS
FAIL
ESCALATE
```

`PASS` means the input satisfied the deterministic rule.

`FAIL` means the input did not satisfy the deterministic rule.

`ESCALATE` means the system should not make a final downstream decision without review.

## Why This Matters

AI, quantum, humanitarian, and operational systems often produce outputs that are not inherently deterministic. But organizations still need consistent ways to decide whether those outputs are acceptable for action.

Deterministic evaluation provides a governed decision surface without overstating certainty about the source system.
