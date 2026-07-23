import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model=os.getenv("HF_EMBEDDING_MODEL"),
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

vector = embeddings.embed_query("What is LangChain?")

print(len(vector))
print(vector[:5])  # First 5 dimensions


# Embed Multiple Documents
# documents = [ 
#     "LangChain is an LLM framework.",
#     "RAG combines retrieval with generation.",
#     "Vector databases store embeddings."
# ]

# vectors = embeddings.embed_documents(documents)

# print(len(vectors))
# print(len(vectors[0]))