from langchain_core.messages import HumanMessage, AIMessage
import json
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Función para guardar un mensaje en el historial de chat por IP
def guardar_mensaje(ip: str, mensaje: str, es_usuario: bool):
    message = HumanMessage(content=mensaje) if es_usuario else AIMessage(content=mensaje)
    print(type(json.dumps(message.to_json())))
    redis_client.rpush(ip, json.dumps(message.to_json()))

# Obtener el historia de la IP
def obtener_historial(ip: str):
    return redis_client.lrange(ip, 0, -1)

# Eliminar el historial de la IP
def eliminar_historial(ip: str):
    redis_client.delete(ip)