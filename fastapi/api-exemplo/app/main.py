from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.routers import user

app = FastAPI(title="API de exemplo")

app.include_router(user.router)

_views_dir = Path(__file__).parent / "views"


@app.get("/", response_class=HTMLResponse)
def home():
    # Serve o front estático — o front que chama o backend, nunca o contrário.
    return (_views_dir / "index.html").read_text()
