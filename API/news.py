import json
import requests
from datetime import datetime

def handler(request, context):
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Referer": "https://www.cls.cn/",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
    }

    today = datetime.now().strftime("%Y-%m-%d")
    # 兜底新闻，接口失败也不会空白
    final_news = [
        {"title": "【重磅】测试重要新闻", "time": f"{today} 10:00", "url": "https://www.cls.cn/", "important": True},
        {"title": "普通测试新闻", "time": f"{today} 09:30", "url": "https://www.cls.cn/", "important": False}
    ]

    try:
        news_api = "https://www.cls.cn/nodeapi/telegraphList?app=ClsApp&category=telegram&page=1&rn=20&lastTime=&sign=1"
        resp = requests.get(news_api, headers=HEADERS, timeout=8)
        resp.raise_for_status()
        news_json = resp.json()
        news_raw = news_json.get("data", {}).get("roll_data", [])

        news_list = []
        for item in news_raw:
            try:
                news_time = datetime.fromtimestamp(int(item["createtime"])).strftime("%Y-%m-%d %H:%M")
                if not news_time.startswith(today):
                    continue

                is_important = item.get("level") == 1 or "【重磅】" in item["title"] or "【突发】" in item["title"]
                news_list.append({
                    "title": item["title"],
                    "time": news_time,
                    "url": f"https://www.cls.cn/detail/{item['id']}.html",
                    "important": is_important
                })
            except Exception as e:
                print(f"单条新闻解析失败: {str(e)}")
                continue

        if news_list:
            final_news = news_list

    except Exception as e:
        print(f"新闻接口异常: {str(e)}")

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(final_news, ensure_ascii=False)
    }
