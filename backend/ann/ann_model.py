import numpy as np
from sklearn.neural_network import MLPRegressor

# Simple ANN trained on synthetic logic (demo-safe)
model = MLPRegressor(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    max_iter=1000,
    random_state=42
)

# Dummy training data (soft computing demo purpose)
X_train = np.array([
    [25, 22, 120, 7, 0.3],
    [45, 30, 150, 5, 0.7],
    [60, 35, 170, 4, 0.9],
    [30, 24, 130, 6, 0.5]
])

y_train = np.array([85, 60, 35, 70])  # health score

model.fit(X_train, y_train)

def predict_health_score(inputs):
    x = np.array([[ 
        inputs["age"],
        inputs["bmi"],
        inputs["bp_sys"],
        inputs["sleep"],
        inputs["stress"]
    ]])
    return float(model.predict(x)[0])
