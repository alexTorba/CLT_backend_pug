from Common.Entities.ComputerFlow import ComputerFlow
from Common.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.JsonFomatterModule.JsonTest.TestEntities.SomeType import SomeType


class JsonTest:
    @staticmethod
    def computer_flow_serialize():
        computer_flow = ComputerFlow.get_random_flow()
        computer_flow_json = JsonFormatter.serialize(computer_flow)
        val = JsonFormatter.deserialize(computer_flow_json, ComputerFlow)
        print()

    @staticmethod
    def request_dto_serialize():
        dto = RequestDto[ComputerFlow]("some_method", ComputerFlow.get_random_flow())
        json_dto = JsonFormatter.serialize(dto)
        dto_value = JsonFormatter.deserialize(json_dto, RequestDto[ComputerFlow])
        print()

        # repeat

        json_dto2 = JsonFormatter.serialize(dto_value)
        dto_value2 = JsonFormatter.deserialize(json_dto2, RequestDto[ComputerFlow])
        print()  # needed for breakpoint to check the result of formatting

    @staticmethod
    def dict_field_serialize():
        some_type = SomeType.get_random_some_type()
        json = JsonFormatter.serialize(some_type)
        val = JsonFormatter.deserialize(json, SomeType)
        print()


if __name__ == '__main__':
    JsonTest.dict_field_serialize()
