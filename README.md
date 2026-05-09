# AI Fact-Check Agent

A web application that automatically verifies factual claims from uploaded PDF documents using AI and live web search.

## Overview

This project extracts claims from PDF files and validates them against live internet sources. It helps identify outdated statistics, false claims, and unsupported information in marketing, research, or technical documents.

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
- Google Gemini API
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
├── .env
│
└── utils/
    ├── extract_text.py
    ├── claims.py
    └── verify.py