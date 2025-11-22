Coding Test – Solution Summary

This repo contains my answers for all parts of the Shopee coding test.
Each question is placed in its own file/folder so it’s easier to check.

1. Parsing small CSV (100k rows)

File: 1.py

I used pandas because the file is not too big, so loading it into memory is fine.
The script prints the dataset shape, simple stats, missing values, and also the top 10 countries and cities.

Make sure the file customers-100000.csv is inside the assets/ folder.

2. Parsing large CSV (2M rows) with low memory

File: 2.py

For the big CSV, I don’t load everything at once.
I process it using chunked reading, and count values manually so the memory stays small.
The script shows the aggregated stats after finishing all chunks.

Put customers-2000000.csv in the assets/ directory.

3. Difference between small vs large file processing

File: 3.md

Short explanation of the approach difference:
small file → load everything, use regular pandas features
large file → read in chunks, update counters manually, keep memory low

4. Vector DB + Cosine Similarity (No high-level library)

Folder: 4/
Files: db_init.py, search.py

I built a tiny vector store using SQLite.
Embeddings are stored as comma-separated strings, then loaded back as float vectors.
Cosine similarity is implemented manually without numpy/FAISS/other libs.

5. Receipt Analysis Platform (UI + CV + DB + LLM)

Repo:
https://github.com/dblitz29/receipt-analysis-system

Inside that repo there are several parts:
upload page (simple web UI)
extraction using computer vision
store receipt info into database
basic AI tools so user can ask things like:
docker container
CI/CD using GitHub Actions