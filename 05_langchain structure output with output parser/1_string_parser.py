from dotenv import load_dotenv

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace,
)

from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

# Output Parser
parser = StrOutputParser()

# Create chain
chain = model | parser

# Invoke
response = chain.invoke(
    "Who invented Python?"
)

print(response)