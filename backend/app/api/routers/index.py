import app

from fastapi import APIRouter, HTTPException, Request, status, Response
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging, os
LIB_ROOT:os.PathLike = os.path.dirname(os.path.realpath(app.__file__))
router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(LIB_ROOT, 'public'))
router.mount("/_next", StaticFiles(directory=os.path.join(LIB_ROOT, 'static/_next/')),)
router.mount("/static", StaticFiles(directory=os.path.join(LIB_ROOT, 'static')),)


@router.get("/", response_class=HTMLResponse)
async def redirect_homepage(request: Request):
    return templates.TemplateResponse("index.html", context={"request":request,})

@router.get("/llama.png")
async def get_favicon(request: Request):
    favicon_path = os.path.join(os.path.join(LIB_ROOT, 'public'), "llama.png")
    return FileResponse(path=favicon_path, media_type="image/vnd.microsoft.icon")

@router.get("/favicon.ico")
async def get_favicon(request: Request):
    favicon_path = os.path.join(os.path.join(LIB_ROOT, 'public'), "favicon.ico")
    return FileResponse(path=favicon_path, media_type="image/vnd.microsoft.icon")