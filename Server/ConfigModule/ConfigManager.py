import os

from Common.Entities.ClientConfig import ClientConfig
from External.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class ConfigManager:
    __file_name = "client_config.txt"

    @staticmethod
    def get_config() -> ResponseDto[ClientConfig]:
        return ResponseDto[ClientConfig](200, ConfigManager.__get_config_impl())

    @classmethod
    def __get_config_impl(cls) -> ClientConfig:
        if os.path.exists(cls.__file_name):
            with open(cls.__file_name, "r") as file:
                file_content = file.read()
            config = JsonFormatter.deserialize(file_content, ClientConfig)
            if not ConfigManager.__validate_config(config):
                raise Exception("Wrong config !")
            return config
        return ClientConfig(20, 2000)

    @staticmethod
    def __validate_config(config: ClientConfig) -> bool:
        if config.check_state_period is not None and config.send_data_period is not None:
            if config.check_state_period < config.send_data_period:
                return True
        return False
