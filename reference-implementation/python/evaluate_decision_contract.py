#!/usr/bin/env python3
"""
Reference deterministic evaluator for Decision Contracts.

This example does not make a probabilistic source deterministic.
It makes the downstream evaluation layer explicit, repeatable, and receipted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "use-cases" / "quantum" / "examples"


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def canonical_hash(value: Dict[str, Any]) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


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
        raise ValueError(f"Unsupported operator for reference evaluator: {operator}")

    rule = contract["rules"][0]
    decision = rule["decision_on_pass"] if passed else rule["decision_on_fail"]

    return {
        "decision": decision,
        "computed_value": round(computed_value, 10),
        "passed": passed,
        "evaluated_fields": fields,
        "threshold": threshold,
        "operator": operator,
        "rule_id": rule["rule_id"],
    }


def build_receipt(output: Dict[str, Any], contract: Dict[str, Any], policy: Dict[str, Any], result: Dict[str, Any]) -> Dict[str, Any]:
    receipt = {
        "receipt_id": f"receipt-{output['output_id']}",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": result["decision"],
        "rule_version": contract["contract_version"],
        "input_hash": canonical_hash(output),
        "evaluator": "reference-deterministic-evaluator",
        "contract_id": contract["contract_id"],
        "policy_id": policy["policy_id"],
        "evaluated_fields": result["evaluated_fields"],
        "computed_value": result["computed_value"],
        "threshold": result["threshold"],
        "decision_reason": (
            "Deterministic threshold satisfied."
            if result["passed"]
            else "Deterministic threshold not satisfied."
        ),
    }
    receipt["output_hash"] = canonical_hash(receipt)
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a deterministic decision contract against a quantum output example.")
    parser.add_argument(
        "--output",
        type=Path,
        default=EXAMPLES / "bell-state-output-pass.json",
        help="Path to quantum output JSON.",
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
    args = parser.parse_args()

    output = load_json(args.output)
    contract = load_json(args.contract)
    policy = load_json(args.policy)

    result = evaluate(output, contract)
    receipt = build_receipt(output, contract, policy, result)

    print(json.dumps(receipt, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
