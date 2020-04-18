import os
import threading
from typing import Tuple, Union

from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.Data.DtoData.RequestData import BaseRequestDto


class UrlManager:
    __host = ""
    __lock = threading.Lock()

    @classmethod
    def get_url(cls, path: str) -> str:
        cls.__lock.acquire()
        result = f"http://{cls.__host}/{path}"
        cls.__lock.release()
        return result

    @classmethod
    def has_host(cls) -> bool:
        return cls.__host != ""

    @classmethod
    def get_host(cls) -> str:
        return cls.__host

    @classmethod
    def set_host(cls, host: str) -> None:
        cls.__lock.acquire()
        print(f"[UrlManager] Setting new host: {host}")
        cls.__host = host
        cls.__lock.release()

    @staticmethod
    def resolve_client_address(dto: BaseRequestDto, client_address: Tuple[str, int]):
        dto.client_ip = client_address[0]
        dto.client_port = client_address[1]
