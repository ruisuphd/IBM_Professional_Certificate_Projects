# Babel Fish — Multilingual LLM with STT & TTS

**Source repo:** https://github.com/ruisuphd/IBM-Babel-Fish-LLM-STT-TTS  
**Programme:** IBM Generative AI Engineering Professional Certificate (Coursera)  
**Stack:** Python, LLM (OpenAI / Hugging Face), IBM Watson / OpenAI STT & TTS, JavaScript, Docker, Shell

## Overview

A real-time multilingual translation pipeline inspired by the Babel Fish from *The Hitchhiker's Guide to the Galaxy*. Users speak in any supported language; the app transcribes the speech, passes it to an LLM for translation, and reads the translated text aloud in the target language.

## Pipeline

```
Microphone → STT (Watson/OpenAI Whisper) → LLM Translation → TTS (Watson/OpenAI) → Speaker
```

## Setup

### With Docker

```bash
docker build -t babel-fish .
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=<your-openai-key> \
  -e WATSON_STT_API_KEY=<your-watson-stt-key> \
  -e WATSON_STT_URL=<your-watson-stt-url> \
  -e WATSON_TTS_API_KEY=<your-watson-tts-key> \
  -e WATSON_TTS_URL=<your-watson-tts-url> \
  babel-fish
```

### Without Docker

```bash
pip install openai ibm-watson flask
export OPENAI_API_KEY=<your-openai-key>
# Set remaining Watson env vars as above
python app.py
```

Open `http://127.0.0.1:8000`, select source and target languages, then speak.

## Prerequisites

- OpenAI API key
- IBM Cloud account with Speech-to-Text and Text-to-Speech service instances
