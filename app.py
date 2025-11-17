from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello from CloudPanel Python App!")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")

if __name__ == "__main__":
    host = "0.0.0.0"
    port = 5000
    print(f"Server running on http://{host}:{port}")
    server = HTTPServer((host, port), SimpleHandler)
    server.serve_forever()