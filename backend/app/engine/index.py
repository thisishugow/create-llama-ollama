import logging
from typing import Literal
from llama_index.core import (
    VectorStoreIndex,
)
from app.engine.utils import init_pg_vector_store_from_env
from app.storage import chroma_vector_store

def get_index(from_:Literal["postgres", "chroma"]="chroma"):
    logger = logging.getLogger("uvicorn")
    if from_ == 'postgres':
        logger.info("Connecting to index from PGVector...")
        store = init_pg_vector_store_from_env()
    elif from_ == 'chroma':
        logger.info("Connecting to index from ChromaDB...")
        store = chroma_vector_store
    else: 
        ValueError(f"arg from_ must be in ['postgres', 'chroma']. Found='{from_}'")
    index = VectorStoreIndex.from_vector_store(store)
    logger.info("Finished connecting to index from Vector Store.")
    return index
