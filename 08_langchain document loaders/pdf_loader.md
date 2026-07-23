# Choosing the Right PDF Loader in LangChain

Not all PDF files are the same. Some contain simple text, while others include tables, images, multiple columns, or are completely scanned. Choosing the right loader improves text extraction quality.

---

# Limitation of `PyPDFLoader`

`PyPDFLoader` uses the **PyPDF** library internally.

It works well for simple PDFs but has limitations.

### Limitations

- Not suitable for scanned PDFs
- Struggles with complex layouts
- May not correctly extract tables
- Can have issues with multi-column documents

---

# Recommended PDF Loaders

| Use Case | Recommended Loader |
|----------|--------------------|
| Simple, clean PDFs | `PyPDFLoader` |
| PDFs with tables or multiple columns | `PDFPlumberLoader` |
| Scanned/Image PDFs | `UnstructuredPDFLoader` or `AmazonTextractPDFLoader` |
| Need layout and image information | `PyMuPDFLoader` |
| Best overall document structure extraction | `UnstructuredPDFLoader` |

---

# When to Use Each Loader

### PyPDFLoader

- Fast
- Lightweight
- Best for text-based PDFs

Example:

- Books
- Notes
- Research papers

---

### PDFPlumberLoader

Designed for PDFs containing:

- Tables
- Columns
- Reports
- Financial documents

---

### UnstructuredPDFLoader

Best for:

- Scanned PDFs
- Complex layouts
- OCR-based extraction
- High-quality document parsing

---

### AmazonTextractPDFLoader

Uses **Amazon Textract** to extract text from scanned or image-based PDFs.

Ideal when OCR accuracy is important.

---

### PyMuPDFLoader

Useful when you also need:

- Images
- Layout information
- Page structure
- Bounding boxes

---

# Key Takeaway

> **Choose your PDF loader based on the type of PDF you have.**  
> `PyPDFLoader` is great for simple PDFs, while specialized loaders provide better results for tables, scanned documents, and complex layouts.