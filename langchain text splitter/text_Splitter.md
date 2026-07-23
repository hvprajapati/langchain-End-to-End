# Why Do We Need Text Splitting?

Large documents often contain more text than an LLM or embedding model can process at once. **Text Splitting** breaks a large document into smaller pieces called **chunks**.

These chunks are easier to process, store, search, and retrieve.

---

# Why is Text Splitting Important?

## 1. Overcoming Context Length Limits

Every LLM and embedding model has a **maximum context length** (token limit).

If a document exceeds this limit, it cannot be processed in a single request.

Text splitting solves this by dividing the document into smaller chunks.

---

## 2. Better Embeddings

Smaller chunks usually represent a single topic.

This helps embedding models generate **more accurate vector representations**, improving retrieval quality.

---

## 3. Better Semantic Search

Searching small, focused chunks returns more relevant results instead of large blocks containing unnecessary information.

---

## 4. Better Summarization

Processing smaller sections reduces:

- Hallucinations
- Topic drift
- Missing important information

---

## 5. Efficient Resource Usage

Working with smaller chunks:

- Uses less memory
- Reduces computation
- Allows parallel processing
- Improves overall performance

---

# Workflow

```
Large Document
        │
        ▼
   Text Splitter
        │
        ▼
Small Chunks
        │
        ▼
Embeddings
        │
        ▼
Vector Database
        │
        ▼
Retriever + LLM
```

---

# Key Takeaway

> **Text Splitting divides large documents into smaller chunks so they fit within model context limits and improve embedding quality, search accuracy, summarization, and overall RAG performance.**