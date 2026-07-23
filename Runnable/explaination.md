# Chapter: Introduction to Runnables

---

# 1. Why Were Runnables Introduced?

## The Early Days of LangChain

When ChatGPT and other Large Language Models (LLMs) became popular, developers started building AI-powered applications such as:

- Chatbots
- PDF Question Answering Systems
- AI Agents
- Text Summarizers
- Document Search Systems

Initially, LangChain mainly focused on providing wrappers around different LLM providers such as OpenAI, Anthropic, Google, Hugging Face, etc.

However, developers quickly realized that interacting with an LLM is only **one small part** of building an AI application.

A complete application usually involves many different components working together.

---

## Example: Building a PDF Chatbot

A typical RAG (Retrieval-Augmented Generation) application performs several tasks:

```
PDF
 │
 ▼
Load Document
 │
 ▼
Split into Chunks
 │
 ▼
Generate Embeddings
 │
 ▼
Store in Vector Database
 │
 ▼
Retrieve Relevant Chunks
 │
 ▼
Build Prompt
 │
 ▼
Call LLM
 │
 ▼
Parse Output
 │
 ▼
Return Response
```

Notice that the LLM is only **one step** in the entire workflow.

---

# 2. Problems with Old Chains

To simplify common workflows, LangChain introduced **Chains**.

For example:

- LLMChain
- RetrievalQAChain
- SequentialChain
- SQLDatabaseChain
- APIChain
- MathChain

Each chain automated a specific workflow.

For example, instead of manually writing:

```python
formatted_prompt = prompt.format(...)
response = llm.predict(formatted_prompt)
```

You could simply write:

```python
chain.run(...)
```

which internally handled everything.

This made development much easier.

---

## The Problem

Over time, LangChain introduced dozens of specialized chains.

```
LLMChain
RetrievalQAChain
ConversationChain
SQLDatabaseChain
APIChain
MathChain
SequentialChain
RouterChain
...
```

This created two major problems:

### Problem 1

The LangChain codebase became very large and difficult to maintain.

### Problem 2

Developers had to learn which chain to use for every different use case.

The learning curve became much steeper.

---

# 3. Evolution of LangChain

The LangChain team realized that creating a new Chain for every workflow was **not scalable**.

Instead of creating hundreds of specialized chains, they redesigned the framework around a single abstraction:

> **Runnable**

The idea was simple:

> Make every component behave the same way so that they can be connected together naturally.

---

# 4. Components vs Chains

Before Runnables, developers manually connected components.

```
PromptTemplate
      │
      ▼
Format Prompt
      │
      ▼
LLM
      │
      ▼
Parser
```

Each component had a different interface.

For example:

| Component | Method |
|-----------|---------|
| PromptTemplate | `format()` |
| LLM | `predict()` |
| Retriever | `get_relevant_documents()` |
| Parser | `parse()` |

Because every component used different methods, LangChain had to write many custom Chains to connect them.

---

# 5. What is a Runnable?

A Runnable is the **fundamental building block** in LangChain.

It represents **one unit of work**.

A Runnable:

- Accepts an input.
- Processes the input.
- Produces an output.

Examples:

```
Text
 │
 ▼
PromptTemplate
 │
 ▼
Prompt
```

```
Prompt
 │
 ▼
Chat Model
 │
 ▼
AIMessage
```

```
AIMessage
 │
 ▼
Output Parser
 │
 ▼
Python Object
```

Every one of these is a Runnable.

---

# 6. Characteristics of a Runnable

Every Runnable has four important characteristics.

## 1. It performs one task.

Every Runnable has a single responsibility.

Examples:

- Create a prompt.
- Call an LLM.
- Parse JSON.
- Retrieve documents.

---

## 2. It follows a common interface.

Every Runnable exposes the same methods.

This standardization allows different components to work together seamlessly.

---

## 3. Runnables can be connected.

The output of one Runnable automatically becomes the input of the next Runnable.

```
Runnable A
     │
     ▼
Runnable B
     │
     ▼
Runnable C
```

---

## 4. A workflow is itself a Runnable.

If you connect multiple Runnables together:

```
Prompt
 │
 ▼
Model
 │
 ▼
Parser
```

the entire pipeline behaves like **one Runnable**.

This allows pipelines to be nested and reused.

---

# 7. Common Runnable Interface

One of the biggest improvements in LangChain is that every Runnable exposes the same interface.

Some commonly used methods are:

| Method | Purpose |
|---------|---------|
| `invoke()` | Process a single input. |
| `batch()` | Process multiple inputs. |
| `stream()` | Stream output as it is generated. |
| `ainvoke()` | Asynchronous version of `invoke()`. |
| `abatch()` | Asynchronous batch processing. |
| `astream()` | Asynchronous streaming. |

Because every Runnable supports these methods, components become interchangeable.

---

# 8. Why Everything is a Runnable

In modern LangChain, almost every component is implemented as a Runnable.

Examples include:

- Chat Models
- Prompt Templates
- Output Parsers
- Retrievers
- Document Transformers
- Entire Pipelines

This means they can all be connected using the same syntax.

---

# 9. Lego Block Analogy

Imagine every Runnable is a Lego block.

Each Lego block:

- Has one purpose.
- Has a standard connector.
- Can connect to any other Lego block.

```
[Lego]
   │
[Lego]
   │
[Lego]
```

Now imagine replacing "Lego" with:

```
Prompt
   │
Model
   │
Parser
```

Exactly the same idea.

The standard connector is what makes Lego powerful.

The common Runnable interface is what makes LangChain powerful.

---

# 10. Visual Diagram

```
User Input
     │
     ▼
PromptTemplate
     │
     ▼
Chat Model
     │
     ▼
Output Parser
     │
     ▼
Python Object
```

Each box is a Runnable.

The entire pipeline is also a Runnable.

---

# 11. Interview Notes

### What is a Runnable?

A Runnable is a standardized unit of work that accepts an input, performs an operation, and produces an output.

---

### Why were Runnables introduced?

To replace the growing number of specialized Chains with a single, reusable abstraction that allows all LangChain components to work together through a common interface.

---

### What is the biggest advantage of Runnables?

All components expose the same interface (`invoke()`, `batch()`, `stream()`, etc.), making them easy to compose into flexible workflows.

---

### Why is every pipeline also a Runnable?

Because a composed workflow behaves exactly like a single Runnable—it accepts an input, processes it, and returns an output. This allows pipelines to be reused and nested.

---

# 12. Summary

- LangChain originally relied on many specialized Chains.
- As the number of Chains grew, the framework became harder to maintain and learn.
- Runnables introduced a common interface for all components.
- Every Runnable accepts input, performs one task, and returns output.
- Runnables can be connected to build complex AI workflows.
- A complete workflow is itself a Runnable, enabling modular and reusable pipelines.
