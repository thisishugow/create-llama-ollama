from llama_index.core.selectors import LLMSingleSelector
from llama_index.core.query_engine import RouterQueryEngine
from llama_index.core.agent import ReActAgent
from app.engine.index import get_index
from app.engine.query_tools import get_tools


def get_compound_chat_engine():
    chat_engine = RouterQueryEngine(
        selector=LLMSingleSelector.from_defaults(),
        query_engine_tools=get_tools()
    )
    return chat_engine
    