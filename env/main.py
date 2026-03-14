from datetime import datetime, timedelta

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import CalendarManager


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")


@app.get("/")
def root():
    return RedirectResponse(url="/calendar")


# Build user cache once at startup
_user_cache: dict = {}

def get_user(user_id: str):
    if user_id not in _user_cache:
        _user_cache[user_id] = CalendarManager.getUser(user_id)
    return _user_cache[user_id]


@app.get("/calendar", response_class=HTMLResponse)
def calendar_page(request: Request):
    # TODO: replace "U001" with session/auth user ID when auth is added
    current_user = get_user("U001")

    current_year = datetime.today().year
    valid_events = [
        e for e in current_user.events
        if (current_year - 1) <= e.date.year <= (current_year + 2)
    ]

    return templates.TemplateResponse(
        "calendar.html",
        {
            "request":  request,
            "events":   valid_events,
            "username": current_user.user,
        },
    )


@app.get("/api/event/{event_id}")
def api_event_details(event_id: int):
    # Search across all users using the cache
    all_events = []
    for uid in CalendarManager.eventdf["userID"].unique():
        all_events.extend(get_user(uid).events)

    event = next((e for e in all_events if e.id == event_id), None)

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


PLACEHOLDER_PAGES = {
    "self-referrals": "Self referrals",
    "advice-sheets":  "Advice sheets",
    "notifications":  "Notifications",
}

@app.get("/{page}", response_class=HTMLResponse)
def placeholder_page(page: str, request: Request):
    if page not in PLACEHOLDER_PAGES:
        return JSONResponse({"error": "Not found"}, status_code=404)
    return templates.TemplateResponse(
        "placeholder.html",
        {
            "request": request,
            "title":  PLACEHOLDER_PAGES[page],
            "active": page,
        },
    )