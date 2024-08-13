import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")


PROJECT_NAME = "hate_speech"

list_of_files = [
    f"{PROJECT_NAME}/components/__init__.py",
    f"{PROJECT_NAME}/components/data_ingestion.py",
    f"{PROJECT_NAME}/components/data_transformation.py",
    f"{PROJECT_NAME}/components/model_train.py",
    f"{PROJECT_NAME}/components/model_evaluation.py",
    f"{PROJECT_NAME}/components/model_deploy.py",
    f"{PROJECT_NAME}/configuration/__init__.py",
    f"{PROJECT_NAME}/configuration/gcp_sync.py",
    f"{PROJECT_NAME}/constant/__init__.py",
    f"{PROJECT_NAME}/entity/__init__.py",
    f"{PROJECT_NAME}/entity/config_entity.py",
    f"{PROJECT_NAME}/entity/artifact_entity.py",
    f"{PROJECT_NAME}/exception/__init__.py",
    f"{PROJECT_NAME}/logger/__init__.py",
    f"{PROJECT_NAME}/pipeline/__init__.py",
    f"{PROJECT_NAME}/pipeline/train_pipeline.py",
    f"{PROJECT_NAME}/pipeline/prediction_pipeline.py",
    f"{PROJECT_NAME}/ml/__init__.py",
    f"{PROJECT_NAME}/ml/model.py",
    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore",
]


for filepath in list_of_files:
    file_path = Path(filepath)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")

    else:
        logging.info(f"{file_name} already exists")
