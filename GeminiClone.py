from dotenv import load_dotenv
load_dotenv() ## For loading all the enviroment variables from the .env file

import streamlit as st
import google.generativeai as genai ## main library to access gemini models
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) ## To use the API key and establish acess to the Google Gemini studio

##Code for selecting the LLM Model
model = genai.GenerativeModel("gemini-pro") ##Variable storing the model to be used

##To Store history
chat = model.start_chat(history=[])

##Function to query the Gemini Model
def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

#Adding the streamlit UI
st.title("Shikhar's GeminiBot Clone")

#Initialising the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Showing the app history on top
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#Adding the input bar
prompt = st.chat_input("How may I help you?")

if prompt is not None:
    #Display the user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    #Adding the user message to the message history session variable
    st.session_state.messages.append({"role":"user", "content":prompt})

    #Adding code for Gemini Assistant
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        response = get_gemini_response(prompt)

        for chunk in response:
            full_response += chunk.text
            message_placeholder.markdown(full_response + "|")
        
        message_placeholder.markdown(full_response)

    #Adding the assistant message to the message history session variable
    st.session_state.messages.append({"role":"assistant", "content":full_response})