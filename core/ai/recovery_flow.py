# recovery_flow.py

import random
from datetime import datetime

def get_recovery_signal():
    coins = ['BTC', 'ETH', 'SOL', 'FLOKI', 'PEPE', 'DOGE']
    selected_coin = random.choice(coins)
    confidence = round(random.uniform(85, 95), 2)
    risk = 'منخفضة' if confidence > 90 else 'متوسطة'
    timestamp = datetime.now().strftime('%H:%M:%S')

    return {
        'coin': selected_coin,
        'confidence': confidence,
        'risk': risk,
        'time': timestamp
    }
