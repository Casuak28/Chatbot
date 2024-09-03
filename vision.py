from dotenv import load_dotenv
load_dotenv() ## For loading all the enviroment variables from the .env file

import streamlit as st
import os
import google.generativeai as genai ## main library to access gemini models
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) ## To use the API key and establish acess to the Google Gemini studio

##Actual code for the functions
model = genai.GenerativeModel("gemini-pro-vision") ##Variable storing the model to be used


##Function to query the Gemini Model
def get_gemini_response(question, image):
    if question!="":
        response = model.generate_content([question, image])
    else:
        response = model.generate_content(image)
    return response.text

##Code to initialize the streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input = st.text_input("Input Prompt: ", key="input")

##Code to set up image upload functionality 
uploaded_file = st.file_uploader("Choose an image...", type=['jpg','jpeg','png'])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.", use_column_width=True)

##Submit Button
submit = st.button("Tell me about the image")

##If Submit is clicked
if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is")
    st.write(response)