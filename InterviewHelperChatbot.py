import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create GenerativeModel instance
model = genai.GenerativeModel('gemini-1.5-flash')


# Function to generate interview questions and answers
def generate_interview_qna(job_title):
    if not job_title:
        return "Please enter a valid job title."

    prompt = f"Generate technical interview questions with 2-3 line answers for a {job_title} position."
    response = model.generate_content(prompt)
    return response.text


# Streamlit UI
st.set_page_config(page_title="Interview Helper Chatbot", page_icon=":robot_face:", layout="centered")

st.title("Interview Helper Chatbot")
st.write("Enter a job title to get technical interview questions with brief answers.")

# Job Title Input
job_title = st.text_input("Job Title:")

# Get Questions Button
if st.button("Get Questions"):
    if job_title:
        result = generate_interview_qna(job_title)
        st.text_area("Technical Interview Questions:", result, height=300)
    else:
        st.warning("Please enter a job title.")

# Exit Button
if st.button("Exit"):
    st.stop()  # Stop the app if the user clicks "Exit"
