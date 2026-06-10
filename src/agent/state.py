from typing import TypedDict


class AgentState(TypedDict, total=False):
    input_text: str
    tone: str
    purpose: str

    is_valid: bool
    error_message: str

    grammar_fixed_text: str
    professional_text: str
    final_output: str