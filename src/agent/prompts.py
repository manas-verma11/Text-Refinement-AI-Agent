ALLOWED_TONES = [
    "Professional",
    "Formal",
    "Concise",
    "Email",
    "LinkedIn",
    "Academic",
    "Casual"
]


ALLOWED_PURPOSES = [
    "General Text",
    "Email",
    "LinkedIn Post",
    "LinkedIn Message",
    "Resume Bullet",
    "Apology Message",
    "Request Message",
    "Follow-up Message"
]


TONE_INSTRUCTIONS = {
    "Professional": "Make the text professional, clear, and polished.",
    "Formal": "Make the text formal and suitable for official communication.",
    "Concise": "Make the text shorter while preserving the original meaning.",
    "Email": "Make the text polite and suitable for email communication.",
    "LinkedIn": "Make the text polished and professional for LinkedIn.",
    "Academic": "Make the text clear, formal, and suitable for academic writing.",
    "Casual": "Make the text natural, friendly, and easy to read."
}


PURPOSE_INSTRUCTIONS = {
    "General Text": "Refine the text normally while keeping its original purpose.",
    "Email": "Make the text suitable for email communication. Add a subject only if the input clearly needs a full email.",
    "LinkedIn Post": "Make the text suitable for a professional LinkedIn post. Keep it polished, clear, and engaging.",
    "LinkedIn Message": "Make the text suitable for a short professional LinkedIn direct message.",
    "Resume Bullet": "Convert the text into a strong resume bullet point using action verbs and measurable impact where possible.",
    "Apology Message": "Make the text polite, respectful, and apologetic without sounding overly dramatic.",
    "Request Message": "Make the text polite, clear, and respectful while asking for help or approval.",
    "Follow-up Message": "Make the text suitable for a polite follow-up message without sounding pushy."
}


def build_grammar_prompt(text: str) -> str:
    return f"""
Correct only grammar and spelling mistakes.

Rules:
- Return ONLY corrected text.
- Do not explain anything.
- Do not add new information.
- Do not change the original meaning.
- Do not rewrite unnecessarily.

Text:
{text}
"""


def build_refinement_prompt(text: str, tone: str, purpose: str) -> str:
    tone_instruction = TONE_INSTRUCTIONS.get(
        tone,
        TONE_INSTRUCTIONS["Professional"]
    )

    purpose_instruction = PURPOSE_INSTRUCTIONS.get(
        purpose,
        PURPOSE_INSTRUCTIONS["General Text"]
    )

    return f"""
Rewrite the text based on the selected tone and purpose.

Tone: {tone}
Tone Instruction: {tone_instruction}

Purpose: {purpose}
Purpose Instruction: {purpose_instruction}

Rules:
- Return ONLY the final refined text.
- Do not explain anything.
- Do not add unnecessary details.
- Do not change the original meaning.
- Keep the output close to the user's original intent.
- Do not add placeholder names like "[Your Name]".
- Do not add fake numbers, fake achievements, or fake experience.
- Do not add greetings or sign-offs unless the purpose requires a full message.
- For Resume Bullet purpose, return only one bullet point.
- For LinkedIn Message purpose, keep it short and direct.
- For Follow-up Message purpose, keep it polite and non-pushy.

Text:
{text}
"""