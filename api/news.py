import json
from datetime import datetime

# handler必须顶格写，在文件最顶层
def handler(event, context):
    today = datetime.now().strftime("%Y-%m-%d")
    news_list = [
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
        "body": json.dumps(news_list, ensure_ascii=False)
    }