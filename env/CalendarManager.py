from datetime import datetime, timedelta

#Other python files
import CEvent


events = []
event1 = CEvent.Event("Steve", datetime(2026, 3, 4, 22, 0), timedelta(minutes=80))
event2 = CEvent.Event("Barry", datetime(2026, 3, 5, 14, 0), timedelta(minutes=60))
events.append(event1)
events.append(event2)

calendar = {}  # { day: { hour: [events] } }

for event in events:
    day = event.date.strftime("%a")
    hour = event.date.hour

    calendar.setdefault(day, {})
    calendar[day].setdefault(hour, [])
    calendar[day][hour].append(event)

