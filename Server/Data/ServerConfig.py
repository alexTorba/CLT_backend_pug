from External.JsonFomatterModule.JsonContract import JsonContract


class ServerConfig(JsonContract):
    prio: int

    __json_fields = {
        "p": "prio"
    }

    def __init__(self, prio: int = 0):
        super().__init__(self.__json_fields)

        if prio is not None:
            self.prio = prio
