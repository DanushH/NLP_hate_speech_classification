import os
import sys
from zipfile import ZipFile
import kaggle
from hate_speech.logger import logging
from hate_speech.exception import CustomException
from hate_speech.entity.config_entity import DataIngestionConfig
from hate_speech.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def get_data_from_kaggle(self) -> None:
        try:
            dataset_name = self.data_ingestion_config.KAGGLE_DATASET_NAME
            kaggle.api.dataset_download_files(
                dataset_name, path=self.data_ingestion_config.ZIP_FILE_DIR, unzip=False
            )
            logging.info(f"Downloaded the dataset {dataset_name} from Kaggle")

        except Exception as e:
            raise CustomException(e, sys) from e

    def unzip_and_clean(self):
        logging.info("Entered the unzip_and_clean method of Data ingestion class")
        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, "r") as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Exited the unzip_and_clean method of Data ingestion class")

            return (
                self.data_ingestion_config.DATA_ARTIFACTS_DIR,
                self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR,
            )

        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info(
            "Entered the initiate_data_ingestion method of Data ingestion class"
        )

        try:
            self.get_data_from_kaggle()
            imbalance_data_file_path, raw_data_file_path = self.unzip_and_clean()
            logging.info("Unzipped file and split into train and valid")

            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalance_data_file_path=imbalance_data_file_path,
                raw_data_file_path=raw_data_file_path,
            )

            logging.info(
                "Exited the initiate_data_ingestion method of Data ingestion class"
            )

            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
