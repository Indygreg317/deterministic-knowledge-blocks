#!/usr/bin/env python3
"""
Reference receipt verifier for deterministic evaluation receipts.

The verifier does not trust a receipt because it exists.
It recomputes the deterministic evaluation and compares the receipt against
input, contract, policy, and outcome evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "use-cases" / "quantum" / "examples"

VALID_RECEIPT = "VALID_RECEIPT"
INVALID_RECEIPT = "INVALID_RECEIPT"
UNSUPPORTED_RECEIPT = "UNSUPPORTED_RECEIPT"


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_hash(value: Dict[str, Any]) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def receipt_hash(receipt: Dict[str, Any]) -> str:
    receipt_without_output_hash = dict(receipt)
    receipt_without_output_hash.pop("output_hash", None)
    return canonical_hash(receipt_without_output_hash)


def evaluate(output: Dict[str, Any], contract: Dict[str, Any]) -> Dict[str, Any]:
    target = contract["evaluation_target"]
    distribution = output["distribution"]
    fields = target.get("fields", [])
    operator = target["operator"]
    threshold = target["threshold"]

    if operator == "sum_gte":
        computed_value = sum(float(distribution.get(field, 0)) for field in fields)
        passed = computed_value >= threshold
    elif operator == "sum_lte":
        computed_value = sum(float(distribution.get(field, 0)) for field in fields)
        passed = computed_value <= threshold
    else:
        return {
            "unsupported": True,
            "reason": f"Unsupported operator for reference verifier: {operator}",
        }

    rule = contract["rules"][0]
    decision = rule["decision_on_pass"] if passed else rule["decision_on_fail"]

    return {
        "unsupported": False,
        "decision": decision,
        "computed_value": round(computed_value, 10),
        "passed": passed,
        "evaluated_fields": fields,
        "threshold": threshold,
        "operator": operator,
        "rule_id": rule["rule_id"],
    }


def verify_receipt(
    receipt: Dict[str, Any],
    output: Dict[str, Any],
    contract: Dict[str, Any],
    policy: Dict[str, Any],
) -> Dict[str, Any]:
    mismatches: List[str] = []
    result = evaluate(output, contract)

    if result.get("unsupported"):
        return {
            "verification_status": UNSUPPORTED_RECEIPT,
            "mismatches": [result["reason"]],
        }

    expected = {
        "status": result["decision"],
        "rule_version": contract["contract_version"],
        "input_hash": canonical_hash(output),
        "contract_hash": canonical_hash(contract),
        "policy_hash": canonical_hash(policy),
        "contract_id": contract["contract_id"],
        "policy_id": policy["policy_id"],
        "evaluated_fields": result["evaluated_fields"],
        "computed_value": result["computed_value"],
        "threshold": result["threshold"],
    }

    for field, expected_value in expected.items():
        actual_value = receipt.get(field)
        if actual_value != expected_value:
            mismatches.append(
                f"{field}: expected {expected_value!r}, found {actual_value!r}"
            )

    if "output_hash" in receipt:
        expected_output_hash = receipt_hash(receipt)
        if receipt["output_hash"] != expected_output_hash:
            mismatches.append(
                f"output_hash: expected {expected_output_hash!r}, found {receipt['output_hash']!r}"
            )

    if receipt.get("evaluator") != "reference-deterministic-evaluator":
        mismatches.append(
            "evaluator: expected 'reference-deterministic-evaluator', "
            f"found {receipt.get('evaluator')!r}"
        )

    verification_status = INVALID_RECEIPT if mismatches else VALID_RECEIPT

    return {
        "verification_status": verification_status,
        "receipt_id": receipt.get("receipt_id"),
        "contract_id": contract.get("contract_id"),
        "policy_id": policy.get("policy_id"),
        "recomputed_decision": result["decision"],
        "mismatches": mismatches,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify a deterministic execution receipt against preserved artifacts.")
    parser.add_argument(
        "--receipt",
        type=Path,
        default=EXAMPLES / "bell-state-receipt-pass.json",
        help="Path to execution receipt JSON.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=EXAMPLES / "bell-state-output-pass.json",
        help="Path to structured output/input artifact JSON.",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        default=EXAMPLES / "bell-state-correlation-contract.json",
        help="Path to decision contract JSON.",
    )
    parser.add_argument(
        "--policy",
        type=Path,
        default=EXAMPLES / "evaluator-policy-basic.json",
        help="Path to evaluator policy JSON.",
    )
    parser.add_argument(
        "--expect",
        choices=[VALID_RECEIPT, INVALID_RECEIPT, UNSUPPORTED_RECEIPT],
        default=VALID_RECEIPT,
        help="Expected verification status for CI and tamper-case checks.",
    )
    args = parser.parse_args()

    receipt = load_json(args.receipt)
    output = load_json(args.output)
    contract = load_json(args.contract)
    policy = load_json(args.policy)

    verification = verify_receipt(receipt, output, contract, policy)
    print(json.dumps(verification, indent=2, sort_keys=True))

    if verification["verification_status"] != args.expect:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
