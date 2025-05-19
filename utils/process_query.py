from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import os

# Tu clave API de OpenAI va aquí:
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = openai_api_key

pdf_docs = SimpleDirectoryReader("pdfs").load_data()
modelo = LLMPredictor(llm=ChatOpenAI(model_name="gpt-4o", temperature=0))
service_context = ServiceContext.from_defaults(llm_predictor=modelo)

index = GPTVectorStoreIndex.from_documents(pdf_docs, service_context=service_context)
query_engine = index.as_query_engine(response_mode="compact")

def procesar_pregunta(pregunta):
    respuesta = query_engine.query(pregunta)
    return {
        "respuesta": respuesta.response,
        "fuentes": [str(m) for m in respuesta.source_nodes]
    }