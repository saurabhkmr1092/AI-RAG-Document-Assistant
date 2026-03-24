# AI RAG Document Assistant

## 📌 Overview

This project implements a Retrieval-Augmented Generation (RAG) based chatbot that answers user queries using structured company documents (Indecimal).

The system retrieves relevant document chunks and generates grounded responses using a Large Language Model (LLM), ensuring transparency and minimal hallucination.

---

## 🚀 Live Demo

👉 https://ai-rag-document-assistant-34ci.onrender.com

---

## ⚙️ Tech Stack

* Python (Flask)
* FAISS (Vector Similarity Search)
* OpenRouter API (LLM + Embeddings)
* NumPy
* Gunicorn (Production Server)
* Render (Deployment)

---

## 🧠 System Architecture

1. **Document Processing**

   * Input documents are split into meaningful chunks using a custom chunking function.
   * Each chunk represents a logical unit (overview, pricing, journey steps, etc.).

2. **Embedding Generation**

   * Embeddings are generated using OpenRouter embedding API (`text-embedding-3-small`).
   * This approach avoids heavy local models and ensures scalability.

3. **Vector Indexing**

   * All chunk embeddings are stored in a FAISS index.
   * Enables efficient similarity-based retrieval.

4. **Query Processing**

   * User query is converted into embedding.
   * Top-k relevant chunks are retrieved using FAISS.

5. **Answer Generation**

   * Retrieved chunks are passed as context to an LLM (OpenRouter).
   * The model generates answers strictly based on retrieved context.

---

## 🔍 Grounding Strategy

To ensure reliable and factual responses:

* The LLM is explicitly instructed to use only retrieved context.
* No external knowledge is allowed.
* This minimizes hallucination and ensures traceability.

---

## 🔎 Transparency

The system provides full transparency by displaying:

* Retrieved document chunks (context)
* Final generated answer

This allows users to verify how answers are formed.

---

## 📊 Quality Evaluation (Bonus)

The system was evaluated using multiple queries derived from the documents.

| Question                | Retrieval Quality | Answer Quality | Hallucination | Completeness | Notes                 |
| ----------------------- | ----------------- | -------------- | ------------- | ------------ | --------------------- |
| What does Indecimal do? | High              | High           | No            | Complete     | Clear and accurate    |
| Operating principles?   | High              | High           | No            | Complete     | Well grounded         |
| Differentiators?        | High              | High           | No            | Complete     | Matches document      |
| Customer journey?       | High              | medium         | No            | Complete     | partial  |
| Pricing packages?       | High              | High           | No            | Complete     | Accurate values       |
| Package differences?    | Medium            | Good           | No            | Partial      | Some details inferred |
| Stage-based payment?    | High              | High           | No            | Complete     | Clearly explained     |
| Quality assurance?      | High              | High           | No            | Complete     | 445+ checks mentioned |
| Delay prevention?       | High              | Good           | Slight        | Partial      | Slight inference      |
| Maintenance program?    | High              | High           | No            | Complete     | Correct coverage      |

### 🧠 Observations

* Retrieval quality is consistently high due to FAISS-based similarity search.
* Most answers are well-grounded in retrieved context.
* Minor hallucination occurs in questions requiring implicit reasoning.
* System performs best on factual queries explicitly defined in documents.

---

## ⚠️ Design Decisions & Trade-offs

### Embedding Model Choice

* Initially implemented using `sentence-transformers`
* Encountered memory limitations due to torch dependency
* Switched to OpenRouter embeddings for stability and scalability

### Deployment Optimization

* Adapted system to run within constrained environments (Render free tier)
* Removed heavy dependencies
* Used API-based embedding approach

### Deterministic vs Conversational Output

* Current system allows slight variation in responses
* Can be made deterministic by adjusting temperature if required

---



## 🧪 Local LLM Integration (Ollama)

1. **Configuration**

   * The system includes a configurable flag to switch between cloud and local LLM:
   * `USE_LOCAL_LLM = False` (default for deployment)
   * `USE_LOCAL_LLM = True` enables local inference using Ollama

2. **Local Setup**

   * Install Ollama from https://ollama.com
   * Pull the required model:
     * `ollama pull phi3`
   * Run the model locally:
     * `ollama run phi3`

3. **Architecture (Local Mode)**

   * When enabled, the pipeline switches from cloud LLM to local inference:
   * User → FAISS → Context → Ollama (Local LLM) → Answer

4. **Execution Behavior**

   * The system uses a conditional switch to route generation:
     * OpenRouter is used when `USE_LOCAL_LLM = False`
     * Ollama is used when `USE_LOCAL_LLM = True`
   * This design ensures seamless switching without affecting retrieval

5. **Deployment Constraint**

   * Local LLM is supported only in a local environment
   * Render deployment uses OpenRouter due to lack of local model support
   * Embedding generation remains API-based (OpenRouter)

---


## 🛠️ How to Run Locally

1. Clone repository:

```bash
git clone <https://github.com/saurabhkmr1092/AI-RAG-Document-Assistant>
cd <AI-RAG-Document-Assistant>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create `.env` file:

```plaintext
OPENROUTER_API_KEY=your_api_key
```

4. Run application:

```bash
python app.py
```

5. Open in browser:

```plaintext
http://127.0.0.1:5000
```

---

## 🌐 Deployment

* Hosted on Render
* Uses Gunicorn for production serving
* Environment variables managed securely

---


## 👨‍💻 Author

Saurabh Kumar

---

## 📌 Summary

This project demonstrates a complete end-to-end RAG pipeline including document processing, vector search, grounded answer generation, deployment, and evaluation under real-world constraints, with support for both cloud-based and local LLM inference.
