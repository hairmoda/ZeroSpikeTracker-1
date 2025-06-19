from pymexc import spot, futures
import time

# تهيئة عميل MEXC
spot_client = spot.HTTP(
    api_key=None,
    api_secret=None
)

def get_liquidations(limit=50):
    try:
        # خذ صفقات BTCUSDT الأخيرة
        trades = spot_client.deals(symbol="BTCUSDT", limit=limit)
        results = [
            {
                "symbol": trade["symbol"].replace("USDT", "/USDT"),
                "vol": float(trade["quantity"]),
                "price": trade["price"],
                "side": "BUY" if trade["side"] == "BID" else "SELL",
                "time": int(trade["time"])
            } 
            for trade in trades
        ]
        return sorted(results, key=lambda x: x["vol"], reverse=True)[:limit]

    except Exception as e:
        return [{"error": str(e)}]
