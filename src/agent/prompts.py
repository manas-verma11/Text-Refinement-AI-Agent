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


ALLOWED_USE_CASES = [
    "General Refinement",
    "Client Email",
    "Project Status Update",
    "Incident Communication",
    "Meeting Summary",
    "Executive Update",
    "Follow-up Email"
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
    "Email": "Make the text suitable for email communication.",
    "LinkedIn Post": "Make the text suitable for a professional LinkedIn post. Keep it polished, clear, and engaging.",
    "LinkedIn Message": "Make the text suitable for a short professional LinkedIn direct message.",
    "Resume Bullet": "Convert the text into a strong resume bullet point using action verbs and measurable impact where possible.",
    "Apology Message": "Make the text polite, respectful, and apologetic without sounding overly dramatic.",
    "Request Message": "Make the text polite, clear, and respectful while asking for help or approval.",
    "Follow-up Message": "Make the text suitable for a polite follow-up message without sounding pushy."
}


USE_CASE_INSTRUCTIONS = {
    "General Refinement": (
        "Refine the text normally without forcing a specific business format."
    ),

    "Client Email": (
        "Rewrite the text as a professional client-facing message. "
        "Use clear, polite, and business-appropriate language. "
        "Avoid internal jargon unless already present in the input."
    ),

    "Project Status Update": (
        "Rewrite the text as a clear project status update. "
        "Focus on progress, completed work, current status, blockers, and next steps only if mentioned. "
        "Do not invent timelines, numbers, or project details."
    ),

    "Incident Communication": (
        "Rewrite the text as a calm and professional incident communication. "
        "Clearly mention the issue, current impact, action being taken, and next update only if provided. "
        "Avoid blame, panic, or unsupported technical claims."
    ),

    "Meeting Summary": (
        "Rewrite the text as a structured meeting summary. "
        "Focus on discussion points, decisions, and action items only if they are present in the input. "
        "Do not create fake attendees, deadlines, or decisions."
    ),

    "Executive Update": (
        "Rewrite the text as a concise executive-level update. "
        "Focus on key outcomes, business impact, risks, and next steps. "
        "Keep it brief, clear, and decision-friendly."
    ),

    "Follow-up Email": (
        "Rewrite the text as a polite follow-up email. "
        "Keep it respectful, clear, and non-pushy. "
        "Do not add fake dates, deadlines, or previous conversation details."
    )
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


def build_refinement_prompt(text: str, tone: str, purpose: str, use_case: str) -> str:
    tone_instruction = TONE_INSTRUCTIONS.get(
        tone,
        TONE_INSTRUCTIONS["Professional"]
    )

    purpose_instruction = PURPOSE_INSTRUCTIONS.get(
        purpose,
        PURPOSE_INSTRUCTIONS["General Text"]
    )

    use_case_instruction = USE_CASE_INSTRUCTIONS.get(
        use_case,
        USE_CASE_INSTRUCTIONS["General Refinement"]
    )

    return f"""
Rewrite the text based on the selected tone, purpose, and enterprise use case.

Tone: {tone}
Tone Instruction: {tone_instruction}

Purpose: {purpose}
Purpose Instruction: {purpose_instruction}

Enterprise Use Case: {use_case}
Enterprise Use Case Instruction: {use_case_instruction}

Rules:
- Return ONLY the final refined text.
- Do not explain anything.
- Do not add unnecessary details.
- Do not change the original meaning.
- Keep the output close to the user's original intent.
- Do not add placeholder names like "[Your Name]".
- Do not add fake names, fake numbers, fake dates, fake achievements, or fake experience.
- Do not add greetings or sign-offs unless the selected purpose or use case clearly requires a message format.
- If the use case is Project Status Update, structure the output clearly.
- If the use case is Incident Communication, keep the tone calm, factual, and professional.
- If the use case is Meeting Summary, use clear sections only if the input contains enough information.
- If the use case is Executive Update, keep it concise and business-focused.
- If the purpose is Resume Bullet, return only one bullet point.

Text:
{text}
"""