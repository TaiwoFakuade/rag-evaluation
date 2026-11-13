"""RAG evaluation - faithfulness check (synthetic demo).
Run: python rag_eval.py
"""
import json

samples = json.load(open("sample_qa.json"))
for s in samples:
    context = s["context"].lower()
    answer = s["answer"].lower()
    # Simple keyword grounding check for demo purposes
    keywords = [w for w in ["photosynthesis", "water", "nigeria", "lagos"] if w in answer]
    grounded = sum(1 for k in keywords if k in context)
    faithfulness = grounded / len(keywords) if keywords else 1.0
    print(f"Q: {s['question']}")
    print(f"  Faithfulness: {faithfulness:.0%} | Relevance: {s['relevance']}/5 | Completeness: {s['completeness']}/5")
