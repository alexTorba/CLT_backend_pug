from CommonExternal.JsonFomatterModule.JsonContract import JsonContract
from Server.Data.ComputerData import ComputerData


class Computer(JsonContract):
    id: int
    data: ComputerData

    __json_fields = {
        "i": "id",
        "d": "data"
    }

    def __init__(self, computer_id: int = None, data: ComputerData = None) -> None:
        super().__init__(self.__json_fields)
        if computer_id is not None:
            self.id = computer_id
        if data is not None:
            self.data = data
