import subprocess
import json
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze
import re
from radon.complexity import cc_visit
import ast
from radon.complexity import cc_visit

def get_radon_metrics(code):
    complexity = cc_visit(code)
    maintainability = mi_visit(code, True)
    raw_metrics = analyze(code)
    return {
        "cyclomatic_complexity": [c.__dict__ for c in complexity],
        "maintainability_index": maintainability,
        "raw_metrics": raw_metrics._asdict()
    }



def get_pylint_score(file_path):
    try:
        result = subprocess.run(
            ["pylint", file_path, "--score=y", "--output-format=text"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        output = result.stdout

        # Extract score using regex
        match = re.search(r"Your code has been rated at ([\d\.]+)/10", output)
        if match:
            return float(match.group(1))
        else:
            return 0.0  # Default if no score found

    except Exception as e:
        print(f"Pylint error: {e}")
        return 0.0




def get_function_complexities(code):
    """Calculate cyclomatic complexity for all functions, marking methods."""
    results = cc_visit(code)
    func_data = []
    for r in results:
        func_type = "method" if r.is_method else "function"
        func_data.append({
            "name": r.name,
            "complexity": r.complexity,
            "type": func_type
        })
    return func_data