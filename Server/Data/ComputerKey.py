from External.JsonFomatterModule.JsonContract import JsonContract


class ComputerKey(JsonContract):
    name: str
    auditorium: str

    __json_fields = {
        "n": "name",
        "a": "auditorium"
    }

    def __init__(self, name: str = None, auditorium: str = None):
        super().__init__(self.__json_fields)

        if name is not None:
            self.name = name
        if auditorium is not None:
            self.auditorium = auditorium

    def __repr__(self) -> str:
        return f"Name: {self.name}, auditorium: {self.auditorium}"
