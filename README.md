<h1 align="center">🧠 DocuMindAI</h1>
<h3 align="center">AI-Powered Document Q&A System using RAG</h3>

<p align="center">
  <img src="https://img.shields.io/badge/AI-RAG%20System-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Tech-LLMs-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Vector-FAISS-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/UI-Streamlit-orange?style=for-the-badge"/>
</p>

---

## 📌 Overview

<div align="center" style="background: linear-gradient(135deg, #0d1117, #161b22); padding:25px; border-radius:15px; border:1px solid #30363d;">

<h3>📄 Intelligent Document Understanding System</h3>

<p>
<b>DocuMindAI</b> is an advanced AI-powered application that enables users to 
<b>interact with unstructured documents using natural language</b>.
</p>

<p>
Built on <b>Retrieval-Augmented Generation (RAG)</b>, the system converts raw text into a 
<b>semantic knowledge base</b>, allowing users to ask questions and receive 
<b>context-aware, accurate responses</b>.
</p>

<p>
It bridges the gap between <b>unstructured data and intelligent decision-making</b>, 
simulating real-world AI-powered document intelligence systems.
</p>

</div>

---

## 🚀 Features

<div align="center">

<table>
<tr>

<td width="50%" style="background:#161b22; padding:20px; border-radius:12px; border:1px solid #30363d;">

### 💬 Natural Language Interaction
<img src="https://img.shields.io/badge/Feature-Chat%20Interface-blue?style=flat-square"/>
<br/><br/>

• Chat directly with documents  
• Human-like conversational experience  
• Simplifies complex information retrieval  

</td>

<td width="50%" style="background:#161b22; padding:20px; border-radius:12px; border:1px solid #30363d;">

### 🧠 Context-Aware Intelligence
<img src="https://img.shields.io/badge/AI-RAG%20Powered-purple?style=flat-square"/>
<br/><br/>

• Uses RAG for accurate responses  
• Reduces hallucinations  
• Maintains contextual relevance  

</td>

</tr>

<tr>

<td width="50%" style="background:#161b22; padding:20px; border-radius:12px; border:1px solid #30363d;">

### 🔍 Semantic Search Engine
<img src="https://img.shields.io/badge/Search-Embeddings-green?style=flat-square"/>
<br/><br/>

• Embedding-based similarity search  
• Finds meaning, not just keywords  
• Efficient knowledge retrieval  

</td>

<td width="50%" style="background:#161b22; padding:20px; border-radius:12px; border:1px solid #30363d;">

### ⚡ High-Performance Retrieval
<img src="https://img.shields.io/badge/Speed-Optimized-orange?style=flat-square"/>
<br/><br/>

• FAISS-powered vector search  
• Fast and scalable retrieval  
• Handles large documents efficiently  

</td>

</tr>

</table>

</div>

---

## 🧠 How It Works

<div style="background:#0d1117; padding:20px; border-radius:12px; border:1px solid #30363d;">

🔹 Upload Document → Extract Text → Chunk Data  
🔹 Generate Embeddings → Store in FAISS Vector DB  
🔹 User Query → Convert to Embedding  
🔹 Semantic Search → Retrieve Relevant Chunks  
🔹 LLM + Context → Generate Final Answer  

</div>

---

## 🏗️ System Architecture

```mermaid
graph TD
A[Upload Document] --> B[Text Extraction]
B --> C[Text Chunking]
C --> D[Generate Embeddings]
D --> E[Store in FAISS Vector DB]

F[User Question] --> G[Convert to Embedding]
G --> H[Semantic Search]
H --> I[Retrieve Relevant Chunks]
I --> J[LLM (RAG)]
J --> K[Context-Aware Answer]
