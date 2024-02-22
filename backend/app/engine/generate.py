from typing import Literal
from dotenv import load_dotenv

load_dotenv()
import logging

from app.engine.constants import DATA_DIR
from app.engine.context import create_service_context
from app.engine.utils import init_pg_vector_store_from_env
from app.engine.loader import get_documents
from app.storage import chroma_vector_store

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def generate_datasource(service_context, from_:Literal["postgres", "chroma"]='chroma'):
    logger.info("Creating new index")
    # load the documents and create the index
    documents = get_documents()

    if from_ == 'postgres':
        logger.info("Connecting to index from PGVector...")
        store = init_pg_vector_store_from_env()
    elif from_ == 'chroma':
        logger.info("Connecting to index from ChromaDB...")
        store = chroma_vector_store
    else: 
        ValueError(f"arg from_ must be in ['postgres', 'chroma']. Found='{from_}'")

    storage_context = StorageContext.from_defaults(vector_store=store)
    VectorStoreIndex.from_documents(
        documents,
        service_context=service_context,
        storage_context=storage_context,
        show_progress=True,  # this will show you a progress bar as the embeddings are created
    )
    logger.info(
        f"Successfully created embeddings in the vector store"
    )


if __name__ == "__main__":
    generate_datasource(create_service_context())
