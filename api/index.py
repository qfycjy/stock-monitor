import json

def handler(event, context):
    # 固定测试数据，保证函数绝对合规、不会崩溃
    test_data = {
        "sh": {
            "value": "3000.00",
            "change": "+10.00",
            "percent": "+0.33"
        },
        "sz": {
            "value": "10000.00",
            "change": "-20.00",
            "percent": "-0.20"
        },
        "northbound": "10.5",
        "northboundChange": "+2.3"
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(test_data, ensure_ascii=False)
    }