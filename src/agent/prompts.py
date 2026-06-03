ALLOWED_TONES = [
    "Professional",
    "Formal",
    "Concise",
    "Email",
    "LinkedIn",
    "Academic",
    "Casual"
]

TONE_INSTRUCTIONS = {
    "Professional": "Make the text professional, clear, and polished.",
    "Formal": "Make the text formal and suitable for official communication.",
    "Concise": "Make the text shorter while preserving the original meaning.",
    "Email": "Make the text polite and suitable for email communication, but do not add greetings, sign-offs, subject lines, or placeholder names unless they already exist.",
    "LinkedIn": "Make the text polished and professional for a LinkedIn post or message, without adding hashtags unless requested.",
    "Academic": "Make the text clear, formal, and suitable for academic writing.",
    "Casual": "Make the text natural, friendly, and easy to read."
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


def build_refinement_prompt(text: str, tone: str) -> str:
    tone_instruction = TONE_INSTRUCTIONS.get(tone, TONE_INSTRUCTIONS["Professional"])

    return f"""
Rewrite the text using the following tone:

Tone: {tone}
Instruction: {tone_instruction}

Rules:
- Return ONLY the refined text.
- Do not explain anything.
- Do not add new information.
- Do not remove the original meaning.
- Keep the output close to the original text.
- Do not add greetings like "Dear Sir/Madam" unless already present.
- Do not add sign-offs like "Best regards" unless already present.
- Do not add placeholder names like "[Your Name]".
- Do not convert a short sentence into a full email.
- Only improve grammar, spelling, clarity, and tone.

Text:
{text}
"""