from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from pydantic import BaseModel, Field

load_dotenv()

# Create the model
model = ChatOpenAI()

# Define the output structure
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City where the person lives")

# Create structured model
structured_model = model.with_structured_output(Person)

# Ask the question
response = structured_model.invoke(
    "John is 25 years old and lives in New York."
)

print(response)