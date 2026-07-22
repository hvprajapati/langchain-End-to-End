import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model=os.getenv("GOOGLE_LANGCHAIN_MODEL"),
    temperature=0
)

response = llm.invoke(
    "Explain LangChain in one paragraph."
)

print(response.content)