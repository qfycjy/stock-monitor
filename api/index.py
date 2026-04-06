import json

def handler(request, context):
    # 固定测试数据，无任何语法和依赖问题
    result = {
        "sh": {"value": "3000.00", "change": "+10.00", "percent": "+0.33%"},
        "sz": {"value": "10000.00", "change": "-20.00", "percent": "-0.20%"},
        "northbound": "10.5",
        "northboundChange": "+2.3"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result, ensure_ascii=False)
    }