import logging
import joblib
import pandas as pd
from config import settings

logger = logging.getLogger("ModelInference")
logger.setLevel(logging.INFO)

class InferenceService:
    def __init__(self):
        self.model_path = settings.MODEL_PATH

    def predict(self, data: dict):
        model = joblib.load(self.model_path)
        df = pd.DataFrame([data])
        preds = model.predict(df)
        probabilities = model.predict_proba(df)
        prediction = int(preds[0])
        probability = float(probabilities[0][prediction])
        logger.info(f"Prediction: {prediction}, Probability: {probability}")
        return prediction, probability

if __name__ == "__main__":
    sample_data = {
        "Pregnancies": 3,
        "Glucose": 120,
        "BloodPressure": 70,
        "SkinThickness": 23,
        "Insulin": 80,
        "BMI": 28.5,
        "DiabetesPedigreeFunction": 0.5,
        "Age": 32
    }
    result = InferenceService().predict(sample_data)
    logger.info(f"Inference result: {result}")
