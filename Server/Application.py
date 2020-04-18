import os

from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.Handlers.MethodHandler import MethodHandler
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from Server.ComputerModule.ComputerManager import ComputerManager
from Server.ConfigModule.ConfigManager import ConfigManager
from Server.ClientsNotifier import ClientsNotifier
from Server.Data.ServerConfig import ServerConfig


class Application:
    __config_file: str = "server_config.txt"
    __default_prio: int = 1
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
        self.__clients_notifier = ClientsNotifier(self.__read_prio())

    def run(self):
        self.__clients_notifier.run()
        NetworkManager.start_listening(self.__method_handler)

    @classmethod
    def __read_prio(cls):
        config = cls.__read_config(cls.__config_file)
        return config.prio if config is not None else cls.__default_prio

    @staticmethod
    def __read_config(file_name: str):
        if os.path.exists(file_name):
            with open(file_name) as file:
                json = file.read()
                if len(json) > 0:
                    return JsonFormatter.deserialize(json, ServerConfig)
        return None
