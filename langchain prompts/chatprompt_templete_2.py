from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert teacher."),
    ("human", "Explain {topic} in {style} style.")
])

formatted_prompt = prompt.invoke({
    "topic": "LangChain",
    "style": "Beginner-Friendly"
})

print(formatted_prompt)