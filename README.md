# 🔍 Real-Time Research Copilot

## Overview

Real-Time Research Copilot is an AI-powered research assistant that combines real-time web search and Retrieval-Augmented Generation (RAG) to answer questions from both live web sources and uploaded PDF documents.

The application enables users to:

* Research current topics from the web
* Upload PDFs and ask questions about them
* Retrieve relevant information using semantic search
* Generate accurate answers using Large Language Models

---

## Features

### 🌐 Web Research Mode

* Real-time web search using Tavily
* AI-generated answers using Groq
* Clickable source references
* Fast response times

### 📄 PDF Research Mode

* Upload PDF documents
* Automatic text extraction
* Text chunking for efficient retrieval
* Semantic search using FAISS
* Question Answering over uploaded documents

---

## Architecture

### Web Research Pipeline

User Question
↓
Tavily Search
↓
Top Relevant Results
↓
Groq LLM
↓
Answer + Sources

### PDF Research Pipeline

PDF Upload
↓
Text Extraction
↓
Chunking
↓
Embeddings (nomic-embed-text)
↓
FAISS Vector Index
↓
Semantic Retrieval
↓
Groq LLM
↓
Answer

---

## Tech Stack

### Frontend

* Streamlit

### Search

* Tavily Search API

### LLM

* Groq
* Llama 3.3 70B Versatile

### Embeddings

* Ollama
* nomic-embed-text

### Vector Search

* FAISS

### Language

* Python

---

## Project Structure

```text
app.py              # Streamlit UI
search.py           # Web Search Logic
llm.py              # Groq Integration
rag.py              # PDF RAG Pipeline

test.py
test_rag.py
test_embeddings.py
test_faiss.py
test_rag_answer.py

README.md
requirements.txt
.env
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd real-time-research-copilot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_tavily_key
GROQ_API_KEY=your_groq_key
```

---

## Run the Application

```bash
streamlit run app.py
```

Application runs at:

```text
http://localhost:8501
```

---

## Key Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Embeddings
* Vector Databases
* FAISS Indexing
* Prompt Engineering
* LLM Integration
* Real-Time Information Retrieval

---

## Future Improvements

* Multi-PDF Support
* Chat History
* Hybrid Web + PDF Search
* Cloud Deployment
* Source Citations for PDF Answers

---

## Author

Muhammed Faris

Aspiring Data Scientist and AI/ML Engineer passionate about Generative AI, Machine Learning, Data Science, and Intelligent Search Systems.
