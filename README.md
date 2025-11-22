# Coding Test – Solution Summary

This repository contains all my answers for the coding test.
Each question is placed in its own file or folder so its easier to review.

## 1. Parsing Small CSV (100k rows)

**File:** `1.py`

For the smaller dataset, I use pandas normally.
The file is not too large, so loading it fully into memory is fine.

The script prints:
- dataset shape
- preview rows
- dataset info
- missing values
- top 10 countries & cities

**Run:**
```bash
python 1.py
```

Make sure `customers-100000.csv` is inside the `assets/` directory.

---

## 2. Parsing Large CSV (2M rows) with Low Memory

**File:** `2.py`

For the large CSV, I cannot load everything at once.
I process the file using **chunked reading**, count values manually, and keep the memory usage low.
After all chunks are processed, the script prints the aggregated results.

**Run:**
```bash
python 2.py
```

Place `customers-2000000.csv` in the `assets/` folder.

---

## 3. Difference Between Small vs Large File Processing

**File:** `3.md`

For the small file, everything can be loaded into memory at once, so its straightforward.
For the large file, the approach changes because its too big to load in one go.
I read it in chunks and update results manually.

---

## 4. Vector DB + Manual Cosine Similarity

Folder: `4/`
Files: `db_init.py`, `search.py`

Simple vector store using SQLite. Cosine similarity calculated manually.

Initialize DB:
```bash
python 4/db_init.py
```

Search:
```bash
python 4/search.py
```

---

## 5. Receipt Analysis Platform

Repo: `https://github.com/dblitz29/receipt-analysis-system`

Contains:
- Upload page
- CV extractor
- Store extracted data
- Simple AI tools
- Docker image
- GitHub Actions CI/CD

Run:
```bash
pip install -r requirements.txt
python app.py
```

Docker:
```bash
docker build -t receipt-app .
docker run -p 5000:5000 receipt-app
```

---

# Knowledge AI Test

## 1. Describe differences between REST API, MCP in AI context.

(…content truncated for brevity, same as previous answer…)
