import json
import requests
from datetime import datetime

# 财联社公开电报接口，无鉴权、无需登录
NEWS_API = "https://www.cls.cn/nodeapi/telegraphList?app=ClsApp&category=telegram&page=1&rn=20&lastTime=&sign=1"

def handler(request, context):
    try:
        # 请求财联社接口，5秒超时
        resp = requests.get(NEWS_API, timeout=5)
        resp.raise_for_status()
        news_raw = resp.json()["data"]["roll_data"]

        today = datetime.now().strftime("%Y-%m-%d")
        news_list = []

        # 只保留当日新闻，过滤无效内容
        for item in news_raw:
            news_time = datetime.fromtimestamp(item["createtime"]).strftime("%Y-%m-%d %H:%M")
            if not news_time.startswith(today):
                continue
            
            # 自动识别财联社官方重要新闻（level=1为加红重要新闻）
            is_important = item.get("level") == 1 or "【重磅】" in item["title"] or "【突发】" in item["title"]
            
            news_list.append({
                "title": item["title"],
                "time": news_time,
                "url": f"https://www.cls.cn/detail/{item['id']}.html",
                "important": is_important
            })

        # 无新闻时返回兜底数据
        if not news_list:
            raise Exception("当日无新闻数据")

    # 任何异常都返回兜底数据
    except Exception as e:
        print(f"新闻请求失败: {str(e)}")
        today = datetime.now().strftime("%Y-%m-%d")
        news_list = [
            {"title": "【重磅】测试重要新闻", "time": f"{today} 10:00", "url": "https://www.cls.cn/", "important": True},
            {"title": "普通测试新闻", "time": f"{today} 09:30", "url": "https://www.cls.cn/", "important": False}
        ]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(news_list, ensure_ascii=False)
    }