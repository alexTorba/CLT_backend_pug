import math
from datetime import datetime
from random import randrange, random

from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class ComputerState(JsonContract):
    State_time: str
    Cpu: float
    Ram: float
    Disk: float

    # parameters are none because of JsonContract need a default ctor
    def __init__(self, state_time: str = None, cpu: float = None, ram: float = None, disk: float = None) -> None:
        if state_time is not None:
            self.State_time = state_time
        if cpu is not None:
            self.Cpu = cpu
        if ram is not None:
            self.Ram = ram
        if disk is not None:
            self.Disk = disk

    @property
    def _json_fields(self) -> dict:
        return {
            "t": "State_time",
            "c": "Cpu",
            "r": "Ram",
            "d": "Disk"
        }

    @staticmethod
    def get_random_state():
        state_time = str(datetime.now())
        cpu = round(random() * 100, 2)
        ram = round(random() * 100, 2)
        disk = round(random() * 100, 2)
        return ComputerState(state_time, cpu, ram, disk)
