from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

def create_tester():
    llm = ChatOllama(model="gemma:2b", temperature=0.7)
    prompt = ChatPromptTemplate.from_template(
        "You are a QA engineer. Write unit tests for the following Python code:\n\n{code}"
    )
    return prompt | llm