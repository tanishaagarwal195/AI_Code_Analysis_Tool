# 🤖 AI-Enhanced Python Code Quality Analysis Tool

A smart assistant for analyzing Python code quality — combining traditional static analysis with GPT-4o-mini powered AI insights. Detects bugs, smells, and maintainability issues in a clean chatbot-style interface.

---

## 🚀 Features

- 📤 Upload or paste Python code
- 🧠 AI-based bug prediction & intelligent refactoring suggestions (GPT-4o)
- 📊 Static analysis using Pylint & Radon
- 🔁 Chatbot-style interactive suggestions
- 📚 AI-powered readability scoring
- 🌡️ Complexity heatmap visualization
- 📝 SQLite-based session logging
- 💻 Simple Streamlit-powered UI

---

## 📦 Project Structure

ASSIGNMENT
├── app/

│ ├── ai_analysis.py # GPT-4o integration for intelligent suggestions

│ ├── static_analysis.py # Handles Pylint and Radon analysis

│ └── db.py # Logs chat and analysis sessions to SQLite

├── app_ui.py # Streamlit-based user interface

├── run_ai_analysis.py # Script for backend testing/debugging

├── sample_code/ # Example Python files for testing

├── requirements.txt # Project dependencies

└── .env # Contains your OpenAI API key (do NOT share)

---

## 🛠️ Installation

```bash
git clone https://github.com/tanishaagarwal195/AI_Code_Analysis_Tool.git
cd ai-code-quality-tool

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the root directory and add your OpenAI API key:

```ini
OPENAI_API_KEY=your_api_key_here
```

## ▶️ Usage

Run the Streamlit app by:

```ini
streamlit run app_ui.py
```

## 💡 Example Output

- 📊 Complexity metrics from **Radon**
- 🤖 AI-suggested refactors with reasoning
- 📚 Readability score: **7/10**
- 💬 Editable follow-up questions for better suggestions

---

## 📈 Bonus Features

- 🌡️ Interactive heatmap of function-level complexity
- 📖 Readability analysis using GPT
- 🗂️ AI chat history persisted using SQLite

---



