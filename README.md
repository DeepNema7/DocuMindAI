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
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Document Ingestion Pipeline</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0d1117; color: #e6edf3; min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem 1rem; }

  .container { max-width: 480px; width: 100%; }
  .header { display: flex; align-items: center; gap: 10px; margin-bottom: 2rem; }
  .header-icon { font-size: 22px; }
  .header-title { font-size: 20px; font-weight: 600; }
  .header-sub { font-size: 13px; color: #8b949e; margin-top: 2px; }

  .pipeline { display: flex; flex-direction: column; align-items: center; gap: 0; }

  /* connector arrow */
  .connector { display: flex; flex-direction: column; align-items: center; height: 36px; position: relative; }
  .connector .line { width: 2px; flex: 1; background: #30363d; transition: background .4s; }
  .connector .arrow { width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 7px solid #30363d; transition: border-top-color .4s; }
  .connector.lit .line { background: var(--accent); }
  .connector.lit .arrow { border-top-color: var(--accent); }

  /* step card */
  .step { width: 100%; border-radius: 12px; border: 1.5px solid #30363d; background: #161b22; cursor: pointer; transition: border-color .3s, background .3s, transform .15s, box-shadow .3s; position: relative; overflow: hidden; }
  .step:hover { transform: translateY(-1px); box-shadow: 0 4px 20px rgba(0,0,0,.4); }
  .step.active { border-color: var(--accent); background: var(--bg); box-shadow: 0 0 0 1px var(--accent-dim), 0 4px 24px var(--glow); }
  .step.done { border-color: var(--accent); background: var(--bg-done); }

  .step-inner { padding: 1rem 1.25rem; display: flex; align-items: center; gap: 12px; }
  .step-icon { font-size: 20px; flex-shrink: 0; }
  .step-label { font-size: 15px; font-weight: 600; color: #e6edf3; }
  .step-badge { margin-left: auto; font-size: 11px; padding: 2px 8px; border-radius: 20px; border: 1px solid; white-space: nowrap; opacity: 0; transition: opacity .3s; }
  .step.active .step-badge, .step.done .step-badge { opacity: 1; }
  .step.active .step-badge { background: var(--badge-bg); border-color: var(--accent); color: var(--accent); }
  .step.done .step-badge { background: var(--badge-bg-done); border-color: var(--accent-dim); color: var(--accent); }

  /* progress bar */
  .progress-bar { position: absolute; bottom: 0; left: 0; height: 2px; width: 0%; background: var(--accent); transition: width var(--dur, .8s) linear; border-radius: 0 2px 2px 0; }
  .step.active .progress-bar { width: 100%; }
  .step.done .progress-bar { width: 100%; }

  /* detail panel */
  .step-detail { max-height: 0; overflow: hidden; transition: max-height .35s ease, opacity .3s; opacity: 0; border-top: 0; }
  .step-detail.open { max-height: 200px; opacity: 1; border-top: 1px solid #30363d; }
  .step-detail-inner { padding: .75rem 1.25rem 1rem; }
  .step-detail-inner p { font-size: 13px; color: #8b949e; line-height: 1.7; }
  .detail-chips { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 8px; }
  .chip { font-size: 11px; padding: 2px 8px; border-radius: 6px; border: 1px solid; }

  /* controls */
  .controls { display: flex; gap: 8px; margin-top: 1.75rem; justify-content: center; }
  .btn { padding: 7px 18px; font-size: 13px; border-radius: 8px; border: 1px solid #30363d; background: #21262d; color: #e6edf3; cursor: pointer; transition: background .15s; }
  .btn:hover { background: #30363d; }
  .btn:disabled { opacity: .4; cursor: default; }
  .btn.primary { background: #1f6feb; border-color: #1f6feb; color: #fff; }
  .btn.primary:hover { background: #388bfd; border-color: #388bfd; }

  /* status */
  .status { text-align: center; font-size: 12px; color: #8b949e; margin-top: 1rem; min-height: 18px; transition: color .3s; }
  .status.done { color: #3fb950; }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <span class="header-icon">🧠</span>
    <div>
      <div class="header-title">Document Ingestion Pipeline</div>
      <div class="header-sub">How your documents become a knowledge base</div>
    </div>
  </div>

  <div class="pipeline" id="pipeline"></div>

  <div class="controls">
    <button class="btn primary" id="run-btn" onclick="runPipeline()">▶ Run pipeline</button>
    <button class="btn" id="reset-btn" onclick="reset()" disabled>↺ Reset</button>
  </div>
  <div class="status" id="status"></div>
</div>

<script>
const steps = [
  {
    icon: "📄",
    label: "Document Upload",
    badge: "Input",
    dur: 900,
    detail: "Accepts PDF, DOCX, and TXT files. Raw binary is read and passed downstream for text extraction.",
    chips: ["PDF", "DOCX", "TXT"],
    chipClass: "chip-gray",
    accent: "#8b949e",
    accentDim: "rgba(139,148,158,.35)",
    bg: "rgba(139,148,158,.07)",
    bgDone: "rgba(139,148,158,.04)",
    badgeBg: "rgba(139,148,158,.15)",
    badgeBgDone: "rgba(139,148,158,.08)",
    glow: "rgba(139,148,158,.08)"
  },
  {
    icon: "🔤",
    label: "Text Extraction",
    badge: "Processing",
    dur: 1100,
    detail: "Raw text is extracted from each document format. PDFs use PyMuPDF; DOCX files use python-docx. Layout and encoding are normalised.",
    chips: ["PyMuPDF", "python-docx", "UTF-8"],
    chipClass: "chip-blue",
    accent: "#58a6ff",
    accentDim: "rgba(88,166,255,.35)",
    bg: "rgba(56,139,253,.08)",
    bgDone: "rgba(56,139,253,.04)",
    badgeBg: "rgba(56,139,253,.15)",
    badgeBgDone: "rgba(56,139,253,.08)",
    glow: "rgba(56,139,253,.12)"
  },
  {
    icon: "✂️",
    label: "Text Chunking",
    badge: "Splitting",
    dur: 1000,
    detail: "Text is split into overlapping chunks (default 500 tokens, 50-token overlap) so no semantic context is lost at boundaries.",
    chips: ["500 tokens", "50 overlap", "RecursiveCharacterTextSplitter"],
    chipClass: "chip-purple",
    accent: "#bc8cff",
    accentDim: "rgba(188,140,255,.35)",
    bg: "rgba(188,140,255,.08)",
    bgDone: "rgba(188,140,255,.04)",
    badgeBg: "rgba(188,140,255,.15)",
    badgeBgDone: "rgba(188,140,255,.08)",
    glow: "rgba(188,140,255,.12)"
  },
  {
    icon: "🔢",
    label: "Generate Embeddings",
    badge: "Encoding",
    dur: 1300,
    detail: "Each chunk is encoded into a dense vector using a sentence-transformer model. Semantic similarity is preserved in the embedding space.",
    chips: ["sentence-transformers", "384-dim", "cosine similarity"],
    chipClass: "chip-orange",
    accent: "#e3b341",
    accentDim: "rgba(227,179,65,.35)",
    bg: "rgba(227,179,65,.08)",
    bgDone: "rgba(227,179,65,.04)",
    badgeBg: "rgba(227,179,65,.15)",
    badgeBgDone: "rgba(227,179,65,.08)",
    glow: "rgba(227,179,65,.10)"
  },
  {
    icon: "🗄️",
    label: "Store in FAISS Index",
    badge: "Indexing",
    dur: 900,
    detail: "Vectors are added to a FAISS index for millisecond nearest-neighbour retrieval at query time. The index is persisted to disk.",
    chips: ["FAISS", "IndexFlatL2", "Persisted"],
    chipClass: "chip-green",
    accent: "#3fb950",
    accentDim: "rgba(63,185,80,.35)",
    bg: "rgba(63,185,80,.08)",
    bgDone: "rgba(63,185,80,.04)",
    badgeBg: "rgba(63,185,80,.15)",
    badgeBgDone: "rgba(63,185,80,.08)",
    glow: "rgba(63,185,80,.10)"
  }
];

const chipColors = {
  "chip-gray":   { bg:"rgba(139,148,158,.1)",  border:"rgba(139,148,158,.3)",  color:"#8b949e" },
  "chip-blue":   { bg:"rgba(56,139,253,.1)",   border:"rgba(56,139,253,.3)",   color:"#58a6ff" },
  "chip-purple": { bg:"rgba(188,140,255,.1)",  border:"rgba(188,140,255,.3)",  color:"#bc8cff" },
  "chip-orange": { bg:"rgba(227,179,65,.1)",   border:"rgba(227,179,65,.3)",   color:"#e3b341" },
  "chip-green":  { bg:"rgba(63,185,80,.1)",    border:"rgba(63,185,80,.3)",    color:"#3fb950" }
};

let openIdx = -1;
let running = false;

function cssVars(s) {
  return `--accent:${s.accent};--accent-dim:${s.accentDim};--bg:${s.bg};--bg-done:${s.bgDone};--badge-bg:${s.badgeBg};--badge-bg-done:${s.badgeBgDone};--glow:${s.glow};--dur:${s.dur}ms;`;
}

function buildUI() {
  const pl = document.getElementById("pipeline");
  pl.innerHTML = "";
  steps.forEach((s, i) => {
    const cc = chipColors[s.chipClass];
    const chipsHTML = s.chips.map(c =>
      `<span class="chip" style="background:${cc.bg};border-color:${cc.border};color:${cc.color}">${c}</span>`
    ).join("");

    const card = document.createElement("div");
    card.className = "step";
    card.id = `step-${i}`;
    card.style.cssText = cssVars(s);
    card.innerHTML = `
      <div class="step-inner" onclick="toggleDetail(${i})">
        <span class="step-icon">${s.icon}</span>
        <span class="step-label">${s.label}</span>
        <span class="step-badge">${s.badge}</span>
      </div>
      <div class="step-detail" id="detail-${i}">
        <div class="step-detail-inner">
          <p>${s.detail}</p>
          <div class="detail-chips">${chipsHTML}</div>
        </div>
      </div>
      <div class="progress-bar" id="bar-${i}"></div>`;
    pl.appendChild(card);

    if (i < steps.length - 1) {
      const conn = document.createElement("div");
      conn.className = "connector";
      conn.id = `conn-${i}`;
      conn.style.setProperty("--accent", steps[i+1].accent);
      conn.innerHTML = `<div class="line"></div><div class="arrow"></div>`;
      pl.appendChild(conn);
    }
  });
}

function toggleDetail(i) {
  if (running) return;
  openIdx = openIdx === i ? -1 : i;
  steps.forEach((_, j) => {
    document.getElementById(`detail-${j}`).classList.toggle("open", j === openIdx);
  });
}

async function runPipeline() {
  if (running) return;
  running = true;
  reset(true);
  document.getElementById("run-btn").disabled = true;
  document.getElementById("reset-btn").disabled = true;
  document.getElementById("status").textContent = "Starting…";
  document.getElementById("status").className = "status";

  for (let i = 0; i < steps.length; i++) {
    const s = steps[i];
    const card = document.getElementById(`step-${i}`);
    const bar  = document.getElementById(`bar-${i}`);

    document.getElementById("status").textContent = `Processing: ${s.label}…`;

    card.classList.add("active");
    bar.style.transition = `width ${s.dur}ms linear`;
    void card.offsetWidth;
    bar.style.width = "100%";

    await delay(s.dur + 100);

    card.classList.remove("active");
    card.classList.add("done");

    const conn = document.getElementById(`conn-${i}`);
    if (conn) conn.classList.add("lit");

    await delay(200);
  }

  document.getElementById("status").textContent = "✓ Knowledge base ready — pipeline complete";
  document.getElementById("status").className = "status done";
  document.getElementById("run-btn").disabled = false;
  document.getElementById("run-btn").textContent = "▶ Run again";
  document.getElementById("reset-btn").disabled = false;
  running = false;
}

function reset(silent) {
  steps.forEach((_, i) => {
    const card = document.getElementById(`step-${i}`);
    if (!card) return;
    card.classList.remove("active", "done");
    const bar = document.getElementById(`bar-${i}`);
    bar.style.transition = "none";
    bar.style.width = "0%";
    document.getElementById(`detail-${i}`).classList.remove("open");
    const conn = document.getElementById(`conn-${i}`);
    if (conn) conn.classList.remove("lit");
  });
  openIdx = -1;
  if (!silent) {
    document.getElementById("run-btn").disabled = false;
    document.getElementById("run-btn").textContent = "▶ Run pipeline";
    document.getElementById("reset-btn").disabled = true;
    document.getElementById("status").textContent = "";
    document.getElementById("status").className = "status";
  }
}

function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

buildUI();
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
