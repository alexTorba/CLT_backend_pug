from Common.Entities.ClientConfig import ClientConfig
from Common.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from Common.NetworkModule.NetworkManager import NetworkManager


class Application:
    def __init__(self):
        pass

    def run(self):
        method_handler: dict = {"ClientConfig": self.get_config}
        NetworkManager.start_listening(method_handler)

    @staticmethod
    def get_config() -> ResponseDto[ClientConfig]:
        return ResponseDto[ClientConfig](data=ClientConfig(20, 1000))
