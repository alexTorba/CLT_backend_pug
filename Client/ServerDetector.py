import threading
import socket

from External.NetworkModule.Managers.UrlManager import UrlManager


class ServerDetector:
    __port: int = 37020
    __buffer_size: int = 128

    def __init__(self):
        self.__current_serv_prio = 0

    def run(self):
        self.__sock = ServerDetector.__setup_socket(self.__port)
        self.__start_detecting()

    @staticmethod
    def __setup_socket(port: int):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(("", port))
        return sock

    def __start_detecting(self):
        self.__receive_thread = threading.Thread(target=ServerDetector.__listen_server_messages, args=(self,))
        self.__receive_thread.start()

    def __listen_server_messages(self):
        while True:
            data, sender = self.__sock.recvfrom(self.__buffer_size)
            message = data.decode()

            prio, port = message.split(".")
            if int(prio) > self.__current_serv_prio:
                print(f"[ServerDetector] Detected new server with prio {prio}")
                self.__current_serv_prio = int(prio)
                new_host = sender[0] + ":" + port
                UrlManager.set_host(new_host)
