import csv
import time

from src.agent.graph import graph
from src.evaluation.benchmark_cases import BENCHMARK_CASES
from src.evaluation.evaluation_utils import evaluate_output
from src.utils.diff_utils import get_text_changes
from src.utils.privacy_utils import detect_sensitive_data, mask_sensitive_data


BENCHMARK_OUTPUT_FILE = "benchmark_results.csv"


FIELDNAMES = [
    "case_id",
    "tone",
    "purpose",
    "use_case",
    "original_text",
    "processed_text",
    "refined_text",
    "processing_time_seconds",
    "change_count",
    "detected_sensitive_data",
    "output_not_empty",
    "changes_detected",
    "expected_terms_preserved",
    "no_banned_placeholders",
    "length_reasonable",
    "privacy_detection_passed",
    "privacy_masking_passed",
    "no_sensitive_data_leaked",
    "passed_checks",
    "total_checks",
    "auto_score",
    "error_message"
]


def run_single_benchmark(case: dict):
    start_time = time.perf_counter()

    original_text = case["input_text"]

    detected_sensitive_data = detect_sensitive_data(original_text)

    processed_text = original_text

    if case.get("mask_sensitive_data", True):
        processed_text = mask_sensitive_data(original_text)

    state = {
        "input_text": processed_text,
        "tone": case["tone"],
        "purpose": case["purpose"],
        "use_case": case["use_case"]
    }

    try:
        result = graph.invoke(state)

        refined_text = result.get("final_output", "")
        error_message = result.get("error_message", "")

        changes = get_text_changes(
            processed_text,
            refined_text
        )

        evaluation = evaluate_output(
            case=case,
            original_text=original_text,
            processed_text=processed_text,
            refined_text=refined_text,
            change_count=len(changes),
            detected_sensitive_data=detected_sensitive_data
        )

    except Exception as e:
        refined_text = ""
        error_message = str(e)
        changes = []

        evaluation = {
            "output_not_empty": False,
            "changes_detected": False,
            "expected_terms_preserved": False,
            "no_banned_placeholders": False,
            "length_reasonable": False,
            "privacy_detection_passed": False,
            "privacy_masking_passed": False,
            "no_sensitive_data_leaked": False,
            "passed_checks": 0,
            "total_checks": 8,
            "auto_score": 0
        }

    processing_time = round(time.perf_counter() - start_time, 2)

    return {
        "case_id": case["case_id"],
        "tone": case["tone"],
        "purpose": case["purpose"],
        "use_case": case["use_case"],
        "original_text": original_text,
        "processed_text": processed_text,
        "refined_text": refined_text,
        "processing_time_seconds": processing_time,
        "change_count": len(changes),
        "detected_sensitive_data": ", ".join(detected_sensitive_data),
        **evaluation,
        "error_message": error_message
    }


def save_results(rows: list[dict]):
    with open(BENCHMARK_OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict]):
    total_cases = len(rows)

    average_score = round(
        sum(float(row["auto_score"]) for row in rows) / total_cases,
        2
    )

    average_processing_time = round(
        sum(float(row["processing_time_seconds"]) for row in rows) / total_cases,
        2
    )

    passed_cases = sum(
        1 for row in rows
        if float(row["auto_score"]) >= 75
    )

    print("\n===== BENCHMARK SUMMARY =====")
    print(f"Total Test Cases: {total_cases}")
    print(f"Passed Cases: {passed_cases}/{total_cases}")
    print(f"Average Auto Score: {average_score}%")
    print(f"Average Processing Time: {average_processing_time} seconds")
    print(f"Results saved to: {BENCHMARK_OUTPUT_FILE}")

    print("\n===== CASE RESULTS =====")

    for row in rows:
        print(
            f"{row['case_id']} | "
            f"Score: {row['auto_score']}% | "
            f"Time: {row['processing_time_seconds']} sec"
        )


def main():
    rows = []

    for case in BENCHMARK_CASES:
        print(f"Running benchmark: {case['case_id']}")
        result = run_single_benchmark(case)
        rows.append(result)

    save_results(rows)
    print_summary(rows)


if __name__ == "__main__":
    main()