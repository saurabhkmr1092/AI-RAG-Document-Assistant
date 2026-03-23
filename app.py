import os
from flask import Flask, render_template, request, jsonify
from rag_pipeline import rag_query

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json["query"]

    chunks, answer = rag_query(user_query)

    return jsonify({
        "context": [c["text"] for c in chunks],
        "answer": answer
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)