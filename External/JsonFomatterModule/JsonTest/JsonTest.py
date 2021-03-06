from Common.Entities.ClientConfig import ClientConfig
from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.JsonFomatterModule.JsonTest.TestEntities.SomeEntity import SomeEntity
from External.JsonFomatterModule.JsonTest.TestEntities.SomeType import SomeType
from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from Server.ComputerModule.ComputerManager import ComputerManager
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey


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

    @staticmethod
    def request_dto_computer_key():
        dto0 = RequestDto[ComputerKey](data=ComputerKey("5", "40"))
        json0 = JsonFormatter.serialize(dto0)
        val0 = JsonFormatter.deserialize(json0, RequestDto[ComputerKey])
        print(val0)

        print(RequestDto.__annotations__["data"])

        dto1 = RequestDto[ComputerManager.GetKeysByAuditoriumDto](data=ComputerManager.GetKeysByAuditoriumDto("37"))
        json1 = JsonFormatter.serialize(dto1)
        val1 = JsonFormatter.deserialize(json1, RequestDto[ComputerManager.GetKeysByAuditoriumDto])
        print(val1)
        print(RequestDto.__annotations__["data"])

    # noinspection PyTypeChecker
    @staticmethod
    def client_config():
        c = ClientConfig(None, None)
        json = JsonFormatter.serialize(c)
        val = JsonFormatter.deserialize(json, ClientConfig)
        print(val.__dict__)
        print(val)


if __name__ == '__main__':
    JsonTest.computer_serialize()
