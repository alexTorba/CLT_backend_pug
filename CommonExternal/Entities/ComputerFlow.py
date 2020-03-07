from typing import List

from CommonExternal.Entities.ComputerState import ComputerState
from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class ComputerFlow(JsonContract):
    flow: List[ComputerState]

    def __init__(self, flow: List[ComputerState] = None) -> None:
        if flow is not None:
            self.flow = flow

    @property
    def _json_fields(self) -> dict:
        return {
            "f": "flow"
        }

    @staticmethod
    def get_random_flow():
        flow: List[ComputerState] = list()
        for i in range(0, 10):
            flow.append(ComputerState.get_random_state())
        return ComputerFlow(flow)
