from app.utils.embeddings import embed_query
from app.utils.data_loader import load_documents
from langchain.vectorstores import VectorStore
from ollama import Client

vector_store = VectorStore()

def generate_rag_response(query: str):
    embedded_query = embed_query(query)
    documents = vector_store.search(embedded_query)
    
    # Assuming Client generates a response using retrieved documents
    client = Client()
    response = client.chat(query)
    return response
