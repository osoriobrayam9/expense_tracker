import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from src.storage import load_data
from src.analytics import get_basic_statistics

_server = None
_thread = None

class SimpleHandler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps(payload, indent=2).encode("utf-8"))

    def do_GET(self):
        if self.path == "/expenses":
            data = load_data()
            self._send(200, {"count": len(data), "items": data})
        elif self.path == "/stats":
            stats = get_basic_statistics()
            self._send(200, {"stats": stats})
        else:
            self._send(404, {"error": "Not Found"})

def start_api_server(port=8000):
    global _server, _thread
    if _server is not None:
        return f"Ya está corriendo en http://127.0.0.1:{_server.server_port}"
    _server = HTTPServer(("127.0.0.1", port), SimpleHandler)
    _thread = threading.Thread(target=_server.serve_forever, daemon=True)
    _thread.start()
    return f"API iniciada en http://127.0.0.1:{port} (endpoints: /expenses, /stats)"

def stop_api_server():
    global _server, _thread
    if _server is None:
        return "API no estaba corriendo."
    _server.shutdown()
    _server.server_close()
    _server = None
    _thread = None
    return "API detenida."
