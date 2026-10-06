# Customer-Sentiment-Analysis-Gen-AI
FastAPI-based GenAI customer sentiment analysis using Ollama and structured outputs.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103+-green.svg)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Supported-lightgrey.svg)](https://python.langchain.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
This repository provides an enterprise-grade Generative AI application engineered to extract, analyze, and interpret customer sentiment from unstructured text. By utilizing Large Language Models (LLMs) via LangChain and a high-performance FastAPI backend, this system surpasses traditional lexicon-based sentiment analysis to understand context, intent, urgency, and nuanced emotional tone.

It is designed for seamless integration into existing Customer Relationship Management (CRM) platforms, helpdesk systems, and data analytics pipelines to provide actionable business intelligence.

## Table of Contents
1. [Architecture & Features](#architecture--features)
2. [Technology Stack](#technology-stack)
3. [Environment Configuration](#environment-configuration)
4. [Installation & Setup](#installation--setup)
5. [API Documentation](#api-documentation)
6. [Project Structure](#project-structure)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Contributing](#contributing)

## Architecture & Features

* **Context-Aware Processing:** Employs advanced prompt engineering and LLMs to detect sarcasm, mixed sentiments, and domain-specific terminology.
* **Asynchronous Backend:** Built on FastAPI to handle high-throughput, concurrent requests with minimal latency.
* **Modular Pipeline:** Decoupled architecture separating data ingestion, LLM inference, and response formatting, allowing for straightforward model swapping (e.g., OpenAI, Anthropic, Google Gemini, or local open-source models).
* **Data Validation:** Strict input/output validation utilizing Pydantic models to ensure reliable API contracts and prevent prompt injection vulnerabilities.

## Technology Stack

* **Core Language:** Python 3.8+
* **API Framework:** FastAPI, Uvicorn (ASGI server)
* **AI & NLP:** LangChain, LLM Provider SDKs (OpenAI, Google)
* **Data Processing:** Pandas, NumPy
* **Validation & Settings:** Pydantic

## Environment Configuration

Create a `.env` file in the root directory. Use `.env.example` as a template for your local configuration.

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `LLM_PROVIDER` | The AI provider to use (e.g., `openai`, `gemini`) | `openai` | Yes |
| `API_KEY` | Authentication key for the chosen LLM provider | `None` | Yes |
| `MODEL_NAME` | Specific model version (e.g., `gpt-4`, `gemini-pro`) | `gpt-3.5-turbo` | No |
| `PORT` | The port on which the FastAPI server runs | `8000` | No |
| `DEBUG_MODE` | Enables detailed logging and stack traces | `False` | No |

## Installation & Setup

### Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alindapal07/Customer-Sentiment-Analysis-Gen-AI.git](https://github.com/alindapal07/Customer-Sentiment-Analysis-Gen-AI.git)
   cd Customer-Sentiment-Analysis-Gen-AI
Initialize a virtual environment:


##Author
Alinda Pal

Full-Stack Software Engineer
