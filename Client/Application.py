import time
import threading

from Client.ComputerStateManager import ComputerStateManager
from Common.Entities.ClientConfig import ClientConfig


class Application:

    def __init__(self):
        self.__config = ClientConfig()
        pass

    def run(self) -> None:
        computer_state_manager = ComputerStateManager()

        lock = threading.Lock()
        receive_thread = threading.Thread(target=Application.__receive_config, args=(self, lock))
        receive_thread.start()

        x = 0  # for testing

        last_time_sent_data = time.time()
        while True:
            computer_state_manager.save_current_state()

            lock.acquire()
            current_config = self.__config.copy()
            lock.release()

            if last_time_sent_data + current_config.send_data_period < time.time():
                computer_state_manager.send_data_to_server()
                last_time_sent_data = time.time()

            x += 1  # for testing
            if x > 4:  # for testing
                break  # for testing

            time.sleep(current_config.check_state_period)

    def __receive_config(self, lock):
        new_config = ClientConfig(3, 1000)  # TODO receive some config from server using network manager

        lock.acquire()
        self.__config = new_config
        lock.release()
