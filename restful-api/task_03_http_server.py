from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)  # Status kodu 200 (OK)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)  # Status kodu 404 (Not Found)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server is running at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
