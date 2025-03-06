import os
import pathlib
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MyDiabetesProject"
    BASE_DIR: str = str(pathlib.Path(__file__).parent.resolve())
    DATA_PATH: str = os.path.join(BASE_DIR, "..", "data", "processed", "diabetes.csv")
    MODEL_PATH: str = os.path.join(BASE_DIR, "..", "models", "diabetes_model.pkl")
    TEST_RATIO: float = 0.2
    RANDOM_STATE: int = 42
    BATCH_SIZE: int = 32
    EPOCHS: int = 10
    LEARNING_RATE: float = 0.001

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
