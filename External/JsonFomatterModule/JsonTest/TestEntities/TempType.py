from typing import List, Tuple

from External.JsonFomatterModule.JsonContract import JsonContract


class TempType(JsonContract):
    my_field: List[Tuple[str, float]]
    __json_fields = {
        "m": "my_field"
    }

    def __init__(self, my_field: List[Tuple[str, float]] = None):
        super().__init__(self.__json_fields)
        if my_field is not None:
            self.my_field = my_field

    @staticmethod
    def get_random_temp_type():
        return TempType([("d", 30.0), ("c", 20.0)])
