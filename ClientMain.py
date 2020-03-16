import time

from Client.ClientConfig import ClientConfig
from Client.ComputerStateManager import ComputerStateManager

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    computer_state_manager = ComputerStateManager()
    client_config = ClientConfig()

    last_time_sent_data = time.time()
    while True:
        computer_state_manager.save_current_state()

        if last_time_sent_data + client_config.send_data_period < time.time():
            computer_state_manager.send_data_to_server()

        time.sleep(client_config.check_state_period)

# ------------------------------------------------------------------------------