import os
from logging import getLogger
from llama_index.llms.ollama import Ollama
from  transformers import AutoTokenizer
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from app.engine.utils import read_json_config

conf:dict = read_json_config()
log = getLogger('uvicorn')
EMBDEDING_MODEL:str = "sentence-transformers/all-mpnet-base-v2"
HF_TOKEN:str = os.environ.get('HF_TOKEN', '')
hf_token_to_log:str = ''
if HF_TOKEN:
    hf_token_to_log:str = f"{HF_TOKEN[0:10]}*********"

log.warning(f'You are using HF_TOKEN: {hf_token_to_log}')
tokenizer = AutoTokenizer.from_pretrained(
    conf.get('embedding', EMBDEDING_MODEL), 
    tokenizer_config={
        "token": HF_TOKEN,
    },)
sys_llm: Ollama = Ollama(model=conf.get('llm', "gemma:7b-instruct"))
sys_embedding: HuggingFaceEmbedding = HuggingFaceEmbedding(
    model_name=conf.get('embedding', EMBDEDING_MODEL),
    tokenizer=tokenizer,
    cache_folder=conf.get("cache_folder", "cache_folder"),
    max_length=512,
    device="mps",
)


__all__ = [
    "tokenizer",
    "sys_llm",
    "sys_embedding",
]