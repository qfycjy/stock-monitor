import json
import requests

def handler(request, context):
    HEADERS = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://quote.eastmoney.com/"
    }

    result = {
        "sh": {"value": "0", "change": "0", "percent": "0%"},
        "sz": {"value": "0", "change": "0", "percent": "0%"},
        "northbound": "0",
        "northboundChange": "0"
    }

    try:
        # 上证指数 + 深证成指
        url_idx = "https://push2.eastmoney.com/api/qt/ulist.np/get?secids=1.000001,0.399001&fields=f2,f3,f4"
        resp = requests.get(url_idx, headers=HEADERS, timeout=10)
        data = resp.json()
        diff = data.get("data", {}).get("diff", [])

        if len(diff) >= 2:
            # 上证
            sh = diff[0]
            sh_val = round(float(sh.get("f2", 0)) / 100, 2)
            sh_chg = round(float(sh.get("f4", 0)) / 100, 2)
            sh_pct = sh.get("f3", "0")
            result["sh"] = {
                "value": f"{sh_val}",
                "change": f"+{sh_chg}" if sh_chg >= 0 else f"{sh_chg}",
                "percent": f"{sh_pct}%"
            }

            # 深证
            sz = diff[1]
            sz_val = round(float(sz.get("f2", 0)) / 100, 2)
            sz_chg = round(float(sz.get("f4", 0)) / 100, 2)
            sz_pct = sz.get("f3", "0")
            result["sz"] = {
                "value": f"{sz_val}",
                "change": f"+{sz_chg}" if sz_chg >= 0 else f"{sz_chg}",
                "percent": f"{sz_pct}%"
            }
    except Exception as e:
        print("index error:", e)

    try:
        # 北向资金
        url_north = "https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=1&fs=b:MK0001&fields=f3"
        resp = requests.get(url_north, headers=HEADERS, timeout=10)
        data = resp.json()
        diff = data.get("data", {}).get("diff", [])
        if diff:
            val = round(float(diff[0].get("f3", 0)) / 100, 2)
            result["northbound"] = f"{val}"
            result["northboundChange"] = f"+{val}" if val >= 0 else f"{val}"
    except Exception as e:
        print("north error:", e)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(result, ensure_ascii=False)
    }
