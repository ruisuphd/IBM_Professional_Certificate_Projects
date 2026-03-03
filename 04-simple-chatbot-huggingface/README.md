# Simple Chatbot with Open-Source LLMs (Hugging Face)

**Source repo:** https://github.com/ruisuphd/IBM-Create-Simple-Chatbot-with-Open-Source-LLMs-using-Python-and-Hugging-Face  
**Programme:** IBM Generative AI Engineering Professional Certificate (Coursera)  
**Stack:** Python, Hugging Face Transformers, HTML, CSS, JavaScript

## Overview

A conversational chatbot powered by an open-source LLM served via a Python backend, with a browser-based chat UI. Demonstrates prompt construction, conversation history management, and integrating a Hugging Face pipeline into a web app.

## Setup

```bash
pip install transformers torch accelerate flask
python app.py
```

Open the URL printed in the terminal.

## Notes

- Model is loaded from Hugging Face Hub on first run; requires ~4 GB disk space depending on the model.
- A GPU is recommended but not required.
