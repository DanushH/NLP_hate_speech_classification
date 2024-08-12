import os
import sys
import kaggle
from zipfile import ZipFile
from hate_speech.logger import logging
from hate_speech.exception import CustomException
from hate_speech.entity.config_entity import DataIngestionConfig
from hate_speech.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def get_data_from_kaggle(self) -> None:
        try:
            logging.info("Entered the get_data_from_kaggle method of DataIngestion class")
            os.makedirs(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, exist_ok=True)

            # Use Kaggle API to download the dataset
            kaggle.api.dataset_download_files(
                self.data_ingestion_config.KAGGLE_DATASET_PATH,
                path=self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,
                unzip=False
            )
            logging.info("Exited the get_data_from_kaggle method of DataIngestion class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def unzip_and_clean(self):
        logging.info("Entered the unzip_and_clean method of DataIngestion class")
        try:
            zip_file_path = os.path.join(self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR, self.data_ingestion_config.ZIP_FILE_NAME)
            with ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info("Exited the unzip_and_clean method of DataIngestion class")

            return self.data_ingestion_config.DATA_ARTIFACTS_DIR, self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR

        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the initiate_data_ingestion method of DataIngestion class")

        try:
            self.get_data_from_kaggle()
            logging.info("Fetched the data from Kaggle dataset")
            imbalance_data_file_path, raw_data_file_path = self.unzip_and_clean()
            logging.info("Unzipped file and split into train and valid")

            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalance_data_file_path=imbalance_data_file_path,
                raw_data_file_path=raw_data_file_path
            )

            logging.info("Exited the initiate_data_ingestion method of DataIngestion class")
            logging.info(f"Data ingestion artifact: {data_ingestion_artifacts}")

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e
