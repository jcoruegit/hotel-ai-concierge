# 🏨 Hotel AI Concierge (RAG)

Este proyecto es un asistente de inteligencia artificial para un hotel, construido utilizando un enfoque de Retrieval-Augmented Generation (RAG).

El sistema responde preguntas de usuarios basándose únicamente en documentación interna del hotel, evitando depender del conocimiento general del modelo.

---

## 🚀 Funcionalidades

- Búsqueda semántica mediante embeddings
- Base de datos vectorial con FAISS
- Generación de respuestas con LLMs
- Prompt engineering para control de alucinaciones
- Control de idioma (respuestas en español o inglés)

---

## 🧠 Tecnologías utilizadas

- Python
- LangChain
- FAISS
- OpenAI API
- Streamlit

---

## 📂 Estructura del proyecto
hotel-ai-concierge
│
├── docs/ # Documentación del hotel
├── app.py # Interfaz web (Streamlit)
├── ingest.py # Generación de embeddings y base vectorial
├── requirements.txt
└── README.md


---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio
git clone https://github.com/jcoruegit/hotel-ai-concierge.git

cd hotel-ai-concierge


---

### 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate # Windows


---

### 3. Instalar dependencias
pip install -r requirements.txt


---

### 4. Configurar variables de entorno y API Key


Para ejecutar este proyecto es necesario contar con una API key de OpenAI.

Podés obtenerla creando una cuenta en OpenAI y generando una clave desde el panel de usuario.

Luego, crear un archivo `.env` en la raíz del proyecto con el siguiente contenido:

OPENAI_API_KEY=tu_api_key


---

### 5. Generar la base vectorial
python ingest.py


Este paso procesa los documentos en `docs/` y genera la base vectorial utilizada para las búsquedas semánticas.

---

### 6. Ejecutar la aplicación
streamlit run app.py


---

## 💡 Consideraciones

- El sistema responde **únicamente con información presente en los documentos**
- Si no encuentra información relevante, devuelve una respuesta controlada
- El objetivo es minimizar alucinaciones del modelo

---

## 📌 Mejoras futuras

- Implementar threshold de similitud para validar contexto
- Re-ranking de resultados de búsqueda
- Memoria conversacional
- Métricas de evaluación para RAG

---

## 🎯 Objetivo del proyecto

Este proyecto fue desarrollado como una demostración práctica de cómo construir un sistema basado en LLMs utilizando RAG, aplicando buenas prácticas para mejorar la precisión y confiabilidad de las respuestas.

## 🌐 Demo online

🔗 https://hotel-ai-concierge.streamlit.app/