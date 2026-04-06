from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        result = {
            "sh": {"value": "3000.00", "change": "+10.00", "percent": "+0.33%"},
            "sz": {"value": "10000.00", "change": "-20.00", "percent": "-0.20%"},
            "northbound": "10.5",
            "northboundChange": "+2.3"
        }

        self.wfile.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))
        return