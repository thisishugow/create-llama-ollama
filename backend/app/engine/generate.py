from typing import Literal
from dotenv import load_dotenv

load_dotenv()
import logging

from app.engine.utils import init_pg_vector_store_from_env
from app.engine.loader import get_documents
from app.storage import chroma_vector_store
from app.engine.utils import read_json_config
from app.conn_llm import sys_embedding, sys_llm
from app.engine.constants import CHUNK_SIZE, CHUNK_OVERLAP
from app.engine.utils import read_json_config

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    Settings,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def generate_datasource(from_:Literal["postgres", "chroma"]='chroma'):
    conf = read_json_config()
    Settings.llm = sys_llm
    Settings.embed_model = sys_embedding
    Settings.chunk_size = conf.get('chunk_size', CHUNK_SIZE) 
    Settings.chunk_overlap = conf.get('chunk_size', CHUNK_OVERLAP)
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
        storage_context=storage_context,
        show_progress=True,  # this will show you a progress bar as the embeddings are created
    )
    logger.info(
        f"Successfully created embeddings in the vector store"
    )


if __name__ == "__main__":
    generate_datasource()
