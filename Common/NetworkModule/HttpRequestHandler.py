from http.server import BaseHTTPRequestHandler

from Common.NetworkModule.MethodHandler import MethodHandler
from External.JsonFomatterModule.JsonFormatter import JsonFormatter


class HttpRequestHandler(BaseHTTPRequestHandler):
    method_handler: MethodHandler

    def do_GET(self):
        print(f"Get request, from {self.client_address}")
        self.send_response(200)
        method_name = MethodHandler.get_server_method_name(self.path)
        result = HttpRequestHandler.method_handler.do_get(method_name)
        result_json = JsonFormatter.serialize(result)
        self.end_headers()
        self.wfile.write(result_json.encode())

    def do_POST(self):
        method_name = MethodHandler.get_server_method_name(self.path)
        self.method_handler.do_post(method_name)
