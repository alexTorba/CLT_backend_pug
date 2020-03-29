from typing import List

import psutil
import time
import os

from Common.Entities.ComputerState import ComputerState
from Common.Entities.ComputerState import DiskInfo
from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class ComputerStateManager:
    __temp_data_file = "temp_computer_flow.dat"

    def send_data_to_server(self) -> None:
        computer_flow = self.__read_temp_data()
        # TODO send
        os.remove(self.__temp_data_file)

    def save_current_state(self) -> None:
        current_state = self.__read_current_computer_state()

        computer_flow = self.__read_temp_data()
        computer_flow.store_computer_state(current_state)
        self.__store_temp_data(computer_flow)

    @classmethod
    def __read_temp_data(cls) -> ComputerFlow:
        if os.path.exists(cls.__temp_data_file):
            with open(cls.__temp_data_file, "r") as file:
                temp_data = file.read()
            return JsonFormatter.deserialize(temp_data, ComputerFlow) if temp_data else ComputerFlow()
        else:
            return ComputerFlow()

    @classmethod
    def __store_temp_data(cls, data) -> None:
        with open(cls.__temp_data_file, "w") as temp_data_file:
            temp_data_file.write(JsonFormatter.serialize(data))

    @classmethod
    def __read_current_computer_state(cls) -> ComputerState:
        current_time = time.time()
        cpu_usage = psutil.cpu_percent()
        ram_usage = cls.__read_memory_usage()
        disk_usage = cls.__read_disk_usage()
        return ComputerState(current_time, cpu_usage, ram_usage, disk_usage)

    @staticmethod
    def __read_memory_usage() -> float:
        memory_usage_percent_index = 2  # psutils related
        memory_info = psutil.virtual_memory()
        return memory_info[memory_usage_percent_index]

    @staticmethod
    def __read_disk_usage() -> list:
        partition_name_index = 0  # psutils related
        partition_usage_percent_index = 3  # psutils related

        result: List[DiskInfo] = list()

        partitions = psutil.disk_partitions()
        for partition in partitions:
            partition_name = partition[partition_name_index]
            partition_usage_data = psutil.disk_usage(partition_name)
            partition_usage_percent = partition_usage_data[partition_usage_percent_index]
            result.append(DiskInfo(partition_name, partition_usage_percent))

        return result
