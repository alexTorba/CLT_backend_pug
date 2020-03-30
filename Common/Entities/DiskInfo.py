from External.JsonFomatterModule.JsonContract import JsonContract


class DiskInfo(JsonContract):
    partition_name: str
    usage_percent: float

    __json_fields = {
        "n": "partition_name",
        "p": "usage_percent"
    }

    def __init__(self, partition_name: str = None, usage_percent: float = None) -> None:
        super().__init__(self.__json_fields)

        if partition_name is not None:
            self.partition_name = partition_name
        if usage_percent is not None:
            self.usage_percent = usage_percent

    def __repr__(self) -> str:
        return f"Partition name: {self.partition_name}, Percent of disk usage: {self.usage_percent}"
