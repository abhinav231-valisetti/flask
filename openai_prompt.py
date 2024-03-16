from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import json


def load_model():
    llm_model = "gpt-4-1106-preview"

    # To control the randomness and creativity of the generated
    # text by an LLM, use temperature = 0.0
    chat = ChatOpenAI(temperature=0.0, model=llm_model, api_key="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")

    return chat


def gen_qa(chat, prompt):
    template_string = """Generate answers based on the question {prompt}. Keep the conversation to be first-person and the answers to be direct. Limit the number of answers to 1.

Please give answer"""
    prompt_template = ChatPromptTemplate.from_template(template_string)
    qnas = prompt_template.format_messages(
        prompt = prompt,
        )

    # # Call the LLM to translate to the style of the customer message
    qnas_response = chat(qnas)
    result = qnas_response.content
    # JSON data clean
    result = result.replace("```", "")
    result = result.replace("json", "")
    qna_array = json.dumps(result)
    return qna_array