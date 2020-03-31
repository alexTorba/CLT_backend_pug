from http.server import HTTPServer
from typing import Union, Dict, Callable

import requests  # pip install requests

from Common.NetworkModule.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from Common.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from Common.NetworkModule.HttpRequestHandler import HttpRequestHandler
from Common.NetworkModule.MethodHandler import MethodHandler
from Common.NetworkModule.UrlManager import UrlManager


class NetworkManager:

    @staticmethod
    def send(path: str, data: str) -> str:
        url = UrlManager.get_url(path)
        response: str = ""
        try:
            response = requests.post(url, data).content.decode("utf-8")
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def get(path: str) -> str:
        url = UrlManager.get_url(path)
        response: str = ""
        try:
            response = requests.get(url).content.decode("utf-8")
        except Exception as e:
            print(f"Connection error ! {e}")
        return response

    @staticmethod
    def start_listening(method_handler: Dict[str, Union[Callable[[], BaseResponseDto], Callable[[BaseRequestDto], BaseResponseDto]]]):
        httpd = HTTPServer(("localhost", 8000), HttpRequestHandler)
        HttpRequestHandler.method_handler = MethodHandler(method_handler)
        httpd.serve_forever()
