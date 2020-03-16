import time
from random import random
from typing import List, Tuple

from External.JsonFomatterModule.JsonContract import JsonContract


class ComputerState(JsonContract):
    time: float
    cpu: float  # percent of CPU usage
    ram: float  # percent of RAM usage
    disk: List[Tuple]  # percent of DISK usage per each partition, [(partition_name, usage_percent), ...]

    __json_fields = {
        "t": "time",
        "c": "cpu",
        "r": "ram",
        "d": "disk"
    }

    # parameters are none because of JsonContract need a default ctor
    def __init__(self, state_time: float = None, cpu: float = None, ram: float = None, disk: list = None) -> None:
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
        disk = [("some_disk_name", round(random() * 100, 2))]
        return ComputerState(current_time, cpu, ram, disk)
