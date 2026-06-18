import csv
import os
import uuid
from datetime import datetime
from collections import Counter


ANALYTICS_FILE = "usage_logs.csv"


FIELDNAMES = [
    "log_id",
    "created_at",
    "tone",
    "purpose",
    "use_case",
    "input_length",
    "output_length",
    "change_count",
    "sensitive_data_count",
    "sensitive_data_types",
    "masked_sensitive_data",
    "processing_time_seconds"
]


def save_usage_log(log_data: dict):
    file_exists = os.path.exists(ANALYTICS_FILE)

    row = {
        "log_id": str(uuid.uuid4()),
        "created_at": datetime.now().isoformat(),
        "tone": log_data.get("tone", ""),
        "purpose": log_data.get("purpose", ""),
        "use_case": log_data.get("use_case", ""),
        "input_length": log_data.get("input_length", 0),
        "output_length": log_data.get("output_length", 0),
        "change_count": log_data.get("change_count", 0),
        "sensitive_data_count": log_data.get("sensitive_data_count", 0),
        "sensitive_data_types": ", ".join(log_data.get("sensitive_data_types", [])),
        "masked_sensitive_data": log_data.get("masked_sensitive_data", False),
        "processing_time_seconds": log_data.get("processing_time_seconds", 0)
    }

    with open(ANALYTICS_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

    return row


def read_usage_logs():
    if not os.path.exists(ANALYTICS_FILE):
        return []

    with open(ANALYTICS_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_most_common_value(rows, column_name):
    values = [
        row.get(column_name, "")
        for row in rows
        if row.get(column_name, "")
    ]

    if not values:
        return "N/A"

    return Counter(values).most_common(1)[0][0]


def safe_float(value):
    try:
        return float(value)
    except Exception:
        return 0.0


def safe_int(value):
    try:
        return int(float(value))
    except Exception:
        return 0


def get_analytics_summary():
    rows = read_usage_logs()

    if not rows:
        return {
            "total_refinements": 0,
            "most_used_tone": "N/A",
            "most_used_purpose": "N/A",
            "most_used_use_case": "N/A",
            "privacy_detection_count": 0,
            "privacy_masking_count": 0,
            "average_processing_time_seconds": 0,
            "average_input_length": 0,
            "average_output_length": 0,
            "total_changes_detected": 0
        }

    total_refinements = len(rows)

    processing_times = [
        safe_float(row.get("processing_time_seconds", 0))
        for row in rows
    ]

    input_lengths = [
        safe_int(row.get("input_length", 0))
        for row in rows
    ]

    output_lengths = [
        safe_int(row.get("output_length", 0))
        for row in rows
    ]

    change_counts = [
        safe_int(row.get("change_count", 0))
        for row in rows
    ]

    privacy_detection_count = sum(
        1 for row in rows
        if safe_int(row.get("sensitive_data_count", 0)) > 0
    )

    privacy_masking_count = sum(
        1 for row in rows
        if str(row.get("masked_sensitive_data", "")).lower() == "true"
        and safe_int(row.get("sensitive_data_count", 0)) > 0
    )

    return {
        "total_refinements": total_refinements,
        "most_used_tone": get_most_common_value(rows, "tone"),
        "most_used_purpose": get_most_common_value(rows, "purpose"),
        "most_used_use_case": get_most_common_value(rows, "use_case"),
        "privacy_detection_count": privacy_detection_count,
        "privacy_masking_count": privacy_masking_count,
        "average_processing_time_seconds": round(
            sum(processing_times) / total_refinements,
            2
        ),
        "average_input_length": round(
            sum(input_lengths) / total_refinements,
            2
        ),
        "average_output_length": round(
            sum(output_lengths) / total_refinements,
            2
        ),
        "total_changes_detected": sum(change_counts)
    }