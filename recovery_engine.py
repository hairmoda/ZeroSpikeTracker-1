# recovery_engine.py
import random
import datetime

def get_recovery_signal():
    # بيانات وهمية قابلة للتوسعة
    coins = ["PEPE", "DOGE", "FLOKI", "1000SATS", "BONK"]
    actions = ["شراء صغير", "صفقة سريعة", "دخول تدريجي", "تعزيز بسيط"]
    confidences = [87, 90, 91, 93, 95]
    risks = ["منخفضة", "متوسطة", "قابلة للانعكاس", "تحت المراقبة"]

    selected_coin = random.choice(coins)
    selected_action = random.choice(actions)
    confidence = random.choice(confidences)
    risk = random.choice(risks)
    now = datetime.datetime.now().strftime("%H:%M:%S")

    message = (
        f"🧠 توصية [{now}]: {selected_action} على {selected_coin} "
        f"– الثقة: {confidence}٪ – المخاطرة: {risk}"
    )

    return message