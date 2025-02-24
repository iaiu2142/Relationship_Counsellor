# Relationship Advisor

This is an AI-powered relationship counselling app deployed on Hugging Face Spaces using Streamlit. The app leverages Retrieval-Augmented Generation (RAG) to provide insightful and context-aware relationship advice based on user queries.

## Features

Upload Documents: Users can upload plain text files containing relationship concerns, chat logs, or journal entries.

Contextual Understanding: Uses FAISS for efficient similarity search and Sentence Transformers for embedding text.

User-Friendly Interface: Built with Streamlit for an interactive and easy-to-use experience.

## Technologies Used

Streamlit: Web framework for interactive UI.

FAISS: Vector search for efficient document retrieval.

Sentence Transformers: Embedding model (all-MiniLM-L6-v2) for text representation.

OpenAI API: Queries an AI model (Deepseek) for generating advice.

Hugging Face Spaces: Deployment platform.

## Installation & Running Locally

To run this app locally, install the dependencies and start the Streamlit server:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deployment

This app is deployed on Hugging Face Spaces and can be accessed [here](https://huggingface.co/spaces/sssfasihieee/RelationshipCounsellor).

---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
