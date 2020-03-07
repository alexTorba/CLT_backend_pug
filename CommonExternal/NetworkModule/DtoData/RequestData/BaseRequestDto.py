from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class BaseRequestDto(JsonContract):
    server_method: str

    def __init__(self, server_method: str = None):
        if server_method is not None:
            self.server_method = server_method

    @property
    def _json_fields(self) -> dict:
        return {
            "s": "server_method"
        }
