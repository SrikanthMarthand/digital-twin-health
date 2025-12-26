import numpy as np


# -----------------------------
# Membership functions
# -----------------------------
def low(x):
    return max(0.0, min(1.0, (0.5 - x) / 0.5))


def medium(x):
    return max(0.0, 1 - abs(x - 0.5) / 0.3)


def high(x):
    return max(0.0, min(1.0, (x - 0.5) / 0.5))


# -----------------------------
# Fuzzy inference system
# -----------------------------
def fuzzy_health_risk(row):
    """
    Input: one row of preprocessed data (normalized)
    Output: health risk label
    """

    bp = row["bp_sys"]
    bmi = row["bmi"]
    sleep = row["sleep"]
    stress = row["stress"]

    # Membership values
    bp_high = high(bp)
    bmi_high = high(bmi)
    sleep_low = low(sleep)
    stress_high = high(stress)

    # Rule evaluation
    rule_critical = max(bp_high, stress_high)
    rule_high = max(bmi_high, sleep_low)
    rule_moderate = medium(bp)
    rule_healthy = min(low(bp), low(stress), high(sleep))

    rules = {
        "Critical": rule_critical,
        "High Risk": rule_high,
        "Moderate": rule_moderate,
        "Healthy": rule_healthy
    }

    # Final decision
    return max(rules, key=rules.get)
