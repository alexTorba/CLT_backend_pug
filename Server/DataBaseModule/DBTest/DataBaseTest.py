from typing import List

from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey
from Server.DataBaseModule.DBManager import DBManager


class DataBaseTest:
    __db_manager: DBManager = DBManager()
    __last_key: ComputerKey

    @classmethod
    def create(cls):
        print("Create row in db test")
        computer = Computer.get_random_computer()
        cls.__last_key = computer.key
        json = JsonFormatter.serialize(computer.data)
        cls.__db_manager.create(computer.key, json)
        print(f"Creating was successful. ComputerKey = {computer.key}")

    @classmethod
    def read(cls, additional_info: bool = None):
        print("\nTry to read last added row in db")
        name, auditorium, json_data = cls.__db_manager.read(cls.__last_key)
        computer_data = JsonFormatter.deserialize(json_data, ComputerFlow)
        key = ComputerKey(name, auditorium)
        computer = Computer(key, computer_data)
        print(f"Key = {key}")
        if additional_info:
            print(computer.data.get_last_state())
        print("Reading the row was successful")

    @classmethod
    def read_auditoriums(cls):
        print("\nTry to read auditoriums in db")
        for auditorium in cls.__db_manager.read_auditoriums():
            print(auditorium)
        print("Reading auditoriums was successful")

    @classmethod
    def read_all(cls):
        print("\nTry to read all rows in db")
        computers: List[Computer] = list()
        for name, auditorium, json_data in cls.__db_manager.read_all():
            computer_data = JsonFormatter.deserialize(json_data, ComputerFlow)
            key = ComputerKey(name, auditorium)
            computer = Computer(key, computer_data)
            computers.append(computer)
        print("Computer ids :")
        for computer in computers:
            print(computer.key)
        print("Reading all rows was successful")

    @classmethod
    def update(cls):
        print(f"\nUpdate last computer data with key = {cls.__last_key}")
        new_computer_data = ComputerFlow.get_random_flow()
        json = JsonFormatter.serialize(new_computer_data)
        cls.__db_manager.update(cls.__last_key, json)
        print("updating was successful")

    @classmethod
    def delete(cls):
        print(f"\nDelete last row - {cls.__last_key}")
        cls.__db_manager.delete(cls.__last_key)
        print("deleting was successful")

    @classmethod
    def clear_db(cls):
        cls.__db_manager.clear_db()

    @classmethod
    def test_wrong_read(cls):
        computer = Computer.get_random_computer()
        result = cls.__db_manager.read(computer.key)
        print(result)

    @staticmethod
    def test_db():
        DataBaseTest.clear_db()
        DataBaseTest.create()
        DataBaseTest.create()
        DataBaseTest.read_all()
        DataBaseTest.read_auditoriums()
        DataBaseTest.read(True)
        DataBaseTest.update()
        DataBaseTest.read(True)
        DataBaseTest.delete()
        DataBaseTest.read_all()


if __name__ == '__main__':
    DataBaseTest.test_db()
