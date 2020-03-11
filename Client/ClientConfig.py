# todo: I think, we will save it in json configuration file. Therefore, ClientConfig must be inherited from JsonContract
class ClientConfig:
    check_state_period: int
    send_data_period: int

    def __init__(self, check_state_period: int, send_data_period: int):
        self.check_state_period = check_state_period  # seconds
        self.send_data_period = send_data_period  # seconds

    @staticmethod
    def create_default_config():
        return ClientConfig(15, 900)
