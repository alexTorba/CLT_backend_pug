import sys
import threading

from Common.Entities.ClientConfig import ClientConfig
from Common.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from Common.NetworkModule.NetworkManager import NetworkManager
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class ConfigManager:
    def __init__(self):
        self.__config = ClientConfig()
        self.__lock = threading.Lock()

    def get_config(self) -> ClientConfig:
        return self.__config

    def start_receiving(self):
        receive_thread = threading.Thread(target=ConfigManager.__receive_config, args=(self, self.__lock))
        receive_thread.start()

    def __receive_config(self, lock: threading.Lock):
        print("try to read remote config")  # check thar thread is abort after taking remote config
        new_config = ConfigManager.__read_from_server()

        if new_config is None:
            return

        print("receive new config")

        lock.acquire()
        self.__config = new_config
        lock.release()
        sys.exit("q")

    def get_config_copy(self):
        return self.__config.copy()

    @staticmethod
    def __read_from_server():
        json: str = NetworkManager.get("GetClientConfig")
        return JsonFormatter.deserialize(json, ResponseDto[ClientConfig]).data if json else None

    def get_current_state(self):
        self.__lock.acquire()
        current_config = self.get_config_copy()
        print(f"Current check_state_period = {current_config.check_state_period}")
        self.__lock.release()
        return current_config
