import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "hate_speech"

list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_train.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_deploy.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/gcp_sync.py",

    f"{project_name}/constant/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",

    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",

    "app.py",
    "demo.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]


for filepath in list_of_files:
    file_path = Path(filepath)
    file_dir, file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating empty file: {file_path}")

    else:
        logging.info(f"{file_name} already exists")
