import random

from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonContract import JsonContract
from Server.Data.ComputerKey import ComputerKey


class Computer(JsonContract):
    key: ComputerKey
    data: ComputerFlow

    __json_fields = {
        "k": "key",
        "d": "data"
    }

    def __init__(self, key: ComputerKey = None, data: ComputerFlow = None) -> None:
        super().__init__(self.__json_fields)

        if key is not None:
            self.key = key
        if data is not None:
            self.data = data

    @staticmethod
    def get_random_computer():
        name: str = str(random.randint(0, 9))
        auditorium: str = str(random.randint(37, 40))
        key = ComputerKey(name, auditorium)
        computer_flow = ComputerFlow.get_random_flow()
        return Computer(key, computer_flow)
