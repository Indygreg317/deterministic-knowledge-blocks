# Schema Catalog

## Purpose

This catalog lists the schemas currently used by deterministic Knowledge Blocks and explains what each schema governs.

It is intended for reviewers, contributors, partners, and external verifiers who need a quick map of the repository's structured artifact layer.

## Schema Summary

| Schema | Governs | Primary example | Evidence role |
|---|---|---|---|
| `schema/knowledge-block.schema.json` | Knowledge Block structure | Planned / baseline schema | Defines governed decision unit structure. |
| `schema/deterministic-outcome.schema.json` | Deterministic outcome shape | Reference evaluator output | Defines PASS / FAIL / ESCALATE style outcome structure. |
| `schema/decision-contract.schema.json` | Decision Contract artifacts | `use-cases/quantum/examples/bell-state-correlation-contract.json` | Defines deterministic rule, operator, threshold, and decision mapping. |
| `schema/evaluator-policy.schema.json` | Evaluator Policy artifacts | `use-cases/quantum/examples/evaluator-policy-basic.json` | Defines allowed decisions, receipt requirements, review behavior, and audit behavior. |
| `schema/quantum-output.schema.json` | Quantum-output-style structured input artifacts | `use-cases/quantum/examples/bell-state-output-pass.json` | Defines preserved probabilistic input shape for the Bell-state example. |
| `schema/execution-receipt.schema.json` | Execution Receipt artifacts | `use-cases/quantum/examples/bell-state-receipt-pass.json` | Defines claimed decision record and supporting artifact references. |
| `schema/verification-report.schema.json` | Verification Report artifacts | `use-cases/quantum/examples/bell-state-verification-report-pass.json` | Defines verifier output, checked fields, checked artifacts, mismatches, and report hash. |
| `schema/governance-record.schema.json` | Governance Record artifacts | Planned | Defines declaration artifact shape for scope, authority context, policy references, continuity assumptions, linked evidence, and boundary statements. |
| `schema/governance-boundary-map.schema.json` | Governance Boundary Map artifacts | `use-cases/quantum/examples/bell-state-governance-boundary-map.json` | Separates declared claims from independently verifiable claims. |
| `schema/audit-package-manifest.schema.json` | Audit Package manifests | `audit-packages/bell-state-minimal/audit-package-manifest.json` | Defines reviewer-facing bundle of evidence references and review boundaries. |
| `schema/artifact-validation-manifest.schema.json` | Artifact Validation Manifest | `validation/artifact-validation-manifest.json` | Defines schema-validation coverage configuration. |
| `schema/schema-validation-report.schema.json` | Schema Validation Report | `validation/reports/schema-validation-report.json` | Defines machine-readable schema validation result evidence. |

## Artifact Flow Coverage

The schema layer supports the current evidence chain:

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
Governance Record
  ↓
Governance Boundary Map
  ↓
Audit Package Manifest
  ↓
Artifact Validation Manifest
```

## Schema Roles

### Knowledge Block Schema

Path:

```text
schema/knowledge-block.schema.json
```

Role:

```text
Defines the reusable governed decision unit abstraction.
```

Current maturity:

```text
Baseline schema / reference structure
```

### Deterministic Outcome Schema

Path:

```text
schema/deterministic-outcome.schema.json
```

Role:

```text
Defines structured output from deterministic evaluation.
```

Current maturity:

```text
Reference schema for evaluator output
```

### Decision Contract Schema

Path:

```text
schema/decision-contract.schema.json
```

Role:

```text
Defines deterministic evaluation rule configuration.
```

Primary example:

```text
use-cases/quantum/examples/bell-state-correlation-contract.json
```

Important note:

```text
Unsupported operators should fail this schema unless deliberately added to the allowed operator set.
```

### Evaluator Policy Schema

Path:

```text
schema/evaluator-policy.schema.json
```

Role:

```text
Defines allowed decisions, receipt behavior, review behavior, and audit behavior.
```

Primary example:

```text
use-cases/quantum/examples/evaluator-policy-basic.json
```

### Quantum Output Schema

Path:

```text
schema/quantum-output.schema.json
```

Role:

```text
Defines the structured input artifact used by the Bell-state example.
```

Primary examples:

```text
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-output-fail.json
```

### Execution Receipt Schema

Path:

```text
schema/execution-receipt.schema.json
```

Role:

```text
Defines claimed deterministic evaluation receipt structure.
```

Primary examples:

```text
use-cases/quantum/examples/bell-state-receipt-pass.json
use-cases/quantum/examples/bell-state-receipt-tampered-status.json
```

Important distinction:

```text
A receipt can be schema-valid while still failing receipt verification.
```

### Verification Report Schema

Path:

```text
schema/verification-report.schema.json
```

Role:

```text
Defines the verifier's structured report artifact.
```

Primary examples:

```text
use-cases/quantum/examples/bell-state-verification-report-pass.json
use-cases/quantum/examples/bell-state-verification-report-tampered-status.json
```

### Governance Record Schema

Path:

```text
schema/governance-record.schema.json
```

Role:

```text
Defines declaration artifact shape for governance context and linked evidence references.
```

Primary example:

```text
Planned
```

Important distinction:

```text
A governance record can be schema-valid while its declared authority, policy, continuity, or scope assumptions remain unverified.
```

### Governance Boundary Map Schema

Path:

```text
schema/governance-boundary-map.schema.json
```

Role:

```text
Defines declaration-vs-verification boundary mapping.
```

Primary example:

```text
use-cases/quantum/examples/bell-state-governance-boundary-map.json
```

### Audit Package Manifest Schema

Path:

```text
schema/audit-package-manifest.schema.json
```

Role:

```text
Defines reviewer-facing audit package manifest structure.
```

Primary example:

```text
audit-packages/bell-state-minimal/audit-package-manifest.json
```

### Artifact Validation Manifest Schema

Path:

```text
schema/artifact-validation-manifest.schema.json
```

Role:

```text
Defines the validation manifest used to declare schema-validation coverage.
```

Primary example:

```text
validation/artifact-validation-manifest.json
```

### Schema Validation Report Schema

Path:

```text
schema/schema-validation-report.schema.json
```

Role:

```text
Defines machine-readable schema validation result evidence.
```

Primary example:

```text
validation/reports/schema-validation-report.json
```

## Validation Relationship

Schema validation currently follows this path:

```text
artifact-validation-manifest.schema.json
  ↓
artifact-validation-manifest.json
  ↓
listed schema/artifact pairs
  ↓
expected-valid or expected-invalid result
```

## Boundary

Schemas define artifact shape.

They do not prove:

- upstream truth
- scientific correctness
- regulatory sufficiency
- total system safety
- production readiness
- legal compliance
- certification

Schemas make artifacts inspectable and machine-checkable. Verification, replay, review, and boundary mapping remain separate layers.
