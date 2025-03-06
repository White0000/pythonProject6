import logging
import os
import joblib
from config import settings
from data_preprocessing import DataPreprocessor
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

logger = logging.getLogger("ModelTraining")
logger.setLevel(logging.INFO)

class ModelTrainer:
    def __init__(self):
        self.model_path = settings.MODEL_PATH
        self.random_state = settings.RANDOM_STATE

    def run(self):
        logger.info("Starting model training")
        x_train, x_test, y_train, y_test = DataPreprocessor().run()
        model = LogisticRegression(max_iter=200, random_state=self.random_state)
        model.fit(x_train, y_train)
        preds = model.predict(x_test)
        accuracy = accuracy_score(y_test, preds)
        logger.info(f"Training completed with accuracy: {accuracy}")
        self.save_model(model)
        logger.info("Model saved successfully")

    def save_model(self, model):
        directory = os.path.dirname(self.model_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        joblib.dump(model, self.model_path)

if __name__ == "__main__":
    ModelTrainer().run()
