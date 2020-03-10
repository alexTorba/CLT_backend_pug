from typing import TypeVar

import typing

from Common.NetworkModule.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from External.JsonFomatterModule.JsonContract import JsonContract

T = TypeVar("T", bound=JsonContract)


class RequestDto(BaseRequestDto, typing.Generic[T]):
    data: T
    __json_field = {"d": "data"}

    def __init__(self, server_method: str = None, data: T = None):
        super().__init__(server_method)

        if data is not None:
            self.data = data
        self._update_json_fields(self.__json_field)
