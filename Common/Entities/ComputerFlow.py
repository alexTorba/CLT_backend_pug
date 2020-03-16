from typing import List

from Common.Entities.ComputerState import ComputerState
from External.JsonFomatterModule.JsonContract import JsonContract


class ComputerFlow(JsonContract):
    flow: List[ComputerState]
    __json_fields = {"f": "flow"}

    def __init__(self, flow: List[ComputerState] = None) -> None:
        super().__init__(self.__json_fields)
        if flow is None:
            flow = list()
        self.flow = flow

    def store_computer_state(self, computer_state: ComputerState) -> None:
        self.flow.append(computer_state)

    @staticmethod
    def get_random_flow():
        flow: List[ComputerState] = list()
        for i in range(0, 10):
            flow.append(ComputerState.get_random_state())
        return ComputerFlow(flow)

    def get_last_state(self) -> ComputerState:
        last_index = len(self.flow) - 1
        return self.flow[last_index]
