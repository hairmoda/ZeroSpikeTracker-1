def detect_trap(candles):
    """
    يحلل الشموع لاكتشاف مصيدة لونغ أو شورت.
    """
    last = candles[-1]
    prev = candles[-2]
    
    if prev['low'] < candles[-3]['low'] and last['close'] > prev['open']:
        return "Long Trap Detected"
    elif prev['high'] > candles[-3]['high'] and last['close'] < prev['open']:
        return "Short Trap Detected"
    return "No Trap"

