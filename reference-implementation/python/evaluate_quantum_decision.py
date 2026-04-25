import json
import hashlib
from pathlib import Path


def evaluate_quantum_decision(data):
    output = data["quantum_output"]
    rule = data["knowledge_block"]

    # Compute value (00 + 11)
    computed_value = output["00"] + output["11"]
    threshold = rule["threshold"]

    decision = "PASS" if computed_value >= threshold else "FAIL"

    # Create a deterministic hash (proof of evaluation inputs)
    hash_input = json.dumps({
        "quantum_output": output,
        "rule": rule
    }, sort_keys=True).encode()

    receipt_hash = hashlib.sha256(hash_input).hexdigest()

    return {
        "computed_value": round(computed_value, 4),
        "threshold": threshold,
        "decision": decision,
        "receipt": {
            "status": "evaluated",
            "rule_id": rule["rule_id"],
            "timestamp": "2026-01-01T12:00:00Z",
            "hash": receipt_hash
        }
    }


if __name__ == "__main__":
    # Path to your example JSON file
    example_path = Path(__file__).parents[2] / "use-cases" / "quantum" / "examples" / "simple_quantum_decision.json"

    with open(example_path, "r") as file:
        data = json.load(file)

    result = evaluate_quantum_decision(data)

    print(json.dumps(result, indent=2))
