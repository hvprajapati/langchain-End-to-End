from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 256,
        "temperature": 0.7
    },
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Explain LangChain in one paragraph.")

print(response.content)