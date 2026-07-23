from typing_extensions import TypedDict

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Create the model
model = ChatOpenAI()

# Define the output structure
class Person(TypedDict):
    name: str
    age: int
    city: str

# Tell the LLM to return this structure
structured_model = model.with_structured_output(Person)

# Ask a question
response = structured_model.invoke(
    "John is 25 years old and lives in New York."
)

print(response)