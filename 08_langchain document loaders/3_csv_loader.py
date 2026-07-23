from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path=r'c:\Users\T14s\Desktop\langchain\08_langchain document loaders\Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))
print(docs[1])