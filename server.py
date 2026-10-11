import http.server
import socketserver
import threading
import time
from config import Config


class ReusableTCPServer(socketserver.TCPServer):
   allow_reuse_address = True


class SimpleFEServer:
   def __init__(self, directory=Config.FE_DIR, port=0):
       self.directory = directory
       self.port = port
       self.httpd = None
       self.thread = None


   def start(self):
       handler = lambda *args, **kwargs: http.server.SimpleHTTPRequestHandler(
           *args, directory=self.directory, **kwargs
       )
       self.httpd = ReusableTCPServer(("127.0.0.1", self.port), handler)
       assigned_port = self.httpd.server_address[1]
       self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
       self.thread.start()
       time.sleep(0.3)
       return f"http://127.0.0.1:{assigned_port}/app/index.html"


   def stop(self):
       if self.httpd:
           self.httpd.shutdown()
           self.httpd.server_close()



