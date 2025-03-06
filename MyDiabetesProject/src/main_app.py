import logging
from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError
from train_model import ModelTrainer
from evaluate_model import ModelEvaluator
from infer import InferenceService

logger = logging.getLogger("MainApp")
logger.setLevel(logging.INFO)

class PredictData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

app = Flask(__name__)

@app.route("/train", methods=["POST"])
def train_endpoint():
    ModelTrainer().run()
    return jsonify({"status": "training_completed"})

@app.route("/evaluate", methods=["POST"])
def evaluate_endpoint():
    ModelEvaluator().run()
    return jsonify({"status": "evaluation_completed"})

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.get_json(force=True)
    try:
        validated = PredictData(**data)
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422
    prediction, probability = InferenceService().predict(validated.dict())
    return jsonify({"prediction": prediction, "probability": probability})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
