from sqlite3 import Cursor


class ComputerDAO:
    __cursor: Cursor

    __create_table: str = """CREATE TABLE IF NOT EXISTS [Computers] (
    [Name] TEXT NOT NULL,
    [Auditorium] TEXT NOT NULL,
    [Data] TEXT NOT NULL,
    PRIMARY KEY ([Name], [Auditorium])
);"""

    __create_query: str = """INSERT INTO [Computers] ([Name], [Auditorium], [Data]) VALUES (?, ?, ?)"""

    __read_query: str = """SELECT * FROM [Computers] WHERE [Name] = {name} AND [Auditorium] = {auditorium}"""

    __read_auditorium_query: str = """SELECT * FROM [Computers] WHERE [Auditorium] = {auditorium}"""

    __read_auditoriums: str = """SELECT DISTINCT [Auditorium] FROM [Computers]"""

    __read_all_query: str = """SELECT * FROM [Computers]"""

    __update_query: str = """UPDATE [Computers] SET [Data] = (?) WHERE [Name] = {name} AND [Auditorium] = {auditorium};"""

    __delete_query: str = """DELETE FROM [Computers] WHERE [Name] = {name} AND [Auditorium]={auditorium}"""

    __clear_db_query: str = """DELETE FROM [Computers]"""

    __count_db_query: str = """SELECT COUNT(*) FROM [Computers]"""

    __count_db_key_query: str = """SELECT COUNT(*) FROM [Computers] WHERE [Name] = {name} AND [Auditorium] = {auditorium}"""

    def __init__(self, cursor: Cursor) -> None:
        self.__cursor = cursor

    def try_initialize(self) -> None:
        self.__cursor.execute(self.__create_table)

    def create(self, name: str, auditorium: str, data: str) -> None:
        query: str = self.__create_query
        self.__cursor.execute(query, (name, auditorium, data))

    def read(self, name: str, auditorium: str) -> None:
        query: str = self.__read_query.format(name=name, auditorium=auditorium)
        self.__cursor.execute(query)

    def read_by_auditorium(self, auditorium: str) -> None:
        query: str = self.__read_auditorium_query.format(auditorium=auditorium)
        self.__cursor.execute(query)

    def read_auditoriums(self) -> None:
        query: str = self.__read_auditoriums
        self.__cursor.execute(query)

    def read_all(self) -> None:
        query: str = self.__read_all_query
        self.__cursor.execute(query)

    def update(self, name: str, auditorium: str, data: str) -> None:
        query: str = self.__update_query.format(name=name, auditorium=auditorium)
        self.__cursor.execute(query, (data,))

    def delete(self, name: str, auditorium: str) -> None:
        query: str = self.__delete_query.format(name=name, auditorium=auditorium)
        self.__cursor.execute(query)

    def clear_db(self) -> None:
        query = self.__clear_db_query
        self.__cursor.execute(query)

    def count(self) -> None:
        query = self.__count_db_query
        self.__cursor.execute(query)

    def count_by_key(self, name: str, auditorium: str) -> None:
        query = self.__count_db_key_query.format(name=name, auditorium=auditorium)
        self.__cursor.execute(query)
