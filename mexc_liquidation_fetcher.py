import requests
import time

def get_liquidations(limit=50):
    try:
        symbols = ["BTC_USDT", "ETH_USDT", "PEPE_USDT", "DOGE_USDT"]
        results = []

        for symbol in symbols:
            url = f"https://api.mexc.com/api/v3/depth?symbol={symbol}&limit=5"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            bids = data.get("bids", [])
            asks = data.get("asks", [])

            if bids:
                results.append({
                    "symbol": symbol.replace("_", "/"),
                    "vol": float(bids[0][1]),
                    "price": bids[0][0],
                    "side": "BUY",
                    "time": int(time.time() * 1000)
                })

            if asks:
                results.append({
                    "symbol": symbol.replace("_", "/"),
                    "vol": float(asks[0][1]),
                    "price": asks[0][0],
                    "side": "SELL",
                    "time": int(time.time() * 1000)
                })

        return sorted(results, key=lambda x: x["vol"], reverse=True)[:limit]
    except Exception as e:
        return [{"error": str(e)}]
