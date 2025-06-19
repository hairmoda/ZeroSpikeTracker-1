from dex_screener_scanner import fetch_dex_opportunities

@app.route("/dex-insights")
def dex_insights():
    return render_template("dex-insights.html")

@app.route("/dex-opportunities")
def dex_data():
    return jsonify(fetch_dex_opportunities())
# ✅ في app.py
from dex_screener_scanner import fetch_dex_opportunities

@app.route("/dex-opportunities")
def dex_data():
    return jsonify(fetch_dex_opportunities())
