from External.JsonFomatterModule.JsonContract import JsonContract


class Person(JsonContract):
    age: int
    __json_fields = {
        "a": "age"
    }

    def __init__(self, age: int = None):
        super().__init__(self.__json_fields)
        if age is not None:
            self.age = age