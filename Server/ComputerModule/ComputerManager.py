from typing import List

from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonContract import JsonContract
from External.NetworkModule.Data.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.Data.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from External.NetworkModule.Data.DtoData.ResponceData.ResponseDto import ResponseDto
from External.NetworkModule.Data.ExceptionsData.ServerLogicException import ServerLogicException
from Server.ComputerModule.ComputerKeyManager import ComputerKeyManager
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey
from Server.DataBaseModule.CachedDBManager import CachedDBManager


class ComputerManager:
    __cache: CachedDBManager = CachedDBManager()

    @staticmethod
    def send_computer_flow(dto: RequestDto[ComputerFlow]) -> BaseResponseDto:
        computer_flow: ComputerFlow = dto.data

        if computer_flow is None or not hasattr(computer_flow, "flow"):
            raise ServerLogicException(401, "Received wrong data from client ! Empty ComputerFlow !")

        computer_key: ComputerKey = ComputerKeyManager.get_computer_key(dto.client_ip, dto.client_port)
        ComputerManager.__send_computer_flow_impl(computer_key, computer_flow)
        return BaseResponseDto(200)

    @classmethod
    def __send_computer_flow_impl(cls, key: ComputerKey, flow: ComputerFlow):
        computer = Computer(key, flow)
        if cls.__cache.count_by_key(key) == 0:
            cls.__cache.create(key, computer)
        else:
            cls.__cache.update(key, computer)

    # ---------------------------------------------------------------------

    @staticmethod
    def get_computer(dto: RequestDto[ComputerKey]) -> ResponseDto[Computer]:
        key: ComputerKey = dto.data

        if not hasattr(key, "auditorium") or not hasattr(key, "name"):
            raise ServerLogicException(401, "Received wrong data from client !")

        computer: Computer = ComputerManager.__get_computer_impl(key)
        return ResponseDto[Computer](200, computer)

    @classmethod
    def __get_computer_impl(cls, key: ComputerKey) -> Computer:
        return cls.__cache.read(key)

    # ---------------------------------------------------------------------

    class GetKeysByAuditoriumDto(JsonContract):
        auditorium: str
        __json_fields = {
            "a": "auditorium"
        }

        def __init__(self, auditorium=None):
            super().__init__(self.__json_fields)
            if auditorium is not None:
                self.auditorium = auditorium

    @staticmethod
    def get_keys_by_auditorium(dto: RequestDto[GetKeysByAuditoriumDto]) -> ResponseDto[List[ComputerKey]]:
        data: ComputerManager.GetKeysByAuditoriumDto = dto.data

        if not hasattr(data, "auditorium"):
            raise ServerLogicException(401, "Received wrong data from client ! Field auditorium must have value !")

        auditorium: str = dto.data.auditorium
        keys: List[ComputerKey] = ComputerManager.__get_keys_by_auditorium_impl(auditorium)
        return ResponseDto[List[ComputerKey]](200, keys)

    @classmethod
    def __get_keys_by_auditorium_impl(cls, auditorium: str) -> List[ComputerKey]:
        return cls.__cache.read_keys_by_auditorium(auditorium)

    # ---------------------------------------------------------------------

    @staticmethod
    def get_auditoriums() -> ResponseDto[List[str]]:
        return ResponseDto[List[str]](200, ComputerManager.__get_auditoriums_impl())

    @classmethod
    def __get_auditoriums_impl(cls) -> List[str]:
        return cls.__cache.read_auditoriums()
