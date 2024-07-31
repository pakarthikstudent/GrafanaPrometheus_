import http.server
from prometheus_client import start_http_server

class myclass(http.server.BaseHTTPRequestHandler):
	def f1(self):
		self.send_response(200)
		self.end_handlers()
		self.wfile.write(b"Hello")

if __name__ == '__main__':
	start_http_server(8000)
	server = http.server.HTTPServer(('localhost',8001),myclass)
	server.serve_forever()
