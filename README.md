<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Space+Mono&size=40&duration=3000&pause=1000&color=818CF8&center=true&vCenter=true&width=800&lines=%F0%9F%A7%A0+DocuMindAI;Intelligent+Document+AI;RAG-Powered+Q%26A+System" />

<p><em>AI-Powered Document Q&A System using RAG</em></p>

</div>

<p>
  <img src="https://img.shields.io/badge/AI-RAG%20System-818cf8?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/LLMs-Powered-c084fc?style=for-the-badge&logo=huggingface&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vector-FAISS-34d399?style=for-the-badge&logo=databricks&logoColor=white"/>
  <img src="https://img.shields.io/badge/UI-Streamlit-fb923c?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.9+-3b82f6?style=for-the-badge&logo=python&logoColor=white"/>
</p>

</div>

---

## 📌 Overview

<div align="center">

> **DocuMindAI** is an advanced AI-powered application that enables users to **interact with unstructured documents using natural language**.
>
> Built on **Retrieval-Augmented Generation (RAG)**, the system converts raw text into a **semantic knowledge base**, allowing users to ask questions and receive **context-aware, accurate responses**.
>
> It bridges the gap between **unstructured data and intelligent decision-making**, simulating real-world AI-powered document intelligence systems.

</div>

---

## 🚀 Features

<table>
<tr>
<td width="50%">

### 💬 Natural Language Interaction
![](https://img.shields.io/badge/-Chat%20Interface-60a5fa?style=flat-square)

- Chat directly with your documents
- Human-like conversational experience
- Simplifies complex information retrieval

</td>
<td width="50%">

### 🧠 Context-Aware Intelligence
![](https://img.shields.io/badge/-RAG%20Powered-a78bfa?style=flat-square)

- Uses RAG for accurate responses
- Reduces hallucinations significantly
- Maintains contextual relevance

</td>
</tr>
<tr>
<td width="50%">

### 🔍 Semantic Search Engine
![](https://img.shields.io/badge/-Embeddings-34d399?style=flat-square)

- Embedding-based similarity search
- Finds meaning, not just keywords
- Efficient knowledge retrieval

</td>
<td width="50%">

### ⚡ High-Performance Retrieval
![](https://img.shields.io/badge/-Speed%20Optimized-fb923c?style=flat-square)

- FAISS-powered vector search
- Fast and scalable retrieval
- Handles large documents efficiently

</td>
</tr>
</table>

---

## 🧠 How It Works

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>How It Works — RAG Pipeline</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;600;700&family=Syne:wght@400;600;800&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --card: #16161f;
    --border: #1e1e2e;
    --pink: #ff3c8e;
    --cyan: #00e5ff;
    --purple: #7c3aed;
    --green: #00ffaa;
    --text: #e8e8f0;
    --muted: #6b6b80;
    --glow-pink: 0 0 20px rgba(255,60,142,0.4);
    --glow-cyan: 0 0 20px rgba(0,229,255,0.4);
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Animated grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,229,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,229,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
    animation: gridShift 20s linear infinite;
  }

  @keyframes gridShift {
    0% { transform: translate(0,0); }
    100% { transform: translate(40px, 40px); }
  }

  .wrapper {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 0 auto;
    padding: 60px 24px;
  }

  /* ── Header ── */
  .header {
    text-align: center;
    margin-bottom: 64px;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,60,142,0.1);
    border: 1px solid rgba(255,60,142,0.3);
    border-radius: 999px;
    padding: 6px 16px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: var(--pink);
    text-transform: uppercase;
    margin-bottom: 20px;
    animation: fadeSlideDown 0.6s ease both;
  }

  .badge::before { content: '●'; animation: pulse 2s infinite; }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
  }

  .title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2rem, 6vw, 3.5rem);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.02em;
    animation: fadeSlideDown 0.6s 0.1s ease both;
  }

  .title .grad {
    background: linear-gradient(135deg, var(--pink), var(--cyan));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .subtitle {
    margin-top: 12px;
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 0.05em;
    animation: fadeSlideDown 0.6s 0.2s ease both;
  }

  @keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-12px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* ── Pipeline Section ── */
  .pipeline-block {
    margin-bottom: 48px;
    animation: fadeUp 0.7s ease both;
  }

  .pipeline-block:nth-child(2) { animation-delay: 0.3s; }
  .pipeline-block:nth-child(3) { animation-delay: 0.5s; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .section-label {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
  }

  .section-icon {
    font-size: 20px;
  }

  .section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: var(--muted);
  }

  .section-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  /* ── Steps Container ── */
  .steps {
    display: flex;
    align-items: stretch;
    gap: 0;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    overflow: hidden;
    position: relative;
  }

  /* Glowing top border */
  .steps.ingestion::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--pink), var(--cyan), var(--pink));
    background-size: 200%;
    animation: shimmer 3s linear infinite;
  }

  .steps.query::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--cyan), var(--green), var(--cyan));
    background-size: 200%;
    animation: shimmer 3s linear infinite;
  }

  @keyframes shimmer {
    0% { background-position: 0% 0; }
    100% { background-position: 200% 0; }
  }

  /* ── Individual Step ── */
  .step {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 24px 12px 20px;
    cursor: pointer;
    position: relative;
    transition: background 0.25s, transform 0.2s;
    border-right: 1px solid var(--border);
    text-align: center;
  }

  .step:last-child { border-right: none; }

  .step:hover { background: rgba(255,255,255,0.03); }

  .step.active.ingestion-step {
    background: rgba(255,60,142,0.07);
  }
  .step.active.query-step {
    background: rgba(0,229,255,0.07);
  }

  .step-num {
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: var(--muted);
    margin-bottom: 10px;
    transition: color 0.25s;
  }

  .step.active.ingestion-step .step-num { color: var(--pink); }
  .step.active.query-step .step-num { color: var(--cyan); }

  .step-icon-wrap {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    margin-bottom: 10px;
    border: 1px solid var(--border);
    background: var(--surface);
    transition: all 0.25s;
  }

  .step.active.ingestion-step .step-icon-wrap {
    border-color: var(--pink);
    box-shadow: var(--glow-pink);
    background: rgba(255,60,142,0.1);
  }

  .step.active.query-step .step-icon-wrap {
    border-color: var(--cyan);
    box-shadow: var(--glow-cyan);
    background: rgba(0,229,255,0.1);
  }

  .step-name {
    font-family: 'Syne', sans-serif;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 4px;
    transition: color 0.25s;
  }

  .step.active.ingestion-step .step-name { color: var(--pink); }
  .step.active.query-step .step-name { color: var(--cyan); }

  .step-sub {
    font-size: 9px;
    color: var(--muted);
    letter-spacing: 0.06em;
    text-transform: uppercase;
  }

  /* Arrow between steps */
  .arrow {
    display: flex;
    align-items: center;
    padding: 0 2px;
    color: var(--border);
    font-size: 12px;
    pointer-events: none;
    transition: color 0.3s;
    flex-shrink: 0;
    align-self: center;
    position: absolute;
  }

  /* ── Detail Panel ── */
  .detail-panel {
    margin-top: 12px;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
    background: var(--surface);
    transition: all 0.35s cubic-bezier(0.4,0,0.2,1);
    max-height: 0;
    opacity: 0;
  }

  .detail-panel.open {
    max-height: 240px;
    opacity: 1;
  }

  .detail-inner {
    padding: 20px 24px;
    display: flex;
    gap: 24px;
    align-items: flex-start;
  }

  .detail-icon {
    font-size: 32px;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .detail-content {}

  .detail-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 6px;
  }

  .detail-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 12px;
  }

  .detail-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }

  .tag {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.08em;
    padding: 3px 10px;
    border-radius: 999px;
    border: 1px solid;
  }

  .tag.pink { color: var(--pink); border-color: rgba(255,60,142,0.3); background: rgba(255,60,142,0.08); }
  .tag.cyan { color: var(--cyan); border-color: rgba(0,229,255,0.3); background: rgba(0,229,255,0.08); }
  .tag.green { color: var(--green); border-color: rgba(0,255,170,0.3); background: rgba(0,255,170,0.08); }
  .tag.purple { color: #a78bfa; border-color: rgba(124,58,237,0.3); background: rgba(124,58,237,0.08); }

  /* ── Flow Connector between pipelines ── */
  .connector {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    padding: 16px 0;
    color: var(--muted);
    font-size: 10px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    animation: fadeUp 0.7s 0.6s ease both;
    opacity: 0;
    animation-fill-mode: both;
  }

  .connector-line {
    width: 1px;
    height: 24px;
    background: linear-gradient(var(--pink), var(--cyan));
    animation: lineGrow 0.5s 0.8s ease both;
    transform-origin: top;
    opacity: 0;
    animation-fill-mode: both;
  }

  @keyframes lineGrow {
    from { opacity: 0; transform: scaleY(0); }
    to { opacity: 1; transform: scaleY(1); }
  }

  /* ── Footer Note ── */
  .footer-note {
    margin-top: 48px;
    padding: 20px 24px;
    border-radius: 12px;
    border: 1px solid var(--border);
    background: var(--card);
    display: flex;
    align-items: center;
    gap: 16px;
    animation: fadeUp 0.7s 0.7s ease both;
    animation-fill-mode: both;
  }

  .footer-icon { font-size: 24px; }

  .footer-text {
    font-size: 11px;
    color: var(--muted);
    line-height: 1.6;
  }

  .footer-text strong {
    color: var(--text);
    font-weight: 600;
  }

  /* Responsive */
  @media (max-width: 640px) {
    .steps { flex-wrap: wrap; }
    .step { min-width: calc(33% - 2px); border-bottom: 1px solid var(--border); }
    .detail-panel.open { max-height: 360px; }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- Header -->
  <div class="header">
    <div class="badge">🧠 Documentation</div>
    <h1 class="title">How It <span class="grad">Works</span></h1>
    <p class="subtitle">AI-powered RAG Pipeline — click any step to explore</p>
  </div>

  <!-- Ingestion Pipeline -->
  <div class="pipeline-block">
    <div class="section-label">
      <span class="section-icon">💾</span>
      <span class="section-title">Ingestion Pipeline</span>
      <div class="section-line"></div>
    </div>

    <div class="steps ingestion" id="ingestion-steps">
      <div class="step ingestion-step" data-index="0" onclick="selectStep('ingestion', 0)">
        <div class="step-num">01</div>
        <div class="step-icon-wrap">📄</div>
        <div class="step-name">Upload</div>
        <div class="step-sub">Document</div>
      </div>
      <div class="step ingestion-step" data-index="1" onclick="selectStep('ingestion', 1)">
        <div class="step-num">02</div>
        <div class="step-icon-wrap">🔍</div>
        <div class="step-name">Extract</div>
        <div class="step-sub">Raw text</div>
      </div>
      <div class="step ingestion-step" data-index="2" onclick="selectStep('ingestion', 2)">
        <div class="step-num">03</div>
        <div class="step-icon-wrap">✂️</div>
        <div class="step-name">Chunk</div>
        <div class="step-sub">Segments</div>
      </div>
      <div class="step ingestion-step" data-index="3" onclick="selectStep('ingestion', 3)">
        <div class="step-num">04</div>
        <div class="step-icon-wrap">🔢</div>
        <div class="step-name">Embed</div>
        <div class="step-sub">Vectors</div>
      </div>
      <div class="step ingestion-step" data-index="4" onclick="selectStep('ingestion', 4)">
        <div class="step-num">05</div>
        <div class="step-icon-wrap">🗄️</div>
        <div class="step-name">Index</div>
        <div class="step-sub">FAISS DB</div>
      </div>
    </div>

    <!-- Detail Panel for Ingestion -->
    <div class="detail-panel" id="ingestion-detail">
      <div class="detail-inner">
        <div class="detail-icon" id="ingestion-detail-icon"></div>
        <div class="detail-content">
          <div class="detail-title" id="ingestion-detail-title"></div>
          <div class="detail-desc" id="ingestion-detail-desc"></div>
          <div class="detail-tags" id="ingestion-detail-tags"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Connector -->
  <div class="connector">
    <div class="connector-line"></div>
    <span>pipeline handoff</span>
    <div class="connector-line"></div>
  </div>

  <!-- Query Pipeline -->
  <div class="pipeline-block">
    <div class="section-label">
      <span class="section-icon">🔎</span>
      <span class="section-title">Query Pipeline</span>
      <div class="section-line"></div>
    </div>

    <div class="steps query" id="query-steps">
      <div class="step query-step" data-index="0" onclick="selectStep('query', 0)">
        <div class="step-num">06</div>
        <div class="step-icon-wrap">💬</div>
        <div class="step-name">Query</div>
        <div class="step-sub">User input</div>
      </div>
      <div class="step query-step" data-index="1" onclick="selectStep('query', 1)">
        <div class="step-num">07</div>
        <div class="step-icon-wrap">🧮</div>
        <div class="step-name">Embed</div>
        <div class="step-sub">Query vector</div>
      </div>
      <div class="step query-step" data-index="2" onclick="selectStep('query', 2)">
        <div class="step-num">08</div>
        <div class="step-icon-wrap">🎯</div>
        <div class="step-name">Search</div>
        <div class="step-sub">Top-K match</div>
      </div>
      <div class="step query-step" data-index="3" onclick="selectStep('query', 3)">
        <div class="step-num">09</div>
        <div class="step-icon-wrap">🤖</div>
        <div class="step-name">LLM + RAG</div>
        <div class="step-sub">Generate</div>
      </div>
      <div class="step query-step" data-index="4" onclick="selectStep('query', 4)">
        <div class="step-num">10</div>
        <div class="step-icon-wrap">✅</div>
        <div class="step-name">Answer</div>
        <div class="step-sub">Response</div>
      </div>
    </div>

    <!-- Detail Panel for Query -->
    <div class="detail-panel" id="query-detail">
      <div class="detail-inner">
        <div class="detail-icon" id="query-detail-icon"></div>
        <div class="detail-content">
          <div class="detail-title" id="query-detail-title"></div>
          <div class="detail-desc" id="query-detail-desc"></div>
          <div class="detail-tags" id="query-detail-tags"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <div class="footer-note">
    <div class="footer-icon">⚡</div>
    <div class="footer-text">
      <strong>Fully local & private.</strong> Documents never leave your environment. FAISS index is stored on disk, embeddings run via your configured model endpoint, and the LLM generates grounded answers using only retrieved context.
    </div>
  </div>

</div>

<script>
const data = {
  ingestion: [
    {
      icon: "📄",
      title: "01 — Upload Document",
      desc: "Accepts PDF, DOCX, TXT, and Markdown files. Files are validated, deduplicated via hash check, and queued for the extraction step. Supports batch uploads and drag-and-drop.",
      tags: [
        { label: "PDF / DOCX / TXT", cls: "pink" },
        { label: "SHA-256 dedup", cls: "purple" },
        { label: "Batch support", cls: "cyan" }
      ]
    },
    {
      icon: "🔍",
      title: "02 — Extract Raw Text",
      desc: "Parses the document using PyMuPDF or python-docx depending on format. Handles multi-column layouts, tables, and embedded images. Outputs clean UTF-8 text with metadata.",
      tags: [
        { label: "PyMuPDF", cls: "pink" },
        { label: "python-docx", cls: "cyan" },
        { label: "UTF-8 clean", cls: "green" }
      ]
    },
    {
      icon: "✂️",
      title: "03 — Chunk into Segments",
      desc: "Splits text into overlapping chunks using a sliding window (default: 512 tokens, 64-token overlap). Preserves sentence boundaries for coherent retrieval context.",
      tags: [
        { label: "512 token chunks", cls: "pink" },
        { label: "64-token overlap", cls: "purple" },
        { label: "Sentence-aware", cls: "cyan" }
      ]
    },
    {
      icon: "🔢",
      title: "04 — Embed Vectors",
      desc: "Each chunk is passed through a sentence-transformers model (e.g. all-MiniLM-L6-v2) to produce dense float32 vectors of dimension 384. Batched for GPU efficiency.",
      tags: [
        { label: "all-MiniLM-L6-v2", cls: "cyan" },
        { label: "384-dim float32", cls: "pink" },
        { label: "GPU batched", cls: "green" }
      ]
    },
    {
      icon: "🗄️",
      title: "05 — Index in FAISS DB",
      desc: "Vectors are added to a FAISS IndexFlatIP (inner product) index. Metadata (source, chunk ID, page) is stored in a parallel SQLite table. Index is persisted to disk after every ingest.",
      tags: [
        { label: "FAISS IndexFlatIP", cls: "pink" },
        { label: "SQLite metadata", cls: "purple" },
        { label: "Disk-persistent", cls: "green" }
      ]
    }
  ],
  query: [
    {
      icon: "💬",
      title: "06 — Receive User Query",
      desc: "The user's natural-language question is received via the API or UI. Input is sanitized, trimmed, and optionally pre-processed with a query rewriting step for better recall.",
      tags: [
        { label: "Natural language", cls: "cyan" },
        { label: "Query rewriting", cls: "purple" },
        { label: "REST / WebSocket", cls: "green" }
      ]
    },
    {
      icon: "🧮",
      title: "07 — Embed Query Vector",
      desc: "The query string is embedded using the same sentence-transformers model used during ingestion, ensuring vector space alignment. Returns a single 384-dim float32 vector.",
      tags: [
        { label: "Same model as ingest", cls: "cyan" },
        { label: "384-dim alignment", cls: "pink" },
        { label: "< 5ms latency", cls: "green" }
      ]
    },
    {
      icon: "🎯",
      title: "08 — FAISS Top-K Search",
      desc: "Performs an approximate nearest-neighbour search against the FAISS index using cosine similarity. Returns the top-K most relevant chunks (default K=5) with their similarity scores.",
      tags: [
        { label: "ANN search", cls: "cyan" },
        { label: "K=5 default", cls: "pink" },
        { label: "Cosine similarity", cls: "purple" }
      ]
    },
    {
      icon: "🤖",
      title: "09 — LLM + RAG Generate",
      desc: "Retrieved chunks are injected into a system prompt as context. The LLM (Claude / GPT / local) is called with the context + user question. Output is constrained to grounded answers only.",
      tags: [
        { label: "Context injection", cls: "cyan" },
        { label: "Grounded output", cls: "green" },
        { label: "Claude / GPT / Local", cls: "pink" }
      ]
    },
    {
      icon: "✅",
      title: "10 — Stream Final Answer",
      desc: "The generated response is streamed token-by-token to the client. Source citations (document name, page, chunk ID) are appended. Response is logged for feedback and evaluation.",
      tags: [
        { label: "SSE streaming", cls: "cyan" },
        { label: "Source citations", cls: "green" },
        { label: "Feedback logging", cls: "purple" }
      ]
    }
  ]
};

let active = { ingestion: null, query: null };

function selectStep(pipeline, index) {
  const steps = document.querySelectorAll(`#${pipeline}-steps .step`);
  const panel = document.getElementById(`${pipeline}-detail`);

  if (active[pipeline] === index) {
    // Toggle off
    steps.forEach(s => s.classList.remove('active'));
    panel.classList.remove('open');
    active[pipeline] = null;
    return;
  }

  steps.forEach(s => s.classList.remove('active'));
  steps[index].classList.add('active');
  active[pipeline] = index;

  const d = data[pipeline][index];
  document.getElementById(`${pipeline}-detail-icon`).textContent = d.icon;
  document.getElementById(`${pipeline}-detail-title`).textContent = d.title;
  document.getElementById(`${pipeline}-detail-desc`).textContent = d.desc;
  document.getElementById(`${pipeline}-detail-tags`).innerHTML = d.tags
    .map(t => `<span class="tag ${t.cls}">${t.label}</span>`)
    .join('');

  // Color the panel top border
  const isCyan = pipeline === 'query';
  panel.style.borderColor = isCyan ? 'rgba(0,229,255,0.25)' : 'rgba(255,60,142,0.25)';

  panel.classList.add('open');
}
</script>
</body>
</html>

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| 🐍 **Language** | Python 3.9+ | Core runtime |
| 🔗 **Framework** | LangChain | RAG orchestration |
| 🤖 **LLM** | OpenAI / HuggingFace | Language generation |
| 🧮 **Embeddings** | Sentence Transformers | Vector representations |
| ⚡ **Vector DB** | FAISS | Similarity search |
| 📊 **UI** | Streamlit | Interactive frontend |
| 📄 **Parsers** | PyPDF2, python-docx | Document ingestion |

---

## 📁 Project Structure

```
DocuMindAI/
├── 📄 app.py                 # Streamlit entrypoint
├── 🔧 config.py              # Configuration & API keys
├── 📁 src/
│   ├── 🔤 ingestion.py       # Document loading & chunking
│   ├── 🧮 embeddings.py      # Embedding generation
│   ├── 🗄️ vectorstore.py     # FAISS index management
│   ├── 🔍 retriever.py       # Semantic search logic
│   └── 🤖 rag_chain.py       # LLM + RAG pipeline
├── 📁 data/                  # Uploaded documents
├── 📁 vectorstore/           # Persisted FAISS index
├── 📄 requirements.txt
└── 📄 README.md
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/DocuMindAI.git
cd DocuMindAI

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Add your OPENAI_API_KEY inside .env

# 5. Run the app
streamlit run app.py
```

---

## 🔐 Environment Variables

```env
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_TOKEN=your_hf_token_here     # optional
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
CHUNK_SIZE=500
CHUNK_OVERLAP=50
TOP_K_RESULTS=5
```

---

## 🎯 Usage

1. **Launch** the Streamlit app via `streamlit run app.py`
2. **Upload** a PDF, DOCX, or TXT document using the sidebar
3. **Wait** for the document to be processed and indexed
4. **Ask** any question in natural language in the chat input
5. **Get** context-aware answers grounded in your document

---

## 🗺️ Roadmap

- [x] PDF & DOCX ingestion
- [x] FAISS vector store integration
- [x] RAG pipeline with LangChain
- [x] Streamlit chat interface
- [ ] Multi-document support
- [ ] Chat history & memory
- [ ] Source citation with page numbers
- [ ] REST API endpoint
- [ ] Docker deployment

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

```bash
# Fork → Clone → Create branch → Commit → Push → PR
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ using RAG, FAISS, LangChain & Streamlit**

⭐ Star this repo if you found it helpful!

</div>
