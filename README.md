##Live Demo
https://factcheck-agent-fpdz5c3rdkhbo7uqb9shrx.streamlit.app/
# AI Fact-Check Agent

A web application that automatically verifies factual claims from uploaded PDF documents using AI and live web search.

## Overview

This project is a web-based fact-checking tool that analyzes PDF documents and verifies factual claims using AI and live web search. The application extracts claims related to statistics, dates, technical facts, and financial figures, then compares them against real-time web data to identify false or outdated information.

The system performs three main tasks:

1. Extract claims from uploaded PDFs
2. Verify claims using live web data
3. Generate verification results with explanations

---

# Features

- PDF upload interface
- Automatic text extraction
- AI-powered claim detection
- Live web verification
- Verification categories:
  - VERIFIED
  - OUTDATED
  - FALSE
  - INSUFFICIENT DATA
- Evidence-based explanations
- Simple and interactive UI

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI & APIs
- OpenRouter API
- Tavily Search API

## Libraries
- PyMuPDF
- Pandas
- python-dotenv

---

# Project Structure


```bash
factcheck-app/
│
├── app.py
├── requirements.txt
├── README.md
│
└── utils/
    ├── extract_text.py
    ├── claims.py
    └── verify.py
```

# How It Works

1. User uploads a PDF document  
2. Text is extracted from the PDF  
3. AI identifies factual claims from the content  
4. Claims are verified using live web search  
5. The system returns verification results with explanations