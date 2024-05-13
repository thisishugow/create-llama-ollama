from llama_index.core.tools import QueryEngineTool, ToolMetadata
from app.engine.index import get_index


def get_tools()->list[QueryEngineTool]:
    query_engine = get_index().as_query_engine()
    tools: list[QueryEngineTool] = [
        QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name='local-knowledge-base-retriever', 
                description=(
                    "It is useful when the given question cannot be answered in current chat context."
                    "This retriever will query the related information from the local vector store and response."
                ),
            )
        ),
        QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name='my-good-friend', 
                description=(
                    "When the question cannot be found in the context, "
                    "then just make a causal talk with user, just like his/her best friend."
                ),
            )
        ),
    ]
    return tools