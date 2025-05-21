from app.static_analysis import get_radon_metrics, get_pylint_score
from app.ai_analysis import analyze_code_with_ai

def analyze_code(filepath):
    # Read code
    with open(filepath, "r") as f:
        code = f.read()

    # Static analysis
    static_results = {
        "pylint_score": get_pylint_score(filepath),
        "radon_metrics": get_radon_metrics(code)
    }

    # AI analysis
    ai_response = analyze_code_with_ai(code)

    return {
        "static": static_results,
        "ai": ai_response,
        "original_code": code
    }

if __name__ == "__main__":
    import pprint
    result = analyze_code("sample_code/test.py")
    pprint.pprint(result)
