from fastapi import FastAPI, HTTPException, Request
from redis_client import guardar_mensaje, obtener_historial, eliminar_historial
from pydantic import BaseModel
from LLMmodel import enviar_mensaje_llm

app = FastAPI()

class MensajeRequest(BaseModel):
    mensaje: str

# Endpoint para enviar un mensaje al chat
@app.post("/chat")
async def enviar_mensaje(request: Request, mensage_request: MensajeRequest):
    ip = request.client.host
    mensaje = mensage_request.mensaje
    if not mensaje:
        raise HTTPException(status_code=400, detail="El mensaje no puede estar vacío")

    print(f"{ip}: {mensaje}")
    respuesta_bot = enviar_mensaje_llm(ip, mensaje)
    print(respuesta_bot)
    guardar_mensaje(ip, mensaje, es_usuario=True)
    guardar_mensaje(ip, respuesta_bot, es_usuario=False)

    return {"respuesta": respuesta_bot}
    

# Endpoint para obtener el historial de chat por IP
@app.get("/chat")
async def obtener_chat(request: Request):
    ip = request.client.host
    historial = obtener_historial(ip)
    if not historial:
        raise HTTPException(status_code=404, detail="No se encontró el historial de chat")
    return {"ip": ip, "historial": historial}


# Endpoint para eliminar el historial de chat por IP
@app.delete("/chat")
async def eliminar_chat(request: Request):
    ip = request.client.host
    eliminar_historial(ip)
    return {"ip": ip, "mensaje": "Historial de chat eliminado correctamente"}
