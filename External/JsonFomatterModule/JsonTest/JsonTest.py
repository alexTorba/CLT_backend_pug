from Common.Entities.ComputerFlow import ComputerFlow
from External.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.JsonFomatterModule.JsonTest.TestEntities.SomeEntity import SomeEntity
from External.JsonFomatterModule.JsonTest.TestEntities.SomeType import SomeType
from Server.Data.Computer import Computer


class JsonTest:
    @staticmethod
    def computer_flow_serialize():
        computer_flow = ComputerFlow.get_random_flow()
        computer_flow_json = JsonFormatter.serialize(computer_flow)
        val = JsonFormatter.deserialize(computer_flow_json, ComputerFlow)
        print(val)

    @staticmethod
    def request_dto_serialize():
        dto = RequestDto[ComputerFlow]("some_method", ComputerFlow.get_random_flow())
        json_dto = JsonFormatter.serialize(dto)
        dto_value = JsonFormatter.deserialize(json_dto, RequestDto[ComputerFlow])
        print(dto_value)

        # repeat

        json_dto2 = JsonFormatter.serialize(dto_value)
        dto_value2 = JsonFormatter.deserialize(json_dto2, RequestDto[ComputerFlow])
        print(dto_value2)  # needed for breakpoint to check the result of formatting

    @staticmethod
    def request_complex_dto_serialize():
        dto = SomeEntity.get_temp_some_entity()
        json_dto = JsonFormatter.serialize(dto)
        dto_val = JsonFormatter.deserialize(json_dto, SomeEntity)
        print(dto_val)

    @staticmethod
    def dict_field_serialize():
        some_type = SomeType.get_random_some_type()
        json = JsonFormatter.serialize(some_type)
        val = JsonFormatter.deserialize(json, SomeType)
        print(val)

    @staticmethod
    def computer_serialize():
        computer = Computer.get_random_computer()
        json = JsonFormatter.serialize(computer)
        val = JsonFormatter.deserialize(json, Computer)
        print(val)


if __name__ == '__main__':
    JsonTest.computer_serialize()
