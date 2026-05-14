# Verification Evidence Index

## Purpose

Deterministic governance requires reviewable evidence, not just claims.

This index helps readers locate the artifacts that support verification, replay, receipt inspection, evaluator behavior, governance boundary review, validation coverage, and audit-package inspection.

It is intentionally conservative. If a category is not present in the repository, it is marked as `Planned` rather than treated as existing evidence.

## Evidence Categories

| Evidence category | Purpose | Expected location | Status | Notes |
| --- | --- | --- | --- | --- |
| Decision contracts | Define explicit deterministic evaluation rules. | `schema/decision-contract.schema.json`; `use-cases/quantum/examples/bell-state-correlation-contract.json`; `docs/decision-contracts.md` | Present | Bell-state example uses `P(00) + P(11) >= 0.95`. |
| Evaluator policies | Define allowed outcomes, receipt behavior, review behavior, and audit behavior. | `schema/evaluator-policy.schema.json`; `use-cases/quantum/examples/evaluator-policy-basic.json` | Present | Supports governed evaluator constraints. |
| Execution receipts | Record claimed evaluation decisions and supporting artifact hashes. | `schema/execution-receipt.schema.json`; `use-cases/quantum/examples/bell-state-receipt-pass.json`; `use-cases/quantum/examples/bell-state-receipt-fail.json` | Present | Receipts are evidence only after verification. |
| Canonical hash examples | Demonstrate stable JSON artifact identity. | `docs/canonical-hashing.md`; `reference-implementation/python/canonical_hash.py`; `examples/canonicalization/artifact-a.json`; `examples/canonicalization/artifact-b-reordered.json`; `examples/canonicalization/artifact-c-changed.json` | Present | Reordered object keys should hash identically; changed content should not. |
| Replay verification examples | Show deterministic recomputation against preserved artifacts. | `docs/receipt-verification.md`; `reference-implementation/python/verify_receipt.py`; `docs/replay-and-receipts.md` | Present | Verifier checks preserved artifacts, hashes, and recomputed outcomes. |
| PASS examples | Show accepted deterministic evaluation outcomes. | `use-cases/quantum/examples/bell-state-output-pass.json`; `use-cases/quantum/examples/bell-state-receipt-pass.json`; `use-cases/quantum/examples/bell-state-verification-report-pass.json` | Present | Baseline successful Bell-state path. |
| FAIL examples | Show rejected deterministic evaluation outcomes. | `use-cases/quantum/examples/bell-state-output-fail.json`; `use-cases/quantum/examples/bell-state-receipt-fail.json` | Present | Demonstrates deterministic fail behavior. |
| ESCALATE examples | Show review-required evaluator outcomes. | Planned | Planned | Outcome is supported conceptually in the repository language, but a dedicated executable example is not yet present. |
| UNSUPPORTED examples | Show unsupported verification behavior. | `use-cases/quantum/examples/failure-modes/bell-state-unsupported-operator-contract.json` | Present | Used with the verifier to produce `UNSUPPORTED_RECEIPT`. |
| Schema definitions | Define structured artifact expectations. | `schema/knowledge-block.schema.json`; `schema/deterministic-outcome.schema.json`; `schema/execution-receipt.schema.json`; `schema/verification-report.schema.json`; `schema/governance-boundary-map.schema.json`; `schema/audit-package-manifest.schema.json`; `schema/artifact-validation-manifest.schema.json`; `schema/decision-contract.schema.json`; `schema/quantum-output.schema.json`; `schema/evaluator-policy.schema.json` | Present | Schemas make artifacts reviewable and machine-checkable. |
| Schema validation manifest | Declares which artifacts are checked against which schemas. | `validation/artifact-validation-manifest.json`; `docs/validation-manifest.md` | Present | Manifest is itself schema-validated before artifact cases are checked. |
| Validation coverage index | Maps schema-validation cases to schemas, artifacts, expected outcomes, and reasons. | `docs/validation-coverage-index.md` | Present | Reviewer-facing coverage map for expected-valid and expected-invalid validation cases. |
| Test cases | Demonstrate executable verification behavior. | `reference-implementation/python/test_canonical_hashing.py`; `reference-implementation/python/validate_artifact_schemas.py`; `.github/workflows/validate-json.yml` | Present | CI and reference scripts provide baseline checks. |
| Governance record examples | Declare scope, authority, policy, or continuity assumptions. | Planned | Planned | Governance record artifacts are planned as a future layer. |
| Verification boundary maps | Separate declarations from independently checkable evidence. | `schema/governance-boundary-map.schema.json`; `docs/governance-boundary-map.md`; `use-cases/quantum/examples/bell-state-governance-boundary-map.json` | Present | Prevents receipts and governance records from being overclaimed. |
| Audit package examples | Bundle evidence into reviewer-facing inspection paths. | `schema/audit-package-manifest.schema.json`; `docs/audit-packages.md`; `audit-packages/bell-state-minimal/README.md`; `audit-packages/bell-state-minimal/audit-package-manifest.json` | Present | Minimal package indexes the current Bell-state evidence chain. |
| Evidence manifest | Machine-readable index of evidence categories and artifact paths. | Planned | Planned | Future upgrade for structured evidence discovery. |

## What Counts as Evidence

Evidence is a reviewable artifact that helps another person or verifier determine:

- what happened
- what input was preserved
- what rule applied
- what policy constrained the rule
- what result was produced
- what hashes or references support artifact identity
- whether the result can be reproduced, challenged, or rejected

Examples of valid evidence include:

- a schema that defines required fields
- a fixture with an expected deterministic output
- a test that proves PASS behavior
- a test that proves FAIL behavior
- a receipt with evaluator version and input references
- a canonical hash example with stable reconstruction inputs
- a replay example with an expected outcome
- a verification report that records checked fields and mismatches
- a validation manifest that declares expected-valid and expected-invalid schema checks
- a validation coverage index that maps schema checks to artifacts and expected outcomes
- a governance boundary map that separates declarations from verified claims

## What Does Not Count as Evidence

The following are not sufficient verification evidence by themselves:

- marketing language
- undocumented claims
- screenshots without source data
- unverifiable declarations
- vague success statements
- unsupported trust assertions
- claims that a system is safe, compliant, or deterministic without preserved artifacts and replayable checks

## Evidence Quality Levels

| Level | Name | Meaning |
| --- | --- | --- |
| Level 0 | Claim only | A statement exists, but no supporting artifact is provided. |
| Level 1 | Documented claim | The claim is explained in documentation, but not yet structured as evidence. |
| Level 2 | Structured artifact | The claim is represented in a schema, fixture, receipt, report, or manifest. |
| Level 3 | Tested artifact | The artifact is exercised by a script, check, or CI workflow. |
| Level 4 | Reproducible verification path | A reviewer can rerun the check and reproduce the expected outcome. |
| Level 5 | Independently falsifiable verification boundary | A verifier can reject the claim using preserved evidence without trusting the originating system. |

The repository should gradually move evidence from lower levels toward higher levels.

## Reviewer Use

A reviewer can use this index to:

1. Find the artifact category.
2. Check the actual file path.
3. Confirm whether the example is present or planned.
4. Review the schema, test, example, or documentation.
5. Confirm whether the outcome is deterministic.
6. Confirm whether the evidence supports the claim being made.
7. Identify which claims remain outside the verification boundary.

## Future Work

Future verification evidence upgrades may include:

- additional negative examples
- dedicated ESCALATE examples
- replay fixtures
- machine-readable evidence manifests
- governance record examples
- verification boundary examples across additional use cases
- audit package examples beyond the Bell-state package
- stronger CI checks for evidence path consistency
