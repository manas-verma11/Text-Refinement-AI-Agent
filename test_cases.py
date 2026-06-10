from src.agent.graph import graph


test_inputs = [
    {
        "input_text": "heloo i hope your doing well can u help me",
        "tone": "Email",
        "purpose": "Email"
    },
    {
        "input_text": "i want job in ai and i am learning python",
        "tone": "Professional",
        "purpose": "LinkedIn Post"
    },
    {
        "input_text": "made ai project using langgraph and groq",
        "tone": "Professional",
        "purpose": "Resume Bullet"
    },
    {
        "input_text": "sorry i forgot to send the assignment",
        "tone": "Formal",
        "purpose": "Apology Message"
    },
    {
        "input_text": "can u send me the file asap",
        "tone": "Formal",
        "purpose": "Request Message"
    }
]


for index, test in enumerate(test_inputs, start=1):
    print(f"\n===== TEST CASE {index} =====")

    result = graph.invoke(test)

    print("Input:", result["input_text"])
    print("Tone:", result["tone"])
    print("Purpose:", result["purpose"])
    print("Output:", result["final_output"])

    if result.get("error_message"):
        print("Error:", result["error_message"])