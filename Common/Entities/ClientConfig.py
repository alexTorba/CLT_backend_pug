from External.JsonFomatterModule.JsonContract import JsonContract


class ClientConfig(JsonContract):
    check_state_period: int  # seconds
    send_data_period: int  # seconds
    __json_fields = {
        "c": "check_state_period",
        "s": "send_data_period"
    }

    def __init__(self, check_state_period: int = 15, send_data_period: int = 900):
        super().__init__(self.__json_fields)
        if check_state_period is not None:
            self.check_state_period = check_state_period
        if send_data_period is not None:
            self.send_data_period = send_data_period

    def copy(self):
        return ClientConfig(self.check_state_period, self.send_data_period)
