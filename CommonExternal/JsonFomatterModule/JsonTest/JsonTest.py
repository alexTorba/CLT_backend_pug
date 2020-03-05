from CommonExternal.Entities.ComputerFlow import ComputerFlow
from CommonExternal.JsonFomatterModule.JsonFormatter import JsonFormatter


class JsonTest:
    @staticmethod
    def test_computer_flow_serialize():
        computer_flow = ComputerFlow.get_random_flow()
        computer_flow_json = JsonFormatter.serialize(computer_flow)
        val = JsonFormatter.deserialize(computer_flow_json, ComputerFlow)
        print()


if __name__ == '__main__':
    JsonTest.test_computer_flow_serialize()
