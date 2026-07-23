import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model=os.getenv("ANTHROPIC_API_MODEL"),
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Explain Retrieval Augmented Generation in simple words."
        }
    ]
)

print(message.content[0].text)