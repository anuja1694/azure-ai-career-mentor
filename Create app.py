import os

import streamlit as st

from dotenv import load_dotenv

from foundry_client import client

load_dotenv()

MODEL_DEPLOYMENT = os.getenv(
    "MODEL_DEPLOYMENT"
)

with open(
    "prompts/system_prompt.txt",
    "r",
    encoding="utf-8"
) as file:
    SYSTEM_PROMPT = file.read()

st.set_page_config(
    page_title="Azure AI Career Mentor",
    page_icon="🤖"
)

st.title(
    "🤖 Azure AI Career Mentor"
)

st.write(
    "Built using Azure AI Foundry"
)

if "response_id" not in st.session_state:
    st.session_state.response_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.write(
            msg["content"]
        )

user_input = st.chat_input(
    "Ask about AI certifications..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    response = client.responses.create(
        model=MODEL_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_input,
        previous_response_id=
        st.session_state.response_id
    )

    answer = response.output_text

    with st.chat_message(
        "assistant"
    ):
        st.write(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.session_state.response_id = response.id