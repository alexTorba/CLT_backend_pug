from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonContract import JsonContract


class ComputerData(JsonContract):
    name: str
    auditorium: str
    flow: ComputerFlow

    __json_fields = {
        "n": "name",
        "a": "auditorium",
        "f": "flow"
    }

    def __init__(self, name: str = None, auditorium: str = None, flow: ComputerFlow = None) -> None:
        super().__init__(self.__json_fields)

        if name is not None:
            self.name = name
        if auditorium is not None:
            self.auditorium = auditorium
        if flow is not None:
            self.flow = flow
