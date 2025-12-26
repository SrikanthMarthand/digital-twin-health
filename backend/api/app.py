from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from fuzzy.fuzzy_engine import fuzzy_health_risk

app = Flask(__name__)
CORS(app)


# -----------------------------
# Helper: normalize value
# -----------------------------
def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)


# -----------------------------
# Health Assessment API
# -----------------------------
@app.route("/assess-health", methods=["POST"])
def assess_health():
    data = request.json

    # Raw inputs from UI
    age = data.get("age")
    bmi = data.get("bmi")
    bp_sys = data.get("bp_sys")
    sleep = data.get("sleep")
    stress = data.get("stress")

    # Normalize (same logic as preprocessing)
    row = {
        "age": normalize(age, 0, 100),
        "bmi": normalize(bmi, 10, 40),
        "bp_sys": normalize(bp_sys, 80, 200),
        "sleep": normalize(sleep, 0, 12),
        "stress": stress  # already normalized (0–1)
    }

    # Fuzzy inference
    risk = fuzzy_health_risk(row)

    # Digital Twin Output
    response = {
        "digital_twin": {
            "health_risk": risk,
            "inputs": row
        }
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
