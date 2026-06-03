from langgraph.graph import StateGraph, END

from src.agent.state import AgentState
from src.agent.nodes import (
    validate_input,
    grammar_correction,
    professional_refinement,
    final_validation
)


builder = StateGraph(AgentState)

builder.add_node("validate_input", validate_input)
builder.add_node("grammar_correction", grammar_correction)
builder.add_node("professional_refinement", professional_refinement)
builder.add_node("final_validation", final_validation)

builder.set_entry_point("validate_input")


def route_after_validation(state):
    if state.get("is_valid"):
        return "grammar_correction"

    return "final_validation"


builder.add_conditional_edges(
    "validate_input",
    route_after_validation,
    {
        "grammar_correction": "grammar_correction",
        "final_validation": "final_validation"
    }
)

builder.add_edge("grammar_correction", "professional_refinement")
builder.add_edge("professional_refinement", "final_validation")
builder.add_edge("final_validation", END)

graph = builder.compile()