import time

from Client.ComputerStateManager import ComputerStateManager
from Client.ConfigManager import ConfigManager
from Client.ServerDetector import ServerDetector


class Application:

    def __init__(self):
        self.__computer_state_manager = ComputerStateManager()
        self.__config_manager = ConfigManager()
        self.__server_detector = ServerDetector()

    def run(self) -> None:
        self.__config_manager.start_receiving()
        self.__server_detector.run()

        last_time_sent_data = time.time()
        while True:
            print("[ClientApplication] Saving current state")
            self.__computer_state_manager.save_current_state()

            current_config = self.__config_manager.get_current_config()

            if last_time_sent_data + current_config.send_data_period < time.time():
                print("[ClientApplication] Sending data to server")
                self.__computer_state_manager.send_data_to_server()
                last_time_sent_data = time.time()

            time.sleep(current_config.check_state_period)
