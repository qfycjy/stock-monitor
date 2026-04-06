from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 标准响应头，解决跨域和编码问题
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        # 固定测试数据，无任何语法错误
        response_data = {
            "sh": {"value": "3000.00", "change": "+10.00", "percent": "+0.33%"},
            "sz": {"value": "10000.00", "change": "-20.00", "percent": "-0.20%"},
            "northbound": "10.5",
            "northboundChange": "+2.3"
        }

        # 返回数据
        self.wfile.write(json.dumps(response_data, ensure_ascii=False).encode('utf-8'))
        return