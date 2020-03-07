from typing import TypeVar

import typing

from CommonExternal.JsonFomatterModule.JsonContract import JsonContract
from CommonExternal.NetworkModule.DtoData.RequestData.BaseRequestDto import BaseRequestDto

T = TypeVar("T", bound=JsonContract)


class RequestDto(BaseRequestDto, typing.Generic[T]):
    data: T

    def __init__(self, server_method: str = None, data: T = None):
        super().__init__(server_method)
        if data is not None:
            self.data = data
        json_field = {"d": "data"}
        self._update_json_fields(json_field)
