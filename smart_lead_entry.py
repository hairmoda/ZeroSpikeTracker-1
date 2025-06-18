def smart_lead_entry(binance_price, mexc_price, block_speed):
    """
    يدخل السوق قبل المؤسسات إذا تم رصد تحرك سريع بالسعر أو البلوك.
    """
    price_gap = abs(binance_price - mexc_price)
    if price_gap > 0.000001 and block_speed < 0.5:
        return "Smart Entry Signal"
    return "No Entry"