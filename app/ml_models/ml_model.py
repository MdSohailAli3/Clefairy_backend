import joblib
import numpy as np

MODEL_PATH = "app/ml_models/safety.pkl"

model = joblib.load(MODEL_PATH)
# receives list of list 
def predict_route_risk(feature_matrix: np.ndarray):
    """
    feature_matrix shape:
    (num_points, num_features)
    """
    predictions = model.predict(feature_matrix)

    # Aggregate segment predictions into route score
    return float(np.mean(predictions))
