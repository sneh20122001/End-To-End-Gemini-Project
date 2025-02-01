from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image]) # Always include text, even if empty
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input_text = st.text_input("Input Prompt: ", key="input")  # More descriptive variable name
uploaded_file = st.file_uploader("Choose an image...", type=["jfif", "jpg", "jpeg", "png"])
image = None  # Initialize image to None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    if image is None:  # Handle the case where no image is uploaded
        st.error("Please upload an image.")
    else:
        response = get_gemini_response(input_text, image)  # Always send text and image
        st.subheader("The Response is")
        st.write(response)