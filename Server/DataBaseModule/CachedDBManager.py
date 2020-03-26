from typing import List, Dict, Union

from Server.DataBaseModule.DBManager import DBManager
from Server.Data.ComputerKey import ComputerKey


class CachedDBManager(DBManager):
    __cache: Dict[ComputerKey, str] = dict()

    def __init__(self) -> None:
        super().__init__()

    def create(self, key: ComputerKey, data: str) -> None:
        self.__cache[key] = data
        super().create(key, data)

    def read(self, key: ComputerKey) -> Union[str, None]:
        value = self.__cache.get(key)
        if value is not None:
            return value

        *_, value = super().read(key) or (None, None)
        if value is not None:
            self.__cache[key] = value

        return value

    def read_all(self) -> List[str]:
        if len(self.__cache) == super().count():
            return [*self.__cache.values()]

        read_all_result = super().read_all()
        json_data_values = []
        for name, auditorium, json_data in read_all_result:
            json_data_values.append(json_data)
        return json_data_values

    def update(self, key: ComputerKey, data: str) -> None:
        self.__cache[key] = data
        super().update(key, data)

    def delete(self, key: ComputerKey) -> None:
        # silently remove key
        self.__cache.pop(key, None)
        super().delete(key)

    def clear_db(self) -> None:
        self.__cache.clear()
        super().clear_db()
