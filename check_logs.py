import sqlite3

conn = sqlite3.connect("logs.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sessions")
rows = cursor.fetchall()

print("ID | Timestamp | Code (Truncated) | Pylint Score | Radon Metrics (Truncated) | AI Feedback (Truncated)")
print("-" * 120)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2][:30]}... | {row[3]} | {row[4][:30]}... | {row[5][:30]}...")

conn.close()
