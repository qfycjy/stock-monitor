import json
from datetime import datetime

def handler(event, context):
    today = datetime.now().strftime("%Y-%m-%d")
    test_news = [
        {
            "title": "【加红】测试重要新闻",
            "time": f"{today} 10:00",
            "url": "https://www.cls.cn/",
            "important": True
        },
        {
            "title": "普通测试新闻",
            "time": f"{today} 09:30",
            "url": "https://www.cls.cn/",
            "important": False
        }
    ]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(test_news, ensure_ascii=False)
    }