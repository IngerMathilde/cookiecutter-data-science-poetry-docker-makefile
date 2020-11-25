from dotenv import find_dotenv, load_dotenv
from pathlib import Path
import logging
import os

# LOGGER
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=log_fmt)

# ENVIRONMENT FILES
# find .env automagically by walking up directories until it's found, then
# load up the .env entries as environment variables
load_dotenv(find_dotenv())

# DIRECTORIES
PROJECT_DIR: str = str(Path(__file__).parents[1])

# # DATA DIRECTORIES
DATA_DIR: str = os.path.join(PROJECT_DIR, "data")
EXTERNAL_DATA_DIR: str = os.path.join(DATA_DIR, "external")
RAW_DATA_DIR: str = os.path.join(DATA_DIR, "raw")
INTERIM_DATA_DIR: str = os.path.join(DATA_DIR, "interim")
PROCESSED_DATA_DIR: str = os.path.join(DATA_DIR, "processed")

# # MODEL DIRECTORIES
MODEL_DIR: str = os.path.join(PROJECT_DIR, "model")

