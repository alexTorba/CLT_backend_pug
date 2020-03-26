from Common.Entities.ComputerFlow import ComputerFlow
from Common.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from External.JsonFomatterModule.JsonContract import JsonContract


class SomeEntity(JsonContract):
    dto: RequestDto[ComputerFlow]
    __json_fields = {
        "d": "dto"
    }

    def __init__(self, dto: RequestDto[ComputerFlow] = None):
        super().__init__(self.__json_fields)
        if dto is not None:
            self.dto = dto

    @staticmethod
    def get_temp_some_entity():
        return SomeEntity(RequestDto[ComputerFlow]("some_method", ComputerFlow.get_random_flow()))
