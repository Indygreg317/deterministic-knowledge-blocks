# Governance Boundary Map

## Purpose

A Governance Boundary Map separates what an artifact declares from what an independent verifier can actually test.

This distinction is central to deterministic Knowledge Blocks:

```text
Governance artifacts make claims.
Verification artifacts test only claims supported by preserved evidence and deterministic replay.
```

## Why This Matters

A governance record may declare that a policy was followed, that authority was valid, or that a decision was produced correctly.

But a declaration is not the same thing as verification.

The Governance Boundary Map prevents the system from collapsing these layers:

```text
Declaration ≠ Verification
Receipt ≠ Proof
Valid transition ≠ Total system safety
```

## Artifact Roles

### Structured Input Artifact

Declares the preserved input submitted for deterministic downstream evaluation.

Verifiable claims may include:

- artifact content matches a declared hash
- referenced fields exist
- required fields can be read by the evaluator

Non-verifiable claims may include:

- upstream source was truthful
- upstream source was complete
- upstream source was deterministic

### Decision Contract

Declares the deterministic rule to be applied.

Verifiable claims may include:

- contract content matches a declared hash
- referenced operator is supported
- threshold and fields can be replayed

Non-verifiable claims may include:

- threshold is scientifically optimal
- contract covers every real-world risk

### Evaluator Policy

Declares allowed decisions, receipt behavior, review behavior, and failure behavior.

Verifiable claims may include:

- policy content matches a declared hash
- receipt-required behavior is visible in preserved artifacts

Non-verifiable claims may include:

- policy satisfies every external regulatory requirement

### Execution Receipt

Declares that a decision was produced under referenced artifacts.

Verifiable claims may include:

- receipt status matches recomputed decision
- receipt input hash matches preserved input
- receipt contract hash matches preserved contract
- receipt policy hash matches preserved policy
- receipt output hash matches receipt content

Non-verifiable claims may include:

- upstream source behaved honestly
- decision is safe for production deployment

### Verification Report

Declares what the verifier checked and what result it found.

Verifiable claims may include:

- report content can be canonically hashed
- report identifies checked artifacts
- report records checked fields and mismatches

Non-verifiable claims may include:

- no other verifier could disagree
- no external review is needed

## Boundary Pattern

The baseline boundary pattern is:

```text
Structured Input Artifact
  ↓
Decision Contract
  ↓
Evaluator Policy
  ↓
Execution Receipt
  ↓
Verification Report
```

At each transition, the map should ask:

```text
What is being declared?
What can be independently checked?
What remains outside the verification boundary?
```

## Verification Outcomes

The current receipt verification boundary supports:

```text
VALID_RECEIPT
INVALID_RECEIPT
UNSUPPORTED_RECEIPT
```

These outcomes are intentionally narrow.

They do not claim total system safety. They claim whether the receipt survived deterministic verification under preserved artifacts and supported rules.

## External Verifier Handoff

A Governance Boundary Map can also support external verification systems.

The map gives an external verifier a clear interface:

- which artifacts exist
- which claims are declared
- which claims are checkable
- which claims are outside scope
- which verification outcomes are expected

This allows the governance system and the verifier to remain separate.

That separation is important:

```text
The system that declares a governance claim should not automatically be treated as the final authority on whether the claim is true.
```

## Bell-State Example

Example file:

```text
use-cases/quantum/examples/bell-state-governance-boundary-map.json
```

The Bell-state boundary map separates:

- structured probabilistic output
- deterministic decision contract
- evaluator policy
- execution receipt
- verification report

It makes clear that a valid receipt does not prove the upstream source was deterministic, truthful, safe, or complete.

It proves a narrower claim:

```text
The receipt matched preserved artifacts and the recomputed deterministic decision under a supported verification rule.
```

## Governance Value

Boundary maps make the repository more inspectable.

They show reviewers where trust is declared, where evidence is checked, and where uncertainty remains.

That is the difference between passive governance paperwork and verifier-ready governance infrastructure.
