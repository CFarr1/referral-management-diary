from datetime import datetime, timedelta


class Event:
    _id_counter = 1

    def __init__(self, patient: str, date: datetime, duration: timedelta):
        self.id = Event._id_counter
        Event._id_counter += 1

        self._patient = patient
        self.date = date
        self.duration = duration

    @property
    def patient(self) -> str:
        return self._patient
