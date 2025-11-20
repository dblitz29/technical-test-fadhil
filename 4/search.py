# this code has function for searching documents in a vector database using cosine similarity
# i am using sqlite as vector db and simple word matching boxing for query to vector conversion

import sqlite3
from cosine_similarity import cosine_similarity

DB_PATH = "vector_db.sqlite"

def str_to_vec(s):
    if not s:
        return []
    return [float(x) for x in s.split(",")]

def query_to_vec(q: str):
    q = q.lower().split()
    groups = [
        ["password", "pass", "login", "account"],
        ["ship", "shipping", "delivery", "order", "track"],
        ["refund", "return", "cancel"],
    ]
    vec = [0.0, 0.0, 0.0]
    for token in q:
        for i, keywords in enumerate(groups):
            for kw in keywords:
                if token == kw:
                    vec[i] += 1.0         
                elif token.startswith(kw):
                    vec[i] += 0.5          

    return vec

def load_docs():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, title, content, embedding FROM documents")
    rows = cur.fetchall()
    conn.close()

    docs = []
    for doc_id, title, content, emb_str in rows:
        docs.append({
            "id": doc_id,
            "title": title,
            "content": content,
            "vec": str_to_vec(emb_str),
        })
    return docs

def search(query, top_k=3):
    q_vec = query_to_vec(query)
    docs = load_docs()

    results = []
    for d in docs:
        score = cosine_similarity(q_vec, d["vec"])
        results.append((score, d))

    results.sort(key=lambda x: x[0], reverse=True)
    return results[:top_k]

if __name__ == "__main__":
    print("U need to init DB before using this search.")

    print("\n=== Simple Vector Search (SQLite + cosine manual) ===")
    print("Ketik 'exit' buat keluar.\n")

    while True:
        q = input("Query: ").strip()
        if q.lower() in ("exit", "quit"):
            break

        hits = search(q, top_k=3)
        print("\nHasil:")
        for i, (score, doc) in enumerate(hits, start=1):
            print(f"{i}. [{score:.4f}] {doc['title']}")
            print(f"   {doc['content']}")
        print("-" * 40)