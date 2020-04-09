from Common.Entities.ComputerFlow import ComputerFlow
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey
from Server.DataBaseModule.CachedDBManager import CachedDBManager


class CacheDataBaseTest:
    __db_manager: CachedDBManager = CachedDBManager()
    __last_key: ComputerKey

    @classmethod
    def create(cls):
        print("Create row in db test")
        computer = Computer.get_random_computer()
        cls.__last_key = computer.key
        cls.__db_manager.create(computer.key, computer)
        print(f"Creating was successful. ComputerKey = {computer.key}")

    @classmethod
    def read(cls, additional_info: bool = None):
        print("\nTry to read last added row in db")
        computer = cls.__db_manager.read(cls.__last_key)
        print(f"Key = {cls.__last_key}")
        if additional_info:
            print(computer.data.get_last_state())
        print("Reading the row was successful")

    @classmethod
    def read_by_auditorium(cls):
        print("\nTry to read computers of last added auditorium")
        computers = cls.__db_manager.read_computers_by_auditorium(cls.__last_key.auditorium)
        for computer in computers:
            print(computer.key)
        print("Reading the row was successful")

    @classmethod
    def read_all(cls):
        print("\nTry to read all rows in db")
        for computer in cls.__db_manager.read_all():
            print(computer.data.get_last_state())
        print("Reading all rows was successful")

    @classmethod
    def update(cls):
        print(f"\nUpdate last computer data with key = {cls.__last_key}")
        new_computer = Computer.get_random_computer()
        cls.__db_manager.update(cls.__last_key, new_computer)
        print("updating was successful")

    @classmethod
    def delete(cls):
        print(f"\nDelete last row - {cls.__last_key}")
        cls.__db_manager.delete(cls.__last_key)
        print("deleting was successful")

    @classmethod
    def clear_db(cls):
        cls.__db_manager.clear_db()


if __name__ == '__main__':
    CacheDataBaseTest.clear_db()
    CacheDataBaseTest.create()
    CacheDataBaseTest.create()
    CacheDataBaseTest.read_all()
    CacheDataBaseTest.read(True)
    CacheDataBaseTest.read_by_auditorium()
    CacheDataBaseTest.update()
    CacheDataBaseTest.read(True)
    CacheDataBaseTest.delete()
    CacheDataBaseTest.read_by_auditorium()
    CacheDataBaseTest.read_all()
