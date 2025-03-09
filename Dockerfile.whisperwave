FROM python:3.10.14-slim-bookworm

RUN mkdir /my-queue
COPY . /my-queue
COPY pyproject.toml /my-queue

WORKDIR /my-queue
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
CMD ["poetry", "run", "my-queue"]