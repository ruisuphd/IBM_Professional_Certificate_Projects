# Build a Chatbot for Your Data (RAG)

**Source repo:** https://github.com/ruisuphd/IBM-Build-a-Chatbot-for-Your-Data  
**Programme:** IBM Generative AI Engineering Professional Certificate (Coursera)  
**Stack:** Python, LangChain, vector store (Chroma/FAISS), HTML, JavaScript, Docker

## Overview

A Retrieval-Augmented Generation (RAG) chatbot that indexes user-provided documents (PDF, TXT, etc.) into a vector store and answers natural-language questions grounded in that data. Prevents hallucination by always citing retrieved passages.

## Setup

### With Docker

```bash
docker build -t rag-chatbot .
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=<your-openai-key> \
  rag-chatbot
```

### Without Docker

```bash
pip install langchain openai chromadb flask tiktoken pypdf
export OPENAI_API_KEY=<your-openai-key>
python app.py
```

Open `http://127.0.0.1:8000`, upload your documents, then start chatting.

## Prerequisites

- OpenAI API key (or replace the LLM with any LangChain-compatible model)
