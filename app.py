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


PURPOSES = [
    "General Text",
    "Email",
    "LinkedIn Post",
    "LinkedIn Message",
    "Resume Bullet",
    "Apology Message",
    "Request Message",
    "Follow-up Message"
]


CHANGE_LABELS = {
    "replace": "Changed",
    "insert": "Added",
    "delete": "Removed"
}


st.set_page_config(
    page_title="Text Refinement AI Agent",
    page_icon="🤖",
    layout="centered"
)


st.title("🤖 Text Refinement AI Agent")

st.write(
    "Enter rough, informal, or grammatically incorrect text and refine it based on tone and purpose."
)


tone = st.selectbox(
    "Choose refinement tone:",
    TONES
)


purpose = st.selectbox(
    "Choose writing purpose:",
    PURPOSES
)


mask_sensitive = st.checkbox(
    "Mask sensitive data before sending to AI",
    value=True
)


user_input = st.text_area(
    "Enter your text:",
    height=180,
    placeholder="Example: hello my email is manas@gmail.com and my phone number is 9876543210 please make this professional"
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
                        "tone": tone,
                        "purpose": purpose,
                        "mask_sensitive_data": mask_sensitive
                    },
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    original_text = data.get("original_text", user_input)
                    processed_text = data.get("processed_text", original_text)
                    refined_text = data.get("refined_text", "")
                    detected_sensitive_data = data.get("detected_sensitive_data", [])
                    changes = data.get("changes", [])

                    if detected_sensitive_data:
                        st.warning(
                            "Sensitive data detected: "
                            + ", ".join(detected_sensitive_data)
                        )

                    st.subheader("Original Text")
                    st.info(original_text)

                    if processed_text != original_text:
                        st.subheader("Text Sent for Refinement")
                        st.warning(processed_text)

                    st.subheader("Selected Options")
                    st.write(f"**Tone:** {data.get('tone', tone)}")
                    st.write(f"**Purpose:** {data.get('purpose', purpose)}")

                    st.subheader("Refined Text")
                    st.success(refined_text)

                    st.subheader("Changes Made")

                    if changes:
                        for index, change in enumerate(changes, start=1):
                            change_type = change.get("type", "change")
                            label = CHANGE_LABELS.get(
                                change_type,
                                change_type.title()
                            )

                            before = change.get("before", "")
                            after = change.get("after", "")

                            with st.expander(f"{index}. {label}"):
                                if before:
                                    st.write("**Before:**")
                                    st.warning(before)

                                if after:
                                    st.write("**After:**")
                                    st.success(after)
                    else:
                        st.info("No major changes detected.")

                else:
                    try:
                        error_data = response.json()
                        st.error(error_data.get("detail", "Something went wrong."))
                    except Exception:
                        st.error("Something went wrong with the backend API.")

            except requests.exceptions.ConnectionError:
                st.error(
                    "Backend is not running. Start FastAPI first using: "
                    "`uvicorn src.api.main:api --reload`"
                )

            except requests.exceptions.Timeout:
                st.error("The request took too long. Please try again.")

            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")