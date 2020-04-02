from typing import Dict

from External.JsonFomatterModule.JsonContract import JsonContract
from Server.Data.ComputerKey import ComputerKey


class ComputerKeysData(JsonContract):
    address_by_computer_key: Dict[str, ComputerKey]
    __json_fields = {
        "a": "__address_by_computer_key"
    }

    def __init__(self, address_by_computer_key: Dict[str, ComputerKey]):
        super().__init__(self.__json_fields)

        if address_by_computer_key is not None:
            self.address_by_computer_key = address_by_computer_key
