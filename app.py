import streamlit as st
import requests

from loaders.pdf_loader import load_pdf
from rag_pipeline.chunker import chunk_text
from embeddings.embedder import generate_embeddings
from vector_store.faiss_store import create_faiss_index, search_index
from rag_pipeline.heading_extractor import extract_heading
from rag_pipeline.section_matcher import match_sections


# -------------------------------
# LOCAL LLM USING OLLAMA
# -------------------------------
def generate_answer(query, results):

    context = "\n".join(results)

    prompt = f"""
You are a helpful AI assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}

Answer in a clear professional sentence:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3",   # you can change to llama3 if installed
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# -------------------------------
# STREAMLIT UI
# -------------------------------
st.title("DocuMind AI")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:

    # Load text
    text = load_pdf(uploaded_file)

    st.subheader("Extracted Text Preview")
    st.write(text[:1000])

    # Chunk text
    chunks = chunk_text(text)

    st.subheader("Number of Chunks Created")
    st.write(len(chunks))

    st.subheader("First Chunk Preview")
    st.write(chunks[0])

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    st.subheader("Embedding Shape")
    st.write(embeddings.shape)

    # Create FAISS index
    index = create_faiss_index(embeddings)

    st.subheader("Vectors Stored in FAISS")
    st.write(index.ntotal)

    # -------------------------------
    # QUESTION SECTION
    # -------------------------------
    st.subheader("Ask Question About Document")

query = st.text_input("Enter your question")

if query:

    query_embedding = generate_embeddings([query])[0]
    results = search_index(index, query_embedding, chunks)

    answer = generate_answer(query, results)

    st.subheader("AI Answer")
    st.write(answer)

     