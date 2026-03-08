from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import jinja2
import CalendarManager


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
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

@app.get("/calendar", response_class=HTMLResponse)
def calendar_page(request: Request):    
    days = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    openHours = [6, 22]



    return templates.TemplateResponse(
        "calendar.html",
        {
            "request": request,
            "calendar": CalendarManager.calendar,
            "events": CalendarManager.events,
            "days" : days,
            "openHours": openHours
        }
    )
