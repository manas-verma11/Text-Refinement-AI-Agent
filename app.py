import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/refine"

TONES = [
    "Professional",
    "Formal",
    "Concise",
    "Email",
    "LinkedIn",
    "Academic",
    "Casual"
]


st.set_page_config(
    page_title="Text Refinement AI Agent",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 Text Refinement AI Agent")

st.write(
    "Enter rough, informal, or grammatically incorrect text and refine it using different tones."
)


tone = st.selectbox(
    "Choose refinement tone:",
    TONES
)


user_input = st.text_area(
    "Enter your text:",
    height=180,
    placeholder="Example: heloo i hope your doing well can u help me"
)


if st.button("Refine Text"):

    if not user_input.strip():
        st.warning("Please enter some text first.")

    else:
        with st.spinner("Refining your text..."):
            try:
                response = requests.post(
                    API_URL,
                    json={
                        "text": user_input,
                        "tone": tone
                    },
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    st.subheader("Original Text")
                    st.info(data["original_text"])

                    st.subheader(f"Refined Text ({data['tone']} Tone)")
                    st.success(data["refined_text"])

                else:
                    error_data = response.json()
                    st.error(error_data.get("detail", "Something went wrong."))

            except requests.exceptions.ConnectionError:
                st.error(
                    "Backend is not running. Start FastAPI first using: "
                    "`uvicorn src.api.main:api --reload`"
                )

            except requests.exceptions.Timeout:
                st.error("The request took too long. Please try again.")

            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")