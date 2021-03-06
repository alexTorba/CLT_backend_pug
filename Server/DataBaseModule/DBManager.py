import sqlite3
from typing import List

from Server.Data.ComputerKey import ComputerKey
from Server.DataBaseModule.DAO.ComputerDAO import ComputerDAO


class DBManager:
    __conn: sqlite3.Connection
    __cursor: sqlite3.Cursor
    __dao: ComputerDAO

    def __init__(self) -> None:
        self.__conn = sqlite3.connect("CLT_DB.db")
        self.__cursor = self.__conn.cursor()
        self.__dao = ComputerDAO(self.__cursor)
        self.__dao.try_initialize()

    def create(self, key: ComputerKey, data: str) -> None:
        self.__dao.create(key.name, key.auditorium, data)
        self.__conn.commit()

    def read(self, key: ComputerKey) -> (str, str, str):
        self.__dao.read(key.name, key.auditorium)
        return self.__cursor.fetchone()

    def read_by_auditorium(self, auditorium: str) -> List:
        self.__dao.read_by_auditorium(auditorium)
        return self.__cursor.fetchall()

    def read_auditoriums(self) -> List[str]:
        self.__dao.read_auditoriums()
        # the transformation needed because "fetchall" returns list of tuples
        return [auditorium[0] for auditorium in self.__cursor.fetchall()]

    def read_all(self) -> List:
        self.__dao.read_all()
        return self.__cursor.fetchall()

    def update(self, key: ComputerKey, data: str) -> None:
        self.__dao.update(key.name, key.auditorium, data)
        self.__conn.commit()

    def delete(self, key: ComputerKey) -> None:
        self.__dao.delete(key.name, key.auditorium)
        self.__conn.commit()

    def count(self) -> int:
        self.__dao.count()
        return self.__cursor.fetchone()[0]

    def count_by_key(self, key: ComputerKey) -> int:
        self.__dao.count_by_key(key.name, key.auditorium)
        return self.__cursor.fetchone()[0]

    def clear_db(self) -> None:
        self.__dao.clear_db()
        self.__conn.commit()

    def __delattr__(self, name: str) -> None:
        self.__conn.close()
        super().__delattr__(name)
