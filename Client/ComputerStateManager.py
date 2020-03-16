import psutil
import time

from Common.Entities.ComputerState import ComputerState
from Common.Entities.ComputerFlow import ComputerFlow

class ComputerStateManager:

    def __init__(self):
        self.__computer_flow = ComputerFlow()

    def send_data_to_server(self) -> None:
        self.__computer_flow = ComputerFlow()
        pass

    def save_current_state(self) -> None:
        current_state = self.__read_current_computer_state()
        self.__computer_flow.store_computer_state(current_state)

    def __read_current_computer_state(self) -> ComputerState:
        current_time = time.time()
        cpu_usage    = psutil.cpu_percent()
        ram_usage    = self.__read_memory_usage()
        disk_usage   = self.__read_disk_usage()
        return ComputerState(current_time, cpu_usage, ram_usage, disk_usage)

    def __read_memory_usage(self) -> float:
        memory_usage_percent_index = 2 # psutils related
        memory_info = psutil.virtual_memory()
        return memory_info[memory_usage_percent_index]

    def __read_disk_usage(self) -> list:
        partition_name_index          = 0 # psutils related
        partition_usage_percent_index = 3 # psutils related

        result = list()

        partitions = psutil.disk_partitions()
        for partition in partitions:
            partition_name = partition[partition_name_index]
            partition_usage_data = psutil.disk_usage(partition_name)
            partition_usage_percent = partition_usage_data[partition_usage_percent_index]
            result.append((partition_name, partition_usage_percent))

        return result
