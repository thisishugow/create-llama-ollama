from llama_index.llms.ollama import Ollama
from  transformers import AutoTokenizer
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

EMBDEDING_MODEL:str = "sentence-transformers/all-mpnet-base-v2"

tokenizer = AutoTokenizer.from_pretrained(EMBDEDING_MODEL)
sys_llm: Ollama = Ollama(model="mistral")
sys_embedding: HuggingFaceEmbedding = HuggingFaceEmbedding(
    model_name=EMBDEDING_MODEL,
    tokenizer=tokenizer,
    cache_folder="cache_folder",
    max_length=512,
    device="mps"
)


__all__ = [
    "tokenizer",
    "sys_llm",
    "sys_embedding",
]