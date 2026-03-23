from chunks import create_chunks

# Step 1: Load chunks
chunks = create_chunks()
texts = [chunk["text"] for chunk in chunks]

# Step 5: Simple search function
def search(query, k=5):
    from sentence_transformers import SentenceTransformer
    import faiss
    import numpy as np
    
    # Load embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Step 2: Generate embeddings
    embeddings = model.encode(texts)

    # Convert to numpy array
    embeddings = np.array(embeddings).astype("float32")

    # Step 3: Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Step 4: Add embeddings to index
    index.add(embeddings)

    print(f"Total vectors in FAISS index: {index.ntotal}")


    query_embedding = model.encode([query]).astype("float32")
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