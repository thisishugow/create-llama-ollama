import os

from llama_index.core import ServiceContext
from llama_index.llms.openai import OpenAI
from llama_index.core import Settings, ServiceContext


def create_base_context():
    # model = os.getenv("MODEL", "gpt-3.5-turbo")
    # return ServiceContext.from_defaults(
    #     llm=OpenAI(model=model),
    # )
    return ServiceContext.from_defaults(llm=Settings.llm, embed_model=Settings.embed_model )