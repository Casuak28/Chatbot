from dotenv import load_dotenv
load_dotenv() ## For loading all the enviroment variables from the .env file

import streamlit as st
import os
import google.generativeai as genai ## main library to access gemini models

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) ## To use the API key and establish acess to the Google Gemini studio

##Actual code for the functions
model = genai.GenerativeModel("gemini-pro") ##Variable storing the model to be used

##Function to query the Gemini Model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

##Setting up the UI using Streamlit
st.set_page_config(page_title="Q&A Demo")
st.header("Shikhar's Gemini LLM Application")

input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

##Code for when the submit button is clicked
if submit:
    response = get_gemini_response(input) ##Call gemini function

    st.subheader("The Response is")
    st.write(response)
    
