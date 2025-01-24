# Gemma2 Chatbot Glud Test
Testing Gemma2 chatbot with 2b parameters about GLUD (Grupo Linux Universidad Distrital)

1. Go to Ollama website and download it
2. Install Gemma2 2b model using `ollama pull gemma2:2b`
3. Create a virtual enviroment and install `streamlit` and `langchain_community` libraries
4. Execute `streamlit run app.py`

Gemma2:2b seems to be better for low computacional cost conversation. <br>
Ejemplo de datos de entrenamiento en formato JSON:
```
[
    {
        "prompt": "¿Qué es GLUD?",
        "completion": "GLUD es el Grupo Linux de la Universidad Distrital, una comunidad que promueve el uso de GNU/Linux y el software libre en la universidad y la sociedad."
    },
    {
        "prompt": "¿Qué es el curso de Gnubies?",
        "completion": "El curso de Gnubies es una formación ofrecida por GLUD que abarca desde conceptos básicos hasta avanzados de GNU/Linux. Incluye temas como la historia del software libre, instalación de GNU/Linux, administración desde la terminal, automatización con scripts, editores de texto y programación, control de versiones con Git y uso de contenedores."
    },
    {
        "prompt": "¿Qué es el software libre?",
        "completion": "El software libre es aquel que respeta la libertad de los usuarios para ejecutar, estudiar, modificar y distribuir el programa. Promueve una cultura abierta y colaborativa, permitiendo que cualquiera participe en la creación y mejora de la tecnología."
    }
]
```
