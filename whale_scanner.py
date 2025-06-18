def scan_whale_intent(orderbook, volume_data):
    """
    يبحث عن أوامر ضخمة مفاجئة أو تغير بحجم التداول يدل على دخول مؤسسات.
    """
    large_orders = [o for o in orderbook if o['size'] > 1_000_000]
    sudden_volume = volume_data[-1] > (sum(volume_data[-10:]) / 10) * 2

    if large_orders or sudden_volume:
        return "Whale Intent Detected"
    return "No Whale Activity"