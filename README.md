# RAG Evaluation

Evaluate Retrieval-Augmented Generation answers for faithfulness, relevance, and completeness — without needing a live LLM.

## What it does

- Checks if the answer is grounded in the retrieved context
- Scores relevance to the question and completeness
- Flags unsupported claims for human review

## Run it

```bash
pip install -r requirements.txt
python rag_eval.py
```

## Files

- `rag_eval.py` — faithfulness + relevance scorer
- `sample_qa.json` — synthetic Q&A with retrieved context
- `rubric.md` — evaluation criteria

## Metrics

- **Faithfulness:** % of claims supported by context
- **Relevance:** 1-5, does it answer the question asked?
- **Completeness:** 1-5, does it cover the key points?

## Skills demonstrated

RAG evaluation, LLMOps testing, faithfulness checking, Python.
