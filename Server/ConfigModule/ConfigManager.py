import os

from Common.Entities.ClientConfig import ClientConfig
from External.NetworkModule.Data.DtoData.ResponceData.ResponseDto import ResponseDto
from External.NetworkModule.Data.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.Data.ExceptionsData.ServerLogicException import ServerLogicException


class ConfigManager:
    __file_name: str = "client_config.txt"

    # -------------------------------------------------------------------------

    @staticmethod
    def get_config() -> ResponseDto[ClientConfig]:
        return ResponseDto[ClientConfig](200, ConfigManager.__get_config_impl())

    @classmethod
    def __get_config_impl(cls) -> ClientConfig:
        try:
            return ConfigManager.__read_config_from_file(cls.__file_name)
        except Exception as e:
            print(e)

        return ClientConfig()

    # -------------------------------------------------------------------------

    @staticmethod
    def set_config(dto: RequestDto[ClientConfig]) -> BaseResponseDto:
        success = ConfigManager.__set_config_impl(dto.data)
        return BaseResponseDto(200 if success else 406)

    @classmethod
    def __set_config_impl(cls, web_config: ClientConfig) -> bool:
        if not hasattr(web_config, "check_state_period") or not hasattr(web_config, "send_data_period"):
            raise ServerLogicException(401, "Received wrong data from client !")

        if ConfigManager.__validate_config(web_config):
            with open(cls.__file_name, "w") as config_file:
                config_file.write(JsonFormatter.serialize(web_config))
                return True

        return False

    # -------------------------------------------------------------------------

    @staticmethod
    def __read_config_from_file(file_name: str) -> ClientConfig:
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                file_content = file.read()
        else:
            raise Exception(f"Can not open file with Client config (file: {file_name})")

        if file_content:
            config = JsonFormatter.deserialize(file_content, ClientConfig)
            if ConfigManager.__validate_config(config):
                return config

        raise Exception(f"Client config in {file_name} is invalid, check the file")

    @staticmethod
    def __validate_config(config: ClientConfig) -> bool:
        has_required_attributes = config.check_state_period is not None and config.send_data_period is not None
        return has_required_attributes and config.check_state_period < config.send_data_period
