from CommonExternal.JsonFomatterModule.JsonContract import JsonContract


class BaseResponseDto(JsonContract):
    state_code: int

    def __init__(self, state_code: int = None):
        if state_code is not None:
            self.state_code = state_code

    @property
    def _json_fields(self) -> dict:
        return {
                "s": "status_code"
            }
