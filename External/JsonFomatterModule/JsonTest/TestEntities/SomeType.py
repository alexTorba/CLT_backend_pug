from typing import Dict, List

from External.JsonFomatterModule.JsonContract import JsonContract
from External.JsonFomatterModule.JsonTest.TestEntities.Person import Person


class SomeType(JsonContract):
    my_list: List[Person]
    my_dict: Dict[str, Person]

    __json_fields = {
        "l": "my_list",
        "d": "my_dict"
    }

    def __init__(self, some_dict: Dict[str, Person] = None, some_list: List[Person] = None):
        super().__init__(self.__json_fields)
        if some_dict is not None:
            self.my_dict = some_dict
        if some_list is not None:
            self.my_list = some_list

    @staticmethod
    def get_random_some_type():
        my_dict = {
            "first_str": Person(1),
            "second_str": Person(2),
            "third_str": Person(3),
            "forth_str": Person(4),
            "fifth_str": Person(5),
        }
        my_list = [Person(20), Person(30)]
        return SomeType(my_dict, my_list)
