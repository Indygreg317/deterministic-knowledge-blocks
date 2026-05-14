# Artifact Type Registry

## Purpose

This registry defines the artifact type names currently used across deterministic Knowledge Blocks documentation, manifests, validation coverage, boundary maps, and audit packages.

The goal is terminology consistency.

When possible, new manifests and examples should reuse these artifact type names instead of inventing nearby variants.

## Current Artifact Types

| Artifact type | Meaning | Primary schema | Primary example |
|---|---|---|---|
| `knowledge_block` | Governed decision unit that binds inputs, constraints, contracts, runtime rules, receipts, and verification requirements. | `schema/knowledge-block.schema.json` | Planned / baseline schema |
| `structured_input_artifact` | Preserved input submitted to deterministic evaluation. | Domain-specific schema, currently `schema/quantum-output.schema.json` | `use-cases/quantum/examples/bell-state-output-pass.json` |
| `decision_contract` | Artifact defining deterministic evaluation rule, target fields, operator, threshold, and outcome mapping. | `schema/decision-contract.schema.json` | `use-cases/quantum/examples/bell-state-correlation-contract.json` |
| `evaluator_policy` | Artifact defining allowed decisions, receipt requirements, review behavior, failure behavior, and audit behavior. | `schema/evaluator-policy.schema.json` | `use-cases/quantum/examples/evaluator-policy-basic.json` |
| `deterministic_outcome` | Structured output from deterministic evaluation. | `schema/deterministic-outcome.schema.json` | Reference evaluator output |
| `execution_receipt` | Artifact recording the claimed deterministic decision and supporting references. | `schema/execution-receipt.schema.json` | `use-cases/quantum/examples/bell-state-receipt-pass.json` |
| `verification_report` | Artifact recording receipt verification result, checked fields, checked artifacts, and mismatches. | `schema/verification-report.schema.json` | `use-cases/quantum/examples/bell-state-verification-report-pass.json` |
| `governance_boundary_map` | Artifact separating declarations from verifiable claims and out-of-scope claims. | `schema/governance-boundary-map.schema.json` | `use-cases/quantum/examples/bell-state-governance-boundary-map.json` |
| `audit_package_manifest` | Artifact indexing reviewer-facing evidence package contents and review boundaries. | `schema/audit-package-manifest.schema.json` | `audit-packages/bell-state-minimal/audit-package-manifest.json` |
| `artifact_validation_manifest` | Artifact declaring schema-validation cases and expected outcomes. | `schema/artifact-validation-manifest.schema.json` | `validation/artifact-validation-manifest.json` |
| `failure_mode_library` | Grouping of executable negative examples used to demonstrate invalid or unsupported behavior. | N/A | `use-cases/quantum/examples/failure-modes/` |

## Naming Rules

Use lowercase snake_case artifact type names:

```text
execution_receipt
verification_report
governance_boundary_map
```

Avoid title case, spaces, hyphens, or plural forms in machine-readable fields:

```text
Execution Receipt        avoid in machine fields
execution-receipt        avoid in machine fields
execution receipts       avoid in machine fields
execution_receipts       avoid unless referring to a collection
```

## Shape vs Truth Boundary

Artifact type names describe what kind of artifact something is.

They do not prove the artifact is true, valid, safe, or verified.

Example:

```text
artifact_type: execution_receipt
```

means the artifact is intended to be interpreted as an execution receipt.

It does not mean the receipt is verified.

A receipt becomes stronger evidence only when it survives receipt verification and is represented in a Verification Report.

## Current Usage Locations

Artifact type names appear in:

```text
validation/artifact-validation-manifest.json
use-cases/quantum/examples/bell-state-governance-boundary-map.json
audit-packages/bell-state-minimal/audit-package-manifest.json
docs/validation-coverage-index.md
docs/schema-catalog.md
```

## Extension Guidance

When adding a new artifact type:

1. Define its purpose.
2. Identify whether it has a schema.
3. Add an example artifact if possible.
4. Add it to this registry.
5. Add it to the schema catalog if it has a schema.
6. Add validation coverage if the artifact is machine-checkable.
7. Clarify what the artifact does not prove.

## Governance Boundary

The registry supports terminology consistency.

It does not replace schema validation, receipt verification, replay, or audit review.

It supports this narrower claim:

```text
The repository uses consistent names for artifact categories across reviewable evidence layers.
```
