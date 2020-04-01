from External.NetworkModule.MethodHandler import MethodHandler
from External.NetworkModule.NetworkManager import NetworkManager
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
