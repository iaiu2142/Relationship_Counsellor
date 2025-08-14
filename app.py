import streamlit as st
import faiss
from sentence_transformers import SentenceTransformer
from groq import Groq

# Initialize Groq API
client = Groq(api_key="Secret key")  # Ensure your API key is valid

# Initialize Sentence Transformer
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# FAISS Index
dimension = 384  # Embedding dimension of the model
index = faiss.IndexFlatL2(dimension)

# Function to chunk text
def chunk_text(text, max_length=500):
    words = text.split()
    chunks = []
    chunk = []
    for word in words:
        if len(" ".join(chunk)) + len(word) <= max_length:
            chunk.append(word)
        else:
            chunks.append(" ".join(chunk))
            chunk = [word]
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks

# Function to embed text and add to FAISS index
def embed_and_store(chunks):
    embeddings = embedding_model.encode(chunks)
    index.add(embeddings)

# Query handling using Groq's streaming completions
def query_llm(prompt):
    # Create a completion request using the Groq model
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",  # Use the provided Groq model
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a relationship counselor. Analyze the given WhatsApp conversation "
                    "and provide insights on potential red flags, toxicity, and room for improvement in behavior. "
                    "Every response must start by rating the overall chat toxicity out of 10."
                )
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=True,
        reasoning_format="raw"
    )
    
    # Stream and collect the response
    full_response = ""
    for chunk in completion:
        full_response += chunk.choices[0].delta.content or ""
    return full_response

# Streamlit App
st.title("AI Relationship Counsellor")

uploaded_file = st.file_uploader("Upload a text file of your WhatsApp chat", type=["txt"])

if uploaded_file:
    text = uploaded_file.read().decode("utf-8")
    st.write("Chat Extracted Successfully!")

    # Chunk and embed text
    chunks = chunk_text(text)
    embed_and_store(chunks)

    # Query Interface
    user_query = st.text_input("Ask a question about your relationship:")
    if user_query:
        # Embed query and search FAISS for the top 5 relevant chunks
        query_embedding = embedding_model.encode([user_query])
        distances, indices = index.search(query_embedding, k=5)
        relevant_chunks = [chunks[i] for i in indices[0]]

        # Combine chunks to form context
        context = " ".join(relevant_chunks)
        final_prompt = f"Context: {context}\n\nQuestion: {user_query}"

        # Get response from the Groq model
        response = query_llm(final_prompt)
        st.write("### AI Analysis")

        st.write(response)

