from typing import Dict, Union, Callable

from Common.NetworkModule.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from Common.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from Common.NetworkModule.MethodHandler import MethodHandler
from Common.NetworkModule.NetworkManager import NetworkManager
from Server.ComputerModule.ComputerManager import ComputerManager
from Server.ConfigModule.ConfigManager import ConfigManager


class Application:
    __method_handler: MethodHandler

    def __init__(self):
        method_by_name = {
            "GetClientConfig": ConfigManager.get_config,
            "SendComputerFlow": ComputerManager.send_computer_state
        }
        self.__method_handler = MethodHandler(method_by_name)

    def run(self):
        NetworkManager.start_listening(self.__method_handler)
