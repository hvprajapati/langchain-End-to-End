from dotenv import load_dotenv

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Create the model
model = ChatOpenAI()

# Define the schema
class Employee(BaseModel):
    employee_name: str = Field(
        min_length=3,
        max_length=50,
        description="Employee name"
    )

    age: int = Field(
        ge=18,
        le=60,
        description="Employee age"
    )

    salary: float = Field(
        gt=0,
        description="Annual salary in LPA"
    )

    city: str = Field(
        min_length=2,
        description="City"
    )

# Create parser
parser = PydanticOutputParser(pydantic_object=Employee)

# Prompt
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

# Chain
chain = template | model | parser

# Invoke
result = chain.invoke({
    "text": """
    Rahul works as a Data Engineer.
    His annual salary is 12.5 LPA.
    He lives in Ahmedabad.
    """
})

print(result)

print(result.employee_name)
print(result.role)
print(result.salary)
print(result.city)