from app.ai_analysis import analyze_code_with_ai

with open("sample_code/test.py", "r") as f:
    code = f.read()

result = analyze_code_with_ai(code)
print("🤖 AI Analysis:\n")
print(result)
