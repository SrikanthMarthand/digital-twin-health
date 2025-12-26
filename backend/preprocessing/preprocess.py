import pandas as pd
import numpy as np


# -------------------------------
# Load dataset
# -------------------------------
def load_data(csv_path):
    """
    Load health dataset from CSV
    """
    df = pd.read_csv(csv_path)
    return df


# -------------------------------
# Normalize numerical columns
# -------------------------------
def normalize_column(series):
    """
    Min-Max normalization
    """
    return (series - series.min()) / (series.max() - series.min())


# -------------------------------
# Stress level mapping
# -------------------------------
def map_stress(value):
    """
    Converts questionnaire stress values to numeric scale
    Low -> 0.2
    Medium -> 0.5
    High -> 0.8
    """
    if value in ["Low", 1]:
        return 0.2
    elif value in ["Medium", 2]:
        return 0.5
    else:
        return 0.8


# -------------------------------
# Main preprocessing function
# -------------------------------
def preprocess_data(df):
    """
    Prepare dataset for ANN and Fuzzy systems
    """

    processed = pd.DataFrame()

    # Numerical features
    processed["age"] = normalize_column(df["RIDAGEYR"])
    processed["bmi"] = normalize_column(df["BMXBMI"])
    processed["bp_sys"] = normalize_column(df["BPXSY1"])
    processed["bp_dia"] = normalize_column(df["BPXDI1"])
    processed["pulse"] = normalize_column(df["BPXPLS"])
    processed["sleep"] = normalize_column(df["SLD010H"])

    # Stress / subjective input
    if "stress_level" in df.columns:
        processed["stress"] = df["stress_level"].apply(map_stress)
    else:
        processed["stress"] = 0.5  # neutral default

    # Optional ANN supervision label
    if "Initial_Health_Label" in df.columns:
        processed["label"] = df["Initial_Health_Label"]

    return processed


# -------------------------------
# Standalone test
# -------------------------------
if __name__ == "__main__":
    import os

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", "health_data.csv")

    data = load_data(DATA_PATH)
    processed = preprocess_data(data)
    print(processed.head())
