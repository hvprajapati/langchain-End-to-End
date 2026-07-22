from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Create the model
model = ChatOpenAI()

# Create the chat prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert teacher."),
    ("human", "Explain {topic} in {style} style.")
])

# Fill the variables
formatted_prompt = prompt.invoke({
    "topic": "LangChain", 
    "style": "Beginner-Friendly"
})

# Send the prompt to the model
response = model.invoke(formatted_prompt)

# Print the answer
print(response.content)