import os
from dotenv import load_dotenv

from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(
    model=os.getenv("ANTHROPIC_LANGCHAIN_MODEL"),
    temperature=0
)

response = llm.invoke(
    "Explain LangChain in one paragraph."
)

print(response.content)