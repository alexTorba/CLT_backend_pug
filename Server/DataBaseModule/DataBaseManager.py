import sqlite3
from typing import List

from Server.DataBaseModule.DAO.ComputerDAO import ComputerDAO


class DataBaseManager:
    __conn: sqlite3.Connection
    __cursor: sqlite3.Cursor
    __dao: ComputerDAO

    def __init__(self) -> None:
        self.__conn = sqlite3.connect("CLT_DB.db")
        self.__cursor = self.__conn.cursor()
        self.__dao = ComputerDAO(self.__cursor)
        self.__dao.try_initialize()

    def create(self, data: str) -> int:
        last_id = self.__dao.create(data)
        self.__conn.commit()
        return last_id

    def read(self, computer_id: int):
        self.__dao.read(computer_id)
        return self.__cursor.fetchone()

    def read_all(self) -> List:
        self.__dao.read_all()
        return self.__cursor.fetchone()

    def update(self, computer_id: int, data: str) -> None:
        self.__dao.update(computer_id, data)
        self.__conn.commit()

    def delete(self, computer_id) -> None:
        self.__dao.delete(computer_id)
        self.__conn.commit()

    def __delattr__(self, name: str) -> None:
        self.__conn.close()
        super().__delattr__(name)
