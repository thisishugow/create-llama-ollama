import os
from logging import getLogger
from llama_index.llms.ollama import Ollama
from  transformers import AutoTokenizer
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.langchain import LangChainLLM
from llama_index.core.chat_engine.types import BaseChatEngine
from langchain.chat_models.ollama import ChatOllama

from app.engine.utils import read_json_config




conf:dict = read_json_config()
log = getLogger('uvicorn')
EMBDEDING_MODEL:str = "sentence-transformers/all-mpnet-base-v2"
HF_TOKEN:str = os.environ.get('HF_TOKEN', '')
hf_token_to_log:str = ''
if HF_TOKEN:
    hf_token_to_log:str = f"{HF_TOKEN[0:10]}*********"


def get_sys_tokenizer():
    conf:dict = read_json_config()
    log.debug(f'You are using HF_TOKEN: {hf_token_to_log}')
    tokenizer = AutoTokenizer.from_pretrained(
        conf.get('embedding', EMBDEDING_MODEL), 
        tokenizer_config={
            "token": HF_TOKEN,
        },)
    return tokenizer

def get_sys_llm()->LangChainLLM:
    conf:dict = read_json_config()
    # sys_llm: Ollama = Ollama(model=conf.get('llm', "mistral"))
    sys_llm = LangChainLLM(ChatOllama(model=conf.get('llm', "llama3")))
    return sys_llm

def get_sys_embedding() -> HuggingFaceEmbedding:
    conf:dict = read_json_config()
    tokenizer = get_sys_tokenizer()
    sys_embedding: HuggingFaceEmbedding = HuggingFaceEmbedding(
        model_name=conf.get('embedding', EMBDEDING_MODEL),
        tokenizer=tokenizer,
        cache_folder=conf.get("cache_folder", "cache_folder"),
        max_length=512,
        device="mps",
    )
    return sys_embedding
