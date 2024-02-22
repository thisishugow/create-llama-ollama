import os
from app.engine.constants import DATA_DIR
from llama_index.core import VectorStoreIndex, download_loader
from llama_index.core import SimpleDirectoryReader


def get_documents():
    return SimpleDirectoryReader(DATA_DIR).load_data()
