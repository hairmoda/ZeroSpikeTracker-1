from flask import Flask, render_template, jsonify, request
from recovery_engine import get_recovery_signal

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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
