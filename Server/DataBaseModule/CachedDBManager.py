from typing import List, Dict, Union

from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from Server.DataBaseModule.DBManager import DBManager
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey


class CachedDBManager(DBManager):
    __cache: Dict[ComputerKey, Computer] = dict()

    def __init__(self) -> None:
        super().__init__()

    def create(self, key: ComputerKey, computer: Computer) -> None:
        self.__cache[key] = computer
        json_data = JsonFormatter.serialize(computer)
        super().create(key, json_data)

    # noinspection PyTypeChecker
    def read(self, key: ComputerKey) -> Union[Computer, None]:
        computer = self.__cache.get(key)
        if computer is not None:
            return computer

        *_, value = super().read(key) or (None, None)
        if value is not None:
            computer = JsonFormatter.deserialize(value, Computer)
            self.__cache[key] = computer

        return None

    def read_all(self) -> List[Computer]:
        if len(self.__cache) == super().count():
            return [*self.__cache.values()]

        read_all_result = super().read_all()
        computers = []
        for name, auditorium, json_data in read_all_result:
            computer: Computer = JsonFormatter.deserialize(json_data, Computer)
            self.__cache[ComputerKey(name, auditorium)] = computer
            computers.append(computer)
        return computers

    def read_keys_by_auditorium(self, auditorium: str) -> List[ComputerKey]:
        read_result = super().read_by_auditorium(auditorium)

        result: List[ComputerKey] = list()
        for name, auditorium, _ in read_result:
            result.append(ComputerKey(name, auditorium))

        return result

    def update(self, key: ComputerKey, computer: Computer) -> None:
        self.__cache[key] = computer
        json_data = JsonFormatter.serialize(computer)
        super().update(key, json_data)

    def delete(self, key: ComputerKey) -> None:
        # silently remove key
        self.__cache.pop(key, None)
        super().delete(key)

    def clear_db(self) -> None:
        self.__cache.clear()
        super().clear_db()
