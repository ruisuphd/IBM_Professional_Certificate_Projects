# Voice Assistant with OpenAI GPT-3 & IBM Watson

**Source repo:** https://github.com/ruisuphd/IBM-Create-a-Voice-Assistant-with-OpenAI-s-GPT-3-and-IBM-Watson  
**Programme:** IBM Generative AI Engineering Professional Certificate (Coursera)  
**Stack:** Python, OpenAI API, IBM Watson STT, IBM Watson TTS, HTML, CSS, JavaScript, Docker

## Overview

A full-stack voice assistant: the browser captures microphone input, IBM Watson Speech-to-Text transcribes it, OpenAI GPT-3 generates a response, and IBM Watson Text-to-Speech reads it back.

## Setup

### With Docker

```bash
docker build -t voice-assistant .
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=<your-openai-key> \
  -e WATSON_STT_API_KEY=<your-watson-stt-key> \
  -e WATSON_STT_URL=<your-watson-stt-url> \
  -e WATSON_TTS_API_KEY=<your-watson-tts-key> \
  -e WATSON_TTS_URL=<your-watson-tts-url> \
  voice-assistant
```

### Without Docker

```bash
pip install openai ibm-watson flask
export OPENAI_API_KEY=<your-openai-key>
export WATSON_STT_API_KEY=<your-watson-stt-key>
export WATSON_STT_URL=<your-watson-stt-url>
export WATSON_TTS_API_KEY=<your-watson-tts-key>
export WATSON_TTS_URL=<your-watson-tts-url>
python app.py
```

Open `http://127.0.0.1:8000` in your browser and allow microphone access.

## Prerequisites

- [IBM Cloud](https://cloud.ibm.com/) account with Speech-to-Text and Text-to-Speech service instances
- OpenAI API key
