import os
from dotenv import load_dotenv
load_dotenv()
import requests
from embedding import search

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

USE_LOCAL_LLM = False      # False for Render, True for local testing


def generate_answer(query, context_chunks):
    context_text = "\n\n".join([chunk["text"] for chunk in context_chunks])

    prompt = f"""
You are an AI assistant for a construction company.

IMPORTANT RULES:
- Answer ONLY from the provided context.
- Do NOT add any external knowledge.
- If answer is not in context, say: "I don't have enough information."

Context:
{context_text}

Question:
{query}

Answer:
"""
    
    if USE_LOCAL_LLM:
        return query_ollama(prompt)
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "RAG Chatbot"
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ],
        }
    )
   
    response_json = response.json()
    print(response_json)  
    if "choices" not in response_json:
        return f"API Error: {response_json}"
    
    return response.json()["choices"][0]["message"]["content"]


def query_ollama(prompt, model="phi3"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        response_json = response.json()

        if "response" in response_json:
            return response_json["response"]
        else:
            return f"Ollama Error: {response_json}"

    except Exception as e:
        return f"Ollama Connection Error: {str(e)}"


def rag_query(query):
    # Step 1: Retrieve
    retrieved_chunks = search(query)

    # Step 2: Generate answer
    answer = generate_answer(query, retrieved_chunks)

    return retrieved_chunks, answer

# Test
if __name__ == "__main__":
    query = "How does Indecimal ensure quality?"

    chunks, answer = rag_query(query)

    print("\n--- Retrieved Context ---")
    for i, c in enumerate(chunks, 1):
        print(f"{i}. {c['text']}")

    print("\n--- Final Answer ---")
    print(answer)