from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import jinja2

app = FastAPI()
templates = Jinja2Templates(directory="template")

@app.get("/index", response_class=HTMLResponse)
def users_page(request: Request):
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    ]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "users": users
        }
    )
