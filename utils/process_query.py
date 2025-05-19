from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms import OpenAI
import os

# Obtener la clave desde variables de entorno
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

# Cargar documentos desde la carpeta "pdfs"
pdf_docs = SimpleDirectoryReader("pdfs").load_data()

# Configurar modelo OpenAI
modelo = OpenAI(model="gpt-4o", temperature=0)
service_context = ServiceContext.from_defaults(llm=modelo)

# Crear índice y motor de consulta
index = VectorStoreIndex.from_documents(pdf_docs, service_context=service_context)
query_engine = index.as_query_engine(response_mode="compact")

# Función para manejar preguntas
def procesar_pregunta(pregunta):
    respuesta = query_engine.query(pregunta)
    return {
        "respuesta": respuesta.response,
        "fuentes": [str(m) for m in respuesta.source_nodes]
    }