import json
from datetime import datetime

def handler(request, context):
    today = datetime.now().strftime("%Y-%m-%d")
    result = [
        {"title": "【加红】测试重要新闻", "time": f"{today} 10:00", "url": "https://www.cls.cn/", "important": True},
        {"title": "普通测试新闻", "time": f"{today} 09:30", "url": "https://www.cls.cn/", "important": False}
    ]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result, ensure_ascii=False)
    }