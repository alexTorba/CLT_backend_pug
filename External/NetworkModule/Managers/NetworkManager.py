from http.server import HTTPServer

import socket
import requests  # pip install requests

from External.NetworkModule.Handlers.HttpRequestHandler import HttpRequestHandler
from External.NetworkModule.Handlers.MethodHandler import MethodHandler
from External.NetworkModule.Managers.UrlManager import UrlManager


class NetworkManager:
    __port: int = 8000

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

    @classmethod
    def get_port(cls) -> int:
        return cls.__port

    @classmethod
    def start_listening(cls, method_handler: MethodHandler):
        local_ip = NetworkManager.__get_local_ip()
        print(f"[NetworkManager] Start listening {local_ip}:{cls.__port}")
        httpd = HTTPServer((local_ip, cls.__port), HttpRequestHandler)
        HttpRequestHandler.method_handler = method_handler
        httpd.serve_forever()

    @staticmethod
    def __get_local_ip():
        return socket.gethostbyname(socket.gethostname())
