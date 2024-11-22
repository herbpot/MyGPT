from langchain_community.embeddings.ollama import OllamaEmbeddings
from pydantic import ConfigDict
import os

embed_query = OllamaEmbeddings(
    base_url=os.environ['OLLAMA_IP'],
    model="bgm-m3",
    )