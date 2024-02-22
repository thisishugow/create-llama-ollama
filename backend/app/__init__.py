from llama_index.core import Settings
from app.conn_llm import sys_embedding, sys_llm
from app.engine.constants import CHUNK_SIZE, CHUNK_OVERLAP
from app.engine.utils import read_json_config

conf = read_json_config()

Settings.llm = sys_llm
Settings.embed_model = sys_embedding
Settings.chunk_size = conf.get('chunk_size', CHUNK_SIZE) 
Settings.chunk_overlap = conf.get('chunk_size', CHUNK_OVERLAP)