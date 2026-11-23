import os

import streamlit as st

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT")
)

st.set_page_config(
    page_title="Azure AI Career Mentor",
    page_icon="🤖"
)

st.title("🤖 Azure AI Career Mentor")

st.write(
    "Ask questions about Azure AI, AI-102 certification, career guidance, and projects."
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input(
    "Ask me anything about Azure AI..."
)

if prompt:

    # Display user message
    st.chat_message("user").markdown(prompt)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.responses.create(
                model=os.getenv("MODEL_DEPLOYMENT"),
                input=prompt
            )

            answer = response.output_text

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )