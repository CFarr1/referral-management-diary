from datetime import datetime, timedelta
from CEvent import Event

events = []

# ── February 2026 (last month) ──
events.append(Event("Alice",   datetime(2026, 2,  3, 9,  0),  timedelta(minutes=45)))
events.append(Event("James",   datetime(2026, 2,  3, 11, 0),  timedelta(minutes=60)))   # same day as Alice, different time
events.append(Event("Carol",   datetime(2026, 2, 10, 14, 30), timedelta(minutes=30)))
events.append(Event("David",   datetime(2026, 2, 17, 9,  0),  timedelta(minutes=60)))
events.append(Event("Emma",    datetime(2026, 2, 17, 11, 0),  timedelta(minutes=45)))   # same day as David
events.append(Event("Frank",   datetime(2026, 2, 17, 14, 0),  timedelta(minutes=30)))   # same day, third appointment
events.append(Event("Grace",   datetime(2026, 2, 24, 9,  30), timedelta(minutes=60)))

# ── March 2026 (current month) ──
events.append(Event("Steve",   datetime(2026, 3,  4, 10, 30), timedelta(minutes=120)))
events.append(Event("Barry",   datetime(2026, 3,  5, 14, 21), timedelta(minutes=60)))
events.append(Event("Bob",     datetime(2026, 3,  6, 14,  0), timedelta(minutes=60)))
events.append(Event("Hannah",  datetime(2026, 3,  9, 8,  30), timedelta(minutes=45)))
events.append(Event("Ivan",    datetime(2026, 3, 11, 9,   0), timedelta(minutes=30)))
events.append(Event("Julia",   datetime(2026, 3, 11, 14,  0), timedelta(minutes=60)))   # same day as Ivan
events.append(Event("Kevin",   datetime(2026, 3, 16, 10,  0), timedelta(minutes=90)))
events.append(Event("Laura",   datetime(2026, 3, 18, 9,   0), timedelta(minutes=45)))
events.append(Event("Marcus",  datetime(2026, 3, 18, 14,  0), timedelta(minutes=60)))   # same day as Laura
events.append(Event("Nina",    datetime(2026, 3, 23, 9,   0), timedelta(minutes=30)))
events.append(Event("Oliver",  datetime(2026, 3, 25, 9,   0), timedelta(minutes=45)))
events.append(Event("Paula",   datetime(2026, 3, 25, 11,  0), timedelta(minutes=45)))   # same day as Oliver
events.append(Event("Quinn",   datetime(2026, 3, 25, 14,  0), timedelta(minutes=60)))   # same day, third appointment
events.append(Event("Rachel",  datetime(2026, 3, 30, 10,  0), timedelta(minutes=90)))

# ── April 2026 (next month) ──
events.append(Event("Sam",     datetime(2026, 4,  1, 9,   0), timedelta(minutes=45)))
events.append(Event("Tina",    datetime(2026, 4,  1, 11,  0), timedelta(minutes=45)))   # same day as Sam
events.append(Event("Uma",     datetime(2026, 4,  7, 14,  0), timedelta(minutes=60)))
events.append(Event("Victor",  datetime(2026, 4, 14, 9,   0), timedelta(minutes=30)))
events.append(Event("Wendy",   datetime(2026, 4, 14, 13,  0), timedelta(minutes=60)))   # same day as Victor
events.append(Event("Xander",  datetime(2026, 4, 20, 9,  30), timedelta(minutes=90)))
events.append(Event("Yasmin",  datetime(2026, 4, 22, 13,  0), timedelta(minutes=45)))
events.append(Event("Zoe",     datetime(2026, 4, 28, 15,  0), timedelta(minutes=60)))