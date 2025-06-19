from flask import Flask, jsonify
from Sbinance_liquidation_fetcher import fetch_liquidations  # استبدال MEXC ب Binance

app = Flask(__name__)

@app.route('/liquidation-data')
def get_liquidation_data():
    data = fetch_liquidations()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
