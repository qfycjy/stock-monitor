import json
import requests
from datetime import datetime

def handler(request, context):
    news = []
    today = datetime.now().strftime("%Y-%m-%d")

    try:
        url = "https://www.cls.cn/nodeapi/telegraphList"
        params = {"app": "ClsApp", "category": "telegram", "page": 1, "rn": 20}
        headers = {"User-Agent": "Mozilla/5.0", "Referer": "https://www.cls.cn/"}
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        data = resp.json()
        items = data.get("data", {}).get("roll_data", [])

        for item in items:
            try:
                ts = item.get("createtime", 0)
                dt = datetime.fromtimestamp(int(ts))
                time_str = dt.strftime("%Y-%m-%d %H:%M")
                if not time_str.startswith(today):
                    continue

                news.append({
                    "title": item.get("title", ""),
                    "time": time_str,
                    "url": f"https://www.cls.cn/detail/{item['id']}.html",
                    "important": item.get("level") == 1
                })
            except Exception as e:
                continue
    except Exception as e:
        print("news error:", e)

    if not news:
        news = [{"title": "暂无新闻", "time": today, "url": "#", "important": False}]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(news, ensure_ascii=False)
    }
