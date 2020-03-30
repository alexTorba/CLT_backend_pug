from typing import Dict, Union, Callable

from Common.NetworkModule.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from Common.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from Common.NetworkModule.NetworkManager import NetworkManager
from Server.ConfigModule.ConfigManager import ConfigManager


class Application:
    __method_handler: Dict[str, Union[Callable[[], BaseResponseDto], Callable[[BaseRequestDto], BaseResponseDto]]]

    def __init__(self):
        self.__method_handler = {
            "GetClientConfig": ConfigManager.get_config
        }

    def run(self):
        NetworkManager.start_listening(self.__method_handler)
