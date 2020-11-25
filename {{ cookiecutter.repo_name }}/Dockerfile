FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# set path to our python api file
ENV MODULE_NAME="server.jp_api"

# copy contents of project into docker
COPY ./pyproject.toml /app/pyproject.toml
COPY ./data/features/ /app/data/features/
COPY ./job_predictor/core /app/job_predictor/core
COPY ./job_predictor/utils /app/job_predictor/utils

COPY ./job_predictor/features/job_predictor/ /app/job_predictor/features/job_predictor/


# upgrade pip
RUN pip install --upgrade pip

# install poetry
RUN pip install poetry

# disable virtualenv for poetry
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install