import re


SENSITIVE_PATTERNS = {
    "Email Address": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "Phone Number": r"(\+91[\s-]?)?[6-9]\d{9}",
    "API Key": r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*[A-Za-z0-9_\-]{10,}",
    "Password": r"(?i)(password|pass)\s*[:=]\s*\S+",
    "Roll Number": r"\b\d{8,12}\b"
}


MASK_VALUES = {
    "Email Address": "[EMAIL]",
    "Phone Number": "[PHONE_NUMBER]",
    "API Key": "[API_KEY]",
    "Password": "[PASSWORD]",
    "Roll Number": "[ROLL_NUMBER]"
}


def detect_sensitive_data(text: str):
    detected = []

    for label, pattern in SENSITIVE_PATTERNS.items():
        if re.search(pattern, text):
            detected.append(label)

    return detected


def mask_sensitive_data(text: str):
    masked_text = text

    for label, pattern in SENSITIVE_PATTERNS.items():
        masked_text = re.sub(
            pattern,
            MASK_VALUES[label],
            masked_text
        )

    return masked_text