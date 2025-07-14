import streamlit as st
import PyPDF2
import io
import os
import cohere
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
CO_API_KEY = os.getenv("CO_API_KEY")

# Validate API key
if not CO_API_KEY:
    st.error("Cohere API key not found. Please make sure it is set in your .env file as CO_API_KEY.")
    st.stop()

# Initialize Cohere client
co = cohere.Client(CO_API_KEY)

# Streamlit page config
st.set_page_config(page_title="AI Resume Critiquer", page_icon="📃", layout="centered")

# Title and instructions
st.title("AI Resume Critiquer")
st.markdown("Upload your resume and get AI-powered feedback tailored to your needs!")

# File upload and job role input
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you're targeting (optional)")

analyze = st.button("Analyze Resume")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

# Function to extract text from uploaded file
def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# Analysis logic
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any readable content.")
            st.stop()

        prompt = f"""
Please analyze the following resume and provide constructive feedback. Focus on:
1. Content clarity and impact
2. Skills presentation
3. Experience descriptions
4. Improvements for the role of {job_role if job_role else "a general job"}

Resume:
{file_content}

Provide your response in a clear, structured format.
"""

        response = co.generate(
            model='command-r-plus',
            prompt=prompt,
            max_tokens=800,
            temperature=0.7
        )

        feedback = response.generations[0].text
        st.markdown("### 📝 Resume Feedback")
        st.markdown(feedback)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
