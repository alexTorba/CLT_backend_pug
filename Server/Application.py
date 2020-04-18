from External.NetworkModule.Handlers.MethodHandler import MethodHandler
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from External.NetworkModule.Managers.UrlManager import UrlManager
from Server.ComputerModule.ComputerManager import ComputerManager
from Server.ConfigModule.ConfigManager import ConfigManager


class Application:
    __method_handler: MethodHandler

    def __init__(self):
        method_by_name = {
            "GetClientConfig": ConfigManager.get_config,
            "SetClientConfig": ConfigManager.set_config,
            "SendComputerFlow": ComputerManager.send_computer_flow,
            "GetAuditoriums": ComputerManager.get_auditoriums,
            "GetKeysByAuditorium": ComputerManager.get_keys_by_auditorium,
            "GetComputer": ComputerManager.get_computer
        }
        self.__method_handler = MethodHandler(method_by_name)
        UrlManager.init_url()

    def run(self):
        print("Start listening")
        NetworkManager.start_listening(self.__method_handler)
