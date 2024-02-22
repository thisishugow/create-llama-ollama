import os
from app.engine.constants import DATA_DIR
from app.engine.utils import read_json_config
from llama_index.core import VectorStoreIndex, download_loader
from llama_index.core import SimpleDirectoryReader
conf = read_json_config()
def get_documents():
    return SimpleDirectoryReader(conf.get('data_dir', DATA_DIR)).load_data()
