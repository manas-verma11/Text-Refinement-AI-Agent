from src.utils.privacy_utils import detect_sensitive_data, mask_sensitive_data


def test_detect_email_and_phone():
    text = "My email is test@example.com and my phone number is 9876543210."

    detected = detect_sensitive_data(text)

    assert "Email Address" in detected
    assert "Phone Number" in detected


def test_mask_email_and_phone():
    text = "My email is test@example.com and my phone number is 9876543210."

    masked_text = mask_sensitive_data(text)

    assert "test@example.com" not in masked_text
    assert "9876543210" not in masked_text
    assert "[EMAIL]" in masked_text
    assert "[PHONE_NUMBER]" in masked_text