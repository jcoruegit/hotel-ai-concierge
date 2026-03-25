import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# cargar embeddings
embeddings = OpenAIEmbeddings()

# cargar base vectorial
if os.path.exists("vector_db"):

    vectorstore = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

else:
    from langchain_community.document_loaders import DirectoryLoader
    from langchain_text_splitters import RecursiveCharacterTextSplitter

    loader = DirectoryLoader("docs")
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    texts = text_splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(texts, embeddings)

    vectorstore.save_local("vector_db")

retriever = vectorstore.as_retriever()

# modelo
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

st.title("🏨 Hotel AI Concierge")
st.write(
    "Ask questions about the hotel. The assistant will answer using hotel documentation."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


question = st.chat_input("Ask about the hotel")

if question:

    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("user"):
        st.markdown(question)

    docs = retriever.invoke(question)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Eres un conserje de IA para un hotel.

Responde ÚNICAMENTE utilizando la información del contexto.

Si la respuesta no está presente, di:
"No tengo esa información en la documentación del hotel".

Reglas de idioma:
- Si la pregunta está en español, responde en español.

- Si la pregunta está en CUALQUIER otro idioma, responde en inglés.

- Nunca respondas en idiomas que no sean español o inglés.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    answer = response.content

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )