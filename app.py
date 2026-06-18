import os
import streamlit as st
import requests


BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

REFINE_API_URL = f"{BACKEND_URL}/refine"
FEEDBACK_API_URL = f"{BACKEND_URL}/feedback"
ANALYTICS_API_URL = f"{BACKEND_URL}/analytics"


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


USE_CASES = [
    "General Refinement",
    "Client Email",
    "Project Status Update",
    "Incident Communication",
    "Meeting Summary",
    "Executive Update",
    "Follow-up Email"
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


if "last_refinement" not in st.session_state:
    st.session_state.last_refinement = None

if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False


st.title("🤖 Text Refinement AI Agent")


refine_tab, analytics_tab = st.tabs(
    ["Text Refinement", "Analytics Dashboard"]
)


def display_refinement_result(data):
    original_text = data.get("original_text", "")
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
    st.write(f"**Tone:** {data.get('tone', '')}")
    st.write(f"**Purpose:** {data.get('purpose', '')}")
    st.write(f"**Enterprise Use Case:** {data.get('use_case', '')}")

    if "processing_time_seconds" in data:
        st.write(f"**Processing Time:** {data.get('processing_time_seconds')} seconds")

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


with refine_tab:
    st.write(
        "Enter rough, informal, or grammatically incorrect text and refine it based on tone, purpose, and enterprise use case."
    )

    tone = st.selectbox(
        "Choose refinement tone:",
        TONES
    )

    purpose = st.selectbox(
        "Choose writing purpose:",
        PURPOSES
    )

    use_case = st.selectbox(
        "Choose enterprise use case:",
        USE_CASES
    )

    mask_sensitive = st.checkbox(
        "Mask sensitive data before sending to AI",
        value=True
    )

    user_input = st.text_area(
        "Enter your text:",
        height=180,
        placeholder="Example: completed api and frontend, testing privacy guard, next adding feedback system"
    )

    if st.button("Refine Text"):

        if not user_input.strip():
            st.warning("Please enter some text first.")

        else:
            with st.spinner("Refining your text..."):
                try:
                    response = requests.post(
                        REFINE_API_URL,
                        json={
                            "text": user_input,
                            "tone": tone,
                            "purpose": purpose,
                            "use_case": use_case,
                            "mask_sensitive_data": mask_sensitive
                        },
                        timeout=60
                    )

                    if response.status_code == 200:
                        data = response.json()

                        st.session_state.last_refinement = data
                        st.session_state.feedback_submitted = False

                    else:
                        try:
                            error_data = response.json()
                            st.error(error_data.get("detail", "Something went wrong."))
                        except Exception:
                            st.error("Something went wrong with the backend API.")

                except requests.exceptions.ConnectionError:
                    st.error(
                        "Backend is not running. Start FastAPI first using: "
                        "`python -m uvicorn src.api.main:api --reload`"
                    )

                except requests.exceptions.Timeout:
                    st.error("The request took too long. Please try again.")

                except Exception as e:
                    st.error(f"Unexpected error: {str(e)}")

    if st.session_state.last_refinement:
        data = st.session_state.last_refinement

        display_refinement_result(data)

        st.divider()

        st.subheader("Feedback")

        if st.session_state.feedback_submitted:
            st.success("Feedback already submitted for this output.")

        else:
            with st.form("feedback_form"):
                rating = st.radio(
                    "Was this output helpful?",
                    ["Good", "Needs Improvement"],
                    horizontal=True
                )

                comment = st.text_area(
                    "Optional feedback",
                    placeholder="Example: Output was good, but it could be shorter."
                )

                submit_feedback = st.form_submit_button("Submit Feedback")

                if submit_feedback:
                    try:
                        feedback_response = requests.post(
                            FEEDBACK_API_URL,
                            json={
                                "original_text": data.get("original_text", ""),
                                "processed_text": data.get("processed_text", ""),
                                "refined_text": data.get("refined_text", ""),
                                "tone": data.get("tone", ""),
                                "purpose": data.get("purpose", ""),
                                "use_case": data.get("use_case", ""),
                                "rating": rating,
                                "comment": comment,
                                "sensitive_data_detected": data.get(
                                    "detected_sensitive_data",
                                    []
                                )
                            },
                            timeout=30
                        )

                        if feedback_response.status_code == 200:
                            st.session_state.feedback_submitted = True
                            st.success("Feedback submitted successfully.")

                        else:
                            try:
                                error_data = feedback_response.json()
                                st.error(
                                    error_data.get(
                                        "detail",
                                        "Failed to submit feedback."
                                    )
                                )
                            except Exception:
                                st.error("Failed to submit feedback.")

                    except requests.exceptions.ConnectionError:
                        st.error(
                            "Backend is not running. Start FastAPI first using: "
                            "`python -m uvicorn src.api.main:api --reload`"
                        )

                    except Exception as e:
                        st.error(
                            f"Unexpected error while submitting feedback: {str(e)}"
                        )


with analytics_tab:
    st.subheader("Audit & Analytics Dashboard")

    st.write(
        "This dashboard shows usage statistics, privacy masking activity, and refinement behavior."
    )

    if st.button("Refresh Analytics"):
        try:
            analytics_response = requests.get(
                ANALYTICS_API_URL,
                timeout=30
            )

            if analytics_response.status_code == 200:
                analytics = analytics_response.json()

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Total Refinements",
                        analytics.get("total_refinements", 0)
                    )

                    st.metric(
                        "Most Used Tone",
                        analytics.get("most_used_tone", "N/A")
                    )

                    st.metric(
                        "Most Used Purpose",
                        analytics.get("most_used_purpose", "N/A")
                    )

                    st.metric(
                        "Privacy Detections",
                        analytics.get("privacy_detection_count", 0)
                    )

                with col2:
                    st.metric(
                        "Most Used Use Case",
                        analytics.get("most_used_use_case", "N/A")
                    )

                    st.metric(
                        "Privacy Masking Count",
                        analytics.get("privacy_masking_count", 0)
                    )

                    st.metric(
                        "Average Processing Time",
                        f"{analytics.get('average_processing_time_seconds', 0)} sec"
                    )

                    st.metric(
                        "Total Changes Detected",
                        analytics.get("total_changes_detected", 0)
                    )

                st.subheader("Length Metrics")

                col3, col4 = st.columns(2)

                with col3:
                    st.metric(
                        "Average Input Length",
                        analytics.get("average_input_length", 0)
                    )

                with col4:
                    st.metric(
                        "Average Output Length",
                        analytics.get("average_output_length", 0)
                    )

            else:
                st.error("Failed to load analytics.")

        except requests.exceptions.ConnectionError:
            st.error(
                "Backend is not running. Start FastAPI first using: "
                "`python -m uvicorn src.api.main:api --reload`"
            )

        except Exception as e:
            st.error(f"Unexpected error while loading analytics: {str(e)}")