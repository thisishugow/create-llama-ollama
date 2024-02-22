
from app.engine.index import get_index

def get_chat_engine():
    chat_engine = get_index().as_chat_engine(
        similarity_top_k=3, 
        chat_mode="condense_plus_context",
    )

    return chat_engine
