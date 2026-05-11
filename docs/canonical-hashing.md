# Canonical Hashing

## Purpose

Deterministic replay and verification depend on stable hashing behavior.

This document defines the canonical hashing assumptions used by the reference framework.

## Core Principle

Equivalent structured artifacts should produce equivalent hashes when evaluated under the same canonicalization rules.

## Canonicalization Rules

The reference implementation currently:

- sorts JSON object keys
- removes formatting ambiguity
- uses UTF-8 encoding
- hashes canonicalized JSON bytes
- uses SHA-256 hashing

Reference implementation:

```text
json.dumps(..., sort_keys=True, separators=(",", ":"))
```

## Current Hash Types

### Input Hash

Hash of the structured input artifact used for deterministic evaluation.

### Output Hash

Hash of the generated execution receipt.

## Important Boundary

Hashes verify artifact consistency.

They do not verify:

- physical truth
- source-system correctness
- quantum state validity
- model honesty
- sensor integrity

Hashes only verify that the referenced structured artifact remained unchanged under the defined canonicalization rules.

## Replay Relationship

Replay verification depends on:

- preserved structured inputs
- preserved contracts
- preserved evaluator policies
- preserved evaluation logic
- stable canonicalization behavior

If these conditions remain stable, deterministic replay should produce matching downstream evaluation results.

## Future Expansion

Future versions may formalize:

- field exclusion rules
- timestamp handling rules
- detached signatures
- multi-artifact receipt chains
- canonical receipt hashing standards
- cross-system verification boundaries
