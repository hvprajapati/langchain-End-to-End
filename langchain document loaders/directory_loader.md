# DirectoryLoader in LangChain

## What is a DirectoryLoader?

`DirectoryLoader` is a document loader that loads **multiple documents** from a **directory (folder)** instead of loading files one by one.

It is useful when you have many files that need to be processed together.

---

## Why Use DirectoryLoader?

Instead of writing:

```python
TextLoader("file1.txt")
TextLoader("file2.txt")
TextLoader("file3.txt")
```

You can simply load the entire folder using one loader.

---

## Common Glob Patterns

| Pattern | What It Loads |
|---------|----------------|
| `"**/*.txt"` | All `.txt` files in all subfolders |
| `"*.pdf"` | All `.pdf` files in the current folder |
| `"data/*.csv"` | All `.csv` files inside the `data` folder |
| `"**/*"` | All files of every type in all folders |

> `**` means **search recursively** through all subfolders.

---

## Workflow

```
Folder
│
├── file1.txt
├── file2.txt
├── notes.pdf
└── reports/
      ├── jan.txt
      └── feb.txt
          │
          ▼
   DirectoryLoader
          │
          ▼
List[Document]
```

---

## Use Cases

- Loading an entire dataset
- Building RAG applications
- Processing hundreds of documents
- Indexing project files

---

## Key Takeaway

> **`DirectoryLoader` loads multiple files from a folder and converts them into a list of LangChain `Document` objects.**