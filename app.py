from flask import Flask, render_template, jsonify
from dex_screener_scanner import fetch_dex_opportunities

app = Flask(__name__)

# الصفحة الرئيسية
@app.route("/")
def home():
    return render_template("quantum_dashboard.html")

# API: بيانات فرص DEX
@app.route("/dex-opportunities")
def dex_data():
    return jsonify(fetch_dex_opportunities())


