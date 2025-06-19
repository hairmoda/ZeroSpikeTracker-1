import requests
import time

def get_liquidations(limit=50):
    try:
        symbols = ["BTC_USDT", "ETH_USDT", "PEPE_USDT", "DOGE_USDT"]
        results = []

        for symbol in symbols:
            url = f"https://api.mexc.com/api/v1/market/deals?symbol={symbol}&limit={limit}"
            response = requests.get(url)
            response.raise_for_status()
            trades = response.json()

            for trade in trades:
                results.append({
                    "symbol": symbol.replace("_", "/"),
                    "vol": float(trade.get("quantity", 0)),
                    "price": trade.get("price"),
                    "side": "BUY" if trade.get("side") == "BID" else "SELL",
                    "time": int(float(trade.get("time", time.time())) * 1000)
                })

        results = sorted(results, key=lambda x: x["vol"], reverse=True)[:50]
        return results

    except Exception as e:
        return [{"error": str(e)}]
