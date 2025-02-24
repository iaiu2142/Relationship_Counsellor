# AI Relationship Counsellor

The AI Relationship Counsellor is an intelligent, context-aware web app that leverages advanced AI techniques to analyze relationship dynamics based on user-uploaded WhatsApp chat logs or textual conversations. It identifies potential red flags, evaluates conversational toxicity, and suggests behavioral improvements.

## Key Features

- Text Uploads: Easily upload WhatsApp chats or plain-text relationship discussions for analysis.

- Context-Aware Insights: Utilizes Retrieval-Augmented Generation (RAG) for accurate, context-driven advice.

- Interactive UI: Developed with Streamlit, ensuring a responsive and intuitive user experience.

## Core Technologies

- Streamlit: Simplifies web application deployment and provides interactive front-end components.

- FAISS: Efficiently searches and retrieves relevant textual segments from large conversations.

- Sentence Transformers: Embedding model (all-MiniLM-L6-v2) generates semantic representations of conversations.

- Groq API (deepseek-r1-distill-llama-70b): Performs relationship-focused conversational analysis, detecting toxic behavior and suggesting improvements.

## Tools Used

- VS Code: Powerful and intuitive IDE for coding.

- GitHub: Version control and hosting for collaborative development.

- Streamlit Cloud: Quick and easy platform for web app deployment.

- Hugging Face Spaces: Flexible and accessible AI model hosting and deployment platform.

## How to Run Locally

Clone the repository, install dependencies, and launch the app with:

pip install -r requirements.txt
streamlit run app.py

The app will open automatically at http://localhost:8501.

## Deployment

This application can be effortlessly deployed using platforms like Streamlit Cloud or Hugging Face Spaces.
