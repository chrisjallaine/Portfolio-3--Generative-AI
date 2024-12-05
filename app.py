import streamlit as st
from dotenv import load_dotenv
from utils import generate_script


# Load environment variables
load_dotenv()

# App title and header
st.title("YouTube Scriptwriting Tool")
st.header("Generate a video script by specifying a topic, length, and creativity level.")

# Sidebar to capture API key
st.sidebar.title("API Configuration")
st.sidebar.text_input("Enter your OpenAI API key:", type="password", key="api_key")

# Main input fields for the video script
prompt = st.text_input("Provide the topic of the video:")
video_length = st.number_input("Specify video length (in minutes):", min_value=1.0, step=0.5)
creativity = st.slider("Set creativity level:", min_value=0.0, max_value=1.0, value=0.5)

# Button to generate the script
generate_script_button = st.button("Generate Script")

# When the button is clicked, the script will be generated
if generate_script_button:
api_key = st.session_state.api_key
if not api_key:
st.error("Please provide a valid OpenAI API key.")
else:

# Generate the script using the utility function
title, script, search_data = generate_script(prompt, video_length, creativity, api_key)
st.success("Script generated successfully!")
st.subheader(f"Title: {title}")
st.write(f"Script:\n\n{script}")
with st.expander("Show search data used for the script"):
st.write(search_data)
