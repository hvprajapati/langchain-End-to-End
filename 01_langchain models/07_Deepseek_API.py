import os
from dotenv import load_dotenv

from langchain_deepseek import ChatDeepSeek

load_dotenv()

llm = ChatDeepSeek(
    model=os.getenv("DEEPSEEK_MODEL"),
    temperature=0,
)

response = llm.invoke(
    "Explain RAG in one paragraph."
)
    
print(response.content)