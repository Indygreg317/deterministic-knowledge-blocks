# Canonical Flow

## Purpose

The canonical flow defines the high-level execution path used by the reference deterministic evaluation framework.

## Canonical Evaluation Path

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

## Flow Description

### Input Signal

The original source signal.

This may originate from:

- quantum systems
- AI systems
- operational telemetry
- humanitarian data
- external services

The source may remain uncertain or probabilistic.

### Structured Input Artifact

The signal is normalized into a governed input structure.

This creates a stable evaluation boundary.

### Decision Contract

Defines how the input will be evaluated.

### Knowledge Block Constraints

Defines runtime rules, limitations, and allowed behaviors.

### Evaluator Policy

Defines:

- allowed decisions
- escalation behavior
- receipt requirements
- review conditions

### Deterministic Evaluation

Applies explicit rules against the structured input.

### Authorization Decision

Determines whether downstream action is permitted.

### Execution Receipt

Produces structured evidence of the evaluation.

### Audit Record

Preserves governance and accountability metadata.
