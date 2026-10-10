from app.students import router as students_router
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

from app.db import initialize_database, get_dashboard_stats

BASE_DIR = Path(__file__).resolve().parent


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    yield


app = FastAPI(
    title="AURA University",
    description="Smart University Automation Platform",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(students_router)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static",
)

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"title": "AURA University"},
    )


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"title": "AURA Dashboard"},
    )


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "application": "AURA University",
        "version": "0.1.0",
    }


@app.get("/api/stats")
def dashboard_stats():
    return get_dashboard_stats()
