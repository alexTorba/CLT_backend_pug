import threading
import socket
import time

from External.NetworkModule.Managers.NetworkManager import NetworkManager


class ClientsNotifier:
    __port: int = 37020
    __period: int = 30  # seconds

    def __init__(self, prio: int):
        self.__prio = prio

    def run(self):
        self.__sock = ClientsNotifier.__setup_socket(self.__port)
        self.__start_notifying()

    @staticmethod
    def __setup_socket(port: int) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.settimeout(0.2)
        return sock

    def __start_notifying(self):
        self.__notify_thread = threading.Thread(target=ClientsNotifier.__notify_job, args=(self,))
        self.__notify_thread.start()

    def __notify_job(self):
        message = ClientsNotifier.__build_message(self.__prio)

        while True:
            self.__sock.sendto(message.encode(), ("<broadcast>", self.__port))
            print("[ClientsNotifier] Notified clients")
            time.sleep(self.__period)

    @staticmethod
    def __build_message(prio: int) -> str:
        return str(prio) + "." + str(NetworkManager.get_port())
