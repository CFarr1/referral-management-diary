from datetime import datetime, timedelta
from CEvent import Event
from CUser import User
import pandas as pd

eventdf = pd.read_excel("TestData.xlsx")
userdf  = pd.read_excel("UserData.xlsx")

def getUser(userID: str) -> User:
    events = []

    # Load events for this user
    current_rows = eventdf[eventdf["userID"] == userID]
    for _, row in current_rows.iterrows():
        events.append(Event(
            row["patient"],
            datetime(row["date"].year, row["date"].month, row["date"].day,
                     row["date"].hour, row["date"].minute),
            timedelta(minutes=int(row["duration"]))
        ))

    # Look up the user's display name from UserData.xlsx
    user_row = userdf[userdf["userID"] == userID]
    username = user_row.iloc[0]["user"] if not user_row.empty else userID

    return User(username, events)