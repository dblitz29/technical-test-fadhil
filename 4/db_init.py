# this file creates the SQLite DB and adds a few example documents.
# just run this once before using search.py.

import sqlite3
from datetime import datetime

DB_PATH = "vector_db.sqlite"

def vec_to_str(vec):
    return ",".join(str(x) for x in vec)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            embedding TEXT,
            created_at TEXT
        )
    """)

    cur.execute("SELECT COUNT(*) FROM documents")
    count = cur.fetchone()[0]
    if count == 0:
        docs = [
            ("Reset Password Help",
             "How to reset my account password.",
             [1.0, 0.0, 0.0]),

            ("Track Shipping Order",
             "How to track my shipping and delivery status.",
             [0.0, 1.0, 0.0]),

            ("Refund and Return Policy",
             "Information about refunds and returns.",
             [0.0, 0.0, 1.0]),
        ]
        now = datetime.utcnow().isoformat()
        for title, content, vec in docs:
            cur.execute(
                "INSERT INTO documents (title, content, embedding, created_at) VALUES (?, ?, ?, ?)",
                (title, content, vec_to_str(vec), now)
            )
        conn.commit()
        print(f"Seeded {len(docs)} documents into the database.")
    else:
        print(f"Database already has {count} documents, skipping seeding.")

    conn.close()

if __name__ == "__main__":
    init_db()