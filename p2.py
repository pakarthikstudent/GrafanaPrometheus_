from http.server import *
  
# creating a class for handling  
# basic Get and Post Requests 
class myclass(BaseHTTPRequestHandler): 
    
    # creating a function for Get Request 
    def do_GET(self): 
        
        # Success Response --> 200 
        self.send_response(200) 
          
        # Type of file that we are using for creating our 
        # web server. 
        self.send_header('content-type', 'text/html') 
        self.end_headers() 
          
        # what we write in this function it gets visible on our 
        # web-server 
        self.wfile.write('<h1>Hello Prometheus</h1>'.encode()) 
  
  
port = HTTPServer(('', 5555), myclass) 
  
port.serve_forever() 