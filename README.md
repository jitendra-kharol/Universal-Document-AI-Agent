# Universal Document AI Agent 🤖

A simple AI-powered document question-answering project using **RAG (Retrieval-Augmented Generation)**.

The user provides a document, the system processes it, creates embeddings, stores them in **Qdrant**, and retrieves relevant information to answer user questions.

## Features

* Upload and process documents
* Text splitting and embeddings
* Semantic search
* Qdrant Vector Database
* RAG-based question answering
* Hugging Face LLM integration

## Technologies

* Python
* LangChain
* Hugging Face
* Sentence Transformers
* Qdrant
* RAG
* Vector Database

## How It Works

```text
Document
   ↓
Text Extraction
   ↓
Text Splitting
   ↓
Embeddings
   ↓
Qdrant Vector Database
   ↓
User Question
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
LLM Answer
```

## Installation

```bash
git clone https://github.com/jitendra-kharol/Universal-Document-AI-Agent.git
cd Universal-Document-AI-Agent
pip install -r requirements.txt
```

Create a `.env` file and add your API keys.

```env
HF_TOKEN=your_huggingface_token
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
```

Run the project:

```bash
python main.py
```

## Note

The `documents/` folder is not uploaded to GitHub because it contains the local/user-uploaded documents.

## Author

**Jitendra Kharol**

GitHub: `jitendra-kharol`
