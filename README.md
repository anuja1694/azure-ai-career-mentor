🤖 Azure AI Career Mentor
An AI-powered career guidance and certification mentor built using Azure AI Foundry, GPT-6-Astra, OpenAI SDK, Streamlit, and Python.

This application allows users to ask questions about Azure AI services, AI-102 certification preparation, career growth, project ideas, and prompt engineering through an interactive chat interface.

🚀 Features
✅ Azure AI Foundry Integration

✅ GPT-6-Astra Deployment

✅ OpenAI Responses API

✅ Interactive Chat Interface

✅ Streamlit Web Application

✅ Environment Variable Configuration

✅ Real-Time AI Responses

✅ Career and Certification Guidance

✅ Beginner-Friendly User Experience

🏗️ Architecture
User
 │
 ▼
Streamlit Web Interface
 │
 ▼
Python Application
 │
 ▼
OpenAI SDK
 │
 ▼
Azure AI Foundry Endpoint
 │
 ▼
GPT-6-Astra Deployment
 │
 ▼
AI Response
📖 How It Works
User enters a question in the chat interface.
Streamlit captures the user input.
Python sends the request to Azure AI Foundry using the OpenAI SDK.
GPT-6-Astra processes the prompt.
The model generates a response.
The response is displayed back to the user in the browser.
🛠️ Technologies Used
Technology	Purpose
Azure AI Foundry	AI platform
GPT-6-Astra	Generative AI model
OpenAI SDK	Model communication
Streamlit	Web interface
Python	Application logic
python-dotenv	Environment configuration
📂 Project Structure
azure-ai-career-mentor/
│
├── .env
├── app.py
├── foundry_client.py
├── requirements.txt
├── README.md
│
├── prompts/
│   └── system_prompt.txt
│
├── assets/
├── docs/
└── screenshots/
⚙️ Installation
Clone Repository
git clone https://github.com/your-username/azure-ai-career-mentor.git
Navigate To Project
cd azure-ai-career-mentor
Create Virtual Environment
python -m venv .venv
Activate Virtual Environment
Windows:

.venv\Scripts\activate
Linux/Mac:

source .venv/bin/activate
Install Dependencies
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file:

AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/openai/v1/

AZURE_OPENAI_API_KEY=your_api_key

MODEL_DEPLOYMENT=gpt-6-astra
▶️ Run The Application
streamlit run app.py
Application opens at:

http://localhost:8501
💬 Example Questions
What is Azure AI Foundry?

Create a 30-day AI-102 study roadmap.

Suggest Azure AI portfolio projects.

Explain Prompt Engineering in simple English.

How can I prepare for an AI Engineer role?
📸 Screenshots
Home Screen
Add screenshot here

AI Response Example
Add screenshot here

Chat Interface
Add screenshot here

🎯 Skills Demonstrated
This project demonstrates:

Azure AI Foundry
Model Deployment
OpenAI SDK
Responses API
Python Development
Prompt Engineering
Streamlit UI Development
API Authentication
Environment Variable Management
Generative AI Application Development
🧠 Learning Outcomes
Through this project I learned:

How to deploy models in Azure AI Foundry
How to connect applications to deployed AI models
How to use the OpenAI Responses API
How to build interactive AI applications using Streamlit
How to securely manage API credentials
How to integrate Generative AI into a real-world application
🚀 Future Enhancements
Chat History Persistence
AI-102 Study Planner
Resume Analyzer
File Upload Support
Azure AI Search Integration
RAG (Retrieval-Augmented Generation)
Azure AI Agent Service Integration
Token Usage Tracking
Conversation Memory
👨‍💻 Author
Anuja Suresh

Aspiring Azure AI Engineer | AI-102 Learner | Azure AI Foundry Enthusiast

⭐ Acknowledgements
Built as part of my Azure AI learning journey and AI-102 certification preparation using Microsoft Azure AI Foundry.
