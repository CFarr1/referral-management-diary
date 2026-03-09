from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import jinja2
import CalendarManager


from fastapi.responses import JSONResponse





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


@app.get("/event/{event_id}", response_class=HTMLResponse)
def event_details(request: Request, event_id: int):
    # Find the event
    event = next((e for e in CalendarManager.events if e.id == event_id), None)

    if not event:
        return HTMLResponse("<h1>Event not found</h1>", status_code=404)

    # Compute end time
    end_time = event.date + event.duration

    return templates.TemplateResponse(
        "event.html",
        {
            "request": request,
            "event": event,
            "end_time": end_time
        }
    )



@app.get("/api/event/{event_id}")
def api_event_details(event_id: int):
    event = next((e for e in CalendarManager.events if e.id == event_id), None)

    if not event:
        return JSONResponse({"error": "Event not found"}, status_code=404)

    end_time = event.date + event.duration

    return {
        "id": event.id,
        "patient": event.patient,
        "start": event.date.strftime("%Y-%m-%d %H:%M"),
        "end": end_time.strftime("%Y-%m-%d %H:%M"),
        "duration": int(event.duration.total_seconds() // 60)
    }