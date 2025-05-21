import openai
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Read the key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_code_with_ai(code):
    prompt = f"""
You are an expert code reviewer. Analyze the following Python code:
- Identify bugs or issues.
- Suggest improvements with examples.
- Rank issues by impact on maintainability.

Code:
{code}

Return your output as a clear explanation with rankings.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response['choices'][0]['message']['content']
