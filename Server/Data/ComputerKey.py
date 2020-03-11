from External.JsonFomatterModule.JsonContract import JsonContract


class ComputerKey(JsonContract):
    name: int
    auditorium: str

    __json_fields = {
        "n": "name",
        "a": "auditorium"
    }

    def __init__(self, name: int = None, auditorium: str = None):
        super().__init__(self.__json_fields)

        if name is not None:
            self.name = name
        if auditorium is not None:
            self.auditorium = auditorium

    def __repr__(self) -> str:
        return f"Name: {self.name}, auditorium: {self.auditorium}"
