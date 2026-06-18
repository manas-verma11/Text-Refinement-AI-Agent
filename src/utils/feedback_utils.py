import csv
import os
import uuid
from datetime import datetime


FEEDBACK_FILE = "feedback.csv"


FIELDNAMES = [
    "feedback_id",
    "created_at",
    "rating",
    "comment",
    "tone",
    "purpose",
    "use_case",
    "sensitive_data_detected",
    "original_text",
    "processed_text",
    "refined_text"
]


def save_feedback(feedback_data: dict):
    file_exists = os.path.exists(FEEDBACK_FILE)

    feedback_id = str(uuid.uuid4())

    row = {
        "feedback_id": feedback_id,
        "created_at": datetime.now().isoformat(),
        "rating": feedback_data.get("rating", ""),
        "comment": feedback_data.get("comment", ""),
        "tone": feedback_data.get("tone", ""),
        "purpose": feedback_data.get("purpose", ""),
        "use_case": feedback_data.get("use_case", ""),
        "sensitive_data_detected": ", ".join(
            feedback_data.get("sensitive_data_detected", [])
        ),
        "original_text": feedback_data.get("original_text", ""),
        "processed_text": feedback_data.get("processed_text", ""),
        "refined_text": feedback_data.get("refined_text", "")
    }

    with open(FEEDBACK_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

    return row
