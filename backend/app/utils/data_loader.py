from langchain.document_loaders.directory import DirectoryLoader

def load_documents():
    # Load documents from a directory
    loader = DirectoryLoader(directory_path="data/raw")
    documents = loader.load()
    return documents
