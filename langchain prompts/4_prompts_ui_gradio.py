from dotenv import load_dotenv
import gradio as gr

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Load model
model = ChatOpenAI()

# Define prompt template inline
template_str = (
    "Please summarize the research paper titled '{paper_input}'. "
    "Make the explanation {style_input} and keep the length {length_input}."
)
template = PromptTemplate.from_template(template_str)


# Function to run when button is clicked
def summarize(paper_input, style_input, length_input):
    chain = template | model    

    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })

    return result.content


# Gradio UI
with gr.Blocks(title="Research Paper Summarizer") as demo:

    gr.Markdown("# 📚 Research Paper Summarizer")

    paper_input = gr.Dropdown(
        choices=[
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis",
        ],
        label="Select Research Paper",
    )

    style_input = gr.Dropdown(
        choices=[
            "Beginner-Friendly",
            "Technical",
            "Code-Oriented",
            "Mathematical",
        ],
        label="Explanation Style",
    )

    length_input = gr.Dropdown(
        choices=[
            "Short (1-2 paragraphs)",
            "Medium (3-5 paragraphs)",
            "Long (detailed explanation)",
        ],
        label="Explanation Length",
    )

    summarize_btn = gr.Button("Summarize")

    output = gr.Textbox(
        label="Summary",
        lines=15,
    )

    summarize_btn.click(
        fn=summarize,
        inputs=[paper_input, style_input, length_input],
        outputs=output,
    )

demo.launch()