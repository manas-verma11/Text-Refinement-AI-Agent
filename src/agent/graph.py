from langgraph.graph import StateGraph, END
from src.agent.state import AgentState
from src.agent.nodes import llm_call

builder = StateGraph(AgentState)

# Add node
builder.add_node("llm_call", llm_call)

# Entry point
builder.set_entry_point("llm_call")

# End graph
builder.add_edge("llm_call", END)

# Compile graph
graph = builder.compile()