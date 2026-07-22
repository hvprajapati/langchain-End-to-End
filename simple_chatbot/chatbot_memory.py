from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# Create the model
model = ChatOpenAI()

# Memory
chat_history = []

print("🤖 Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Save user message
    chat_history.append(HumanMessage(content=user_input))

    # Send entire conversation
    response = model.invoke(chat_history)

    # Save AI response
    chat_history.append(AIMessage(content=response.content))

    print("AI:", response.content)
    print()