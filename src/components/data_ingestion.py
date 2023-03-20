
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('airtifacts', 'train.csv')
    test_data_path: str = os.path.join('airtifacts', 'test.csv')
    raw_data_path: str = os.path.join('airtifacts', 'data.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiated_data_ingestion(self):
        logging.info('Initiated data ingestion method or component')
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info(
                'Data ingestion completed successfully stud.csv as a dataframe')
            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,
                      index=False, header=True)
            logging.info("Train test split started")

            train_set, test_set = train_test_split(
                df, test_size=0.2, random_state=42)

            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)
            logging.info(
                "Ingestion of the date is completed Train test split completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiated_data_ingestion()
