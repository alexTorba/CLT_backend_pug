from http.server import BaseHTTPRequestHandler

from External.NetworkModule.MethodHandler import MethodHandler
from External.JsonFomatterModule.JsonFormatter import JsonFormatter
from External.NetworkModule.UrlManager import UrlManager


class HttpRequestHandler(BaseHTTPRequestHandler):
    method_handler: MethodHandler

    def do_GET(self):
        print(f"Receive get request from {self.client_address}")

        method_name = MethodHandler.get_server_method_name(self.path)
        result = HttpRequestHandler.method_handler.do_get(method_name)
        self.send_response(result.state_code)

        result_json = JsonFormatter.serialize(result)
        self.end_headers()
        self.wfile.write(result_json.encode())

    def do_POST(self):
        print(f"Receive post request from {self.client_address}")

        length = int(self.headers.get('content-length', 0))
        json_request_dto = self.rfile.read(length).decode("utf-8")
        method_name = MethodHandler.get_server_method_name(self.path)
        dto_type = self.method_handler.get_request_type(method_name)
        request_dto = JsonFormatter.deserialize(json_request_dto, dto_type)
        UrlManager.resolve_client_address(request_dto, self.client_address)

        response_dto = self.method_handler.do_post(method_name, request_dto)
        self.send_response(response_dto.state_code)
        response_dto_json = JsonFormatter.serialize(response_dto)
        self.end_headers()
        self.wfile.write(response_dto_json.encode())
