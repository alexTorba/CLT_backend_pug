import time

from Client.ComputerStateManager import ComputerStateManager
from Client.ConfigManager import ConfigManager


class Application:
    def __init__(self):
        self.__computer_state_manager = ComputerStateManager()
        self.__config_manager = ConfigManager()

    def run(self) -> None:
        self.__config_manager.start_receiving()

        last_time_sent_data = time.time()
        while True:
            print("Saving current state")
            self.__computer_state_manager.save_current_state()

            current_config = self.__config_manager.get_current_config()

            if last_time_sent_data + current_config.send_data_period < time.time():
                print("Sending data to server")
                self.__computer_state_manager.send_data_to_server()
                last_time_sent_data = time.time()

            time.sleep(current_config.check_state_period)
