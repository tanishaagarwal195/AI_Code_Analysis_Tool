import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


def analyze_code_with_ai(code, chat_state=None):
    """
    Analyze Python code using OpenAI and maintain conversation history using chat_state.
    """
    prompt = f"""
You are an advanced code analysis assistant helping developers improve Python code.

Analyze the following code and provide:

1. 🐞 **Bug Predictions**  
   - Identify any parts of the code that may raise runtime errors, logic bugs, or unsafe operations.

2. 🧹 **Code Quality Issues**  
   - Style violations, lack of typing, missing edge case handling, poor naming, etc.

3. 💡 **Improvement Suggestions**  
   - Refactor suggestions, readability upgrades, performance optimizations, with examples.

4. 📊 **Maintainability Impact Ranking**  
   - Rank all issues from High → Medium → Low impact on code maintainability.

5. 🔁 Conversational modular feedback  
   - Modular responses so the user can follow-up with targeted questions.

### Python Code:
```python
{code}
"""
    
    # Use provided chat_state
    if chat_state:
        chat_state.add_user_message(prompt)
        messages = chat_state.get_conversation()
    else:
        messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3
    )

    reply = response.choices[0].message.content

    if chat_state:
        chat_state.add_ai_message(reply)

    return reply


def get_readability_score(code, chat_state=None):
    """
    Evaluate the readability and maintainability of Python code using OpenAI.
    Returns a scored assessment with specific feedback.
    """
    prompt = f"""
You are a senior software engineer and expert in code readability assessment.

Your task is to review the following Python code and:
- Rate its readability and maintainability on a scale of 1 (very poor) to 10 (excellent).
- Justify your rating with specific observations about the code style, clarity, documentation, and structure.
- Suggest concrete ways to improve the score if applicable.

Return your response in this format:
Score: X/10
Explanation: ...

Code:
{code}
"""
    messages = [{"role": "user", "content": prompt}]

    if chat_state:
        chat_state.add_user_message(prompt)
        messages = chat_state.get_conversation()  # Changed from get_history() to get_conversation()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.2
    )

    output = response.choices[0].message.content
    if chat_state:
        chat_state.add_ai_message(output)
    return output