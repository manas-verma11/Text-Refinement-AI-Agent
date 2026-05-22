from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def llm_call(state):
    user_input = state["input_text"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
                Correct and refine the following text professionally.
                Return ONLY the corrected sentence.
                Do not explain anything.

                Text: {user_input}
                """
            }
        ]
    )

    refined_text = response.choices[0].message.content

    return {
        "input_text": user_input,
        "output_text": refined_text
    }