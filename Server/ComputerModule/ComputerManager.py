from typing import List

from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonContract import JsonContract
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from External.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from Server.ComputerModule.ComputerKeyManager import ComputerKeyManager
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey
from Server.DataBaseModule.CachedDBManager import CachedDBManager


class ComputerManager:
    __cache: CachedDBManager = CachedDBManager()

    @staticmethod
    def send_computer_flow(dto: RequestDto[ComputerFlow]) -> BaseResponseDto:
        computer_flow: ComputerFlow = dto.data
        computer_key: ComputerKey = ComputerKeyManager.get_computer_key(dto.client_ip, dto.client_port)
        ComputerManager.__send_computer_flow_impl(computer_key, computer_flow)
        return BaseResponseDto(200)

    @classmethod
    def __send_computer_flow_impl(cls, key: ComputerKey, flow: ComputerFlow):
        computer = Computer(key, flow)
        cls.__cache.update(key, computer)
        pass

    # ---------------------------------------------------------------------

    @staticmethod
    def get_computer(dto: RequestDto[ComputerKey]) -> ResponseDto[Computer]:
        key: ComputerKey = dto.data
        computer: Computer = ComputerManager.__get_computer_impl(key)
        return ResponseDto[Computer](200, computer)

    @classmethod
    def __get_computer_impl(cls, key: ComputerKey) -> Computer:
        return cls.__cache.read(key)

    # ---------------------------------------------------------------------

    class GetComputersDto(JsonContract):
        auditorium: str
        __json_fields = {
            "a": "auditorium"
        }

        def __init__(self, auditorium=None):
            super().__init__(self.__json_fields)
            if auditorium is not None:
                self.auditorium = auditorium

    @staticmethod
    def get_computers(dto: RequestDto[GetComputersDto]) -> ResponseDto[List[Computer]]:
        auditorium: str = dto.data.auditorium
        computers: List[Computer] = ComputerManager.__get_computers_impl(auditorium)
        return ResponseDto[List[Computer]](200, computers)

    @classmethod
    def __get_computers_impl(cls, auditorium: str) -> List[Computer]:
        return cls.__cache.read_computers_by_auditorium(auditorium)
