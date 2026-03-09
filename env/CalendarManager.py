from datetime import datetime, timedelta
from CEvent import Event

events = []

# Example events – adjust dates to be near your current date if you want to see them
events.append(Event("Steve", datetime(2026, 3, 4, 10, 30), timedelta(minutes=120)))
events.append(Event("Barry", datetime(2026, 3, 5, 14, 0), timedelta(minutes=60)))
events.append(Event("bob", datetime(2026, 3, 6, 14, 0), timedelta(minutes=60)))
