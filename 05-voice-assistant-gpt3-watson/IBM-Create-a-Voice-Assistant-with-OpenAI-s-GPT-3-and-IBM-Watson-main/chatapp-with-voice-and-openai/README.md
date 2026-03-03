# Voice-Enabled Chatbot powered by OpenAI GPT and IBM Watson

A voice-enabled chatbot application that uses IBM Watson's Speech-to-Text and Text-to-Speech services together with OpenAI's GPT models to provide a conversational assistant you can talk to in your browser.

## Prerequisites

- [Docker](https://www.docker.com/) installed and running
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Usage

Build the Docker image:

```bash
docker build . -t voice-chatapp-powered-by-openai
```

Run the container:

```bash
docker run -p 8000:8000 voice-chatapp-powered-by-openai
```

The app will be accessible at `http://localhost:8000`.

### Passing your OpenAI API key at runtime

To avoid baking your API key into the Docker image, pass it as an environment variable when starting the container:

```bash
docker run -p 8000:8000 -e OPENAI_API_KEY="your-key-here" voice-chatapp-powered-by-openai
```

## Features

- **Speech-to-Text** — powered by IBM Watson
- **Text-to-Speech** — powered by IBM Watson
- **AI chat responses** — powered by OpenAI GPT
