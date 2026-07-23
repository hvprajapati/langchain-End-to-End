# Types of Retrievers in LangChain

A **Retriever** is a LangChain component that fetches the most relevant documents for a user's query.

LangChain provides different retrievers depending on where your data is stored and how you want to search it.

---

# 1. Vector Store Retriever ⭐ (Most Common)

Retrieves documents from a **Vector Database** using embeddings.

Supported Vector Stores include:

- Chroma
- FAISS
- Pinecone
- Weaviate
- Milvus
- Qdrant
- PGVector
- MongoDB Atlas Vector Search

### Best For

- RAG Applications
- Semantic Search
- Question Answering

---

# 2. Wikipedia Retriever

Searches Wikipedia articles and retrieves relevant information.

### Best For

- General knowledge
- Learning applications
- Educational chatbots

---

# 3. BM25 Retriever

Uses **keyword-based search** instead of embeddings.

It ranks documents using the BM25 ranking algorithm.

### Best For

- Exact keyword matching
- Small document collections
- Traditional search systems

---

# 4. MultiQuery Retriever

Uses an LLM to generate **multiple versions of the user's query**.

Each query searches the database, and the results are combined.

### Best For

- Improving recall
- Ambiguous questions
- Better document coverage

---

# 5. Parent Document Retriever

Stores **small chunks** for retrieval but returns the **larger parent document**.

### Best For

- Maintaining context
- Large documents
- RAG pipelines

---

# 6. Self-Query Retriever

The LLM understands the user's question and automatically generates:

- Semantic query
- Metadata filters

Example:

```
"Show AI papers after 2024."
```

Automatically applies:

```
topic = AI
year > 2024
```

### Best For

- Metadata filtering
- Enterprise search

---

# 7. MultiVector Retriever

Stores **multiple embeddings** for the same document.

Examples:

- Summary embedding
- Title embedding
- Chunk embedding

This improves retrieval accuracy.

---

# 8. Ensemble Retriever

Combines results from **multiple retrievers**.

Example:

```
BM25
     +
Vector Retriever
     ↓
Combined Results
```

### Best For

- Hybrid Search
- Higher accuracy

---

# 9. Contextual Compression Retriever

Retrieves documents first, then uses an LLM to **remove unnecessary information** before sending the context to the final LLM.

### Best For

- Reducing token usage
- Long documents
- Cost optimization

---

# 10. Time-Weighted Retriever

Gives higher priority to **recent documents** while still considering relevance.

### Best For

- Chat history
- News
- Frequently updated knowledge bases

---

# Summary

| Retriever | Data Source | Best Use Case |
|-----------|-------------|---------------|
| Vector Store Retriever | Vector Database | General RAG |
| Wikipedia Retriever | Wikipedia | General Knowledge |
| BM25 Retriever | Local Documents | Keyword Search |
| MultiQuery Retriever | Vector Database | Better Recall |
| Parent Document Retriever | Large Documents | Preserve Context |
| Self-Query Retriever | Vector DB + Metadata | Metadata Filtering |
| MultiVector Retriever | Multiple Embeddings | Better Accuracy |
| Ensemble Retriever | Multiple Retrievers | Hybrid Search |
| Contextual Compression Retriever | Retrieved Documents | Reduce Tokens |
| Time-Weighted Retriever | Time-based Data | Recent Information |

---

# Which Retriever Should You Learn First?

1. ⭐ Vector Store Retriever
2. ⭐ BM25 Retriever
3. ⭐ Self-Query Retriever
4. ⭐ MultiQuery Retriever
5. ⭐ Parent Document Retriever
6. ⭐ Ensemble Retriever
7. ⭐ Contextual Compression Retriever

The remaining retrievers are more specialized and can be learned as needed.

---

# Key Takeaway

> **LangChain offers many retrievers for different scenarios. For most RAG applications, the `VectorStoreRetriever` is the default choice, while advanced retrievers like `SelfQueryRetriever`, `MultiQueryRetriever`, and `EnsembleRetriever` improve retrieval quality for more complex use cases.**