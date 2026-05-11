# Decision Contracts

## Purpose

A Decision Contract defines how uncertain or probabilistic inputs are evaluated before downstream action is authorized.

The contract does not define reality.

It defines the deterministic rules used to interpret an input.

## Contract Components

A Decision Contract may include:

- evaluation targets
- thresholds
- allowed operators
- deterministic rule definitions
- downstream decision states
- escalation conditions

## Example

A Bell-state evaluation contract may define:

```text
Accept if P(00) + P(11) >= 0.95
```

The quantum output itself remains probabilistic.

The deterministic layer defines how the output is interpreted.

## Why Contracts Matter

Without explicit contracts, downstream systems may:

- silently change evaluation behavior
- drift between versions
- produce inconsistent decisions
- lose auditability
- collapse operational accountability

Decision Contracts make evaluation behavior explicit and reviewable.

## Relationship to Knowledge Blocks

A Knowledge Block may reference one or more Decision Contracts.

The Knowledge Block governs:

- which contract applies
- which evaluator policy is active
- which decisions are permitted
- whether receipts are required
- whether escalation or review is mandatory
