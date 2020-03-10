import psutil
import time

from Client.ClientConfig import ClientConfig
from Common.Entities.ComputerState import ComputerState
from Common.Entities.ComputerFlow import ComputerFlow

#------------------------------------------------------------------------------

def send_data_to_server(computer_flow: ComputerFlow):
    pass

#------------------------------------------------------------------------------

def read_current_computer_state() -> ComputerState:
    memory_info = psutil.virtual_memory()

    current_time = time.time()
    cpu = psutil.cpu_percent()
    ram = memory_info[2]
    disk = 10.0
    return ComputerState(current_time, cpu, ram, disk)

#------------------------------------------------------------------------------

if __name__ == '__main__':
    client_config = ClientConfig.create_default_config()
    computer_flow = ComputerFlow()

    last_time_sent_data = time.time()
    while True:
        current_state = read_current_computer_state()
        computer_flow.store_computer_state(current_state)

        if last_time_sent_data + client_config.send_data_period < time.time():
            send_data_to_server(computer_flow)
            computer_flow = ComputerFlow()
            last_time_sent_data = time.time()

        time.sleep(client_config.check_state_period)

#------------------------------------------------------------------------------
