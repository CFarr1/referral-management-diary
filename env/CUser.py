from CEvent import Event


class User:
    _id_counter = 1

    def __init__(self, user: str, events: list[Event]):
        self._user = user
        self._events = events  

    @property
    def user(self) -> str:
        return self._user

    @property
    def events(self) -> list[Event]:
        return self._events