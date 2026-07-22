import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("OPENAI_LANGCHAIN_MODEL"),
    temperature=0
)

response = llm.invoke(
    "Explain LangChain in one paragraph."
)

print(response.content)