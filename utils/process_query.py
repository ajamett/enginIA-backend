from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import os

# Obtener API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY no está definida en las variables de entorno.")

# Ya no se necesita esta línea:
# os.environ["OPENAI_API_KEY"] = openai_api_key
# Cargar los documentos PDF
pdf_docs = SimpleDirectoryReader("pdfs").load_data()

# Instanciar el modelo
modelo = LLMPredictor(llm=ChatOpenAI(model_name="gpt-4", temperature=0))

# Crear índice
service_context = ServiceContext.from_defaults(llm_predictor=modelo)
index = GPTVectorStoreIndex.from_documents(pdf_docs, service_context=service_context)
query_engine = index.as_query_engine(response_mode="compact")

def procesar_pregunta(pregunta):
    respuesta = query_engine.query(pregunta)
    return {
        "respuesta": respuesta.response,
        "fuentes": [str(m) for m in respuesta.source_nodes]
    }