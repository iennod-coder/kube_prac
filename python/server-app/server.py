from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse
import json


class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'id': '1', 'message': 'Hello world'}).encode())
        return


def run(addr="localhost", port=8000):
    server = HTTPServer((addr, port), RequestHandler)
    print(f"Starting httpd server on {addr}:{port}")
    server.serve_forever()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
