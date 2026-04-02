from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# 上证指数
@app.route("/api/sh")
def sh():
    data = requests.get("https://push2.eastmoney.com/api/qt/stock/get?secid=1.000001&fields=f43,f44,f45").json()
    return jsonify(data)

# 深证成指
@app.route("/api/sz")
def sz():
    data = requests.get("https://push2.eastmoney.com/api/qt/stock/get?secid=0.399001&fields=f43,f44,f45").json()
    return jsonify(data)

# 北向资金
@app.route("/api/north")
def north():
    data = requests.get("https://push2.eastmoney.com/api/qt/kamt.getAll/get?fields=f1,f2").json()
    return jsonify(data)

# 财联社实时新闻
@app.route("/api/news")
def news():
    headers = {"Referer": "https://www.cls.cn/"}
    data = requests.get("https://www.cls.cn/api/sw?app=CailianNewsWeb&type=telegram&page=1&rn=30", headers=headers).json()
    return jsonify(data)

# 启动
if __name__ == "__main__":
    app.run(port=3000)