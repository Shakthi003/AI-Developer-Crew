from langchain.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

def create_reviewer():
    llm = ChatOllama(model="gemma:2b", temperature=0.7)
    prompt = ChatPromptTemplate.from_template(
        "You are a senior code reviewer. Review the following code and suggest improvements or identify issues:\n\n{code}"
    )
    return prompt | llm