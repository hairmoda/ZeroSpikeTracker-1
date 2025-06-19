from flask import Flask, render_template, jsonify, request
from recovery_engine import get_recovery_signal   # استخدم هذا إذا اسم الملف recovery_engine.py
# من الأفضل توحيد الاسم مع recovery_flow.py إذا أردت
from mexc_liquidation_fetcher import get_liquidations  # لجلب بيانات التصفيات

app = Flask(__name__)

# ✅ الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("quantum_dashboard.html")

# ✅ واجهة الاسترداد
@app.route("/recovery-flow")
def recovery():
    return render_template("recovery_flow.html")

# ✅ تفعيل الذكاء السيادي (زر أو تلقائي)
@app.route("/trigger-recovery", methods=["POST"])
def trigger_recovery():
    result = get_recovery_signal()
    return jsonify({"message": result})

# ✅ واجهة تتبع التصفيات
@app.route("/liquidation-tracker")
def liquidation_tracker():
    return render_template("liquidation-tracker.html")

# ✅ بيانات التصفيات API
@app.route("/liquidation-data")
def liquidation_data():
    data = get_liquidations()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
