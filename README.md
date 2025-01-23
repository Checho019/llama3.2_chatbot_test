# Llama3.2 Chatbot Glud Test
Testing llama 3.2 chatbot with 1b and 3b parameters about glud website

1. Go to Ollama website and download it
2. Install Llama3.2 1b and 3b models using `ollama pull llama3.2:1b` and `ollama pull llama3.2:3b`
3. Create a virtual enviroment and install `streamlit` and `langchain_community` libraries
4. Execute `streamlit run app.py`

Gemma2:2b seems to be better for low computacional cost conversation. <br>
Ejemplo de datos de entrenamiento en formato JSON:
```
[
    {
        "prompt": "¿Cuántos casos de hurto a personas se registraron en Bogotá entre enero y septiembre de 2024?",
        "completion": "En Bogotá se registraron 99,194 casos de hurto a personas entre enero y septiembre de 2024."
    },
    {
        "prompt": "¿Cómo se compara el hurto a personas en Bogotá en 2024 con el mismo periodo en 2023?",
        "completion": "En 2024, hubo una disminución del 17.7% en los casos de hurto a personas en Bogotá en comparación con el mismo periodo en 2023."
    },
    {
        "prompt": "¿El hurto a personas sigue siendo un delito frecuente en Bogotá en 2024?",
        "completion": "Sí, a pesar de una reducción general en 2024, el hurto a personas sigue siendo uno de los delitos más frecuentes en Bogotá."
    }
]
```
