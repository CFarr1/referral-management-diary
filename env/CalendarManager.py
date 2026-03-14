from datetime import datetime, timedelta
from CEvent import Event
from CUser import User
import pandas as pd
import openpyxl


events = []

eventdf = pd.read_excel("TestData.xlsx")
userdf = pd.read_excel("UserData.xlsx")

def getEvents(userID):
    current_rows = eventdf[eventdf["userID"] == userID]
    for index, row in current_rows.iterrows():
        name = row["patient"]
        date = row["date"]
        duration = int(row["duration"])  
        events.append(Event(name,   datetime(date.year, date.month, date.day, date.hour, date.minute),  timedelta(minutes=duration)))
    newUser = User(userdf["user"] , events)
    print(len(events))
    return newUser
