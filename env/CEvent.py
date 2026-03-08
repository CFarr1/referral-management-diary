from datetime import datetime, timedelta

class Event:
    def __init__(self, patient, date, duration):
        self._patient = patient
        self.date = date
        self.duration = duration

    @property
    def patient(self):
        return self._patient

