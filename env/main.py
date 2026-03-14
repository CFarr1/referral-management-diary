from datetime import datetime
import hashlib
import hmac
import secrets
 
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
 
import CalendarManager
 
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")
 
# Secret key for signing session cookies
SECRET_KEY = secrets.token_hex(32)
 
 
# ── Session helpers ──────────────────────────────────────────────────────────
 
def make_session_token(user_id: str) -> str:
    sig = hmac.new(SECRET_KEY.encode(), user_id.encode(), hashlib.sha256).hexdigest()
    return f"{user_id}:{sig}"
 
def verify_session_token(token: str) -> str | None:
    try:
        user_id, sig = token.rsplit(":", 1)
        expected = hmac.new(SECRET_KEY.encode(), user_id.encode(), hashlib.sha256).hexdigest()
        if hmac.compare_digest(sig, expected):
            return user_id
    except Exception:
        pass
    return None
 
def get_current_user_id(request: Request) -> str | None:
    token = request.cookies.get("session")
    if not token:
        return None
    return verify_session_token(token)
 
 
# ── Password helpers ─────────────────────────────────────────────────────────
 
def verify_password(plain: str, stored: str) -> bool:
    return plain == stored
 
 
# ── User cache ───────────────────────────────────────────────────────────────
 
_user_cache: dict = {}
 
def get_user(user_id: str):
    if user_id not in _user_cache:
        _user_cache[user_id] = CalendarManager.getUser(user_id)
    return _user_cache[user_id]
 
 
# ── Auth routes ──────────────────────────────────────────────────────────────
 
@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    if get_current_user_id(request):
        return RedirectResponse(url="/calendar")
    return RedirectResponse(url="/login")
 
 
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    if get_current_user_id(request):
        return RedirectResponse(url="/calendar")
    return templates.TemplateResponse("login.html", {"request": request, "error": None})
 
 
@app.post("/login", response_class=HTMLResponse)
async def login_post(request: Request, username: str = Form(...), password: str = Form(...)):
    userdf = CalendarManager.userdf
    match = userdf[userdf["user"].str.lower() == username.strip().lower()]
 
    error = None
    row = None
    if match.empty:
        error = "Invalid username or password."
    else:
        row = match.iloc[0]
        if not verify_password(password, str(row["password"])):
            error = "Invalid username or password."
 
    if error:
        return templates.TemplateResponse("login.html", {"request": request, "error": error})
 
    token = make_session_token(row["userID"])
    response = RedirectResponse(url="/calendar", status_code=303)
    response.set_cookie("session", token, httponly=True, samesite="lax")
    return response
 
 
@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("session")
    return response
 
 
# ── Calendar routes ──────────────────────────────────────────────────────────
 
@app.get("/calendar", response_class=HTMLResponse)
def calendar_page(request: Request):
    user_id = get_current_user_id(request)
    if not user_id:
        return RedirectResponse(url="/login")
 
    current_user = get_user(user_id)
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
def api_event_details(event_id: int, request: Request):
    if not get_current_user_id(request):
        return JSONResponse({"error": "Unauthorised"}, status_code=401)
 
    all_events = []
    for uid in CalendarManager.eventdf["userID"].unique():
        all_events.extend(get_user(uid).events)
 
    event = next((e for e in all_events if e.id == event_id), None)
    if not event:
        return JSONResponse({"error": "Event not found"}, status_code=404)
 
    end_time = event.date + event.duration
    return {
        "id":       event.id,
        "patient":  event.patient,
        "start":    event.date.strftime("%Y-%m-%d %H:%M"),
        "end":      end_time.strftime("%Y-%m-%d %H:%M"),
        "duration": int(event.duration.total_seconds() // 60),
    }
 
 
# ── Placeholder routes ───────────────────────────────────────────────────────
 
PLACEHOLDER_PAGES = {
    "self-referrals": "Self referrals",
    "advice-sheets":  "Advice sheets",
    "notifications":  "Notifications",
}
 
@app.get("/{page}", response_class=HTMLResponse)
def placeholder_page(page: str, request: Request):
    if not get_current_user_id(request):
        return RedirectResponse(url="/login")
    if page not in PLACEHOLDER_PAGES:
        return JSONResponse({"error": "Not found"}, status_code=404)
    return templates.TemplateResponse(
        "placeholder.html",
        {"request": request, "title": PLACEHOLDER_PAGES[page], "active": page},
    )