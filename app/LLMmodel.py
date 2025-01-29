from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from redis_client import obtener_historial

llm = Ollama(model="gemma2:2b")

with open("new-data.txt", "r", encoding="utf-8") as file:
    data = file.read()
data_description = "\n".join(data.split("\n"))
bot_desc = "Soy un bot encargado de dar recomendaciones de seguridad con respecto a los hurtos en Bogotá. Doy datos numéricos y porcentuales de tu base de datos para concientizar a la población, teniendo en cuenta la siguiente información:\n" + data_description

prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", bot_desc),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )

chain = prompt_template | llm

def enviar_mensaje_llm(ip: str, message: str):
    response = chain.invoke({
        "input": message, 
        "chat_history":obtener_historial(ip)
        })
    return response
