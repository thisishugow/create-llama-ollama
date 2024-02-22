from llama_index.core import Settings
from app.conn_llm import sys_embedding, sys_llm
from app.engine.constants import CHUNK_SIZE, CHUNK_OVERLAP

Settings.llm = sys_llm
Settings.embed_model = sys_embedding
Settings.chunk_size = CHUNK_SIZE
Settings.chunk_overlap = CHUNK_OVERLAP