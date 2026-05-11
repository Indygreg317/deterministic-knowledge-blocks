# Boundaries and Limitations

## Purpose

This document defines what the Deterministic Knowledge Blocks reference framework verifies, what it does not verify, and where uncertainty remains.

Clear boundaries are essential for trustworthy governance architectures.

## What This Framework Verifies

This framework can verify that:

- a structured input artifact was evaluated under an explicit Decision Contract
- an Evaluator Policy was applied to the evaluation process
- a deterministic outcome was produced from defined rules
- an Execution Receipt records the evaluation event
- replay can recompute the same deterministic result when artifacts and logic remain unchanged
- hashes can detect changes to preserved artifacts under defined canonicalization rules

## What This Framework Does Not Verify

This framework does not verify:

- physical truth
- moral correctness
- medical validity
- humanitarian intervention correctness
- quantum state truth
- source-system honesty
- sensor integrity
- model intent
- organizational approval legitimacy
- legal compliance by itself

It verifies deterministic evaluation behavior around preserved artifacts.

It does not prove that the upstream world, model, system, or institution was correct.

## Source Uncertainty Remains

A probabilistic or uncertain source remains probabilistic or uncertain.

The deterministic layer begins only after the source output has been captured as a structured input artifact.

```text
Source uncertainty
  ↓
Structured artifact
  ↓
Deterministic evaluation
```

The evaluation can be repeatable even when the original source process is not.

## Replay Boundary

Replay verifies whether the deterministic evaluation can be reproduced from preserved artifacts.

Replay does not prove:

- the original measurement was accurate
- the original model was aligned
- the original source system was safe
- the original real-world condition was true

Replay only proves that the preserved artifact, contract, policy, and evaluator can produce the same deterministic result.

## Hash Boundary

Hashes verify artifact consistency under canonicalization rules.

Hashes do not verify semantic truth.

A hash can show that an artifact changed or stayed the same.

It cannot prove that the artifact was truthful, complete, lawful, ethical, or safe.

## Human and Institutional Oversight

This framework does not replace human review.

For high-impact domains, review by qualified professionals remains necessary, especially in:

- healthcare
- humanitarian intervention
- safety-critical systems
- legal compliance
- financial decisions
- autonomous operations

## External Verification Boundary

External verifiers may independently inspect receipts, hashes, replay outputs, policy fingerprints, or governance records.

Those external results should remain distinguishable from the original deterministic evaluation artifact.

Boundary mapping should not become trust-surface merger.

## Experimental Status

This repository is experimental.

It is intended for research, architecture exploration, and reference implementation work.

Production use requires independent validation, domain review, security review, and operational governance controls.
