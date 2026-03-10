from datetime import datetime, timedelta

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import CalendarManager


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")


@app.get("/calendar", response_class=HTMLResponse)
def calendar_page(request: Request):

    # Reject dates that are clearly invalid (e.g., 2020)
    current_year = datetime.today().year
    min_valid_year = current_year - 1
    max_valid_year = current_year + 2

    valid_events = [
        e for e in CalendarManager.events
        if min_valid_year <= e.date.year <= max_valid_year
    ]

    # Build calendar dictionary dynamically
    calendar = {}
    for event in valid_events:
        day = event.date.strftime("%a")  # "Mon", "Tue", ...
        hour = event.date.hour

        calendar.setdefault(day, {})
        calendar[day].setdefault(hour, [])
        calendar[day][hour].append(event)

    # Only Monday–Friday
    days = ["", "Mon", "Tue", "Wed", "Thu", "Fri"]
    openHours = [8, 18]

    return templates.TemplateResponse(
        "calendar.html",
        {
            "request": request,
            "calendar": calendar,
            "events": valid_events,
            "days": days,
            "openHours": openHours,
        },
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
        "duration": int(event.duration.total_seconds() // 60),
    }
