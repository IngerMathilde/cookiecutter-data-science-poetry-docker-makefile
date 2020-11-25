FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# set path to our python api file
ENV MODULE_NAME="server.api"

# copy contents of project into docker
COPY ./pyproject.toml /app/pyproject.toml
COPY ./data/features/ /app/data/features/
COPY ./{{ cookiecutter.source_name }}/core /app/{{ cookiecutter.source_name }}/core
COPY ./{{ cookiecutter.source_name }}/util.py /app/{{ cookiecutter.source_name }}/util.py

COPY ./{{ cookiecutter.source_name }}/features/{{ cookiecutter.source_name }}/ /app/{{ cookiecutter.source_name }}/features/job_predictor/


# upgrade pip
RUN pip install --upgrade pip

# install poetry
RUN pip install poetry

# disable virtualenv for poetry
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install