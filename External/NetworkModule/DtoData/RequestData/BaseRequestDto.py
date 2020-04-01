from External.JsonFomatterModule.JsonContract import JsonContract


class BaseRequestDto(JsonContract):
    server_method: str
    __json_fields = {"s": "server_method"}

    def __init__(self, server_method: str = None):
        super().__init__(self.__json_fields)

        if server_method is not None:
            self.server_method = server_method
