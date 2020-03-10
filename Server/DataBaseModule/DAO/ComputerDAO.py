from sqlite3 import Cursor


class ComputerDAO:
    _cursor: Cursor

    __create_table: str = """CREATE TABLE IF NOT EXISTS [Computers] ([Id] INTEGER PRIMARY KEY AUTOINCREMENT, [Data] TEXT NOT NULL)"""

    __create_query: str = """INSERT INTO [Computers] ([Data]) VALUES (?)"""

    __read_query: str = """SELECT Data FROM [Computers] WHERE [Id] = {Id}"""

    __read_all_query: str = """SELECT * FROM [Computer]"""

    __update_query: str = """UPDATE [{table_name}] SET [Data] = {data} WHERE [Id] = {Id}"""

    __delete_query: str = """DELETE FROM [{table_name}] WHERE [Id] = {Id}"""

    def __init__(self, cursor: Cursor) -> None:
        self._cursor = cursor

    def try_initialize(self) -> None:
        query: str = self.__create_table
        self._cursor.execute(query)

    def create(self, data: str) -> int:  # return last autoincrement id
        query: str = self.__create_query
        self._cursor.execute(query, *data)
        return self._cursor.lastrowid

    def read(self, computer_id: int):
        query: str = self.__read_query.format(Id=computer_id)
        self._cursor.execute(query)

    def read_all(self):
        query: str = self.__read_all_query
        self._cursor.execute(query)

    def update(self, computer_id: int, data: str) -> None:
        query: str = self.__update_query.format(Id=computer_id, Data=data)
        self._cursor.execute(query)

    def delete(self, computer_id: int):
        query: str = self.__delete_query.format(Id=computer_id)
        self._cursor.execute(query)
