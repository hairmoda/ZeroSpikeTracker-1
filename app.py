from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("quantum_dashboard.html")

@app.route("/recovery-flow")
def recovery():
    return render_template("recovery_flow.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
