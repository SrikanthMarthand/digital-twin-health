from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from fuzzy.fuzzy_engine import fuzzy_health_risk
from ann.ann_model import predict_health_score

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

    # Normalize inputs
    row = {
        "age": normalize(age, 0, 100),
        "bmi": normalize(bmi, 10, 40),
        "bp_sys": normalize(bp_sys, 80, 200),
        "sleep": normalize(sleep, 0, 12),
        "stress": stress
    }

    # ANN prediction (numeric)
    ann_score = predict_health_score(row)

    # Fuzzy inference (linguistic)
    risk = fuzzy_health_risk(row)

    # Digital Twin Output (HYBRID)
    response = {
        "digital_twin": {
            "health_risk": risk,
            "health_score": round(ann_score, 1),
            "inputs": row
        }
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
