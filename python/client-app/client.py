from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import json
import argparse

class RequestHandler(BaseHTTPRequestHandler):		
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self, url="http://localhost:8000"):
        self._set_headers()
        response = requests.get(url)
        json_dict = json.loads(response.content)
        reversed_message = json_dict['message'][::-1]
        self.wfile.write(json.dumps({'reversed-message': reversed_message}).encode())
        return


def run(addr="localhost", port=8001, url="http://localhost:8000"):
    server = HTTPServer((addr, port), RequestHandler)
    print(f"Starting httpd server on {addr}:{port}")
    server.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser = argparse.ArgumentParser(description="Reverse message in json from specified url")
    parser.add_argument(
      "-u",
      "--url",
      default="http://localhost:8000",
      help="Specify the url to get the json response",
    )
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
      default=8001,
      help="Specify the port on which the server listens",
    )

    args = parser.parse_args()
    run(addr=args.listen, port=args.port, url=args.url)

