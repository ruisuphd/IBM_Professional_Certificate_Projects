# IBM Professional Certificate Projects

A consolidated portfolio of hands-on projects completed across several IBM Professional Certificate programmes on Coursera. Each subdirectory is a self-contained project with its own README and source code.

## Programmes Covered

| # | Folder | Project |
|---|--------|---------|
| 1 | [`01-data-science`](./01-data-science/) | IBM Data Science Professional Certificate — SpaceX Capstone |
| 2 | [`02-developing-ai-apps-flask`](./02-developing-ai-apps-flask/) | Developing AI Applications with Python and Flask |
| 3 | [`03-image-captioning-gradio`](./03-image-captioning-gradio/) | Image Captioning App with Gradio |
| 4 | [`04-simple-chatbot-huggingface`](./04-simple-chatbot-huggingface/) | Simple Chatbot with Open-Source LLMs (Hugging Face) |
| 5 | [`05-voice-assistant-gpt3-watson`](./05-voice-assistant-gpt3-watson/) | Voice Assistant with OpenAI GPT-3 & IBM Watson |
| 6 | [`06-meeting-companion-stt`](./06-meeting-companion-stt/) | Business AI Meeting Companion (STT) |
| 7 | [`07-chatbot-for-your-data`](./07-chatbot-for-your-data/) | Build a Chatbot for Your Data (RAG) |
| 8 | [`08-babel-fish-llm-stt-tts`](./08-babel-fish-llm-stt-tts/) | Babel Fish — Multilingual LLM with STT & TTS |
| 9 | [`09-personalized-learning`](./09-personalized-learning/) | Building Personalized Learning for Developers |

## Project Summaries

### 01 · Data Science — SpaceX Landing Prediction
**Stack:** Python, Jupyter Notebook, Plotly Dash, SQL  
End-to-end data science capstone predicting SpaceX Falcon 9 first-stage landing success. Covers data collection via REST API and web scraping, EDA with SQL and visualisation, interactive geospatial analysis with Folium, and ML classification (logistic regression, SVM, decision tree, KNN).

### 02 · Developing AI Applications with Python and Flask
**Stack:** Python, Flask, HTML/JS  
Backend AI application development with Flask — routing, templating, REST API design, and integrating IBM Watson NLP services.

### 03 · Image Captioning App with Gradio
**Stack:** Python, Gradio, Hugging Face Transformers  
Web app that generates natural-language captions for uploaded images using a vision-language model, served through a Gradio interface.

### 04 · Simple Chatbot with Open-Source LLMs
**Stack:** Python, Hugging Face Transformers, CSS/JS/HTML  
Conversational chatbot built on open-source LLMs from Hugging Face, with a lightweight browser-based UI.

### 05 · Voice Assistant with OpenAI GPT-3 & IBM Watson
**Stack:** Python, OpenAI API, IBM Watson STT/TTS, HTML/JS, Docker  
Full-stack voice assistant: speech-to-text (Watson), GPT-3 for response generation, text-to-speech (Watson), all containerised with Docker.

### 06 · Business AI Meeting Companion (STT)
**Stack:** Python, IBM Watson Speech-to-Text  
Transcribes and analyses meeting audio, extracting summaries using Watson STT and NLP post-processing.

### 07 · Chatbot for Your Data (RAG)
**Stack:** Python, LangChain, vector store, HTML/JS, Docker  
Retrieval-Augmented Generation chatbot that indexes user-provided documents and answers questions grounded in that data.

### 08 · Babel Fish — Multilingual LLM with STT & TTS
**Stack:** Python, LLM, Watson/OpenAI STT & TTS, JavaScript, Docker, Shell  
Real-time multilingual translation pipeline: speech in → LLM translation → speech out, inspired by the Hitchhiker's Guide to the Galaxy.

### 09 · Personalized Learning for Developers
**Stack:** Python, HTML/JS  
AI-driven personalized learning path generator that adapts content recommendations to a developer's skill profile.

## Getting Started

Each project folder contains a `README.md` with setup instructions specific to that project. Common requirements:

- Python 3.10+
- IBM Cloud account (for Watson services)
- OpenAI API key (for GPT-3/GPT-4 projects)
- Docker (for containerised projects: 05, 07, 08)

## Migrating Source Files

The source code for each project lives in its own repository. To copy the files into this monorepo locally:

```bash
# Clone this repo
git clone https://github.com/ruisuphd/IBM_Professional_Certificate_Projects.git
cd IBM_Professional_Certificate_Projects

# For each source repo, clone it temporarily and copy its contents
# Example for project 01:
git clone https://github.com/ruisuphd/IBM_Data_Science.git /tmp/01
cp -r /tmp/01/. 01-data-science/
rm -rf /tmp/01

# Repeat for the remaining 8 projects, adjusting paths accordingly.
# See each project's README for its source repo URL.

git add .
git commit -m "chore: migrate source files from individual repos"
git push
```

## Licence

Individual projects retain their original licences (MIT or Apache 2.0) as documented in each subdirectory.