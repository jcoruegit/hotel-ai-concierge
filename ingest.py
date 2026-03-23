from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Cargar documentos desde la carpeta docs
loader = DirectoryLoader("docs")
documents = loader.load()

print(f"Documentos cargados: {len(documents)}")

# Dividir documentos en chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print(f"Chunks generados: {len(chunks)}")

# Crear embeddings
embeddings = OpenAIEmbeddings()

# Crear vector database
vectorstore = FAISS.from_documents(chunks, embeddings)

# Guardar la base vectorial
vectorstore.save_local("vector_db")

print("Vector database creada en carpeta vector_db")