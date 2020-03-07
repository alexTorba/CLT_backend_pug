from CommonExternal.JsonFomatterModule.JsonContract import JsonContract
from Server.Data.ComputerData import ComputerData


class Computer(JsonContract):
    id: int
    data: ComputerData

    def __init__(self, computer_id: int = None, data: ComputerData = None) -> None:
        if computer_id is not None:
            self.id = computer_id
        if data is not None:
            self.data = data

    @property
    def _json_fields(self) -> dict:
        return {
            "i": "id",
            "d": "data"
        }
