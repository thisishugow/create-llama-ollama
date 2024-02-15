from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from chromadb import Collection, PersistentClient

V_DB_NAME = "chromadb"
chroma_client = PersistentClient(V_DB_NAME)
COLLECTION_NAME:str = 'test'
chroma_collection:Collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
chroma_vector_store = ChromaVectorStore(chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=chroma_vector_store)

__all__ = [
    "V_DB_NAME",
    "COLLECTION_NAME",
    "storage_context",
    "chroma_vector_store"
]