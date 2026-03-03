# Business AI Meeting Companion (STT)

**Source repo:** https://github.com/ruisuphd/IBM-Business-AI-Meeting-Companion  
**Programme:** IBM Generative AI Engineering Professional Certificate (Coursera)  
**Stack:** Python, IBM Watson Speech-to-Text

## Overview

Transcribes and analyses meeting audio using IBM Watson Speech-to-Text. Post-processing with NLP extracts key topics, action items, and a concise summary from the transcript, acting as an AI-powered meeting companion.

## Setup

```bash
pip install ibm-watson flask
export WATSON_STT_API_KEY=<your-watson-stt-key>
export WATSON_STT_URL=<your-watson-stt-url>
python app.py
```

## Usage

1. Upload a meeting audio file (WAV or MP3) via the web interface.
2. Watson STT returns a full transcript.
3. NLP post-processing extracts a summary, key topics, and action items.

## Prerequisites

- [IBM Cloud](https://cloud.ibm.com/) account with a Speech-to-Text service instance
