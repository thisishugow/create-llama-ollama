import argparse
import os

from llama_index.core import Settings
from app.conn_llm import get_sys_embedding, get_sys_llm
from app.engine.constants import CHUNK_SIZE, CHUNK_OVERLAP
from app.engine.utils import read_json_config



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", 
        "--config", 
        help="Config path",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    return args
if "CREATE_LLAMA_APP_CONF" not in os.environ.keys():
    args = get_args()
    os.environ['CREATE_LLAMA_APP_CONF'] = args.config

else:
    conf = read_json_config()

    Settings.llm = get_sys_llm()
    Settings.embed_model = get_sys_embedding()
    Settings.chunk_size = conf.get('chunk_size', CHUNK_SIZE) 
    Settings.chunk_overlap = conf.get('chunk_size', CHUNK_OVERLAP)