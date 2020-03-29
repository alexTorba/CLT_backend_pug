from Common.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from Common.NetworkModule.NetworkManager import NetworkManager
from External.JsonFomatterModule.JsonContract import JsonContract
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class ClientConfig(JsonContract):
    check_state_period: int  # seconds
    send_data_period: int  # seconds
    __json_fields = {
        "c": "check_state_period",
        "s": "send_data_period"
    }

    def __init__(self, check_state_period: int = 15, send_data_period: int = 900):
        super().__init__(self.__json_fields)
        self.check_state_period = check_state_period
        self.send_data_period = send_data_period

    def copy(self):
        return ClientConfig(self.check_state_period, self.send_data_period)

    @staticmethod
    def read_from_file(file_name):
        file = open(file_name, "r")
        file_content = file.read()
        return JsonFormatter.deserialize(file_content, ClientConfig)

    @staticmethod
    def read_from_server():
        json = NetworkManager.get("ClientConfig")
        return JsonFormatter.deserialize(json, ResponseDto[ClientConfig]).data if json else None
