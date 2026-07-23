from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Create the model
model = ChatOpenAI()

# Create the parser
parser = JsonOutputParser()

# Prompt
template = PromptTemplate(
    template="""
Extract the following information from the given text.

Return ONLY valid JSON.

{format_instructions}

Text:
{text}
""",
    input_variables=["text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Chain
chain = template | model | parser

# Invoke
result = chain.invoke({
    "text": "John is 25 years old and lives in New York."
})

print(result)



'''
parser.get_format_instructions() means
"Hey Parser...
Tell me what instructions I should give to GPT so it returns JSON.
"'''
