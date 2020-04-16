from typing import Tuple

from External.NetworkModule.Data.DtoData.RequestData import BaseRequestDto


class UrlManager:
    __host: str = "127.0.0.1:8000"

    @classmethod
    def get_url(cls, path: str) -> str:
        return f"http://{cls.__host}/{path}"

    @classmethod
    def set_host(cls, host: str) -> None:
        cls.__host = host

    @staticmethod
    def resolve_client_address(dto: BaseRequestDto, client_address: Tuple[str, int]):
        dto.client_ip = client_address[0]
        dto.client_port = client_address[1]
