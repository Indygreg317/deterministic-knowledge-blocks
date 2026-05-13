# Canonical Hashing Specification

## Purpose

Deterministic receipt verification depends on stable artifact identity.

A verifier cannot reliably compare a receipt to an input artifact, Decision Contract, Evaluator Policy, or Verification Report unless both sides agree on how those artifacts are serialized before hashing.

This document defines the repository's baseline canonical JSON hashing behavior.

## Scope

This specification applies to JSON artifacts used by the reference implementation, including:

- structured input artifacts
- Decision Contracts
- Evaluator Policies
- Execution Receipts
- Verification Reports
- Audit Package manifests

This baseline is intentionally small and implementation-readable. Future versions may define stricter JSON Canonicalization Scheme compatibility, numeric normalization, signature envelopes, or domain-specific semantic normalization.

## Canonicalization Rules

The baseline canonicalization process is:

1. Parse the artifact as JSON.
2. Serialize the parsed value as UTF-8 JSON.
3. Sort object keys lexicographically.
4. Remove insignificant whitespace.
5. Preserve array order.
6. Preserve parsed JSON scalar values.
7. Hash the resulting UTF-8 byte sequence with SHA-256.
8. Prefix the digest with `sha256:`.

Reference Python behavior:

```python
json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
```

The canonical hash is:

```python
"sha256:" + hashlib.sha256(canonical_bytes).hexdigest()
```

## Important Boundaries

Canonical hashing does not prove semantic equivalence across arbitrary representations.

For example, these may or may not mean the same thing to a domain expert, but this baseline does not treat them as automatically equivalent:

```text
0.95
0.9500
"0.95"
95e-2
```

This specification defines deterministic artifact identity, not full semantic normalization.

## Stable Hash Property

Changing object key order must not change the hash.

Example:

```json
{
  "status": "PASS",
  "policy_id": "basic-deterministic-policy"
}
```

and:

```json
{
  "policy_id": "basic-deterministic-policy",
  "status": "PASS"
}
```

produce the same canonical representation and hash.

## Changed Artifact Property

Changing artifact content must change the hash.

Examples of content changes include:

- `PASS` changed to `FAIL`
- threshold changed from `0.95` to `0.90`
- policy ID changed
- contract ID changed
- distribution value changed
- evaluated field list changed

## Array Boundary

Array order is preserved.

These are different artifacts:

```json
["00", "11"]
```

and:

```json
["11", "00"]
```

The baseline does not sort arrays because array order may carry domain meaning.

## Reference Utility

Compute a canonical hash:

```bash
python reference-implementation/python/canonical_hash.py \
  examples/canonicalization/artifact-a.json
```

Print the canonical JSON representation and hash:

```bash
python reference-implementation/python/canonical_hash.py \
  examples/canonicalization/artifact-a.json \
  --print-canonical
```

Run regression checks:

```bash
python reference-implementation/python/test_canonical_hashing.py
```

## Verification Role

Canonical hashes are used by receipt verification to test whether a receipt still points to the same preserved artifacts.

A receipt may declare:

```json
{
  "input_hash": "sha256:...",
  "contract_hash": "sha256:...",
  "policy_hash": "sha256:..."
}
```

The verifier recomputes those hashes from preserved artifacts and compares them to the declared values.

If they do not match, the receipt is not accepted as valid.

## Governance Meaning

Canonical hashes provide a stable artifact identity boundary.

They support this claim:

```text
The verifier checked the same artifact content that the receipt claims to reference.
```

They do not support this broader claim:

```text
The originating source system was deterministic, truthful, safe, or complete.
```

That distinction preserves the boundary between uncertain upstream systems and deterministic downstream governance checks.
