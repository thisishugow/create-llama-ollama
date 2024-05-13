from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core.chat_engine import CondensePlusContextChatEngine
from llama_index.core.agent import ReActAgent
from app.engine.index import get_index
from app.engine.query_tools import get_tools
def get_chat_engine()->BaseChatEngine:
    chat_engine = get_index().as_chat_engine(
        similarity_top_k=3, 
        chat_mode="condense_plus_context",
    )

    return chat_engine
