from External.NetworkModule.MethodHandler import MethodHandler
from External.NetworkModule.NetworkManager import NetworkManager
from Server.ComputerModule.ComputerManager import ComputerManager
from Server.ConfigModule.ConfigManager import ConfigManager


class Application:
    __method_handler: MethodHandler

    def __init__(self):
        method_by_name = {
            "GetClientConfig": ConfigManager.get_config,
            "SendComputerFlow": ComputerManager.send_computer_flow,
            "GetAuditoriums": ComputerManager.get_auditoriums,
            "GetKeysByAuditorium": ComputerManager.get_keys_by_auditorium,
            "GetComputer": ComputerManager.get_computer
        }
        self.__method_handler = MethodHandler(method_by_name)

    def run(self):
        NetworkManager.start_listening(self.__method_handler)
