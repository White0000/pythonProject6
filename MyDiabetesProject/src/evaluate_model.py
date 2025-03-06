import logging
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from config import settings
from data_preprocessing import DataPreprocessor

logger = logging.getLogger("ModelEvaluation")
logger.setLevel(logging.INFO)

class ModelEvaluator:
    def __init__(self):
        self.model_path = settings.MODEL_PATH

    def run(self):
        x_train, x_test, y_train, y_test = DataPreprocessor().run()
        model = joblib.load(self.model_path)
        preds = model.predict(x_test)
        accuracy = accuracy_score(y_test, preds)
        precision = precision_score(y_test, preds)
        recall = recall_score(y_test, preds)
        f1 = f1_score(y_test, preds)
        auc = roc_auc_score(y_test, preds)
        logger.info(f"Evaluation metrics -> ACC: {accuracy}, PREC: {precision}, RECALL: {recall}, F1: {f1}, AUC: {auc}")

if __name__ == "__main__":
    ModelEvaluator().run()
