from app.static_analysis import get_radon_metrics, get_pylint_score

with open("sample_code/test.py", "r") as f:
    code = f.read()

print("🔍 Radon Metrics:")
print(get_radon_metrics(code))

print("\n🧹 Pylint Score:")
print(get_pylint_score("sample_code/test.py"))
