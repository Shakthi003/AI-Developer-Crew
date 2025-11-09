from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

def create_planner():
    llm = ChatOllama(model="gemma:2b", temperature=0.7)
    prompt = ChatPromptTemplate.from_template(
        "You are a software architect. Break down the following requirement into a structured project plan:\n\n{task}"
    )
    return prompt | llm