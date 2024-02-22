from dotenv import load_dotenv

load_dotenv()

import logging
import os, sys
import uvicorn
from app.api.routers.chat import chat_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set


if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(chat_router, prefix="/api/chat")


if __name__ == "__main__":
    conf_fp: os.PathLike|None = sys.argv[1] if len(sys.argv)>1 else None
    if conf_fp:
        print(f'Read config from {conf_fp}')
        os.environ['CREATE_LLAMA_APP_CONF'] = conf_fp
    else: 
        print('Use default settings from constants.py')
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)
