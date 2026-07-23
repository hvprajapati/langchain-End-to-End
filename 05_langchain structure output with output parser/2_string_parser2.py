from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Create the model
model = ChatOpenAI()

# Prompt 1 - Generate an explanation
template1 = PromptTemplate(
    template="""
Explain the following topic in detail:

Topic: {topic}
""",
    input_variables=["topic"]
)

# Prompt 2 - Summarize the explanation
template2 = PromptTemplate(
    template="""
Summarize the following text in exactly 5 bullet points.

{text}
""",
    input_variables=["text"]
)

# Output Parser
parser = StrOutputParser()

# LCEL Chain
chain = (
    template1
    | model
    | parser
    | template2
    | model
    | parser
)

# Invoke
result = chain.invoke({
    "topic": "Artificial Intelligence"
})

print(result)