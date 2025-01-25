from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = Ollama(model="gemma2:2b")

if __name__ == "__main__":
    question = input("Pregunta: ")  

    # Data upload
    with open("new-data.txt", "r", encoding="utf-8") as file:
        data = file.read()
    data = data.split("\n")
    data_description = ""
    for data_ in data:
        data_description += data_ + "\n"

    bot_desc = "Soy un bot encargado de dar información acerca del GLUD (Grupo Linux Universidad Distrital) y el software libre, teniendo en cuenta la siguiente información:\n" + data_description

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", bot_desc),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )

    chain = prompt_template | llm
    user_input = question
    print("Preguntando")
    response = chain.invoke({"input": user_input, "chat_history":[]})
    print(response)