from ollama import Client

# Client를 사용해 로컬에서 임베딩 생성
def embed_query(query: str):
    client = Client()
    # 'your-local-embedding-model' 부분은 사용하려는 임베딩 모델로 교체
    embedded_query = client.embed(query, model="your-local-embedding-model")
    return embedded_query
