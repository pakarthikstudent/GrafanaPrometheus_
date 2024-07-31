import http.server
import random
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS = Counter('hello_worlds_total',
        'Hello Worlds requested.')
SALES = Counter('hello_world_sales_n_total',
        'n made serving Hello World.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        REQUESTS.inc()
        n = random.random()
        SALES.inc(n)
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello World for {} counts.".format(n).encode())

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()