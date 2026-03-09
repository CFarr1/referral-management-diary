from datetime import datetime, timedelta
from CEvent import Event

events = []

# Example events – adjust dates to be near your current date if you want to see them
events.append(Event("Steve", datetime(2026, 3, 4, 22, 0), timedelta(minutes=80)))
events.append(Event("Barry", datetime(2026, 3, 5, 14, 0), timedelta(minutes=60)))
