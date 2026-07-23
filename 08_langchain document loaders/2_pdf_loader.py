from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'c:\Users\T14s\Desktop\langchain\08_langchain document loaders\guide_en.pdf')

docs = loader.load()

# The number of documents is the same as the number of pages in the pdf
print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)