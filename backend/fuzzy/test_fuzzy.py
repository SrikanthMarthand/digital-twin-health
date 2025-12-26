import os
import sys

# -----------------------------
# Add backend root to PYTHONPATH
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from preprocessing.preprocess import load_data, preprocess_data
from fuzzy.fuzzy_engine import fuzzy_health_risk


# -----------------------------
# Load and preprocess data
# -----------------------------
DATA_PATH = os.path.join(BASE_DIR, "data", "health_data.csv")

df = load_data(DATA_PATH)
processed = preprocess_data(df)

# -----------------------------
# Test fuzzy logic
# -----------------------------
for i in range(5):
    risk = fuzzy_health_risk(processed.iloc[i])
    print(f"Row {i} → Fuzzy Risk: {risk}")
