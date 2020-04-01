class UrlManager:
    __host: str = "127.0.0.1:8000"

    @classmethod
    def get_url(cls, path: str) -> str:
        return f"http://{cls.__host}/{path}"

    @classmethod
    def set_host(cls, host: str) -> None:
        cls.__host = host
