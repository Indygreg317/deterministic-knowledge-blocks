import json
from pathlib import Path


def evaluate_quantum_decision(data):
    output = data["quantum_output"]
    rule = data["knowledge_block"]

    computed_value = output["00"] + output["11"]
    threshold = rule["threshold"]

    decision = "PASS" if computed_value >= threshold else "FAIL"

    return {
        "computed_value": round(computed_value, 4),
        "threshold": threshold,
        "decision": decision
    }


if __name__ == "__main__":
    example_path = Path(__file__).parents[2] / "use-cases" / "quantum" / "examples" / "simple_quantum_decision.json"

    with open(example_path, "r") as file:
        data = json.load(file)

    result = evaluate_quantum_decision(data)

    print(json.dumps(result, indent=2))
