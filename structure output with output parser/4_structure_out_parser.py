from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import (
    ResponseSchema,
    StructuredOutputParser,
)

load_dotenv()

model = ChatOpenAI()

schemas = [
    ResponseSchema(
        name="employee_name",
        description="Full name of the employee"
    ),
    ResponseSchema(
        name="role",
        description="Job role"
    ),
    ResponseSchema(
        name="salary",
        description="Salary package"
    ),
    ResponseSchema(
        name="city",
        description="City where the employee lives"
    ),
]

parser = StructuredOutputParser.from_response_schemas(
    schemas
)

template = PromptTemplate(
    template="""
Extract the employee information.

{format_instructions}

Text:
{text}
""",
    input_variables=["text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({
    "text": """
    Rahul works as a Data Engineer.
    His salary is ₹12 LPA.
    He lives in Ahmedabad.
    """
})

print(result)