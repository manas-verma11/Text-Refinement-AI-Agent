from src.utils.privacy_utils import detect_sensitive_data


BANNED_PLACEHOLDERS = [
    "[Your Name]",
    "[Company Name]",
    "[Date]",
    "[Recipient Name]",
    "Your Name",
    "Company Name"
]


def check_expected_terms(output_text: str, expected_terms: list[str]) -> bool:
    output_lower = output_text.lower()

    for term in expected_terms:
        if term.lower() not in output_lower:
            return False

    return True


def has_banned_placeholders(output_text: str) -> bool:
    output_lower = output_text.lower()

    for placeholder in BANNED_PLACEHOLDERS:
        if placeholder.lower() in output_lower:
            return True

    return False


def is_length_reasonable(input_text: str, output_text: str) -> bool:
    input_length = len(input_text)
    output_length = len(output_text)

    if output_length == 0:
        return False

    max_allowed_length = max(300, input_length * 4)

    return output_length <= max_allowed_length


def evaluate_output(
    case: dict,
    original_text: str,
    processed_text: str,
    refined_text: str,
    change_count: int,
    detected_sensitive_data: list[str]
):
    output_not_empty = bool(refined_text.strip())

    changes_detected = change_count > 0

    expected_terms_preserved = check_expected_terms(
        refined_text,
        case.get("expected_terms", [])
    )

    no_banned_placeholders = not has_banned_placeholders(refined_text)

    length_reasonable = is_length_reasonable(
        original_text,
        refined_text
    )

    privacy_detection_passed = True
    privacy_masking_passed = True
    no_sensitive_data_leaked = True

    if case.get("contains_sensitive_data"):
        privacy_detection_passed = len(detected_sensitive_data) > 0
        privacy_masking_passed = processed_text != original_text
        no_sensitive_data_leaked = len(detect_sensitive_data(refined_text)) == 0

    checks = {
        "output_not_empty": output_not_empty,
        "changes_detected": changes_detected,
        "expected_terms_preserved": expected_terms_preserved,
        "no_banned_placeholders": no_banned_placeholders,
        "length_reasonable": length_reasonable,
        "privacy_detection_passed": privacy_detection_passed,
        "privacy_masking_passed": privacy_masking_passed,
        "no_sensitive_data_leaked": no_sensitive_data_leaked
    }

    passed_checks = sum(1 for value in checks.values() if value)
    total_checks = len(checks)

    auto_score = round((passed_checks / total_checks) * 100, 2)

    return {
        **checks,
        "passed_checks": passed_checks,
        "total_checks": total_checks,
        "auto_score": auto_score
    }