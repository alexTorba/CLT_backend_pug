from typing import List

from Common.Entities.ComputerFlow import ComputerFlow
from External.JsonFomatterModule.JsonContract import JsonContract
from External.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from External.NetworkModule.DtoData.ResponceData.ResponseDto import ResponseDto
from Server.ComputerModule.ComputerKeyManager import ComputerKeyManager
from Server.Data.Computer import Computer
from Server.Data.ComputerKey import ComputerKey


class ComputerManager:

    @staticmethod
    def send_computer_flow(dto: RequestDto[ComputerFlow]) -> BaseResponseDto:
        computer_flow: ComputerFlow = dto.data
        computer_key: ComputerKey = ComputerKeyManager.get_computer_key(dto.client_ip, dto.client_port)
        ComputerManager.__send_computer_flow_impl(computer_key, computer_flow)
        return BaseResponseDto(200)

    @staticmethod
    def __send_computer_flow_impl(key: ComputerKey, flow: ComputerFlow):
        # todo: do something with computer_flow and key
        pass

    # ---------------------------------------------------------------------

    @staticmethod
    def get_computer(dto: RequestDto[ComputerKey]) -> ResponseDto[Computer]:
        key: ComputerKey = dto.data
        computer: Computer = ComputerManager.__get_computer_impl(key)
        return ResponseDto[Computer](200, computer)

    @staticmethod
    def __get_computer_impl(key: ComputerKey) -> Computer:
        # todo: get computer by key
        return Computer.get_random_computer()

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

    @staticmethod
    def __get_computers_impl(auditorium: str) -> List[Computer]:
        # todo: get computers by auditorium
        computers: List[Computer] = [Computer.get_random_computer(), Computer.get_random_computer()]
        return computers
