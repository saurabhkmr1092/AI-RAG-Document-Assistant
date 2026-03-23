from chunks import create_chunks
import faiss
import numpy as np
import requests
import os
from dotenv import load_dotenv


load_dotenv()


# Step 1: Load chunks
chunks = create_chunks()
texts = [chunk["text"] for chunk in chunks]

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")


# 🔹 Get embedding from OpenRouter
def get_embedding(text):
    response = requests.post(
        url="https://openrouter.ai/api/v1/embeddings",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": "text-embedding-3-small",
            "input": text
        }
    )
    return response.json()["data"][0]["embedding"]


# 🔹 Create FAISS index (once)
embeddings = [get_embedding(text) for text in texts]
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Step 5: Simple search function
def search(query, k=5):

    query_embedding = get_embedding(query)
    query_embedding = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(query_embedding, k)

    results = []
    seen = set()

    for idx in indices[0]:
        text = chunks[idx]["text"]
        if text not in seen:
            results.append(chunks[idx])
            seen.add(text)
        
    return results


# Test search
if __name__ == "__main__":
    query = "How does Indecimal ensure quality?"
    results = search(query)

    print("\nTop Results:")
    for r in results:
        print("-", r["text"])