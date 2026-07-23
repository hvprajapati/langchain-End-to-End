# WebBaseLoader in LangChain

## What is WebBaseLoader?

`WebBaseLoader` is a document loader used to **load and extract text content from web pages (URLs).**

It fetches the HTML of a webpage and converts the visible text into LangChain `Document` objects.

---

## How Does It Work?

`WebBaseLoader` uses **BeautifulSoup** internally to:

- Download the webpage
- Parse the HTML
- Extract visible text
- Return one or more `Document` objects

---

## Workflow

```
Website URL
      │
      ▼
WebBaseLoader
      │
      ▼
BeautifulSoup
      │
      ▼
Extract Visible Text
      │
      ▼
Document Object(s)
```

---

## When to Use

`WebBaseLoader` is ideal for:

- Blogs
- News articles
- Documentation websites
- Public text-based webpages
- Static HTML pages

---

## Limitations

- ❌ Does not work well with JavaScript-heavy websites.
- ❌ Extracts only the HTML available when the page is downloaded.
- ❌ Cannot capture content loaded dynamically after the page renders.

> For JavaScript-rendered websites, use loaders such as **SeleniumURLLoader** or **PlaywrightURLLoader**.

---

## Key Takeaway

> **`WebBaseLoader` is used to load text from static web pages by parsing HTML with BeautifulSoup and converting the extracted content into LangChain `Document` objects.**