from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are an expert teacher.

Explain the research paper:
{paper_name}

Explanation Style:
{style}

Explanation Length:
{length}
""",
    input_variables=["paper_name", "style", "length"],
    validate_template=True
)

prompt = template.invoke({
    "paper_name": "Attention Is All You Need",
    "style": "Beginner-Friendly",
    "length": "Short"
})

print(prompt.text)