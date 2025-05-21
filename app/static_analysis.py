import subprocess
import json
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze

def get_radon_metrics(code):
    complexity = cc_visit(code)
    maintainability = mi_visit(code, True)
    raw_metrics = analyze(code)
    return {
        "cyclomatic_complexity": [c.__dict__ for c in complexity],
        "maintainability_index": maintainability,
        "raw_metrics": raw_metrics._asdict()
    }

def get_pylint_score(filepath):
    result = subprocess.run(['pylint', filepath, '--score', 'y', '-f', 'json'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return {"error": "Pylint failed"}
