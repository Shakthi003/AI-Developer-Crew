from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

def create_coder():
    llm = ChatOllama(model="gemma:2b", temperature=0.7)
    prompt = ChatPromptTemplate.from_template(
        "You are a Python developer. Write clean, modular code to implement the following plan:\n\n{plan}"
    )
    return prompt | llm