import threading
import time

from Common.Entities.ClientConfig import ClientConfig
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.Data.DtoData.ResponceData.ResponseDto import ResponseDto
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from External.NetworkModule.Managers.UrlManager import UrlManager


class ConfigManager:
    __refresh_config_period: float = 15

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
        while True:
            print("[ConfigManager] Try to read remote config")  # check that thread is abort after taking remote config
            new_config = ConfigManager.__read_from_server()

            if new_config is not None:
                print(f"[ConfigManager] Received new config: check_state_period={new_config.check_state_period}, send_data_period={new_config.send_data_period}")
                lock.acquire()
                self.__config = new_config
                lock.release()

            time.sleep(self.__refresh_config_period)

    @staticmethod
    def __read_from_server():
        if UrlManager.has_host():
            json: str = NetworkManager.get("GetClientConfig")
            if json:
                return JsonFormatter.deserialize(json, ResponseDto[ClientConfig]).data

        return None
