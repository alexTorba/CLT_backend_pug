from typing import Union, Callable, Dict

from Common.NetworkModule.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from Common.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto


class MethodHandler:
    __method_handler: Dict[str, Union[Callable[[], BaseResponseDto], Callable[[BaseRequestDto], BaseResponseDto]]]

    def __init__(self, method_handler: dict):
        self.__method_handler = method_handler

    def do_get(self, server_method: str):
        return self.__method_handler[server_method]()

    def do_post(self):
        pass

    @staticmethod
    def get_server_method_name(request_path: str) -> str:
        return request_path[1:]