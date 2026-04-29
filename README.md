




# Deterministic Knowledge Blocks

## Overview

Deterministic Knowledge Blocks are structured decision units for converting uncertain or probabilistic inputs into repeatable, auditable downstream decisions.

This repository provides an open reference framework for applying Knowledge Blocks to domains where the source system may remain probabilistic, uncertain, or noisy, including:

- quantum output evaluation
- AI decision pipelines
- humanitarian risk modeling
- operational authorization workflows

The framework does **not** remove uncertainty from source systems.

It structures how decisions are made around uncertainty.

---

## Core Principle

> We do not make uncertain systems deterministic.  
> We make the evaluation layer deterministic, traceable, and auditable.

For quantum systems, this means:

> Quantum outputs remain probabilistic.  
> The Knowledge Block defines how those outputs are evaluated before any downstream decision is made.

---

## Core Flow

```text
Input Signals
   ↓
Decision Contract
   ↓
Knowledge Block Constraints
   ↓
Deterministic Evaluation
   ↓
Authorization Layer
   ↓
Execution Receipt
   ↓
Audit Record
```

---

## What This Repo Demonstrates

This repository explores how to:

- apply explicit constraints to probabilistic inputs
- evaluate uncertain outputs against deterministic rules
- produce consistent PASS / FAIL / ESCALATE decisions
- validate execution conditions before action
- generate receipted, hash-linked audit records

---

## Runtime Governance Upgrade

The repository now includes a stronger contract-based evaluation model:

- **Decision Contract**: Defines what is being evaluated and which constraints apply
- **Evaluator Policy**: Defines allowed decisions, thresholds, failure behavior, and review rules
- **Quantum Output Schema**: Provides a structured representation of probabilistic outputs
- **Execution Receipt**: Records what was evaluated, which rule was applied, and what decision was produced

The key governance rule is:

> Inputs are uncertain. Evaluation rules are explicit. Outcomes are receipted.

---

## Quick Start

Run the reference example:

```bash
python reference-implementation/python/evaluate_decision_contract.py
```

This will:

- read a sample quantum probability distribution
- apply a deterministic decision contract
- produce a deterministic outcome
- generate a hash-linked execution receipt

---

## Use Cases

### Quantum Output Evaluation

Quantum systems produce probabilistic output distributions.

Using Knowledge Blocks, those outputs can be evaluated against defined constraints to produce:

- deterministic downstream decisions
- repeatable evaluation logic
- auditable execution paths

Important:

> This does not make quantum systems deterministic.  
> It makes decisions about quantum outputs structured and verifiable.

Example:

```text
Quantum Output:
00 = 0.48
01 = 0.02
10 = 0.01
11 = 0.49

Rule:
Accept if P(00) + P(11) >= 0.95

Outcome:
PASS
```

### Malnutrition and Humanitarian Risk Modeling

Malnutrition is a complex, multi-variable humanitarian challenge.

This repository does not attempt to solve malnutrition.

Instead, it demonstrates how Knowledge Blocks may help structure:

- risk signals
- intervention triggers
- review thresholds
- auditable recommendations

All humanitarian and medical outputs require validation by qualified professionals.

---

## Repository Structure

```text
docs/                         Concepts, architecture, and evaluation notes
schema/                       JSON Schema specifications
use-cases/quantum/            Quantum examples and decision contracts
use-cases/malnutrition/       Humanitarian examples
reference-implementation/     Minimal Python evaluation logic
assets/                       Diagrams and visuals
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
docs/quantum-decision-contract.md
docs/replay-and-receipts.md

use-cases/quantum/examples/bell-state-correlation-contract.json
use-cases/quantum/examples/bell-state-output-pass.json
use-cases/quantum/examples/bell-state-receipt-pass.json
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

- ethical AI systems
- deterministic decision frameworks
- auditable computational pipelines
- runtime governance patterns
- transparent decision infrastructure

---

## License

Apache 2.0
