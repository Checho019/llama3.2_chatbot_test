import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = Ollama(model="gemma2:2b")

def main():
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # Data upload
    with open("new-data.txt", "r", encoding="utf-8") as file:
        data = file.read()
    data = data.split("\n")
    data_description = ""
    for data_ in data:
        data_description += data_ + "\n"
    
    # Warning
    #data_description = ""

    st.title("Prueba gemma2 2b")
    bot_desc = st.text_area("Descripción", value="Soy un bot encargado de dar recomendaciones de seguridad con respecto a los hurtos en Bogotá, das datos númericos y porcentuales de tu base de datos para concientizar a la población teniendo en cuenta la siguiente información:\n" + data_description)

    # bot_desc is the personality of the bot, we can use it to teach what the bot must say
    # chat_history is the list of messages that the bot has sent
    # input is the message that the user sends to the bot
    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", bot_desc),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )

    chain = prompt_template | llm
    user_input = st.text_input("Pregunta", key="user_input")

    if st.button("Enviar"):
        if user_input.lower() == "adios":
            st.stop()
        else:
            # Get the response from the chain (it must be a response from a HTTP request with the user input)
            response = chain.invoke({"input": user_input, "chat_history":st.session_state["chat_history"]})
            st.session_state["chat_history"].append(HumanMessage(content=user_input))
            st.session_state["chat_history"].append(AIMessage(content=response))

    chat_display = ""
    for msg in st.session_state["chat_history"]:
        if isinstance(msg, HumanMessage):
            chat_display += f"👦 Humano: {msg.content} \ "
        else:
            chat_display += f"🤖 AI: {msg.content} \ "
    
    # Don't show it as a markdown, just show it as a text
    # st.text(chat_display)
    st.markdown(chat_display)



if __name__ == "__main__":
    main()