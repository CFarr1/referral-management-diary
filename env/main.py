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

    # Filter to a reasonable date range
    current_year = datetime.today().year
    valid_events = [
        e for e in CalendarManager.events
        if (current_year - 1) <= e.date.year <= (current_year + 2)
    ]

    return templates.TemplateResponse(
        "calendar.html",
        {
            "request": request,
            "events": valid_events,
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