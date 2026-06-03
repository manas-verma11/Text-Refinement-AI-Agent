from src.agent.graph import graph


state = {
    "input_text": "heloo i hope your doing well can u help me",
    "tone": "Email"
}

result = graph.invoke(state)

print("\n===== FINAL OUTPUT =====\n")

print("Original Text:")
print(result["input_text"])

print("\nTone:")
print(result["tone"])

print("\nFinal Refined Text:")
print(result["final_output"])

if result.get("error_message"):
    print("\nError:")
    print(result["error_message"])