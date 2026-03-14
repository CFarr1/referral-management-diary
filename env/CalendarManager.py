from datetime import datetime, timedelta
from CEvent import Event
from CUser import User
import pandas as pd

eventdf = pd.read_excel("TestData.xlsx", parse_dates=["date"])
userdf  = pd.read_excel("UserData.xlsx")

def getUser(userID: str) -> User:
    events = []

    current_rows = eventdf[eventdf["userID"] == userID]
    for _, row in current_rows.iterrows():
        date = row["date"]
        # Handle both datetime and string formats
        if isinstance(date, str):
            date = datetime.strptime(date.strip(), "%Y-%m-%d %H:%M")
        elif hasattr(date, 'to_pydatetime'):
            date = date.to_pydatetime()

        events.append(Event(
            row["patient"],
            datetime(date.year, date.month, date.day, date.hour, date.minute),
            timedelta(minutes=int(row["duration"]))
        ))

    user_row = userdf[userdf["userID"] == userID]
    username = user_row.iloc[0]["user"] if not user_row.empty else userID

    return User(username, events)