import time
from random import random
from typing import List, Tuple

from External.JsonFomatterModule.JsonContract import JsonContract

class DiskInfo(JsonContract):
    partition_name: str
    usage_percent: float

    __json_fields = {
        "n": "partition_name",
        "p": "usage_percent"
    }

    def __init__(self, partition_name: str = None, usage_percent: float = None ) -> None:
        super().__init__(self.__json_fields)

        if partition_name is not None:
            self.partition_name = partition_name
        if usage_percent is not None:
            self.usage_percent = usage_percent

    def __repr__(self) -> str:
        return f"Partition name: {self.partition_name}, Percent of disk usage: {self.usage_percent}"

class ComputerState(JsonContract):
    time: float
    cpu: float  # percent of CPU usage
    ram: float  # percent of RAM usage
    disk: List[DiskInfo]  # percent of DISK usage per each partition, [(partition_name, usage_percent), ...]

    __json_fields = {
        "t": "time",
        "c": "cpu",
        "r": "ram",
        "d": "disk"
    }

    # parameters are none because of JsonContract need a default ctor
    def __init__(self, state_time: float = None, cpu: float = None, ram: float = None, disk: DiskInfo = None) -> None:
        super().__init__(self.__json_fields)

        if state_time is not None:
            self.time = state_time
        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if disk is not None:
            self.disk = disk

    def __repr__(self) -> str:
        return f"Time: {self.time}, Cpu: {self.cpu}, Ram: {self.ram}, Disk: {self.disk}"

    @staticmethod
    def get_random_state():
        current_time = time.time()
        cpu = round(random() * 100, 2)
        ram = round(random() * 100, 2)
        disk = [DiskInfo("some_disk_name", round(random() * 100, 2))]
        return ComputerState(current_time, cpu, ram, disk)