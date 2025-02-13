from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
import openai

# ✅ Set Page Config (Only Once & First)
st.set_page_config(page_title='CHATBOT-DEMO')

# Title & Intro
st.title('Welcome to the Gemini Chatbot')
st.write('Let’s start chatting!')

# API Key Setup
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAWGXuxsmGUhWnBzfj0dy9-zv61BHIH7i8'
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Gemini Model Setup
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Function to Get Response
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Header
st.header('GEMINI LLM APPLICATION')

# Session State for Chat History
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User Input Section
input = st.text_input('Input:', key='input')
submit = st.button('ASK THE QUESTION')

# Handling User Query
if submit and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(('YOU', input))
    st.subheader('The Response Is:')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('BOT', chunk.text))

# Displaying Chat History
st.subheader('THE CHAT HISTORY IS:')
for role, text in st.session_state['chat_history']:
    st.write(f'{role}: {text}')
