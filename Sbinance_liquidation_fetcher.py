import requests
import time

def fetch_liquidations():
    url = "https://fapi.binance.com/fapi/v1/allForceOrders"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        all_data = response.json()

        # تصفية البيانات لجلب أحدث عمليات التصفية فقط
        filtered_data = []
        for order in all_data:
            if order.get("status") == "FILLED" and float(order.get("executedQty", 0)) > 0:
                filtered_data.append({
                    "symbol": order["symbol"],
                    "side": order["side"],
                    "price": order["avgPrice"],
                    "qty": order["executedQty"],
                    "time": order["time"]
                })

        # ترتيب من الأحدث للأقدم
        filtered_data.sort(key=lambda x: x["time"], reverse=True)

        return filtered_data[:50]  # نرجع آخر 50 فقط
    except Exception as e:
        return {"error": str(e)}
