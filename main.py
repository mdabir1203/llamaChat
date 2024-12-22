import streamlit as st
import requests
import plotly.graph_objects as go
from together import Together
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
# Load Client ID and Client Secret from environment variables
client = Together()

# Define the endpoint for the Llama 3.3 API
API_URL = "https://api.together.xyz/v1/chat/completions"  # Replace with the actual Llama 3.3 model endpoint
headers = {"Authorization":  f"Bearer {os.getenv('API_TOKEN')}"}

def get_response(message):
    payload = {
        "model": "Qwen/QwQ-32B-Preview",
        "messages": [{"role": "user", "content": message}],
        "max_tokens": None,
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "repetition_penalty": 1,
        "stream": False
    }
    # The http response
    response = requests.post(API_URL, headers=headers, json=payload, stream=True)
    
    ## Returns the JSON content of the response
    response_json = response.json()
    return response_json['choices'][0]['message']['content']

def create_3d_view():
    fig = go.Figure(data=[go.Scatter3d(
        x=[1, 2, 3, 4],
        y=[1, 2, 3, 4],
        z=[1, 2, 3, 4],
        mode='markers',
        marker=dict(size=12, color='red')
    )])
    fig.update_layout(title='3D View Example', scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
    return fig

st.title("Chatbot with Llama 3.3 API and 3D Views")

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type in your prompt / ভালোভাবে প্রশ্ন করুন "):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant") as assistant_chat:
        response_placeholder = st.empty()
        response = get_response(prompt)
        response_placeholder.markdown(response)
    
    # get a response from the LLM
    messages = [
        {"role": "system", "content": "The chatbot is answering..."},
        {"role": "assistant", "content": response},
        *st.session_state.chat_history
    ]
    st.session_state.messages.append({"role": "assistant", "content": response})

# 3D View
st.header("3D View")
st.plotly_chart(create_3d_view())