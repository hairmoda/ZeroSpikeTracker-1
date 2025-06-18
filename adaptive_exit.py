def should_exit(market_momentum, position):
    """
    يقرر الخروج الذكي قبل انعكاس الاتجاه.
    """
    if market_momentum < 0 and position == "long":
        return "Exit Long"
    elif market_momentum > 0 and position == "short":
        return "Exit Short"
    return "Hold"