from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Create the model
model = ChatOpenAI()

print("🤖 Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    response = model.invoke(user_input)

    print("AI:", response.content)
    print()