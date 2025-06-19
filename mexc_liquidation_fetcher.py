import requests
import time

def get_liquidations(limit=50):
    try:
        symbols = ["BTCUSDT", "ETHUSDT", "PEPEUSDT", "DOGEUSDT"]
        results = []

        for symbol in symbols:
            url = f"https://api.mexc.com/api/v3/market/trades?symbol={symbol}&limit={limit}"
            response = requests.get(url)
            response.raise_for_status()
            trades = response.json()

            for trade in trades:
                results.append({
                    "symbol": symbol[:-4] + "/USDT",
                    "vol": float(trade.get("qty", 0)),
                    "price": trade.get("price"),
                    "side": "SELL" if trade.get("isBuyerMaker") else "BUY",
                    "time": int(trade.get("time"))
                })

        results = sorted(results, key=lambda x: x["vol"], reverse=True)[:50]
        return results

    except Exception as e:
        return [{"error": str(e)}]
