#!/usr/bin/env python3
"""
Replay a deterministic evaluation and compare the recomputed result to a stored receipt.

Replay verifies the evaluation layer, not the upstream truth of the source system.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List

from evaluate_decision_contract import build_receipt, evaluate, load_json

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "use-cases" / "quantum" / "examples"


def compare_receipt(recomputed: Dict[str, Any], stored: Dict[str, Any]) -> List[str]:
    mismatches: List[str] = []

    comparable_fields = [
        "status",
        "contract_id",
        "policy_id",
        "evaluated_fields",
        "computed_value",
        "threshold",
        "input_hash",
    ]

    for field in comparable_fields:
        if recomputed.get(field) != stored.get(field):
            mismatches.append(
                f"{field}: recomputed={recomputed.get(field)!r} stored={stored.get(field)!r}"
            )

    return mismatches


def main() -> None:
    parser = argparse.ArgumentParser(description="Replay a deterministic evaluation receipt.")
    parser.add_argument(
        "--output",
        type=Path,
        default=EXAMPLES / "bell-state-output-pass.json",
        help="Path to the structured input/output artifact.",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        default=EXAMPLES / "bell-state-correlation-contract.json",
        help="Path to the decision contract.",
    )
    parser.add_argument(
        "--policy",
        type=Path,
        default=EXAMPLES / "evaluator-policy-basic.json",
        help="Path to the evaluator policy.",
    )
    parser.add_argument(
        "--receipt",
        type=Path,
        default=EXAMPLES / "bell-state-receipt-pass.json",
        help="Path to the stored execution receipt.",
    )
    args = parser.parse_args()

    output = load_json(args.output)
    contract = load_json(args.contract)
    policy = load_json(args.policy)
    stored_receipt = load_json(args.receipt)

    result = evaluate(output, contract)
    recomputed_receipt = build_receipt(output, contract, policy, result)

    mismatches = compare_receipt(recomputed_receipt, stored_receipt)

    report = {
        "verification_status": "VERIFIED" if not mismatches else "MISMATCH",
        "mismatches": mismatches,
        "recomputed": {
            "status": recomputed_receipt.get("status"),
            "computed_value": recomputed_receipt.get("computed_value"),
            "threshold": recomputed_receipt.get("threshold"),
            "input_hash": recomputed_receipt.get("input_hash"),
        },
        "stored": {
            "status": stored_receipt.get("status"),
            "computed_value": stored_receipt.get("computed_value"),
            "threshold": stored_receipt.get("threshold"),
            "input_hash": stored_receipt.get("input_hash"),
        },
    }

    print(json.dumps(report, indent=2, sort_keys=True))

    if mismatches:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
