import sys
import logging
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout, QTextEdit
)
from train_model import ModelTrainer
from evaluate_model import ModelEvaluator
from infer import InferenceService

logger = logging.getLogger("PyQtApp")
logger.setLevel(logging.INFO)

class DiabetesApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diabetes Detection")
        self.input_fields = {}
        self.layout = QVBoxLayout()
        self.form_layout = QGridLayout()
        self.buttons_layout = QHBoxLayout()
        self.result_box = QTextEdit()
        self.init_ui()

    def init_ui(self):
        labels = [
            "Pregnancies", "Glucose", "BloodPressure",
            "SkinThickness", "Insulin", "BMI",
            "DiabetesPedigreeFunction", "Age"
        ]
        for i, label_text in enumerate(labels):
            label = QLabel(label_text)
            line_edit = QLineEdit()
            self.input_fields[label_text] = line_edit
            self.form_layout.addWidget(label, i, 0)
            self.form_layout.addWidget(line_edit, i, 1)

        train_button = QPushButton("Train")
        evaluate_button = QPushButton("Evaluate")
        predict_button = QPushButton("Predict")

        train_button.clicked.connect(self.train_model)
        evaluate_button.clicked.connect(self.evaluate_model)
        predict_button.clicked.connect(self.predict)

        self.buttons_layout.addWidget(train_button)
        self.buttons_layout.addWidget(evaluate_button)
        self.buttons_layout.addWidget(predict_button)

        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.buttons_layout)
        self.result_box.setReadOnly(True)
        self.layout.addWidget(self.result_box)
        self.setLayout(self.layout)

    def train_model(self):
        ModelTrainer().run()
        self.result_box.append("Training completed")

    def evaluate_model(self):
        ModelEvaluator().run()
        self.result_box.append("Evaluation completed, please check logs")

    def predict(self):
        data = {}
        for key, field in self.input_fields.items():
            value = field.text().strip()
            try:
                if key in ["BMI", "DiabetesPedigreeFunction"]:
                    data[key] = float(value)
                else:
                    data[key] = int(value)
            except ValueError:
                data[key] = 0
        prediction, probability = InferenceService().predict(data)
        self.result_box.append(f"Prediction: {prediction}, Probability: {probability}")

def main():
    app = QApplication(sys.argv)
    window = DiabetesApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
