import streamlit as st
from test_generator import generate_test_cases

st.title("AI Manual Test Case Generator")

user_story = st.text_area("User Story")
acceptance_criteria = st.text_area("Acceptance Criteria")

if st.button("Generate Test Cases"):
    result = generate_test_cases(user_story, acceptance_criteria)
    st.json(result)
