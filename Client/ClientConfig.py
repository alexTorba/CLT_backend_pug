class ClientConfig:

    def __init__(self, check_state_period, send_data_period):
        self.check_state_period = check_state_period #seconds
        self.send_data_period   = send_data_period #seconds

    @staticmethod
    def create_default_config():
        return ClientConfig(15, 900)
