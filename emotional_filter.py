def emotional_spike_filter(rsi, fear_greed_index):
    """
    يمنع الدخول وقت الطمع المفرط أو الخوف الجماعي.
    """
    if rsi > 75 or fear_greed_index > 80:
        return "Greed Spike - Block Trade"
    elif rsi < 25 or fear_greed_index < 20:
        return "Fear Spike - Block Trade"
    return "Safe"

