import streamlit as st
import requests

st.title("Text Refinement AI Agent")

user_input = st.text_area("Enter your text")

if st.button("Refine Text"):

    response = requests.post(
        "http://127.0.0.1:8000/refine",
        json={"text": user_input}
    )

    if response.status_code == 200:
        data = response.json()

        st.subheader("Refined Text")
        st.write(data["refined_text"])

    else:
        st.error("Something went wrong")