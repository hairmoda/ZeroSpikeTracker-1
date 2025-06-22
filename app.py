from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quantum-dashboard')
def quantum_dashboard():
    return render_template('quantum_dashboard.html')

@app.route('/liquidation-tracker')
def liquidation_tracker():
    return render_template('liquidation-tracker.html')

# 👇 علّق الباقي مؤقتًا:
# @app.route('/routes-dashboard')
# def routes_dashboard():
#     return render_template('routes_dashboard.html')

# @app.route('/execution-logs')
# def execution_logs():
#     return render_template('execution_logs.html')

# @app.route('/whale-visualizer')
# def whale_visualizer():
#     return render_template('whale_visualizer.html')