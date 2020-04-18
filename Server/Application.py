from External.NetworkModule.Handlers.MethodHandler import MethodHandler
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from External.NetworkModule.Managers.UrlManager import UrlManager
from Server.ComputerModule.ComputerManager import ComputerManager
from Server.ConfigModule.ConfigManager import ConfigManager
from Server.ClientsNotifier import ClientsNotifier


class Application:
    __method_handler: MethodHandler
    __clients_notifier: ClientsNotifier

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
        self.__clients_notifier = ClientsNotifier(10)

    def run(self):
        self.__clients_notifier.run()
        NetworkManager.start_listening(self.__method_handler)
