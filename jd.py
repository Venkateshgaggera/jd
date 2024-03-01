import streamlit as st
import requests

# Function to upload a file and get its content
def get_file_content(file):
    if file is None:
        return None
    content = file.read()
    return content

# Streamlit UI
def main():
    st.title("Job Matching App")

    # Job selection
    selected_job = st.selectbox("Select your desired job:", ["Job 1", "Job 2", "Job 3"])

    # Resume upload
    st.subheader("Upload your resume:")
    resume_file = st.file_uploader("Choose a file", type=["jpg", "png", "pdf"])

    if st.button("Submit"):
        if resume_file is not None:
            # Display uploaded resume
            st.subheader("Uploaded Resume:")
            st.image(resume_file, caption="Uploaded Resume", use_column_width=True)

            # Get job description from the server (replace YOUR_API_KEY with your actual API key)
            api_key = "YOUR_API_KEY"
            job_description = requests.get(f"https://api.example.com/job/{selected_job}?api_key={api_key}").json()

            # Perform matching using Gemini API (replace with the actual Gemini API endpoint)
            gemini_api_endpoint = "https://gemini.example.com/match"
            resume_content = get_file_content(resume_file)

            # Make a request to Gemini API
            response = requests.post(gemini_api_endpoint, json={"job_description": job_description, "resume_content": resume_content})

            # Display matching result
            st.subheader("Matching Result:")
            st.text(response.json()["result"])
        else:
            st.warning("Please upload a resume before submitting.")

if __name__ == "__main__":
    main()
