import os, json
from llama_index.vector_stores.postgres import PGVectorStore
from urllib.parse import urlparse
from app.engine.constants import PGVECTOR_SCHEMA, PGVECTOR_TABLE


def init_pg_vector_store_from_env():
    original_conn_string = os.environ.get("PG_CONNECTION_STRING")
    if original_conn_string is None or original_conn_string == "":
        raise ValueError("PG_CONNECTION_STRING environment variable is not set.")

    # The PGVectorStore requires both two connection strings, one for psycopg2 and one for asyncpg
    # Update the configured scheme with the psycopg2 and asyncpg schemes
    original_scheme = urlparse(original_conn_string).scheme + "://"
    conn_string = original_conn_string.replace(
        original_scheme, "postgresql+psycopg2://"
    )
    async_conn_string = original_conn_string.replace(
        original_scheme, "postgresql+asyncpg://"
    )
    conf = read_json_config()
    return PGVectorStore(
        connection_string=conn_string,
        async_connection_string=async_conn_string,
        schema_name=conf.get('pgvector_schema', PGVECTOR_SCHEMA),
        table_name=conf.get('pgvector_table', PGVECTOR_TABLE),
    )

def read_json_config(env:str='CREATE_LLAMA_APP_CONF')->dict:
    fp:os.PathLike = os.environ.get(env, None)
    if fp is None: 
        return {}
    with open(fp, 'r') as f:
        res:dict = json.load(f)
    return res