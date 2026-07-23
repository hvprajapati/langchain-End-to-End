# Retrieval in RAG

## What is Retrieval?

**Retrieval** is the process of finding the **most relevant pieces of information (chunks/documents)** from a knowledge base based on a user's query.

Instead of sending the entire database to the LLM, only the most relevant documents are retrieved.

---

# Why is Retrieval Needed?

Without retrieval:

- Large knowledge bases cannot fit into an LLM's context window.
- The LLM may generate inaccurate or hallucinated answers.
- Searching becomes slow and inefficient.

Retrieval ensures that the LLM receives only the information needed to answer the user's question.

---

# Retrieval Workflow

```
User Query
      │
      ▼
Retriever
      │
      ▼
Relevant Chunks
      │
      ▼
LLM
      │
      ▼
Final Answer
```

---

# Types of Retrieval

## 1. Similarity Search

The retriever finds documents whose embeddings are **most similar** to the query embedding.

**How it works**

- Convert the query into an embedding.
- Compare it with document embeddings.
- Return the Top-K most similar documents.

### Advantages

- Fast
- Simple
- Most commonly used

### Best For

- General-purpose RAG
- Question Answering
- Document Search

---

## 2. Similarity Search with Score Threshold

Instead of always returning the Top-K documents, this method returns **only documents whose similarity score exceeds a specified threshold**.

Example:

```
Score ≥ 0.80
```

If no document meets the threshold, nothing is returned.

### Advantages

- Removes low-quality matches
- Reduces irrelevant context
- Improves answer quality

### Best For

- High-accuracy applications
- Enterprise RAG systems

---

## 3. Maximum Marginal Relevance (MMR)

MMR balances **relevance** and **diversity**.

Instead of returning several nearly identical chunks, it selects documents that are:

- Relevant to the query
- Different from one another

### Advantages

- Reduces duplicate information
- Covers multiple aspects of a topic
- Produces richer context

### Best For

- Long documents
- Research assistants
- Multi-topic questions

---

# Comparison

| Retrieval Type | Returns | Best Use Case |
|---------------|----------|---------------|
| Similarity Search | Top-K most similar documents | General RAG |
| Similarity + Score Threshold | Only documents above a similarity score | High-precision retrieval |
| Maximum Marginal Relevance (MMR) | Relevant and diverse documents | Research, complex queries |

---

# Which One Should You Use?

- **Similarity Search** → Default choice for most RAG applications.
- **Similarity + Score Threshold** → When accuracy is more important than always returning results.
- **MMR** → When you want diverse information and fewer duplicate chunks.

---

# Key Takeaway

> **Retrieval is the process of selecting the most relevant documents for a user's query. The three most common retrieval strategies are Similarity Search, Similarity Search with Score Threshold, and Maximum Marginal Relevance (MMR).**