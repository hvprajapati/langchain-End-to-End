import os
from dotenv import load_dotenv

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace,
)

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id=os.getenv("HF_MODEL"),
    task="text-generation",
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Explain LangChain in one paragraph.")

print(response.content)