### Generate Test Cases Automatically from User Stories & Acceptance Criteria

This project demonstrates how to use LangChain, OpenAI GPT models, and structured output parsers to automatically generate high-quality test cases for manual and automation QA workflows.

It follows a simple architecture:

User Story + Acceptance Criteria
        ↓
LangChain Prompt Template
        ↓
LLM (GPT-4.1-mini)
        ↓
JsonOutputParser
        ↓
Structured Test Cases in JSON

🔥 Features

Convert any user story into structured test cases.
Uses LangChain Expression Language (LCEL) for clean chaining.
Enforces strict JSON output using JsonOutputParser.

Produces:

- Happy path test cases
- Negative scenarios
- Edge case scenarios
- Easy to integrate into CI/CD, Promptfoo evaluation, or Auto-Test pipelines.

📂 Project Structure
project2-langchain/
│── helper.py
│── test_generator.py
│── requirements.txt
│── README.md
│── .env
│── .gitignore

# Getting started
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows

pip install -r requirements.txt

streamlit run helper.py