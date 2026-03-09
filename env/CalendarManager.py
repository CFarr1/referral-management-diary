from datetime import datetime, timedelta

#Other python files
import CEvent


events = []
event1 = CEvent.Event("Steve", datetime(2026, 3, 4, 10, 30), 120.0)
event2 = CEvent.Event("Peter", datetime(2026, 3, 4, 14, 30), 60.0)
event3 = CEvent.Event("Barry", datetime(2026, 3, 5, 16, 0), 120.0)
events.append(event1)
events.append(event2)
events.append(event3)

calendar = {}

for event in events:
    day = event.date.strftime("%a")
    hour = event.date.hour

    calendar.setdefault(day, {})
    calendar[day].setdefault(hour, [])
    calendar[day][hour].append(event)

