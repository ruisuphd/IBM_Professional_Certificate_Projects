# Building Personalized Learning for Developers

**Source repo:** https://github.com/ruisuphd/IBM-Building-Personalized-Learning-for-Developers  
**Programme:** IBM Generative AI Engineering Professional Certificate (Coursera)  
**Stack:** Python, HTML, JavaScript

## Overview

An AI-driven personalized learning path generator that adapts content recommendations to a developer's current skill profile. The system prompts an LLM with the user's background and goals, then produces a structured, step-by-step learning plan with curated resources.

## Setup

```bash
pip install openai flask
export OPENAI_API_KEY=<your-openai-key>
python app.py
```

Open `http://127.0.0.1:5000`, fill in your skill profile and learning goals, and receive a personalized curriculum.

## Prerequisites

- OpenAI API key (GPT-3.5 or GPT-4)
