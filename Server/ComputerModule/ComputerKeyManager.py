import os
from typing import Union

from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from Server.Data.ComputerKey import ComputerKey
from Server.Data.ComputerKeysData import ComputerKeysData


class ComputerKeyManager:
    __computer_keys_data: ComputerKeysData = None
    __file_name: str = "computer_key_map.txt"

    @classmethod
    def get_computer_key(cls, client_address: str, client_port: int) -> ComputerKey:
        if cls.__computer_keys_data is None:
            cls.__read_keys_from_file()  # try read from file

        key: Union[ComputerKey, None] = None
        if cls.__computer_keys_data is not None:
            key = cls.__computer_keys_data.address_by_computer_key.get(client_address, None)

        if key is None:
            key = cls.__create_computer_key(client_address, client_port)
        return key

    @classmethod
    def __read_keys_from_file(cls):
        if os.path.exists(cls.__file_name):
            with open(cls.__file_name, "r") as file:
                keys = file.read()
            return JsonFormatter.deserialize(keys, ComputerKeysData) if keys else None

    @classmethod
    def __create_computer_key(cls, client_address: str, client_port: int) -> ComputerKey:
        auditorium: str = client_address[:3][1:]
        name: str = str(client_port)[:1]
        return ComputerKey(name, auditorium)
