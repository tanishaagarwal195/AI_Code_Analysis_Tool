import streamlit as st
from app.static_analysis import get_pylint_score, get_radon_metrics, get_function_complexities
from app.ai_analysis import analyze_code_with_ai, get_readability_score
from app.chat_state import ChatState
from app.logger import init_db, log_session
import matplotlib.pyplot as plt
import seaborn as sns



init_db()

# Initialize chat state
if "chat_state" not in st.session_state:
    st.session_state.chat_state = ChatState()

st.set_page_config(page_title="AI Code Analyzer", layout="wide")
st.title("🧠 AI-Enhanced Python Code Quality Analyzer")

st.markdown("""
Choose how you'd like to input your Python code:
- 📁 Upload a `.py` file
- 📝 Or paste your code directly
""")

# Input method
input_method = st.radio("Choose input method", ["Upload .py file", "Paste code"])

code = ""

# File upload
if input_method == "Upload .py file":
    uploaded_file = st.file_uploader("Upload your Python file", type=["py"])
    if uploaded_file is not None:
        code = uploaded_file.read().decode("utf-8")
        st.code(code, language="python")

# Paste code
elif input_method == "Paste code":
    code = st.text_area("Paste your Python code below", height=300, placeholder="def example():\n    print('Hello')")
    if code:
        st.code(code, language="python")

if code:
    # Save to temp file for pylint analysis
    temp_path = "temp_uploaded_code.py"
    with open(temp_path, "w", encoding="utf-8") as f:
        f.write(code)

    st.subheader("🔍 Static Analysis Results")

    pylint_score = get_pylint_score(temp_path)
    radon_metrics = get_radon_metrics(code)

    st.write(f"**Pylint Score:** {pylint_score}/10")
    st.write("**Radon Cyclomatic Complexity:**")
    st.json(radon_metrics)

    st.subheader("🤖 AI-Powered Code Review")

    


    if st.button("Run AI Analysis"):
        ai_response = analyze_code_with_ai(code, chat_state=st.session_state.chat_state)
        st.session_state.last_ai_response = ai_response
        log_session(code, pylint_score, radon_metrics, ai_response)
        st.markdown("**AI Feedback:**")
        st.write(ai_response)

    st.subheader("📊 Code Readability Assessment")

    if st.button("Get Readability Score"):
        readability = get_readability_score(code, chat_state=st.session_state.chat_state)
        st.markdown("**Readability Analysis:**")
        st.write(readability)

    if "last_ai_response" in st.session_state:
        st.subheader("💬 Refine the AI Suggestions")
        followup = st.text_area("Enter a follow-up prompt", placeholder="e.g. Optimize for memory efficiency...")
        if st.button("Send Follow-up"):
            st.session_state.chat_state.add_user_message(followup)
            response = analyze_code_with_ai(code, chat_state=st.session_state.chat_state)
            st.session_state.chat_state.add_ai_message(response)
            st.markdown("**AI Response:**")
            st.write(response)

    st.subheader("🌡️ Code Complexity Heatmap")

    func_complexities = get_function_complexities(code)

    if func_complexities:
        st.markdown("Visualizing cyclomatic complexity of each function:")
        func_names = [f["name"] for f in func_complexities]
        scores = [f["complexity"] for f in func_complexities]

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=scores, y=func_names, palette="coolwarm", ax=ax)
        ax.set_xlabel("Complexity Score")
        ax.set_ylabel("Function Name")
        st.pyplot(fig)
    else:
        st.info("No functions found in the code for complexity analysis.")


