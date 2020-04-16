import sys
import threading

from Common.Entities.ClientConfig import ClientConfig
from External.NetworkModule.Data.DtoData.ResponceData.ResponseDto import ResponseDto
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class ConfigManager:
    def __init__(self):
        self.__config = ClientConfig()
        self.__lock = threading.Lock()

    def get_current_config(self) -> ClientConfig:
        self.__lock.acquire()
        current_config = self.__config.copy()
        self.__lock.release()
        return current_config

    def start_receiving(self) -> None:
        receive_thread = threading.Thread(target=ConfigManager.__receive_config, args=(self, self.__lock))
        receive_thread.start()

    def __receive_config(self, lock: threading.Lock):
        print("Try to read remote config")  # check that thread is abort after taking remote config
        new_config = ConfigManager.__read_from_server()

        if new_config is None:
            return

        print("Received new config")

        lock.acquire()
        self.__config = new_config
        lock.release()
        sys.exit("q")

    @staticmethod
    def __read_from_server():
        json: str = NetworkManager.get("GetClientConfig")
        return JsonFormatter.deserialize(json, ResponseDto[ClientConfig]).data if json else None
