from Common.Entities.ClientConfig import ClientConfig
from Common.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class ConfigManager:
    @staticmethod
    def get_config() -> ResponseDto[ClientConfig]:
        return ResponseDto[ClientConfig](data=ConfigManager.__get_config_impl())
    
    @staticmethod
    def __get_config_impl() -> ClientConfig:
        file = open("client_config.txt", "r")
        file_content = file.read()
        config = JsonFormatter.deserialize(file_content, ClientConfig)
        if not ConfigManager.__validate_config(config):
            raise Exception("Wrong config !")
        return config

    @staticmethod
    def __validate_config(config: ClientConfig) -> bool:
        if config.check_state_period is not None and config.send_data_period is not None:
            if config.check_state_period < config.send_data_period:
                return True
        return False
