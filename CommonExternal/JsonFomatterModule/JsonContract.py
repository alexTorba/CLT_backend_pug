from abc import ABC, abstractmethod
from copy import copy
from typing import Dict


class JsonContract(ABC):
    """Each class that will override this class must have :\n
    - annotations for all fields\n
    - implement _json_field\n
    - open ctor\n"""

    @property
    @abstractmethod
    def _json_fields(self) -> dict:  # key = minimized field name, value = full field name
        pass

    __field_json: dict = NotImplemented  # key = full field name, value = minimized field name

    def to_minimize_dict(self) -> dict:
        """format object to minimize dict"""
        if self.__field_json is NotImplemented:
            self.__field_json = dict(zip(self._json_fields.values(), self._json_fields.keys()))
        for n, v in self.__dict__.items():
            if not n.startswith("_"):
                yield self.__field_json[n], copy(v)

    def _update_json_fields(self, json_fields: Dict[str, str]) -> None:
        self._json_fields.update(json_fields)

    def json_to_field(self, min_field: str) -> str:
        """convert minimize field to full name field"""
        return self._json_fields.get(min_field)
