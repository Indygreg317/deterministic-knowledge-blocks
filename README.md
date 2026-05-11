# Deterministic Knowledge Blocks

Deterministic Knowledge Blocks are governed decision units for applying explicit, repeatable evaluation rules to uncertain or probabilistic inputs.

This repository provides a reference framework for converting structured uncertainty into auditable downstream decisions without pretending the source system itself has become deterministic.

> We do not make uncertain systems deterministic.  
> We make the evaluation layer deterministic, traceable, and auditable.

---

## What This Repository Is

This repository is a reference architecture for deterministic evaluation around uncertain systems.

It demonstrates how to:

- capture uncertain outputs as structured input artifacts
- evaluate those artifacts through explicit Decision Contracts
- apply governed Evaluator Policies
- produce PASS / FAIL / ESCALATE decisions
- generate hash-linked Execution Receipts
- preserve auditability and replay boundaries

The initial working use case is quantum output evaluation, where probabilistic distributions are evaluated through deterministic downstream rules.

---

## What This Repository Is Not

This repository does not:

- make quantum systems deterministic
- eliminate uncertainty from AI or probabilistic systems
- provide production-ready safety infrastructure
- replace domain experts, medical experts, humanitarian experts, or safety reviewers
- authorize autonomous deployment in critical systems

It defines a controlled evaluation layer around uncertain outputs.

---

## Canonical Flow

```text
Input Signal
  ↓
Structured Input Artifact
  ↓
Decision Contract
  ↓
Knowledge Block Constraints
  ↓
Evaluator Policy
  ↓
Deterministic Evaluation
  ↓
Authorization Decision
  ↓
Execution Receipt
  ↓
Audit Record
```

---

## Quick Start

Run the reference evaluator from the repository root:

```bash
python reference-implementation/python/evaluate_decision_contract.py
```

This evaluates the default Bell-state PASS example.

Run the FAIL example:

```bash
python reference-implementation/python/evaluate_decision_contract.py \
  --output use-cases/quantum/examples/bell-state-output-fail.json
```

The evaluator loads:

```text
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-correlation-contract.json
use-cases/quantum/examples/evaluator-policy-basic.json
```

and emits a structured execution receipt.

---

## Reference Quantum Example

A probabilistic output may look like:

```text
00 = 0.48
01 = 0.02
10 = 0.01
11 = 0.49
```

A deterministic Decision Contract may define:

```text
Accept if P(00) + P(11) >= 0.95
```

The evaluator computes:

```text
0.48 + 0.49 = 0.97
```

Result:

```text
PASS
```

The source remains probabilistic. The evaluation rule is deterministic.

---

## Core Concepts

### Decision Contract

Defines what is being evaluated, which fields are in scope, what threshold applies, and which decision should be produced on pass or fail.

### Evaluator Policy

Defines allowed decisions, receipt requirements, failure behavior, review conditions, and audit behavior.

### Deterministic Outcome

A structured PASS / FAIL / ESCALATE result produced by applying explicit rules to a structured input artifact.

### Execution Receipt

A record of what was evaluated, which contract and policy applied, what decision was produced, and which hashes support replay or audit.

### Knowledge Block

A governed decision unit that binds inputs, constraints, contracts, runtime rules, and verification requirements into a reusable evaluation structure.

---

## Repository Structure

```text
.github/workflows/                  Validation workflows
docs/                               Architecture and governance documentation
schema/                             JSON Schema specifications
use-cases/quantum/examples/         Quantum decision-contract examples
reference-implementation/python/    Minimal Python evaluator
assets/                             Diagrams and visuals
```

---

## Key Files

```text
schema/knowledge-block.schema.json
schema/deterministic-outcome.schema.json
schema/execution-receipt.schema.json
schema/decision-contract.schema.json
schema/quantum-output.schema.json
schema/evaluator-policy.schema.json

docs/deterministic-evaluation.md
docs/decision-contracts.md
docs/replay-and-receipts.md
docs/canonical-flow.md

use-cases/quantum/examples/bell-state-correlation-contract.json
use-cases/quantum/examples/evaluator-policy-basic.json
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-output-fail.json
use-cases/quantum/examples/bell-state-receipt-pass.json
use-cases/quantum/examples/bell-state-receipt-fail.json

reference-implementation/python/evaluate_decision_contract.py
```

---

## Validation

This repository includes a GitHub Actions workflow that:

- validates all JSON files parse correctly
- runs the reference evaluator against the PASS example
- runs the reference evaluator against the FAIL example

Workflow:

```text
.github/workflows/validate-json.yml
```

---

## Experimental Status

This framework is experimental.

It should not be used for:

- medical decisions
- humanitarian deployment
- safety-critical systems
- production quantum control
- autonomous execution

without expert validation, independent review, and operational oversight.

---

## AIPA Alignment

This project supports the broader AIPA mission of building:

- deterministic decision frameworks
- auditable computational pipelines
- governed AI systems
- runtime verification patterns
- transparent decision infrastructure

---

## License

Apache License 2.0
