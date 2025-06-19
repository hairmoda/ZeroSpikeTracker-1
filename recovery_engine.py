# recovery_engine.py

import random
import datetime

def get_recovery_signal():
    coins = ["PEPE", "DOGE", "FLOKI", "1000SATS"]
    actions = ["صفقة سريعة", "شراء متدرج", "شراء صغير", "دخول تدريجي"]
    confidences = [87, 90, 91, 93, 95]
    risks = ["منخفضة", "متوسطة", "قابلة للانعكاس"]

    selected_coin = random.choice(coins)
    selected_action = random.choice(actions)
    confidence = random.choice(confidences)
    risk = random.choice(risks)
    now = datetime.datetime.now().strftime("%H:%M:%S")

    message = (
        f"🧠 توصية [{now}]: {selected_action} على {selected_coin} – "
        f"الثقة: {confidence}% – المخاطرة: {risk}"
    )
    return message
