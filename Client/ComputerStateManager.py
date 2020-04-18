import os
import time
from typing import List

import psutil

from Common.Entities.ComputerFlow import ComputerFlow
from Common.Entities.ComputerState import ComputerState
from Common.Entities.ComputerState import DiskInfo
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.Managers.NetworkManager import NetworkManager
from External.NetworkModule.Managers.UrlManager import UrlManager


class ComputerStateManager:
    __temp_data_file = "temp_computer_flow.dat"

    # -------------------------------------------------------------------------

    def send_data_to_server(self) -> None:
        if UrlManager.has_host():
            computer_flow = self.__read_temp_data()
            self.__send_data_to_server_impl(computer_flow)
            os.remove(self.__temp_data_file)

    @staticmethod
    def __send_data_to_server_impl(computer_flow: ComputerFlow):
        dto = RequestDto[ComputerFlow](data=computer_flow)
        dto_json = JsonFormatter.serialize(dto)
        NetworkManager.send("SendComputerFlow", dto_json)

    # -------------------------------------------------------------------------

    def save_current_state(self) -> None:
        current_state = self.__read_current_computer_state()

        computer_flow = self.__read_temp_data()
        computer_flow.store_computer_state(current_state)
        self.__store_temp_data(computer_flow)

    @classmethod
    def __read_temp_data(cls) -> ComputerFlow:
        temp_data = ""

        if os.path.exists(cls.__temp_data_file):
            with open(cls.__temp_data_file, "r") as file:
                temp_data = file.read()

        return JsonFormatter.deserialize(temp_data, ComputerFlow) if temp_data else ComputerFlow()

    @classmethod
    def __store_temp_data(cls, data) -> None:
        with open(cls.__temp_data_file, "w") as temp_data_file:
            temp_data_file.write(JsonFormatter.serialize(data))

    # -------------------------------------------------------------------------

    @classmethod
    def __read_current_computer_state(cls) -> ComputerState:
        current_time = time.time()
        cpu_usage = psutil.cpu_percent()
        ram_usage = cls.__read_memory_usage()
        disk_usage = cls.__read_disk_usage()
        return ComputerState(current_time, cpu_usage, ram_usage, disk_usage)

    @staticmethod
    def __read_memory_usage() -> float:
        memory_info = psutil.virtual_memory()
        return memory_info.percent

    @staticmethod
    def __read_disk_usage() -> list:
        result: List[DiskInfo] = list()

        partitions = psutil.disk_partitions()
        for partition in partitions:
            if "cdrom" in partition.opts and partition.fstype == "":  # specific of psutil on windows
                continue

            partition_usage = psutil.disk_usage(partition.device)
            result.append(DiskInfo(partition.device, partition_usage.percent))

        return result
