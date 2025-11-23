# Coding Test – Solution Summary

This repository contains all my answers for the coding test.  
Each question is placed in its own file or folder so its easier to review.

---

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

For the small file, everything can be loaded into memory at once, so its straightforward. I can use pandas normally, explore the whole dataset, and run things like value_counts() or describe() without worrying about memory.

For the large file, the approach changes because its too big to load in one go. Instead of reading the entire CSV, I read it in chunks. Each chunk is processed and then discarded, which keeps memory usage low. I can still count things like countries and cities, but I have to do it manually by updating a dictionary, since I dont have the full dataset in memory.
- **Small file** : load everything, use pandas features directly.  
- **Large file** : read chunk-by-chunk and only store what’s needed.  

The complete explanation is inside the markdown file.

---

## 4. Vector DB + Manual Cosine Similarity

**Folder:** `4/`  
**Files:** `db_init.py`, `search.py`

I created a simple vector store using SQLite.  
Each embedding is stored as a comma-separated string, then converted back into floats when searching.  
Cosine similarity is implemented manually without using numpy, FAISS, or other high-level libraries.

**Initialize the database:**
```bash
python 4/db_init.py
```

**Search using cosine similarity:**
```bash
python 4/search.py
```

---

## 5. Receipt Analysis Platform (UI + CV + DB + LLM)

**Repo:**  
https://github.com/dblitz29/receipt-analysis-system

The project contains:
- upload page for food receipts  
- computer vision extractor  
- store extracted data into a database  
- basic AI tools so users can ask things 
- packaged into a Docker image  
- CI/CD via GitHub Actions  

**Run locally:**
```bash
pip install -r requirements.txt
python app.py
```

**Run with Docker:**
```bash
docker build -t receipt-app .
docker run -p 5000:5000 receipt-app
```

---

## Notes

- For question #4, no external vector libraries were used.

<br><br><br>

# Knowledge AI Test

Engineering Knowledge AI Agent Test

## 1. Describe differences between REST API, MCP in the context of AI.

Answer : 
REST API and MCP have major differences even though both of them are useful to run AI engine, especially from their protocol to communication. The major difference is REST API is stateless and traditional, instead MCP designed for dynamic and contextual communication. Besides that there are some aspect that made REST API different than MCP.



## 2. How REST API, MCP, can improve the AI use case?

Answer :

Both of them improve the AI use case.
REST API helps systems by allowing them to connect with external services and data source. For example, an AI chatbot use a REST API to fetch weather data, stock prices, or user information from a database. REST is stateless, its simple, widely supported, and works well for tasks

MCP on other hand is more supported for AI agents that need to maintain context over time. It allows AI engine to remember previous messages, use tools calling dynamically, and handle more complex, multi-step tasks. Some of scenarios like virtual assistants, customer support bots or autonomous agents that need to reason, plan, adapt based ongoing conversation


## 3. How do you ensure that your AI agent answers correctly?

Answer :

To make sure an AI agent gives correct answers, several practical steps can be followed. These steps help the agent stay accurate, consistent, and reliable:

Use a trusted data source
The agent should always refer to a verified source, such as a database or a curated knowledge base. Using clean and reliable data reduces the chance of wrong answers.

Set clear rules
The agent needs simple and clear instructions about what it can answer, what it should avoid, and the expected format. Clear rules make the output more stable.

Provide the right context
 When a task requires specific information, the correct documents or data must be attached to the query. This ensures the agent answers based on real references rather than guessing.

Check the output
The agent’s output should be reviewed before it is used. For example, when the agent generates SQL, the structure and logic of the query can be checked to make sure it is valid and reasonable.

Use fallback options
When the first answer looks incorrect, incomplete, or not in the right format, a fallback process can be triggered. This may involve regenerating the answer with simpler rules or returning a safe explanation instead of a wrong output.

Evaluate and improve regularly
Ongoing evaluation helps the agent become more accurate over time. Some simple evaluation methods include:

Sample checking: Random answers are reviewed manually.

Error tracking: Mistakes are logged and patterns are identified.

User feedback: Feedback from users is collected to spot unclear or incorrect responses.

Test prompts: Regular test questions are used to check if the agent still follows the rules.

Comparison with ground truth: When a correct answer exists, the agent’s output is compared with it.


## 4. Describe what can you do with Docker / Containerize environment in the context of AI.

Answer:

In the context of AI, Docker helps keep everything consistent and easy to deploy. It lets the model, code, and dependencies run in the same environment across different machines.

Docker also makes it easier to package GPU or CPU requirements, manage versioning of each model build, and scale the inference service when traffic grows. For training jobs, containers help ensure that each run uses the same setup, which makes experiments more reliable.

Overall, Docker gives a clean, repeatable, and portable environment for both AI training and serving.


## 5. How do you finetune the LLM model from raw ?

To fine-tune an LLM from raw data, the process usually looks like this:

Define the task
First decide what the model should do better: for example, customer support Q&A, code generation, or classification. This will guide how the data is prepared.

Prepare and clean the data
Take the raw data and turn it into a clear input–output format (e.g. prompt  -> answer). Remove sensitive data, duplicates, and noisy content. Add simple metadata if needed (language, domain, difficulty).

Format into training examples
Convert each example into the model’s prompt style (system + user + assistant, or instruction + response). Then split into train / validation / test sets.

Set up the training pipeline
Load a base LLM, set tokenizer, max sequence length, batch size, and learning rate. For large models, often use parameter-efficient methods like LoRA / QLoRA so training is cheaper and fits on limited GPUs.

Train and monitor
Run fine-tuning on the training set, while watching loss and key metrics on the validation set. Use early stopping or regularization to avoid overfitting.

Evaluate quality and safety
After training, test on a held-out dataset and some real examples. Check not only accuracy and relevance, but also hallucinations, latency, and safety (no leakage of sensitive info, no harmful content).

Deploy and iterate
Package the fine-tuned model into a serving container (e.g. Docker), expose it via API, then monitor logs and user feedback. If new data comes in, repeat the process and refresh the model.

