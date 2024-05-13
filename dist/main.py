from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

load_dotenv()

import logging
import os, sys
import uvicorn
import app
from app.api.routers.chat import chat_router
from app.api.routers.index import router as front_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

main_app = FastAPI()

environment = os.getenv("ENVIRONMENT", "dev")  # Default to 'development' if not set


if environment == "dev":
    logger = logging.getLogger("uvicorn")
    logger.warning("Running in development mode - allowing CORS for all origins")
    main_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

main_app.include_router(chat_router, prefix="/api/chat")
main_app.include_router(front_router)
LIB_ROOT:os.PathLike = os.path.dirname(os.path.realpath(app.__file__))
main_app.mount("/_next", StaticFiles(directory=os.path.join(LIB_ROOT, 'static/_next')))


if __name__ == "__main__":
    uvicorn.run(app="main:main_app", host="0.0.0.0", port=8080, reload=True)
