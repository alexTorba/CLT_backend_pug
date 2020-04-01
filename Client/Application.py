import time

from Client.ComputerStateManager import ComputerStateManager
from Client.ConfigModule.ConfigManager import ConfigManager


class Application:
    def __init__(self):
        self.__computer_state_manager = ComputerStateManager()
        self.__config_manager = ConfigManager()
        pass

    def run(self) -> None:
        self.__config_manager.start_receiving()

        x = 0  # for testing

        last_time_sent_data = time.time()
        while True:
            self.__computer_state_manager.save_current_state()

            current_config = self.__config_manager.get_current_state()
            # self.__computer_state_manager.send_data_to_server()  # to check server method

            if last_time_sent_data + current_config.send_data_period < time.time():
                self.__computer_state_manager.send_data_to_server()
                last_time_sent_data = time.time()

            x += 1  # for testing
            if x > 4:  # for testing
                break  # for testing

            time.sleep(current_config.check_state_period)
