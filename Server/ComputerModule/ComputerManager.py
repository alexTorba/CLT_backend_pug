from Common.Entities.ComputerFlow import ComputerFlow
from Common.NetworkModule.DtoData.RequestData.RequestDto import RequestDto
from Common.NetworkModule.DtoData.ResponceData.BaseResponseDto import BaseResponseDto


class ComputerManager:
    @staticmethod
    def send_computer_state(dto: RequestDto[ComputerFlow]) -> BaseResponseDto:
        # todo: do something with computer_flow
        computer_flow = dto.data
        print(computer_flow)
        return BaseResponseDto(200)
