from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        today = datetime.now().strftime("%Y-%m-%d")
        result = [
            {"title": "【加红】测试重要新闻", "time": f"{today} 10:00", "url": "https://www.cls.cn/", "important": True},
            {"title": "普通测试新闻", "time": f"{today} 09:30", "url": "https://www.cls.cn/", "important": False}
        ]

        self.wfile.write(json.dumps(result, ensure_ascii=False).encode('utf-8'))
        return