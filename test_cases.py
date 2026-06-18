from src.agent.graph import graph


test_inputs = [
    {
        "input_text": "completed api and frontend, testing privacy guard, next adding feedback system",
        "tone": "Professional",
        "purpose": "General Text",
        "use_case": "Project Status Update"
    },
    {
        "input_text": "server is down and users are facing login issue team is checking",
        "tone": "Formal",
        "purpose": "Email",
        "use_case": "Incident Communication"
    },
    {
        "input_text": "we discussed api work frontend work and next we need analytics dashboard",
        "tone": "Professional",
        "purpose": "General Text",
        "use_case": "Meeting Summary"
    },
    {
        "input_text": "project has privacy guard tone purpose and diff tracking ready next feedback and analytics",
        "tone": "Concise",
        "purpose": "General Text",
        "use_case": "Executive Update"
    },
    {
        "input_text": "checking if you got time to review the latest project update",
        "tone": "Formal",
        "purpose": "Follow-up Message",
        "use_case": "Follow-up Email"
    }
]


for index, test in enumerate(test_inputs, start=1):
    print(f"\n===== TEST CASE {index} =====")

    result = graph.invoke(test)

    print("Input:", result["input_text"])
    print("Tone:", result["tone"])
    print("Purpose:", result["purpose"])
    print("Enterprise Use Case:", result["use_case"])
    print("Output:", result["final_output"])

    if result.get("error_message"):
        print("Error:", result["error_message"])