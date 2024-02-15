from llama_index.core import Settings
from app.conn_llm import sys_embedding, sys_llm

Settings.llm = sys_llm
Settings.embed_model = sys_embedding