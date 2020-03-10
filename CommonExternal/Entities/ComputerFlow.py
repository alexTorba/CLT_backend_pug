from typing import List, Dict

from CommonExternal.Entities.ComputerState import ComputerState
from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class ComputerFlow(JsonContract):
    flow: List[ComputerState]
    __json_fields = {"f": "flow"}

    def __init__(self, flow: List[ComputerState] = None) -> None:
        super().__init__(self.__json_fields)

        if flow is not None:
            self.flow = flow

    def store_computer_state(self, computer_state: ComputerState) -> None:
        self.flow.append(computer_state)

    @staticmethod
    def get_random_flow():
        flow: List[ComputerState] = list()
        for i in range(0, 10):
            flow.append(ComputerState.get_random_state())
        return ComputerFlow(flow)
