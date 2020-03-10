import math
import time
from random import randrange, random

from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class ComputerState(JsonContract):
    time: float
    cpu: float # percent of CPU usage
    ram: float # percent of RAM usage
    disk: float # percent of DISK usage

    # parameters are none because of JsonContract need a default ctor
    def __init__(self, time: float = None, cpu: float = None, ram: float = None, disk: float = None) -> None:
        if time is not None:
            self.time = time
        if cpu is not None:
            self.cpu = cpu
        if ram is not None:
            self.ram = ram
        if disk is not None:
            self.disk = disk

    @property
    def _json_fields(self) -> dict:
        return {
            "t": "time",
            "c": "cpu",
            "r": "ram",
            "d": "disk"
        }

    @staticmethod
    def get_random_state():
        current_time = time.time()
        cpu = round(random() * 100, 2)
        ram = round(random() * 100, 2)
        disk = round(random() * 100, 2)
        return ComputerState(current_time, cpu, ram, disk)
