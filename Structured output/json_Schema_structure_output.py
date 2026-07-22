from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Create the model
model = ChatOpenAI()

# Define JSON Schema
json_schema = {
    "title": "User",
    "description": "Information about a user",
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "description": "User's name"
        },
        "age": {
            "type": "integer",
            "description": "User's age"
        },
        "email": {
            "type": "string",
            "description": "User's email address"
        }
    },
    "required": ["name", "age", "email"]
}

# Create structured model
structured_model = model.with_structured_output(json_schema)

# Invoke the model
response = structured_model.invoke(
    """
    My name is Hardik.
    I am 22 years old.
    My email is hardik@gmail.com.
    """
)

print(response)