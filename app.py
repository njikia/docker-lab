from http.server import HTTPServer, BaseHTTPRequestHandler
import signal
import threading

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Kubernetes!")

server = HTTPServer(("", 8080), Handler)

def handle_sigterm(signum, frame):
    print("SIGTERM received, shutting down gracefully", flush=True)
    threading.Thread(target=server.shutdown).start()

signal.signal(signal.SIGTERM, handle_sigterm)

print("Server starting on port 8080", flush=True)
server.serve_forever()
print("Server stopped cleanly", flush=True)
