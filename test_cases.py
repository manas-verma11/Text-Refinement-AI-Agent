from src.agent.graph import graph


test_inputs = [
    {
        "input_text": "heloo i hope your doing well can u help me",
        "tone": "Email"
    },
    {
        "input_text": "i want job in ai and i am learning python",
        "tone": "LinkedIn"
    },
    {
        "input_text": "this project is good and i made it using ai",
        "tone": "Professional"
    },
    {
        "input_text": "can u send me the file asap",
        "tone": "Formal"
    },
    {
        "input_text": "i have completed the work and now testing it",
        "tone": "Concise"
    }
]


for index, test in enumerate(test_inputs, start=1):
    print(f"\n===== TEST CASE {index} =====")

    result = graph.invoke(test)

    print("Input:", result["input_text"])
    print("Tone:", result["tone"])
    print("Output:", result["final_output"])

    if result.get("error_message"):
        print("Error:", result["error_message"])