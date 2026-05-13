# Audit Packages

## Purpose

An Audit Package is a reviewer-facing bundle of references to the artifacts needed to inspect a deterministic Knowledge Block evaluation.

It does not replace verification. It organizes verification evidence.

## Minimal Package Model

The first audit package uses a manifest-based structure.

Instead of duplicating every artifact, the manifest indexes existing repository artifacts:

- structured input artifact
- Decision Contract
- Evaluator Policy
- Execution Receipt
- Verification Report
- Governance Boundary Map
- optional failure-mode examples

## Bell-State Minimal Package

Package directory:

```text
audit-packages/bell-state-minimal/
```

Manifest:

```text
audit-packages/bell-state-minimal/audit-package-manifest.json
```

Reviewer guide:

```text
audit-packages/bell-state-minimal/README.md
```

## Review Questions

An audit package should help a reviewer answer:

```text
What artifact was evaluated?
What rule governed the decision?
What policy constrained the evaluator?
What receipt was produced?
Was the receipt verified?
What verification report was produced?
What claims remain outside the verification boundary?
How can the reviewer replay or inspect the chain?
```

## Manifest Fields

The manifest includes:

- `audit_package_id`
- `audit_package_version`
- `purpose`
- `package_scope`
- `artifacts`
- `verification_summary`
- `review_boundaries`
- `review_commands`
- `notes`

## Boundary Discipline

An audit package should not inflate narrow verification into broad trust claims.

A valid audit package can support this claim:

```text
The listed artifacts are sufficient to inspect and replay the deterministic verification path described by the package.
```

It does not automatically support this claim:

```text
The upstream system was safe, truthful, complete, or production-ready.
```

## Governance Value

Audit packages make the evidence chain easier to review, share, and inspect.

They provide a bridge from repository artifacts to external reviewer workflows without merging the governance declaration layer and the verification layer.
