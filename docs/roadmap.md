# Roadmap

## Purpose

This roadmap describes likely next layers for the deterministic Knowledge Blocks reference framework.

It is not a promise of production readiness. It is a public direction of travel for reviewers, contributors, partners, and external verifier discussions.

## Current Baseline

The current repository demonstrates:

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
  ↓
Governance Boundary Map
  ↓
Audit Package
```

## Near-Term Priorities

### 1. Schema Validation Hardening

Add formal JSON Schema validation for key artifacts in CI:

- Decision Contracts
- Evaluator Policies
- Execution Receipts
- Verification Reports
- Governance Boundary Maps
- Audit Package Manifests

Current CI validates JSON parsing and selected structural expectations. The next step is full schema-based validation.

### 2. Verification Report Regeneration Tests

Add tests that regenerate verification reports from receipts and compare expected fields.

This would strengthen the chain:

```text
receipt -> verifier -> report -> report hash
```

### 3. Audit Package Expansion

Expand the minimal audit package into richer package variants:

- compact package
- full package
- external verifier handoff package
- failure-mode package

### 4. Additional Domain Examples

Add examples beyond the Bell-state reference case.

Candidate domains:

- model output policy checks
- data quality gates
- compliance rule checks
- human review routing
- safety escalation thresholds

The goal is to show the same governance pattern across domains without overstating production readiness.

### 5. External Verifier Handoff

Define a package format for external verifiers.

A verifier handoff package should include:

- preserved artifacts
- canonical hashes
- expected verification boundary
- supported outcomes
- failure behavior
- boundary map
- audit package manifest

### 6. Cross-Language Reference Implementations

Add additional minimal verifiers in other languages after the Python reference implementation stabilizes.

Possible future targets:

- JavaScript / TypeScript
- Go
- Rust

### 7. Signing and Attestation Layer

Explore optional signing for receipts, reports, and audit packages.

This should be added carefully. Signatures should not collapse the distinction between:

```text
artifact authenticity
and
claim validity
```

A signed false claim is still false.

### 8. Governance Studio Compatibility

Prepare artifacts so they can later be rendered, reviewed, or assembled by a governance studio interface.

Potential interface functions:

- inspect artifact chain
- compare hashes
- replay verification
- show mismatch details
- export audit package
- display boundary map

## Long-Term Direction

The long-term direction is a verifier-ready governance artifact stack:

```text
Knowledge Block
Decision Contract
Evaluator Policy
Execution Receipt
Verification Report
Governance Boundary Map
Audit Package
External Verifier Handoff
```

The goal is not to make uncertain systems deterministic.

The goal is to make governance claims inspectable, replayable, and bounded.

## Non-Goals

This roadmap does not claim the repository will become:

- a universal AI safety system
- a complete compliance platform
- a replacement for domain experts
- a replacement for external audit
- a proof that upstream systems are truthful, safe, or deterministic

## Guiding Principle

```text
Do not overclaim.
Preserve the boundary.
Make evidence replayable.
Make failures inspectable.
Make review easier.
```
