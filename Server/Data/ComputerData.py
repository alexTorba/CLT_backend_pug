from CommonExternal.Entities.ComputerFlow import ComputerFlow
from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class ComputerData(JsonContract):
    Name: str
    Auditorium: str
    Flow: ComputerFlow

    def __init__(self, name: str = None, auditorium: str = None, flow: ComputerFlow = None) -> None:
        if name is not None:
            self.Name = name
        if auditorium is not None:
            self.Auditorium = auditorium
        if flow is not None:
            self.Flow = flow

    @property
    def _json_fields(self) -> dict:
        return {
            "n": "Name",
            "a": "Auditorium",
            "f": "Flow"
        }
