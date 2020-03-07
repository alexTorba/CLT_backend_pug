from CommonExternal.Entities.ComputerFlow import ComputerFlow
from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class ComputerData(JsonContract):
    name: str
    auditorium: str
    flow: ComputerFlow

    def __init__(self, name: str = None, auditorium: str = None, flow: ComputerFlow = None) -> None:
        if name is not None:
            self.name = name
        if auditorium is not None:
            self.auditorium = auditorium
        if flow is not None:
            self.flow = flow

    @property
    def _json_fields(self) -> dict:
        return {
            "n": "name",
            "a": "auditorium",
            "f": "flow"
        }
