import logging
import pandas as pd
import numpy as np
from config import settings
from sklearn.model_selection import train_test_split

logger = logging.getLogger("DataPreprocessing")
logger.setLevel(logging.INFO)

class DataPreprocessor:
    def __init__(self):
        self.data_path = settings.DATA_PATH
        self.test_ratio = settings.TEST_RATIO
        self.random_state = settings.RANDOM_STATE

    def load_data(self):
        df = pd.read_csv(self.data_path)
        return df

    def clean_data(self, df):
        df = df.dropna()
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = df[col].fillna(df[col].mean())
        return df

    def split_data(self, df):
        x = df.drop("Outcome", axis=1)
        y = df["Outcome"]
        return train_test_split(x, y, test_size=self.test_ratio, random_state=self.random_state)

    def run(self):
        logger.info("Starting data preprocessing")
        df = self.load_data()
        df = self.clean_data(df)
        x_train, x_test, y_train, y_test = self.split_data(df)
        logger.info("Data preprocessing completed")
        return x_train, x_test, y_train, y_test
