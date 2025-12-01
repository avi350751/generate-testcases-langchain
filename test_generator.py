import os
import logging
from typing import Any, Dict, List, Tuple
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_template("""
You are a senior QA engineer.

Given the user story and acceptance criteria, 
Perform every possible permutation and combination and
generate positive, negative and edge test cases.
Don't justify your answers.
Don't give information not mentioned in the CONTEXT INFORMATION.
Do not say "according to the context" or "mentioned in the context" or similar.
Respond in the following JSON format:

{{
  "test_cases": [
    {{
      "id": "TC-001",
      "title": "string",
      "type": "happy | negative | edge",
      "preconditions": ["..."],
      "steps": ["step 1", "step 2", "..."],
      "expected_result": "..."
    }}
  ]
}}

User story:
{user_story}

Acceptance criteria:
{acceptance_criteria}
""")

chain = prompt | llm | parser

def generate_test_cases(user_story: str, acceptance_criteria: str) -> dict:
    """Call the LLM chain and return the parsed JSON."""
    return chain.invoke(
        {
            "user_story": user_story,
            "acceptance_criteria": acceptance_criteria,
        }
    )