from flask import Flask, render_template, jsonify, request
from recovery_engine import get_recovery_signal
from mexc_liquidation_fetcher import get_liquidations  # جديد

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("quantum_dashboard.html")

@app.route("/recovery-flow")
def recovery():
    return render_template("recovery_flow.html")

@app.route("/trigger-recovery", methods=["POST"])
def trigger_recovery():
    result = get_recovery_signal()
    return jsonify({"message": result})

@app.route("/liquidation-tracker")  # جديد
def liquidation_tracker():
    return render_template("liquidation-tracker.html")

@app.route("/liquidation-data")  # جديد
def liquidation_data():
    data = get_liquidations()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    from flask import Flask, render_template
from recovery_flow import get_recovery_signal  # تأكد من المسار الصحيح

app = Flask(__name__)

@app.route("/recovery-flow")
def recovery_flow():
    signal = get_recovery_signal()
    return render_template("recovery_flow.html", signal=signal)

if __name__ == "__main__":
    app.run(debug=True)
