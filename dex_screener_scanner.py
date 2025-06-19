# dex_screener_scanner.py
import requests

def fetch_dex_opportunities():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        top_pairs = []
        for pair in data.get("pairs", []):
            try:
                price_change = float(pair.get("priceChange", 0))
                if price_change > 30:
                    top_pairs.append({
                        "symbol": pair.get("baseToken", {}).get("symbol", ""),
                        "dex": pair.get("dexId", ""),
                        "priceUsd": pair.get("priceUsd", ""),
                        "volume": pair.get("volume", ""),
                        "changePercent": price_change,
                        "url": pair.get("url", "")
                    })
            except Exception:
                continue
        return top_pairs
    except Exception as e:
        return [{"error": str(e)}]
