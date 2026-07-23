# Document Loaders in LangChain

## What is a Document Loader?

A **Document Loader** is a LangChain component used to **load data from different sources** and convert it into a **standardized `Document` object**.

This standardized format allows the document to be used in later stages such as:

- Text Splitting (Chunking)
- Embedding Generation
- Vector Database Storage
- Retrieval
- RAG Applications

---

## Standard Document Format

Every loader returns one or more `Document` objects.

```python
Document(
    page_content="The actual text content",
    metadata={
        "source": "filename.pdf"
    }
)
```

### `page_content`
Contains the actual text extracted from the source.

### `metadata`
Stores additional information about the document, such as:

- Source filename
- Page number
- URL
- Author
- Creation date
- etc.

---

## Why Standardize Documents?

Different data sources have different formats:

- PDF
- Word Documents
- Text Files
- CSV
- HTML
- Websites
- Notion
- Google Drive

Instead of handling each format separately, LangChain converts all of them into the same `Document` format, making the rest of the pipeline consistent.

---

## Workflow

```
Data Source
      │
      ▼
Document Loader
      │
      ▼
Document Object
      │
      ▼
Text Splitter
      │
      ▼
Embeddings
      │
      ▼
Vector Database
      │
      ▼
Retriever
      │
      ▼
LLM
```

---

## Key Takeaway

> **A Document Loader is the first step in most RAG pipelines. Its job is to read data from any source and convert it into LangChain's standard `Document` object.**