from src.agent.graph import graph

# Input state
state = {
    "input_text": "heloo how are u doing today"
}

# Run graph
result = graph.invoke(state)

# Print result
print("\n===== FINAL OUTPUT =====\n")

for key, value in result.items():
    print(f"{key}: {value}")