from Common.Entities.ComputerFlow import ComputerFlow
from Common.NetworkModule.DtoData.RequestData.RequestDto import RequestDto

from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class JsonTest:
    @staticmethod
    def test_computer_flow_serialize():
        computer_flow = ComputerFlow.get_random_flow()
        computer_flow_json = JsonFormatter.serialize(computer_flow)
        val = JsonFormatter.deserialize(computer_flow_json, ComputerFlow)
        print()

    @staticmethod
    def test_request_dto_serialize():
        dto = RequestDto[ComputerFlow]("some_method", ComputerFlow.get_random_flow())
        json_dto = JsonFormatter.serialize(dto)
        dto_value = JsonFormatter.deserialize(json_dto, RequestDto[ComputerFlow])
        print()

        # repeat

        json_dto2 = JsonFormatter.serialize(dto_value)
        dto_value2 = JsonFormatter.deserialize(json_dto2, RequestDto[ComputerFlow])
        print()


if __name__ == '__main__':
    JsonTest.test_request_dto_serialize()
