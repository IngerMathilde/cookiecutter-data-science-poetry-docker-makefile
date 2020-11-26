FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# upgrade pip
RUN pip install --upgrade pip

# install poetry
RUN pip install poetry

# disable virtualenv for poetry
COPY ./pyproject.toml /app/pyproject.toml
RUN poetry config virtualenvs.create false

# install dependencies
RUN poetry install

# copy contents of project into docker
COPY ./model/ /app/model/

COPY ./pyproject.toml /app/pyproject.toml
COPY ./models/ /app/models/

COPY ./{{ cookiecutter.source_name }}/util.py /app/{{ cookiecutter.source_name }}/util.py
COPY ./{{ cookiecutter.source_name }}/config.py /app/{{ cookiecutter.source_name }}/config.py

COPY ./{{ cookiecutter.source_name }}/core /app/{{ cookiecutter.source_name }}/core
COPY ./{{ cookiecutter.source_name }}/server /app/{{ cookiecutter.source_name }}/server
COPY ./{{ cookiecutter.source_name }}/model/ /app/{{ cookiecutter.source_name }}/model


# set path to our python api file
ENV MODULE_NAME="{{ cookiecutter.source_name }}.server.api"
ENV PYTHONPATH=/app/{{ cookiecutter.source_name }}/