import sqlite3
import hashlib
import datetime
import json

DB_FILE = "logs.db"

def init_db():
    """Initialize the database with proper table structure"""
    conn = None
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            code_hash TEXT,
            pylint_score REAL,
            radon_json TEXT,
            ai_response TEXT
        )
        """)
        conn.commit()
    except Exception as e:
        print(f"Database initialization error: {e}")
    finally:
        if conn:
            conn.close()

def log_session(code, pylint_score, radon_json, ai_response):
    """Log a code analysis session to the database"""
    conn = None
    try:
        # Validate code input
        if not code or not isinstance(code, str):
            raise ValueError("Invalid code input")

        code_hash = hashlib.sha256(code.encode()).hexdigest()
        timestamp = datetime.datetime.now().isoformat()

        # ✅ Extract score from various possible formats
        if isinstance(pylint_score, dict):
            pylint_score = pylint_score.get("score")  # Change 'score' to actual key if needed
        elif isinstance(pylint_score, list) and pylint_score:
            pylint_score = pylint_score[0]

        pylint_score = float(pylint_score) if pylint_score is not None else None

        # Serialize radon metrics
        radon_str = json.dumps(radon_json) if radon_json else "null"

        # AI response as string
        ai_response = str(ai_response) if ai_response else ""

        # Insert into DB
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sessions (timestamp, code_hash, pylint_score, radon_json, ai_response)
        VALUES (?, ?, ?, ?, ?)
        """, (timestamp, code_hash, pylint_score, radon_str, ai_response))
        conn.commit()

    except ValueError as ve:
        print(f"Validation error: {ve}")
    except (TypeError, ValueError) as e:
        print(f"Data serialization error: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
