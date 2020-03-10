from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class BaseResponseDto(JsonContract):
    state_code: int
    __json_fields = {"s": "status_code"}

    def __init__(self, state_code: int = None):
        super().__init__(self.__json_fields)

        if state_code is not None:
            self.state_code = state_code
