"""Small, reproducible evaluation for the included labelled examples."""
import json
from pathlib import Path

from app import search_catalog

CASES_PATH = Path(__file__).with_name("evaluation_cases.json")


def main() -> None:
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    correct = 0
    answered = 0

    for case in cases:
        results = search_catalog(case["query"])
        predicted = results[0]["id"] if results else None
        answered += predicted is not None
        is_correct = predicted == case["expected_id"]
        correct += is_correct
        print(f"{'PASS' if is_correct else 'FAIL'} | {case['query']} | expected={case['expected_id']} | predicted={predicted}")

    total = len(cases)
    print(f"Top-1 accuracy: {correct}/{total} ({correct / total:.1%})")
    print(f"Coverage: {answered}/{total} ({answered / total:.1%})")
    print("Note: this is a tiny hand-labelled demo set, not a general performance claim.")


if __name__ == "__main__":
    main()
