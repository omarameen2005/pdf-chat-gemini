# 📄 Chat with your PDF — RAG App

A production-ready Retrieval-Augmented Generation (RAG) application that lets you upload any PDF and ask questions about it in plain English. Built with **Gemini API**, **ChromaDB**, and **Streamlit**.

---

## 🚀 Live Demo

[👉 Open the app](https://pdf-chat-gemini-f5wvqbq8zubmvhwceqknbw.streamlit.app/)

---

## ✨ Features

- 📤 Upload any PDF and get it indexed in seconds
- 💬 Ask natural-language questions about the document
- 🔍 Semantic search using Gemini embeddings (not just keyword matching)
- 🧠 Answers grounded strictly in the document — no hallucination
- 🔄 Upload a new PDF anytime to start a fresh session
- 🗂️ Persistent vector store using ChromaDB

---

## 🏗️ Architecture

```
pdf-chat-gemini/
│
├── app.py               # Streamlit UI — entry point
├── config.py            # All constants (models, chunk size, paths)
├── requirements.txt
├── .env                 # Your API key (never committed)
├── .env.example         # Template for contributors
│
└── core/
    ├── pdf_processor.py # PDF text extraction + chunking
    ├── embedder.py      # Gemini embedding (document + query)
    ├── vector_store.py  # ChromaDB index/search/delete
    └── rag_chain.py     # Full RAG pipeline orchestration
```

### How it works

```
User uploads PDF
      ↓
Extract text (PyPDF)
      ↓
Split into ~500-char overlapping chunks
      ↓
Embed each chunk (Gemini: task_type=retrieval_document)
      ↓
Store in ChromaDB (persisted to disk)
      ↓
User asks a question
      ↓
Embed question (Gemini: task_type=retrieval_query)
      ↓
Retrieve top-3 most relevant chunks from ChromaDB
      ↓
Build prompt: context + question → Gemini Flash
      ↓
Return grounded answer
```

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit |
| LLM | Gemini 2.5 Flash Lite |
| Embeddings | Gemini Embedding 001 |
| Vector DB | ChromaDB (local persistent) |
| PDF Parsing | PyPDF |
| Config | python-dotenv |

---

## ⚙️ Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/omarameen2005/pdf-chat-gemini.git
cd pdf-chat-gemini
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

```bash
cp .env.example .env
```

Open `.env` and add your key:

```
GEMINI_API_KEY=your_key_here
```

Get a free key at [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🔧 Configuration

All behaviour is controlled from `config.py` — no need to touch any other file:

| Variable | Default | Description |
|---|---|---|
| `EMBEDDING_MODEL` | `gemini-embedding-001` | Gemini embedding model |
| `CHAT_MODEL` | `gemini-2.5-flash-lite` | Gemini chat model |
| `CHUNK_SIZE` | `500` | Characters per chunk |
| `CHUNK_OVERLAP` | `50` | Overlap between chunks |
| `TOP_K_RESULTS` | `3` | Chunks retrieved per query |
| `CHROMA_PATH` | `chroma_store` | Local ChromaDB directory |

---

## 📁 .env.example

```
GEMINI_API_KEY=your_gemini_api_key_here
```

---

## 🚢 Deployment (Streamlit Cloud)

See the [Deployment Guide](#) below, or follow these steps:

1. Push this repo to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Set `GEMINI_API_KEY` in **Secrets** (Streamlit's secure env system)
5. Click **Deploy** — done in ~2 minutes

---

## 📌 Roadmap

- [ ] Multi-PDF support
- [ ] Streaming responses
- [ ] Chat history export
- [ ] Source citation (highlight which chunk answered the question)
- [ ] Support for DOCX and TXT files

---

## 📄 License

MIT — free to use, modify, and deploy.

---

## 🙋 About

Built as part of a learning journey into AI Automation freelancing.  
Tools used: Gemini API · ChromaDB · Streamlit · Python