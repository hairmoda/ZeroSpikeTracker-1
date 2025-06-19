# dex_screener_scanner.py
import requests

def fetch_dex_opportunities():
    url = "https://api.dexscreener.com/latest/dex/pairs"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        top_pairs = []
        for pair in data.get("pairs", []):
            try:
                price_change = float(pair.get("priceChange", {}).get("h1", 0))
                if price_change > 30:  # العملات المجنونة خلال ساعة
                    top_pairs.append({
                        "symbol": pair.get("pairSymbol"),
                        "dex": pair.get("dexId"),
                        "priceUsd": pair.get("priceUsd"),
                        "volume": pair.get("volume", {}).get("h1"),
                        "changePercent": price_change,
                        "url": pair.get("url")
                    })
            except:
                continue

        return sorted(top_pairs, key=lambda x: x["changePercent"], reverse=True)[:10]

    except Exception as e:
        return [{"error": str(e)}]
