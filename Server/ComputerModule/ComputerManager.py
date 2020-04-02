from Common.Entities.ComputerFlow import ComputerFlow
from External.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from External.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from Server.ComputerModule.ComputerKeyManager import ComputerKeyManager
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
