
import requests
import hmac
import hashlib
import time
import os

MEXC_API_KEY = os.getenv("MEXC_API_KEY")
MEXC_SECRET_KEY = os.getenv("MEXC_SECRET_KEY")

BASE_URL = "https://api.mexc.com"

def get_signature(params: dict, secret_key: str):
    query_string = "&".join([f"{k}={v}" for k, v in sorted(params.items())])
    return hmac.new(secret_key.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def fetch_liquidations(limit=50):
    """جلب صفقات التصفية الحديثة من MEXC Futures"""
    try:
        path = "/api/v1/private/future/position/open_positions"
        timestamp = str(int(time.time() * 1000))
        params = {
            "timestamp": timestamp,
            "recvWindow": "5000"
        }

        signature = get_signature(params, MEXC_SECRET_KEY)
        headers = {
            "Content-Type": "application/json",
            "ApiKey": MEXC_API_KEY
        }
        params["signature"] = signature

        response = requests.get(BASE_URL + path, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # تحليل صفقات مهددة بالتصفية بناءً على نسبة المخاطرة أو Margin ratio
        liquidations = []
        for pos in data.get("data", []):
            if float(pos.get("unrealizedPnl", 0)) < 0 and float(pos.get("marginRatio", 0)) > 0.8:
                liquidations.append({
                    "symbol": pos["symbol"],
                    "size": pos["positionAmt"],
                    "risk": pos["marginRatio"],
                    "entry": pos["entryPrice"],
                    "mark": pos["markPrice"]
                })

        return liquidations
    except Exception as e:
        return {"error": str(e)}
