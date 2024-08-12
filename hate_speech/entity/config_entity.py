from dataclasses import dataclass
from hate_speech.constant import *
import os


@dataclass
class DataIngestionConfig:
    def __init__(self):
        self.DATA_INGESTION_ARTIFACTS_DIR = "artifacts/data_ingestion/"
        self.KAGGLE_DATASET_PATH = "danuherath/hate-speech"
        self.ZIP_FILE_NAME = "hate-speech.zip"
        self.ZIP_FILE_DIR = "data/raw"
        self.DATA_ARTIFACTS_DIR = "data/artifacts"
        self.NEW_DATA_ARTIFACTS_DIR = "data/new_artifacts"
